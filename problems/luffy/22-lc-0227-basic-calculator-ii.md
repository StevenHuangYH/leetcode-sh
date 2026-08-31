# LC 0227: Basic Calculator II | 基本计算器 II

- **LeetCode ID**: LC 0227
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 06: Stack & Parsing)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/basic-calculator-ii/)
- **Solution File**: [`22-lc-0227-basic-calculator-ii.py`](problems/luffy/22-lc-0227-basic-calculator-ii.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a string `s` which represents an expression, evaluate this expression and return its value. The integers in the expression are non-negative, and operators are '+', '-', '*', '/'.

### [CN] 中文描述
给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。整数除法仅保留整数部分。

### Constraints / 约束条件
1 <= s.length <= 3 * 10^5, s 由整数和算符 ('+', '-', '*', '/') 组成

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Data Structures] ➔ [Stack & Queue]`

```
┌────────────────────────────────────────────────────────┐
│ 栈运算符优先级计算                                     │
│ 遇到 +: stack.append(num)                              │
│ 遇到 -: stack.append(-num)                             │
│ 遇到 *: stack.append(stack.pop() * num)                │
│ 遇到 /: stack.append(int(stack.pop() / num))           │
│ 最后求和 sum(stack)                                    │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
高优先级即时结合：乘除法立即出栈计算压回，加减法转化为正负数最后统求和。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-227-basic calculator

class Solution:
    def calculate(self, s: str) -> int:

        s=s.replace(" ", "")
        stack=[]
        num=0
        pre_sign="+"
        n=len(s)

        for i in range(n):
            char=s[i]
            #if char is a number
            if char.isdigit():
                num=num*10 + int(char)
            #if char is sign
            if not char.isdigit() or i==n-1: #n-1 --> last one
                if pre_sign=="+":
                    stack.append(num)
                elif pre_sign=="-":
                    stack.append(-num)
                elif pre_sign=="*":
                    top=stack.pop()
                    multi=top*num
                    stack.append(multi)
                elif pre_sign=="/":
                    top=stack.pop()
                    divide=int(top/num) 
                    stack.append(divide)

                pre_sign=char
                num=0

        return sum(stack)
```

1. 基于 `22-lc-0227-basic-calculator-ii.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“Python 负数除法整除向负无穷取整的问题如何处理？”*
  - **Candidate**: Python 的 `//` 面对负数时如 `-3 // 2 = -2`，必须使用 `int(a / b)` 向零截断。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 负数整除截断错误 | 使用 // 导致向负无穷取整 | 除法舍入 | 必须使用 int(float(a) / b) |

### Complete Dry-Run Table / 实例推演表

s='3+2*2' -> stack=[3, 4] -> sum=7

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 遍历字符串一次。 |
| **Space Complexity** | $O(n)$ | 数字栈。 |
