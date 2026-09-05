from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


CONFIG_PATH = Path.home() / '.ppt-master' / 'wps-compat.json'
PREFERENCES_PATH = Path.home() / '.ppt-master' / 'preferences.json'
ALLOWLIST = (
    'scripts/pptx_animations.py',
    'scripts/svg_to_pptx/animation_config.py',
    'scripts/svg_to_pptx/pptx_package/builder.py',
    'scripts/svg_to_pptx/wps_compat.py',
    'scripts/tests/test_wps_animation_compat.py',
    'references/animations.md',
    'references/wps-animation-compatibility.md',
    'workflows/stages/customize-animations.md',
)


def load_config() -> dict[str, Any]:
    try:
        value = json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f'cannot read {CONFIG_PATH}: {exc}') from exc
    if not isinstance(value, dict):
        raise RuntimeError(f'{CONFIG_PATH} must contain a JSON object')
    return value


def roots(config: dict[str, Any]) -> tuple[Path, Path, Path]:
    repository = Path(str(config.get('repository', ''))).expanduser()
    active = Path(str(config.get('active_skill', ''))).expanduser()
    source = repository / 'skills' / 'ppt-master'
    if not (repository / '.git').exists():
        raise RuntimeError(f'configured repository is not a Git checkout: {repository}')
    if not (active / 'SKILL.md').exists():
        raise RuntimeError(f'active PPT Master skill is missing: {active}')
    return repository, source, active


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def drift(source: Path, active: Path) -> list[str]:
    mismatches: list[str] = []
    for relative in ALLOWLIST:
        source_file = source / relative
        active_file = active / relative
        if not source_file.is_file():
            mismatches.append(f'missing source: {relative}')
        elif not active_file.is_file():
            mismatches.append(f'missing active: {relative}')
        elif digest(source_file) != digest(active_file):
            mismatches.append(f'different: {relative}')
    return mismatches


def run(args: list[str], *, cwd: Path) -> None:
    result = subprocess.run(args, cwd=cwd, text=True)
    if result.returncode:
        raise RuntimeError(f'command failed ({result.returncode}): {args!r}')


def status(config: dict[str, Any]) -> int:
    repository, source, active = roots(config)
    branch = subprocess.run(
        ['git', 'branch', '--show-current'],
        cwd=repository,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    mismatches = drift(source, active)
    mode = 'missing'
    if PREFERENCES_PATH.exists():
        try:
            preferences = json.loads(PREFERENCES_PATH.read_text(encoding='utf-8'))
            mode = preferences.get('animations', {}).get(
                'interactive_sequence_mode',
                'standard',
            )
        except (OSError, json.JSONDecodeError, AttributeError):
            mode = 'invalid'
    print(f'repository={repository}')
    print(f'branch={branch}')
    print(f'active_skill={active}')
    print(f'default_mode={mode}')
    print(f'drift={len(mismatches)}')
    for mismatch in mismatches:
        print(f'- {mismatch}')
    return 0 if branch == 'local/wps-compat' and mode == 'wps' and not mismatches else 1


def sync(config: dict[str, Any]) -> None:
    _, source, active = roots(config)
    mismatches = drift(source, active)
    if not mismatches:
        print('active skill already matches the maintained WPS overlay')
        return
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup = Path.home() / '.ppt-master' / 'backups' / timestamp
    for relative in ALLOWLIST:
        source_file = source / relative
        active_file = active / relative
        if not source_file.is_file():
            raise RuntimeError(f'cannot synchronize missing source file: {source_file}')
        if active_file.exists():
            backup_file = backup / relative
            backup_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(active_file, backup_file)
        active_file.parent.mkdir(parents=True, exist_ok=True)
        temporary = active_file.with_suffix(active_file.suffix + '.wps-tmp')
        shutil.copy2(source_file, temporary)
        temporary.replace(active_file)
    print(f'synchronized {len(ALLOWLIST)} allowlisted files')
    print(f'backup={backup}')


def test(config: dict[str, Any]) -> None:
    _, source, _ = roots(config)
    run(
        [sys.executable, str(source / 'scripts/tests/test_wps_animation_compat.py'), '-v'],
        cwd=source,
    )


def update(config: dict[str, Any]) -> None:
    repository, _, _ = roots(config)
    run(['git', 'pull', '--rebase', 'origin', 'main'], cwd=repository)
    test(config)
    sync(config)
    if status(config):
        raise RuntimeError('WPS compatibility status is not healthy after update')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Maintain PPT Master WPS compatibility')
    parser.add_argument('command', choices=('status', 'sync', 'test', 'update'))
    args = parser.parse_args(argv)
    try:
        config = load_config()
        if args.command == 'status':
            return status(config)
        if args.command == 'sync':
            sync(config)
        elif args.command == 'test':
            test(config)
        else:
            update(config)
        return 0
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
