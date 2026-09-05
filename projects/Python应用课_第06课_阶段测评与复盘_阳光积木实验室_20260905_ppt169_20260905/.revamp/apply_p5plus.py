#!/usr/bin/env python3
from pathlib import Path
import gzip, hashlib, json, re

PROJECT = Path(__file__).resolve().parents[1]
SVG_DIR = PROJECT / "svg_final"
ANIM = PROJECT / "animations.json"
PAYLOAD = Path(__file__).with_name("p5plus_payload.json.gz")
PROTECTED = [
    "01_阶段测评与复盘.svg",
    "02_今天的120分钟.svg",
    "03_今天要带走什么.svg",
    "04_十题热身赛.svg",
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

before = {name: sha(SVG_DIR / name) for name in PROTECTED}
data = json.loads(gzip.decompress(PAYLOAD.read_bytes()).decode("utf-8"))
for name, content in data["svg"].items():
    if not re.match(r"^(?:0[5-9]|[12][0-9]|3[0-6])_", name):
        raise SystemExit(f"unexpected slide in payload: {name}")
    (SVG_DIR / name).write_text(content + "\n", encoding="utf-8")

cfg = json.loads(ANIM.read_text(encoding="utf-8"))
slides = cfg.setdefault("slides", {})
for key in list(slides):
    m = re.match(r"^(\d{2})_", key)
    if m and 5 <= int(m.group(1)) <= 36:
        del slides[key]
slides.update(data["animations_patch"]["slides"])
ANIM.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

after = {name: sha(SVG_DIR / name) for name in PROTECTED}
if before != after:
    raise SystemExit("P01-P04 changed; refusing output")
print("P05-P36 rebuilt; P01-P04 hashes unchanged")
