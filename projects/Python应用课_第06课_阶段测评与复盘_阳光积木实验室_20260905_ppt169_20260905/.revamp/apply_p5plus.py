#!/usr/bin/env python3
from pathlib import Path
import base64, gzip, hashlib, json, re

PROJECT = Path(__file__).resolve().parents[1]
SVG_DIR = PROJECT / "svg_final"
ANIM = PROJECT / "animations.json"
PAYLOAD = Path(__file__).with_name("p5plus_payload.json.gz")
PREFIX = "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"
PROTECTED = ["01_阶段测评与复盘.svg", "02_今天的120分钟.svg", "03_今天要带走什么.svg", "04_十题热身赛.svg"]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

before = {name: sha(SVG_DIR / name) for name in PROTECTED}
# The first staging commit accidentally decoded a base64 substring as binary.
# Re-encoding that binary recovers the tail exactly except its final '=' padding.
tail = base64.b64encode(PAYLOAD.read_bytes()).decode("ascii").rstrip("=") + "="
packed = base64.b64decode(PREFIX + tail)
data = json.loads(gzip.decompress(packed).decode("utf-8"))
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
