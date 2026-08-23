# LeetCode 3090. Maximum Length Substring With at Most Two Occurrences
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (滑动窗口频数统计)
- **Tags:** Hash Table, String, Sliding Window
- **Corresponding Python File:** [`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a string `s`, return the **maximum length** of a substring such that each character in the substring appears **at most twice**.
* **[CN]** 给你一个字符串 `s` ，请找出满足每个字符 **最多出现两次** 的最长子字符串，并返回该子字符串的 **最大长度** 。

---

## 2. Code Implementation / 代码实现

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        right = 0
        left = 0
        counts = {}
        max_len = 0

        while right < len(s):
            # 当右端字符已经出现了 2 次，加入新字符就会超标 (达到 3 次)
            # 因此必须收缩左边界，直到该字符频数减少
            if counts.get(s[right], 0) == 2:
                counts[s[left]] -= 1
                left += 1
            else:
                counts[s[right]] = counts.get(s[right], 0) + 1
                max_len = max(max_len, right - left + 1)
                right += 1

        return max_len
```

---

## 3. Step-by-Step Walkthrough / 逐步核心逻辑

1. **变长滑动窗口**：维护左右指针 `left` 和 `right` 以及字符频数哈希表 `counts`。
2. **合法状态扩张**：当 `counts.get(s[right], 0) < 2` 时，将字符频数加 1，更新最长长度 `max_len = max(max_len, right - left + 1)`，并将 `right += 1`。
3. **超标状态收缩**：当 `counts.get(s[right], 0) == 2` 时，当前字符不能再加入窗口。通过不断从左端移出字符（`counts[s[left]] -= 1; left += 1`），直到当前字符可以合法加入。

---

## 4. Complexity Analysis / 复杂度分析

* **时间复杂度 (Time):** $\mathcal{O}(n)$ —— 每个字符最多被 `right` 访问一次，被 `left` 移出一次。
* **空间复杂度 (Space):** $\mathcal{O}(|\Sigma|)$ —— 哈希表最多存储 26 个小写英文字母，空间开销为 $\mathcal{O}(1)$。
