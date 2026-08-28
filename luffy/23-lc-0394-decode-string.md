# LC 0394: Decode String | 字符串解码

- **LeetCode ID**: LC 0394
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 06: Stack & Recursion)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/decode-string/)
- **Solution File**: [`23-lc-0394-decode-string.py`](luffy/23-lc-0394-decode-string.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly k times.

### [CN] 中文描述
给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。

### Constraints / 约束条件
1 <= s.length <= 30

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 双栈法 (倍数栈 count_stack + 字符串栈 str_stack)       │
│ 遇 '[': 将当前 res 和 k 压栈，清空临时变量             │
│ 遇 ']': 弹出上一层字符串与倍数: res = prev + k * res   │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
括号嵌套层级维护：栈中保存上一层级的字符前缀和当前层级的重复倍数。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-394-decode-string
class Solution:
    def decodeString(self, s: str) -> str:
        # 初始化一个栈来保存之前读取的字符和重复次数，cur_num用来累积当前数字
        stack = []
        cur_num = 0
        
        for char in s:
            if char.isdigit():
                # 如果是数字，累加计算多位数值（例如，连续读到'1'和'2'会变成12）
                cur_num = cur_num * 10 + int(char)
                
            elif char == "[":
                # 遇到 '[' 代表前面的数字已经完整，把数字和 '[' 压入栈中保存状态
                stack.append(cur_num)
                cur_num = 0       # 重置 cur_num，以便记录嵌套在里面的下一个数字
                stack.append("[")
                
            elif char == "]":
                # 遇到 ']' 代表当前括号内的子串结束，开始处理
                sub_strs = []
                # 一直出栈，直到遇到与之匹配的 '[' 为止
                while stack[-1] != "[":
                    sub_strs.append(stack.pop())
                
                # 因为栈是后进先出，所以取出来的字符顺序是反的，需要反转一下
                sub_strs.reverse()
                inner_strs = "".join(sub_strs) # 组合成正确的括号内字符串
                
                stack.pop() # 弹出栈顶的 '['
                
                # 弹出对应的重复次数（在压入 '[' 前压入的那个数字）
                repeat_time = stack.pop()
                
                # 将括号内的字符串复制对应的次数，并作为一个整体重新压入栈中
                stack.append(inner_strs * repeat_time)
                
            else: 
                # 如果是普通的英文字母，直接压入栈中
                stack.append(char)
                
        # 遍历结束后，栈中只剩下解码后的字符串片段，将它们拼接成最终结果返回
        return "".join(stack)


#  O(n)
```

1. 基于 `23-lc-0394-decode-string.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何用递归方式实现？”*
  - **Candidate**: 将括号内容视作子问题递归调用，遇到 `]` 返回当前层级结果与消费后的索引指针。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 多位数解析错误 | 遇到多位数字如 100 仅解析了首位 | 数字累加 | k = k * 10 + int(c) |

### Complete Dry-Run Table / 实例推演表

s='3[a2[c]]' -> a2[c]->acc -> 3[acc]->accaccacc

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(S)$ | $S$ 为解码后最终字符串的总长度。 |
| **Space Complexity** | $O(S)$ | 栈存储嵌套层级字符。 |
