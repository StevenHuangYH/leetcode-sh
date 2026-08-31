# LC 0003: Longest Substring Without Repeating Characters | 无重复字符的最长子串

- **LeetCode ID**: LC 0003
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 01: Sliding Window)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **Solution File**: [`04-lc-0003-longest-substring-without-repeating-characters.py`](problems/luffy/04-lc-0003-longest-substring-without-repeating-characters.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a string `s`, find the length of the longest substring without duplicate characters.

### [CN] 中文描述
给定一个字符串 `s` ，请你找出其中不含有重复字符的最长子串的长度。

### Constraints / 约束条件
0 <= s.length <= 5 * 10^4

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Sliding Window]`

```
┌────────────────────────────────────────────────────────┐
│ 滑动窗口: 右进左出维持窗口内字符无重复                 │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
窗口内字符唯一性：集合记录当前窗口内出现的无重复字符。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List


#try sliding window 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right =0
        my_set = set()
        max_len = 0
        while right < len(s):
            if s[right] in my_set: #if the set has recorded
                my_set.remove(s[left])
                left += 1
            else: # if the current character is not in the set
                my_set.add(s[right])
                max_len = max(max_len, right-left+1)
                right += 1

        return max_len
```

1. 基于 `04-lc-0003-longest-substring-without-repeating-characters.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何进一步优化左指针移动步长？”*
  - **Candidate**: 记录字符最后出现下标，遇到重复直接跳转 `left = max(left, last_pos[c] + 1)`。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 空串报错 | s='' 未防御 | 未初始化 ans=0 | 初始化 ans=0 |

### Complete Dry-Run Table / 实例推演表

输入: `s='abcabcbb'` -> max len = 3 ('abc')

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个字符进出集合一次。 |
| **Space Complexity** | $O(|\Sigma|)$ | 字符集大小。 |
