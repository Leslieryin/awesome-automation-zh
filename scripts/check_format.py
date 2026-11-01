# -*- coding: utf-8 -*-
"""README 条目格式校验（CI format job 与本地共用的同一份实现）。

用法：python scripts/check_format.py   （在仓库根目录运行）

规则：`- [名称](链接) —— 点评`（中文破折号，前后各一个空格），点评至少 6 字，
链接不得重复。改了规则记得同步 CONTRIBUTING.md。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
text = (ROOT / "README.md").read_text(encoding="utf-8")
lines = text.splitlines()
problems = []
items = 0
seen = {}

for i, line in enumerate(lines, 1):
    s = line.strip()
    if not s.startswith("- "):
        continue
    items += 1

    m = re.match(r"^- \[[^\]]+\]\((https?://[^)]+)\)\s+——\s+(.+)$", s)
    if not m:
        problems.append(f"  L{i}: 格式不符，应为 `- [名称](链接) —— 点评`  |  {s[:70]}")
        continue

    url, comment = m.group(1), m.group(2).strip()
    if len(comment) < 6:
        problems.append(f"  L{i}: 点评只有 {len(comment)} 字，至少要 6 字  |  {s[:70]}")
    if url in seen:
        problems.append(f"  L{i}: 链接重复（L{seen[url]} 已出现过）  |  {url}")
    else:
        seen[url] = i

print(f"检查了 {items} 条推荐")
if problems:
    print("::error::README 格式不合规，详见下方")
    print("\n".join(problems))
    sys.exit(1)
print("格式全部合规 ✓")
