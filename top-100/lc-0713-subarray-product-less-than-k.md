# LC 0713: Subarray Product Less Than K | 乘积小于 K 的子数组

- **LeetCode ID**: LC 0713
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/subarray-product-less-than-k/)
- **Solution File**: [lc-0713-subarray-product-less-than-k.py](top-100/lc-0713-subarray-product-less-than-k.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

### [CN] 中文描述
给你一个整数数组 `nums` 和一个整数 `k` ，请你返回子数组内所有元素的乘积严格小于 `k` 的连续子数组的数目。

### Constraints / 约束条件
- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Sliding Window]`

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ 暴力枚举子数组乘积 O(n^2)                               │
│ 乘积在正整数下单调递增，存在大段冗余穷举               │
└───────────────────────────┬────────────────────────────┘
                            │ 利用正整数单调乘积与滑动窗口计数
                            ▼
┌────────────────────────────────────────────────────────┐
│ 滑动窗口子数组计数原理                                 │
│ 关键计数公式: 以 right 为右端点的合法子数组个数为      │
│ count = right - left + 1                               │
└───────────────────────────┬────────────────────────────┘
                            │ 边界特判 k <= 1
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 713 乘积小于 K 的子数组 (本题)                      │
│ 当 prod >= k 时持续 left += 1，最后累加 r - l + 1      │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

对于合法窗口 $[left, right]$，其内部所有元素乘积 $< k$。
以 $right$ 为固定右端点，能构成的连续子数组包含：
$[nums[right]], [nums[right-1], nums[right]], \dots, [nums[left], \dots, nums[right]]$。
这些子数组的个数恰好等于窗口长度：
$$\Delta \text{ans} = right - left + 1$$

边界防御：因为所有 $nums[i] \ge 1$，若 $k \le 1$，任何非空子数组的乘积至少为 1，不可能严格小于 $k$，直接特判返回 0。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = 0
        prod = 1
        left = 0

        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1

        return ans
```

1. **特判边界**：`if k <= 1: return 0`。
2. **初始化窗口**：`ans = 0, prod = 1, left = 0`。
3. **右指针推进与窗口维护**：
   - 乘以当前值 `prod *= val`。
   - 若当前乘积 `prod >= k`，除以左端元素 `prod //= nums[left]` 并移动 `left += 1`，恢复窗口合法性。
   - 累加以 `right` 为结尾的子数组个数 `ans += right - left + 1`。
4. **返回答案**：遍历完成返回 `ans`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么每次累加的是 `right - left + 1` 而不是 1？”*
  - **Candidate Response**: 若一个大区间 $[left, right]$ 的乘积 $< k$，由于数组全为正整数，该区间内以 $right$ 为结尾的任何子区间 $[i, right]$（$left \le i \le right$）的乘积也必定严格小于 $k$。符合条件的子区间恰有 $right - left + 1$ 个。

- **Interviewer**: *“如何用前缀对数和 + 二分查找解决本题？”*
  - **Candidate Response**: $\prod nums[i] < k \iff \sum \log(nums[i]) < \log(k)$。利用对数将乘积转化为单调前缀和，对每个左端点二分右端点，时间复杂度为 $O(n \log n)$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 漏掉 `k <= 1` 特判 | 当 $k = 0$ 或 $k = 1$ 时进入死循环或返回非 0 | 正整数乘积 $\ge 1$，当 $k \le 1$ 时 `while` 无法终止 | 必须前置特判 `if k <= 1: return 0` |
| 除法浮点精度丢失 | 精度误差导致比较错误 | 使用浮点除法 `/` 可能产生精度损耗 | 必须使用整除 `//=` 保证整型准确性 |

### Complete Dry-Run Table / 实例推演表

输入: `nums = [10, 5, 2, 6], k = 100`

| `right` | `val` | `prod` | `while prod >= 100` | `left` | Window Subarrays Added | `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 10 | 10 | No | 0 | `[10]` (+1) | 1 |
| 1 | 5 | 50 | No | 0 | `[5], [10, 5]` (+2) | 3 |
| 2 | 2 | 100 | Yes -> `prod //= 10 = 10`, `left = 1` | 1 | `[2], [5, 2]` (+2) | 5 |
| 3 | 6 | 60 | No | 1 | `[6], [2, 6], [5, 2, 6]` (+3) | 8 |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 左右指针均单调移动，数组中每个元素最多被乘一次、除一次，总步数 $\le 2n$。 |
| **Space Complexity** | $O(1)$ | 仅使用固定的常数级整型变量 `prod, left, ans`。 |
