# LC 0209: Minimum Size Subarray Sum | 长度最小的子数组

- **LeetCode ID**: LC 0209
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/minimum-size-subarray-sum/)
- **Solution File**: [lc-0209-minimum-size-subarray-sum.py](top-100/lc-0209-minimum-size-subarray-sum.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

### [CN] 中文描述
给定一个含有 `n` 个正整数的数组和一个正整数 `target` 。
找出该数组中满足其总和大于等于 `target` 的长度最小的子数组 `[numsl, numsl+1, ..., numsr-1, numsr]` ，并返回其长度。如果不存在符合条件的子数组，返回 `0` 。

### Constraints / 约束条件
- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ 暴力枚举子数组起点终点 O(n^2)                           │
│ 枚举所有区间 [i, j]，计算元素和并比较长度               │
└───────────────────────────┬────────────────────────────┘
                            │ 利用正整数数组单调累加性质
                            ▼
┌────────────────────────────────────────────────────────┐
│ 滑动窗口 / 尺蠖法 (Sliding Window Invariant)            │
│ • 进窗: 扩张 right，总和 s 严格递增                    │
│ • 满足 s >= target: 记录最小长度并收缩 left            │
└───────────────────────────┬────────────────────────────┘
                            │ 泛化为不定长滑动窗口标准模板
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 209 长度最小的子数组 (本题)                         │
│ while s >= target: ans = min(ans, r-l+1), s -= nums[l] │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

由于 `nums` 中所有元素均为**正整数**，窗口和具有严格的单调性：
- 增大 `right`，窗口和必单调递增；
- 增大 `left`，窗口和必单调递减。

滑动窗口循环不变量：
1. 右指针 `right` 不断向右探索，将 `nums[right]` 累加至窗口和 `s`。
2. 当 `s >= target` 时，当前窗口 $[left, right]$ 构成一个可行解，更新 `ans = min(ans, right - left + 1)`。
3. 随后尝试收缩左边界 `s -= nums[left]; left += 1`，直到窗口和重新 $< target$。

```
nums: [ 2,  3,  1,  2,  4,  3 ], target = 7
      [─── window ────]  s = 8 >= 7 -> ans = 4, 收缩 left
          [── window ─]  s = 6 < 7  -> 继续扩张 right
```

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1 # 初始化为不可能的大值 (哨兵)
        s = 0
        left = 0

        for right, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1

        return ans if ans <= n else 0
```

1. **初始化**：`ans = n + 1`，`s = 0`, `left = 0`。
2. **右指针遍历进窗**：`for right, x in enumerate(nums):`，将当前元素加入 `s += x`。
3. **内层 `while` 条件出窗**：
   - 只要当前窗口和 `s >= target`，记录最小长度 `ans = min(ans, right - left + 1)`。
   - 移出左端元素 `s -= nums[left]` 并推进左指针 `left += 1`。
4. **返回值处理**：若 `ans <= n` 返回 `ans`，否则说明无解返回 `0`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果数组中包含负数，滑动窗口还能用吗？如何解决？”*
  - **Candidate Response**: 不能。因为包含负数时，窗口扩张和收缩不再具备单调性。此时需使用**前缀和 + 单调双端队列**（如 LC 862 和至少为 K 的最短子数组），时间复杂度仍为 $O(n)$。

- **Interviewer**: *“如何用前缀和 + 二分查找做到 O(n log n)？”*
  - **Candidate Response**: 构建前缀和数组 `prefix`。因为元素为正，`prefix` 严格单调递增。对于每个起点 $i$，在 `prefix` 中二分查找第一个 $\ge prefix[i] + target$ 的终点 $j$，取最小 $j - i$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 内层使用 `if` 替代 `while` | 返回长度大于实际最优解 | 每次可能连续出窗多个元素才能使 `s < target` | 必须使用 `while s >= target` 持续压缩 |
| 无法达成 target 时返回 `n + 1` | 未通过所有无解测试用例 | 初始化哨兵未在返回时转为 0 | 统一返回 `ans if ans <= n else 0` |

### Complete Dry-Run Table / 实例推演表

输入: `target = 7, nums = [2, 3, 1, 2, 4, 3]`

| `right` | `x` | `s` | `s >= 7?` | `left` | `right - left + 1` | `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 2 | 2 | False | 0 | - | 7 |
| 1 | 3 | 5 | False | 0 | - | 7 |
| 2 | 1 | 6 | False | 0 | - | 7 |
| 3 | 2 | 8 | True | 0 -> 1 | `3 - 0 + 1 = 4` | 4 |
| 4 | 4 | 10 | True | 1 -> 2 -> 3 | `4 - 1 + 1 = 4` -> `4 - 2 + 1 = 3` | 3 |
| 5 | 3 | 8 | True | 3 -> 4 | `5 - 3 + 1 = 3` -> `5 - 4 + 1 = 2` | 2 |

最终返回 `2`（对应子数组 `[4, 3]`）。

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 尽管存在两层循环，但每个元素最多进窗一次、出窗一次，`left` 和 `right` 指针均单调右移，总步数 $\le 2n$。 |
| **Space Complexity** | $O(1)$ | 仅维护若干标量整型变量，空间复杂度为 $O(1)$。 |
