# LC 0020: Valid Parentheses | 有效的括号

- **LeetCode ID**: LC 0020
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 06: Stacks)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/valid-parentheses/)
- **Solution File**: [`19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

### [CN] 中文描述
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

### Constraints / 约束条件
1 <= s.length <= 10^4

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Data Structures] ➔ [Stack & Queue]`

```
┌────────────────────────────────────────────────────────┐
│ 栈后进先出匹配 (LIFO Matching)                         │
│ 遇左括号入栈；遇右括号出栈并检查是否与哈希映射匹配     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
后进先出对称性：最近入栈的未闭合左括号必须与当前遇到的第一个右括号严格闭合配对。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-20-valid0-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","]":"[","}":"{"}
        for char in s:
            if char in {"(","[","{"}:
                stack.append(char)
            else:
                if stack==[]: #if not stack:
                    return False


                top_ele=stack.pop()
                if mapping[char]!=top_ele:
                    return False


        if stack:
            return False
        else:
            return True
```

1. 基于 `19-lc-0020-valid-parentheses.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“奇数长度字符串如何快速短路优化？”*
  - **Candidate**: 有效括号必须成对出现，若 `len(s) % 2 != 0` 可直接在首行 `return False`。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 空栈 pop 异常 | 字符串以右括号开头 stack 为空直接 pop | IndexError | pop 前必须检查 not stack |

### Complete Dry-Run Table / 实例推演表

s='()[]{}' -> stack 依次进出 -> 最终 stack 为空 -> return True

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 遍历每个字符一次。 |
| **Space Complexity** | $O(n)$ | 最坏情况全为左括号存入栈中。 |
