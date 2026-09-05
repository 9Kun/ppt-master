---
name: ppt-master-wps-compat
description: Preserve, verify, and restore WPS-compatible interactive animations for PPT Master across projects and upstream updates. Use with ppt-master whenever WPS Presentation is a delivery target, when animations use trigger_shape or click-driven/typewriter timelines, or when checking/updating the local WPS compatibility installation.
---

# PPT Master WPS Compatibility

Use this companion skill together with `ppt-master`; it does not replace PPT
Master's routing or export workflow.

Before authoring or exporting WPS-targeted interactive animation:

1. Run `python scripts/maintain.py status` from this skill directory.
2. If status reports drift and the persistent configuration has
   `auto_repair: true`, state that this skill is restoring the maintained WPS
   overlay, then run `python scripts/maintain.py sync`.
3. Read the active PPT Master reference
   `references/wps-animation-compatibility.md` and follow its trigger-hit-area,
   entrance-Wipe direction mapping, sidecar, export, and real-WPS acceptance
   rules. Keep project sidecars PowerPoint-semantic; the maintained WPS overlay
   performs the required `up ↔ down` and `left ↔ right` serialization mapping.
4. Use the normal PPT Master SVG -> PPTX export. Never use WPS automation to
   author or rewrite the final PPTX.

For updating the maintained fork, Git hooks, recovery, or changing the global
default, read [references/maintenance.md](references/maintenance.md).

Do not overwrite `.env`. The WPS default lives in
`~/.ppt-master/preferences.json`, outside the upstream checkout.
