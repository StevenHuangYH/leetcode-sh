# LC 2235: Add Two Integers | 两整数相加

- **LeetCode ID**: LC 2235
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 01: Foundations & Arithmetic)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/add-two-integers/)
- **Solution File**: [`01-lc-2235-add-two-integers.py`](problems/luffy/01-lc-2235-add-two-integers.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given two integers `num1` and `num2`, return the sum of the two integers.

### [CN] 中文描述
给你两个整数 `num1` 和 `num2`，请你返回这两个整数的和。

### Constraints / 约束条件
-100 <= num1, num2 <= 100

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Other] ➔ [Math]`

```
┌────────────────────────────────────────────────────────┐
│ 直接代数求和: sum = num1 + num2                         │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
代数加法公理：$$\text{sum}(num1, num2) = num1 + num2$$

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-2235

#add two integers

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1+num2
```

1. 基于 `01-lc-2235-add-two-integers.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何不用加号实现？”*
  - **Candidate**: 利用位运算 `a ^ b` 结合进位 `(a & b) << 1` 循环累加。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 溢出边界 | 其他语言 32 位溢出 | 整型边界 | Python 原生支持大整数运算 |

### Complete Dry-Run Table / 实例推演表

输入: `num1 = 12, num2 = 5` -> `17`

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(1)$ | 硬件级加法。 |
| **Space Complexity** | $O(1)$ | 常数空间。 |
