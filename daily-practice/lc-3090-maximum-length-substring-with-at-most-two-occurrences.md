# LC 3090: Maximum Length Substring With Two Occurrences | 最多包含两个相同字符的最长子字符串

- **LeetCode ID**: LC 3090
- **Difficulty**: Easy
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)
- **Solution File**: [lc-3090-maximum-length-substring-with-at-most-two-occurrences.py](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a string `s`, return the maximum length of a substring such that it contains at most two occurrences of each character.

### [CN] 中文描述
给你一个字符串 `s` ，请你返回满足每个字符 最多 出现两次的最长子字符串的长度。

### Constraints / 约束条件
- `2 <= s.length <= 100`
- `s` 仅由小写英文字母组成

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Sliding Window]`

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ LC 3 Longest Substring Without Repeating Characters    │
│ 约束: 每个字符频数 <= 1 (无重复)                       │
└───────────────────────────┬────────────────────────────┘
                            │ 频数上限放宽为至多 2 次
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 3090 最多包含 2 次字符的最长子串 (本题)              │
│ 核心机制: counts[c] > 2 时滑动窗口收缩 left 指针       │
│ 动态更新: ans = max(ans, right - left + 1)             │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

使用滑动窗口与哈希表/字典统计当前窗口 $[left, right]$ 内各字符的出现频数：
1. **右指针探索**：`right` 递增，将 `s[right]` 频数加 1。
2. **非法状态收缩**：若 `counts[s[right]] > 2`，则当前窗口非法。持续推进 `left` 并扣减 `counts[s[left]] -= 1; left += 1`，直至 `counts[s[right]] <= 2`。
3. **有效状态更新**：每次循环末尾窗口合法，更新 `max_len = max(max_len, right - left + 1)`。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        right = 0
        left = 0
        counts = {}
        max_len = 0

        while right < len(s):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1

            while counts[char] > 2:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
```

1. **变量初始化**：`left = 0, right = 0, counts = {}, max_len = 0`。
2. **窗口扩张**：`counts[char] = counts.get(char, 0) + 1`。
3. **内层合法性纠正**：`while counts[char] > 2:`，弹出左侧字符 `counts[left_char] -= 1; left += 1`。
4. **长度结算**：`max_len = max(max_len, right - left + 1)`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“字符集只有小写字母，如何优化哈希表空间与寻址性能？”*
  - **Candidate Response**: 可以将字典替换为长度为 26 的定长数组 `counts = [0] * 26`，通过 `ord(c) - ord('a')` 映射下标，避免哈希查找开销，达成绝对常数空间 $O(1)$ 与极致运行速度。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 内层收缩误减 `counts[char]` 而非 `counts[s[left]]` | 字典计数混乱导致死循环 | 左指针移出的是 `s[left]`，应减少移出字符的频数 | 严谨使用 `counts[s[left]] -= 1` |
| 误将 `max_len` 在 `while` 内部更新 | 漏算初始较短合法子串 | 窗口结算必须在恢复合法性之后执行 | 放在内层 `while` 之后执行 `max_len = max(...)` |

### Complete Dry-Run Table / 实例推演表

输入: `s = "bcbbbcba"`

| `right` | `char` | `counts[char]` (更新后) | `while counts > 2` | `left` | Window Substring | `max_len` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 'b' | 1 | No | 0 | `"b"` | 1 |
| 1 | 'c' | 1 | No | 0 | `"bc"` | 2 |
| 2 | 'b' | 2 | No | 0 | `"bcb"` | 3 |
| 3 | 'b' | 3 | Yes -> `left` 从 0 ('b') 移到 1 | 1 | `"cbb"` | 3 |
| 4 | 'b' | 3 | Yes -> `left` 依次移过 'c', 'b' 到 3 | 3 | `"bb"` | 3 |
| 5 | 'c' | 2 | No | 3 | `"bbc"` | 3 |
| 6 | 'b' | 3 | Yes -> `left` 移过 'b' 到 4 | 4 | `"bcb"` | 4 |
| 7 | 'a' | 1 | No | 4 | `"bcba"` | 4 |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 字符串中每个字符最多进窗一次、出窗一次，指针操作总步数不超过 $2n$。 |
| **Space Complexity** | $O(|\Sigma|)$ | 字典最多存储 26 个小写英文字母的计数，空间为常数级别 $O(1)$。 |
