# Maintenance and update contract

The installation uses three independent durable layers:

1. A maintained Git branch, `local/wps-compat`, rebased on official
   `origin/main`. The WPS implementation, documentation, and tests are committed
   there, so `git pull` cannot silently discard them.
2. A user preference at `~/.ppt-master/preferences.json`. It selects WPS as the
   default for new projects and is outside every Git checkout.
3. This companion skill. Its `maintain.py` compares the maintained branch with
   the active PPT Master installation and can restore only the allowlisted WPS
   files. It never copies or modifies `.env`.

## Update

Preferred command:

```bash
python C:/Users/Administrator/.codex/skills/ppt-master-wps-compat/scripts/maintain.py update
```

This fetches and rebases the local compatibility branch on official `main`,
runs the WPS regression tests, and synchronizes the allowlisted files into the
active skill installation. A merge conflict stops the update without deleting
the local commit.

Plain `git pull` is also supported in the configured repository. The branch is
configured with rebase, and external `post-merge` / `post-rewrite` hooks run the
same safe synchronization after a successful update.

## Recovery

Run `maintain.py status`. If files drifted, run `maintain.py sync`. Every sync
backs up replaced allowlisted files under
`~/.ppt-master/backups/<timestamp>/`. The operation never touches `.env`,
project sources, or exported presentations.

## Defaults

```bash
python <maintained-skill>/scripts/svg_to_pptx/wps_compat.py enable
python <maintained-skill>/scripts/svg_to_pptx/wps_compat.py disable
```

`enable` makes WPS mode the host default. A page can still explicitly request
`"interactive_sequence_mode": "standard"` in `animations.json`.
