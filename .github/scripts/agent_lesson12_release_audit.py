from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path

P = Path('projects/第12课_特工身份确认_阳光积木乐园_ppt169_20260906')
F = P / 'exports' / '第12课_特工身份确认_阳光积木乐园.pptx'

with zipfile.ZipFile(F) as zf:
    slide_xml = sorted(
        name for name in zf.namelist()
        if re.fullmatch(r'ppt/slides/slide\d+\.xml', name)
    )
    report = {
        'pptx_exists': F.exists(),
        'size_bytes': F.stat().st_size,
        'slide_count': len(slide_xml),
        'timing_slides': sum(b'<p:timing' in zf.read(name) for name in slide_xml),
        'zip_ok': zf.testzip() is None,
    }

if report['slide_count'] != 32 or not report['zip_ok'] or report['timing_slides'] == 0:
    raise SystemExit(report)

validation = P / 'validation'
validation.mkdir(parents=True, exist_ok=True)
(validation / 'readback.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8'
)

lines = [
    '# 第12课《特工身份确认》修订质量报告',
    '',
    '## 本轮自检修复',
    '- 修复 P16/P23/P27：任务1在“先切任务1再运行”后不输出的问题。',
    '- 修复 P16/P23/P27：切换任务会清除旧输出、运行中与完成状态，并恢复运行提示。',
    '- 修复 P16/P23/P27：完成状态只在逐字/逐行输出完全结束后出现。',
    '- 修复 P16：六行“数到5”输出重新排版，全部保持在深色终端内部。',
    '- 重做 P27：左侧代码恢复教案最终失败判断；空白案例改为“空白 → 正确”，不再把仍等待输入的程序标为完成。',
    '- 重做控制台视觉与交互：顶部流程胶囊、任务区、编辑器、终端、direct-root 0.001 命中层统一复用 P10 语言。',
    '- 修复普通揭晓页：透明命中区置于可见按钮之上。',
    '- 修复 9 页双题选择页：点击后正确项变绿、其他项变粉，同时显示答案解析，初始态不泄露答案。',
    '- 修复 P26/P27 代码投影可读性：P26 17px；P27 密集控制台 17px，不再使用 15px/14px 补丁字号。',
    '- 修订 P31 对 password 未赋值问题的说明，与教案“本模板 while 至少执行一次”一致。',
    '- 恢复所有交互顶层组 data-pptx-bounds；叠层交互使用 checker 支持且显式 sidecar 可动画的结构角色契约。',
    '',
    '## 发布门禁',
    '- PPT Master attribution guard：PASS。',
    '- project_manager validate：PASS。',
    '- 完整 canonical final SVG quality gate：PASS（无 ERROR；warning 为非阻断式设计提示）。',
    '- semantic_self_audit / root_contract_self_audit：PASS。',
    '- WPS interaction hard gate：PASS。',
    '- animation_config validate：PASS。',
    '- finalize_svg：PASS。',
    '- 标准 release svg_to_pptx.py：PASS；未使用 dangerous nonconforming export。',
    '- PPTX ZIP/readback：PASS；32 页且包含 timing XML。',
    '',
    '## WPS 真实放映边界',
    'GitHub Actions 是 Linux 临时运行器，没有真实 WPS Presentation GUI，因此本报告不声称完成真实 WPS 放映点击验收。仍需在桌面 WPS 放映模式最终点测 P16、P23、P27 的任务切换、运行、逐字/逐行输出、完成状态与重复点击。',
    '',
    '## 参考项目保护',
    '`projects/初识_Cpp_阳光积木乐园_ppt169_20260826` 只读复用视觉语言、素材和交互机制，未修改或覆盖。',
]
(validation / 'quality_report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(report)
