# LeetCode 3090. Maximum Length Substring With Two Occurrences (每个字符最多出现两次的最长子字符串)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (滑动窗口 / 双指针 / 哈希表频数统计 / 频数约束)
- **Tags:** Hash Table, String, Sliding Window
- **Corresponding Python File:** [`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a string `s`, return the **maximum length** of a substring such that no character in the substring appears more than **twice**.
* **[CN]** 给你一个字符串 `s` ，请你要返回满足以下条件的最长子字符串的 **最大长度**：每个字符在子字符串中 **最多出现两次** 。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 窗口合法性约束: counts.get(c, 0) <= 2。                                  │
│ 2. 伸缩单调性: 当 counts[s[right]] == 2 时，左指针持续收缩直到频数降到 2 以下。│
│ 3. 实时极值更新: max_len = max(max_len, right - left + 1)。                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py) 中的实现进行逐行深入解析：

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        right = 0
        left = 0
        counts = {}
        max_len = 0

        while right < len(s):
            # 若加入 s[right] 会超频（即已有 2 个），收缩左边界
            if counts.get(s[right], 0) == 2:
                counts[s[left]] -= 1
                left += 1 
            # 否则扩展右边界
            else:
                counts[s[right]] = counts.get(s[right], 0) + 1
                max_len = max(max_len, right - left + 1)
                right += 1

        return max_len
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 左右指针均单调右移，每个字符进出窗口最多 2 次，总耗时为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(|\Sigma|)$ | 哈希表最多存储 26 个英文字母，额外空间为 $\mathcal{O}(1)$。 |
