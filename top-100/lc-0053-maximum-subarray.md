# LC 0053: Maximum Subarray | 最大子数组和

- **LeetCode ID**: LC 0053
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/maximum-subarray/)
- **Solution File**: [lc-0053-maximum-subarray.py](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0053-maximum-subarray.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

### [CN] 中文描述
给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。

### Constraints / 约束条件
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ 暴力枚举所有子数组 O(n^2)                               │
│ 枚举起点 i 和终点 j，求 sum(nums[i..j])                 │
└───────────────────────────┬────────────────────────────┘
                            │ 发现最优子结构：当前数要么自立门户，要么加入前人
                            ▼
┌────────────────────────────────────────────────────────┐
│ 经典 Kadane 动态规划算法 (DP 状态转移)                  │
│ 状态定义: dp[i] = max(nums[i], dp[i-1] + nums[i])      │
└───────────────────────────┬────────────────────────────┘
                            │ 滚动变量空间压缩 O(n) -> O(1)
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 53 最大子数组和 (本题)                               │
│ current_sum = max(nums[i], current_sum + nums[i])      │
│ max_sum = max(max_sum, current_sum)                    │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

定义 $dp[i]$ 为**以 $nums[i]$ 为结尾的最大连续子数组和**。
对于 $nums[i]$，只有两种抉择：
1. **加入前面的子数组**：$dp[i-1] + nums[i]$（当前面累加和大于 0 时，有正向增益）。
2. **自立门户重新开始**：$nums[i]$（当前面累加和小于等于 0 时，带上前面的子数组只会拖累当前和）。

状态转移方程：
$$dp[i] = \max(nums[i], dp[i-1] + nums[i])$$
最终全局最大子数组和为：
$$\text{Ans} = \max_{0 \le i < n} dp[i]$$

由于 $dp[i]$ 仅依赖前一项 $dp[i-1]$，因此只需维护一个滚动变量 `current_sum`，实现空间复杂度 $O(1)$。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
```

1. **初始基准**：
   - `max_sum = nums[0]`: 全局最大和初始化为首个元素（妥善处理全为负数的情况）。
   - `current_sum = nums[0]`: 维护以当前元素结尾的最大连续和。
2. **线性扫描与状态推进**：
   - `for i in range(1, len(nums)):` 从下标 1 开始向后遍历。
   - `current_sum = max(nums[i], current_sum + nums[i])`: 比较自立门户与并入前驱，取较大者。
   - `max_sum = max(max_sum, current_sum)`: 动态更新全局历史最大值。
3. **返回结果**：
   - 遍历完成返回 `max_sum`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果数组全是负数，这段代码能正确运行吗？”*
  - **Candidate Response**: 可以。因为 `max_sum` 和 `current_sum` 初始化为 `nums[0]` 而不是 `0`。在全负数数组中，`max(nums[i], current_sum + nums[i])` 会始终选择单点较大负数，最终输出数组中的最大负数。

- **Interviewer**: *“如何用分治法 (Divide and Conquer) 解决本题并支持动态区间查询 (如线段树)？”*
  - **Candidate Response**: 分治法将区间分为左右两半，维护 4 个信息：区间总和 `sum`、前缀最大和 `lsum`、后缀最大和 `rsum`、区间最大子段和 `msum`。合并左右子区间可在 $O(1)$ 时间内完成，支持线段树以 $O(\log n)$ 单次响应区间修改与动态查询。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| `max_sum` 初始化为 0 | 在全负数输入 `[-3, -2, -1]` 下错误返回 `0` | 题目要求子数组至少包含一个元素，全负数时答案应为最大负数 | 必须初始化为 `nums[0]` 或 `-math.inf` |
| 误用滑动窗口收缩条件 | 包含负数时滑动窗口单调性失效 | 滑动窗口要求元素全为非负数时才具备单调扩张/收缩性质 | 存在负数时必须使用动态规划或前缀和差值法 |

### Complete Dry-Run Table / 实例推演表

输入: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| Index `i` | `nums[i]` | `current_sum` (`max(x, cur+x)`) | `max_sum` | Decision Rationale |
|:---:|:---:|:---:|:---:|:---:|
| Init | -2 | -2 | -2 | 初始元素 |
| 1 | 1 | `max(1, -2+1) = 1` | 1 | 前和为负，自立门户 (1) |
| 2 | -3 | `max(-3, 1-3) = -2` | 1 | 并入前和 (-2) |
| 3 | 4 | `max(4, -2+4) = 4` | 4 | 前和为负，自立门户 (4) |
| 4 | -1 | `max(-1, 4-1) = 3` | 4 | 并入前和 (3) |
| 5 | 2 | `max(2, 3+2) = 5` | 5 | 并入前和 (5) |
| 6 | 1 | `max(1, 5+1) = 6` | 6 | 并入前和 (6, **最大**) |
| 7 | -5 | `max(-5, 6-5) = 1` | 6 | 并入前和 (1) |
| 8 | 4 | `max(4, 1+4) = 5` | 6 | 并入前和 (5) |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 仅单次遍历数组，每个元素在常数步 $O(1)$ 内完成状态转移计算。 |
| **Space Complexity** | $O(1)$ | 仅使用 `current_sum` 和 `max_sum` 两个浮点/整型变量，空间复杂度为 $O(1)$。 |
