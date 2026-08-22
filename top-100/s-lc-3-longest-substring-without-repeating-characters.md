# LeetCode 3. Longest Substring Without Repeating Characters (无重复字符的最长子串)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (高频面试经典题 / 滑动窗口模版题)
- **Tags:** Hash Table, String, Sliding Window
- **Corresponding Python Files:**
  - [`top-100/s-lc-3-longest-substring-without-repeating-characters.py`](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/s-lc-3-longest-substring-without-repeating-characters.py)
  - [`luffy/4-lc-3-longest-substring-without-repeating-characters.py`](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/luffy/4-lc-3-longest-substring-without-repeating-characters.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a string `s`, find the length of the **longest substring** without repeating characters.
* **[CN]** 给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

---

## 2. Code Implementations / 代码实现

### 方案 1：滑动窗口 + 集合去重 (Sliding Window + Hash Set)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        my_set = set()
        max_len = 0

        while right < len(s):
            # 当右端字符已在集合中（出现重复），收缩左边界
            if s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            else:
                my_set.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1

        return max_len
```

---

### 方案 2：滑动窗口 + 频数哈希表 (Sliding Window + Frequency Map / Counter)

```python
class SolutionCounter:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        cnt = {}
        max_len = 0

        while right < len(s):
            # 若右端字符在当前窗口中频数 >= 1，说明产生重复，需要从左端移出字符
            if cnt.get(s[right], 0) >= 1:
                cnt[s[left]] -= 1
                left += 1
            else:
                cnt[s[right]] = cnt.get(s[right], 0) + 1
                max_len = max(max_len, right - left + 1)
                right += 1

        return max_len
```

---

### 方案 3：哈希表记录最后出现位置 (Direct Index Jump - $\mathcal{O}(n)$ 最优跳跃)

```python
class SolutionJump:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            # 如果字符出现过且上次出现的位置在当前窗口内，直接把 left 跳到其下一位
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len
```

---

## 3. Deep Dive: Why `cnt[s[left]] -= 1`? / 核心原理解析

### 🇺🇸 English Explanation
* **`s[left]`**: The leftmost character currently inside the sliding window `[left, right]`.
* **`cnt`**: A dictionary / frequency table tracking the occurrence count of each character in the current window.
* **`cnt[s[left]] -= 1`**: When `right` encounters a duplicate character, the window is invalid. To restore validity, we shrink the window from the left by advancing `left` (`left += 1`). Before advancing, `s[left]` is **evicted from the window**, so we must decrement its recorded count in `cnt` by `1`.

### 🇨🇳 中文详解
* **`s[left]`**：当前滑动窗口 `[left, right]` 最左端的字符（即将被移出窗口的字符）。
* **`cnt`**：频数哈希表，用于记录当前窗口内各个字符出现的次数。
* **`cnt[s[left]] -= 1`**：当右指针 `right` 指向的字符导致窗口产生重复（不合法）时，必须向右移动左指针 `left` 来缩小窗口。在 `left += 1` 之前，由于 `s[left]` 离开了窗口范围，必须先将哈希表中该字符的计数减 1，以保持哈希表与窗口实际内容的一致性。

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解 (方案 1 & 方案 2)

### 1. 初始化双指针与状态 (Initialization)

```python
left = 0
right = 0
my_set = set() # 或 cnt = {}
max_len = 0
```

* **[EN] Action:**
  * `left`: Start index of the sliding window.
  * `right`: End index of the sliding window.
  * `my_set` / `cnt`: Tracks active characters inside `[left, right]`.
  * `max_len`: Stores the maximum length found so far.
* **[CN] 动作**：
  * `left`：滑动窗口左端点。
  * `right`：滑动窗口右端点。
  * `my_set` / `cnt`：记录当前窗口 `[left, right]` 内包含的字符状态。
  * `max_len`：记录历史最大无重复子串长度。

---

### 2. 窗口收缩阶段 (Window Contraction)

```python
if s[right] in my_set:        # 方案 1
    my_set.remove(s[left])
    left += 1

# 或者方案 2:
if cnt.get(s[right], 0) >= 1: # 方案 2
    cnt[s[left]] -= 1
    left += 1
```

* **[EN] Logic:** If `s[right]` is already recorded, extending the window to `right` would cause a duplicate. We must shrink from the left:
  1. Remove `s[left]` from the set or decrement `cnt[s[left]] -= 1`.
  2. Advance `left += 1`.
  * *Note:* Notice `right` does not increment in this branch, allowing the while loop to re-check `s[right]` until the duplicate is completely cleared.
* **[CN] 逻辑**：如果 `s[right]` 已经在窗口内存在，直接加入会导致重复。因此进入收缩分支：
  1. 将左端字符 `s[left]` 从集合移除，或执行 `cnt[s[left]] -= 1`。
  2. 左指针右移 `left += 1`。
  * *注意*：此时 `right` 不自增，下一轮循环会继续检查 `s[right]`，直到窗口内的冲突字符被彻底移出。

---

### 3. 窗口扩张与答案更新 (Window Expansion & Update)

```python
else:
    my_set.add(s[right])       # 或 cnt[s[right]] = cnt.get(s[right], 0) + 1
    max_len = max(max_len, right - left + 1)
    right += 1
```

* **[EN] Logic:** When `s[right]` is not a duplicate:
  1. Add `s[right]` to `my_set` (or increment `cnt[s[right]] += 1`).
  2. Update `max_len` with current window size `right - left + 1`.
  3. Expand window by advancing `right += 1`.
* **[CN] 逻辑**：当 `s[right]` 不冲突时：
  1. 将 `s[right]` 加入集合（或哈希表计数加 1）。
  2. 用当前窗口长度 `right - left + 1` 更新全局最大值 `max_len`。
  3. 右指针右移 `right += 1` 继续探索新字符。

---

## 5. Execution Trace Example / 模拟运行全过程

以输入 `s = "abcabcbb"` 为例：

| 步骤 (Step) | `right` (`s[right]`) | `left` | 窗口内容 `s[left..right]` | 集合状态 `my_set` | 动作 (Action) | 当前 `max_len` |
| :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| 1 | 0 (`'a'`) | 0 | `"a"` | `{'a'}` | 无重复，加入并 `right += 1` | 1 |
| 2 | 1 (`'b'`) | 0 | `"ab"` | `{'a', 'b'}` | 无重复，加入并 `right += 1` | 2 |
| 3 | 2 (`'c'`) | 0 | `"abc"` | `{'a', 'b', 'c'}` | 无重复，加入并 `right += 1` | **3** |
| 4 | 3 (`'a'`) | 0 | `"abc"` | `{'a', 'b', 'c'}` | **冲突**：`remove('a')`, `left += 1` | 3 |
| 5 | 3 (`'a'`) | 1 | `"bca"` | `{'b', 'c', 'a'}` | 无重复，加入并 `right += 1` | 3 |
| 6 | 4 (`'b'`) | 1 | `"bca"` | `{'b', 'c', 'a'}` | **冲突**：`remove('b')`, `left += 1` | 3 |
| 7 | 4 (`'b'`) | 2 | `"cab"` | `{'c', 'a', 'b'}` | 无重复，加入并 `right += 1` | 3 |
| 8 | 5 (`'c'`) | 2 | `"cab"` | `{'c', 'a', 'b'}` | **冲突**：`remove('c')`, `left += 1` | 3 |
| 9 | 5 (`'c'`) | 3 | `"abc"` | `{'a', 'b', 'c'}` | 无重复，加入并 `right += 1` | 3 |
| 10 | 6 (`'b'`) | 3 | `"abc"` | `{'a', 'b', 'c'}` | **冲突**：`remove('a')`, `left += 1` | 3 |
| 11 | 6 (`'b'`) | 4 | `"bc"` | `{'b', 'c'}` | **仍冲突**：`remove('b')`, `left += 1` | 3 |
| 12 | 6 (`'b'`) | 5 | `"cb"` | `{'c', 'b'}` | 无重复，加入并 `right += 1` | 3 |
| 13 | 7 (`'b'`) | 5 | `"cb"` | `{'c', 'b'}` | **冲突**：`remove('c')`, `left += 1` | 3 |
| 14 | 7 (`'b'`) | 6 | `"b"` | `{'b'}` | **仍冲突**：`remove('b')`, `left += 1` | 3 |
| 15 | 7 (`'b'`) | 7 | `"b"` | `{'b'}` | 无重复，加入并 `right += 1` | 3 |

* **最终返回**：`3`（最长子串为 `"abc"`）。

---

## 6. Comparison & Complexity Analysis / 解法对比与复杂度分析

| 解法 (Approach) | 时间复杂度 (Time) | 空间复杂度 (Space) | 特点与适用场景 |
| :--- | :--- | :--- | :--- |
| **方案 1：Set 集合滑动窗口** | $\mathcal{O}(2n) = \mathcal{O}(n)$ | $\mathcal{O}(|\Sigma|)$ | 逻辑最直观，滑动窗口经典模版 |
| **方案 2：Counter 频数哈希表** | $\mathcal{O}(2n) = \mathcal{O}(n)$ | $\mathcal{O}(|\Sigma|)$ | 通用性最强（可轻松扩展到 LC 3090 等“最多允许 $k$ 次”的变形题） |
| **方案 3：哈希表记录下标跳跃** | $\mathcal{O}(n)$ | $\mathcal{O}(|\Sigma|)$ | 左指针一步跳到位，每个字符只访问 1 次，常数最小 |

*注：$|\Sigma|$ 表示字符集大小（ASCII 码字符集 $|\Sigma| \le 128$），因此空间复杂度为严格的 $\mathcal{O}(1)$。*
