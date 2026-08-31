import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LUFFY_DIR = REPO_ROOT / "luffy"

NOTES = {}

# 01-lc-2235-add-two-integers.md
NOTES["01-lc-2235-add-two-integers.md"] = """# LC 2235: Add Two Integers | 两整数相加

- **LeetCode ID**: LC 2235
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 01: Foundations)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/add-two-integers/)
- **Solution File**: [`01-lc-2235-add-two-integers.py`](luffy/01-lc-2235-add-two-integers.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given two integers `num1` and `num2`, return the sum of the two integers.

### [CN] 中文描述
给你两个整数 `num1` 和 `num2`，请你返回这两个整数的和。

### Constraints / 约束条件
- $-100 \le \text{num1, num2} \le 100$

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 基础算术基石 (Foundational Arithmetic)                │
│ 直接返回 num1 + num2                                   │
└───────────────────────────┬────────────────────────────┘
                            │ 引入位运算无加号加法
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 371 两整数之和 (Bitwise XOR + Carry Shift)          │
│ a ^ b (无进位和) + (a & b) << 1 (进位)                  │
└────────────────────────────────────────────────────────┘
```

### 核心数学不变量
直接应用算术加法运算：
$$\text{sum}(num1, num2) = num1 + num2$$

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
```

1. **直接求和**：计算 `num1 + num2` 并返回整型结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果面试要求不准使用 `+` 运算符，该如何实现？”*
  - **Candidate Response**: 可利用位运算模拟半加器逻辑：`a ^ b` 得到不进位和，`(a & b) << 1` 计算进位，循环直至进位为 0（Python 需处理 32 位掩码）。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 整数溢出 (其他语言) | C++/Java 中超过 $2^{31}-1$ | 基础类型越界 | Python 原生支持大数整型，无溢出风险 |

### Complete Dry-Run Table / 实例推演表

输入: `num1 = 12, num2 = 5`

| `num1` | `num2` | 计算公式 | 返回值 |
|:---:|:---:|:---:|:---:|
| 12 | 5 | `12 + 5` | 17 |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(1)$ | 仅执行单次硬件级加法指令。 |
| **Space Complexity** | $O(1)$ | 仅使用 $O(1)$ 局部寄存器空间。 |
"""

# 02-lc-0001-two-sum.md
NOTES["02-lc-0001-two-sum.md"] = """# LC 0001: Two Sum | 两数之和

- **LeetCode ID**: LC 0001
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 01: Arrays & Hash Table)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/two-sum/)
- **Solution File**: [`02-lc-0001-two-sum.py`](luffy/02-lc-0001-two-sum.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

### [CN] 中文描述
给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target` 的那 **两个** 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

### Constraints / 约束条件
- $2 \le \text{nums.length} \le 10^4$
- $-10^9 \le \text{nums}[i] \le 10^9$
- $-10^9 \le \text{target} \le 10^9$
- 只会存在一个有效答案。

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 暴力枚举 O(n^2)                                         │
│ 双重循环检查 nums[i] + nums[j] == target                │
└───────────────────────────┬────────────────────────────┘
                            │ 空间换时间：哈希表缓存补数
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 1 两数之和 (哈希表缓存 O(n)) (本题)                  │
│ 遍历 x，查询 target - x 是否存在于 cache 中            │
└───────────────────────────┬────────────────────────────┘
                            │ 若数组已有序
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 167 两数之和 II (双指针对撞 O(n) + O(1) 空间)       │
│ left + right 指针对撞逼近 target                       │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
建立单遍哈希表（Single-pass Hash Map）：
遍历当前元素 $x$，若目标补数 $target - x$ 已经在哈希表中，则直接返回 $[cache[target - x], i]$；否则将当前值及索引存入哈希表 $cache[x] = i$。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List

class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, item in enumerate(nums):
            val = target - item
            if val in cache:
                return [cache[val], i]
            cache[item] = i
        return [-1, -1]
```

1. **初始化哈希表**：`cache = {}` 用于记录 `数值 -> 下标` 映射。
2. **单遍遍历与补数探测**：
   - 计算所需补数 `val = target - item`。
   - 若 `val in cache`，说明之前出现过匹配数值，立即返回 `[cache[val], i]`。
   - 若未匹配，将当前数值与索引存入哈希表 `cache[item] = i`。
3. **安全返回值**：若未找到则返回 `[-1, -1]`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么可以一边查哈希表一边存，而不需要先存入所有元素再查？”*
  - **Candidate Response**: 一边遍历一边插入可以自然避免“同一元素使用两次”的 Bug（例如 $nums = [3, 2, 4], target = 6$，若先全量存入，遍历第一个 3 时可能匹配到自己）。单遍哈希只匹配之前的元素，完全避免了自匹配。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 同一下标重复使用 | $target = 6, nums = [3, 4, 2]$ 返回 `[0, 0]` | 查表时未排除自身下标 | 单遍边遍历边插入，或检查 `cache[val] != i` |

### Complete Dry-Run Table / 实例推演表

输入: `nums = [2, 7, 11, 15], target = 9`

| `i` | `item` | `val = 9 - item` | `val in cache`? | `cache` 状态 | 输出 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 2 | 7 | 否 | `{2: 0}` | - |
| 1 | 7 | 2 | 是 (`cache[2] = 0`) | `{2: 0}` | `[0, 1]` |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 遍历数组 $n$ 次，每次哈希查找与插入平均耗时 $O(1)$，总时间严格为 $O(n)$。 |
| **Space Complexity** | $O(n)$ | 哈希表最多存储 $n$ 个键值对，额外空间为 $O(n)$。 |
"""

# Write files
for filename, content in NOTES.items():
    file_path = LUFFY_DIR / filename
    file_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Generated {filename}")
