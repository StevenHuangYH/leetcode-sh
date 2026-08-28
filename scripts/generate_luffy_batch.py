import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LUFFY_DIR = REPO_ROOT / "luffy"

def create_note(filename, lc_id, title_en, title_cn, diff, topic, en_desc, cn_desc, constraints, ascii_art, invariant, py_code, walkthrough_steps, interview_qa, anti_patterns, dry_run_table, time_comp, space_comp):
    py_filename = filename.replace(".md", ".py")
    
    anti_pattern_rows = "\n".join(f"| {p[0]} | {p[1]} | {p[2]} | {p[3]} |" for p in anti_patterns)
    walkthrough_text = "\n".join(f"{i+1}. {step}" for i, step in enumerate(walkthrough_steps))
    
    note = f"""# LC {lc_id}: {title_en} | {title_cn}

- **LeetCode ID**: LC {lc_id}
- **Difficulty**: {diff}
- **Category**: Luffy Structured Curriculum ({topic})
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/{title_en.lower().replace(' ', '-')}/)
- **Solution File**: [`{py_filename}`](luffy/{py_filename})

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
{en_desc}

### [CN] 中文描述
{cn_desc}

### Constraints / 约束条件
{constraints}

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
{ascii_art}
```

### 核心思维模型与数学不变量
{invariant}

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
{py_code.strip()}
```

{walkthrough_text}

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

{interview_qa}

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
{anti_pattern_rows}

### Complete Dry-Run Table / 实例推演表

{dry_run_table}

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | {time_comp[0]} | {time_comp[1]} |
| **Space Complexity** | {space_comp[0]} | {space_comp[1]} |
"""
    target_path = LUFFY_DIR / filename
    target_path.write_text(note.strip() + "\n", encoding="utf-8")
    print(f"Upgraded {filename}")

