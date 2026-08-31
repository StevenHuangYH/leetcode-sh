# LC 3471: Find the Largest Almost Missing Integer | 找出最大的几乎缺失整数

- **LeetCode ID**: LC 3471
- **Difficulty**: Easy
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/find-the-largest-almost-missing-integer/)
- **Solution File**: [lc-3471-find-the-largest-almost-missing-integer.py](problems/daily-practice/lc-3471-find-the-largest-almost-missing-integer.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
You are given an integer array `nums` and an integer `k`.
An integer `x` is **almost missing** from `nums` if `x` appears in exactly one subarray of size `k` within `nums`.
Return the largest almost missing integer from `nums`. If no such integer exists, return `-1`.
A subarray is a contiguous sequence of elements within an array.

### [CN] 中文描述
给你一个整数数组 `nums` 和一个整数 `k` 。
如果在 `nums` 的所有大小为 `k` 的子数组中，整数 `x` 恰好只在 1 个子数组中出现，则称 `x` 是一个 **几乎缺失** 的整数。
请你找出并返回 `nums` 中的 最大 几乎缺失整数。如果不存在这样的整数，返回 `-1` 。

### Constraints / 约束条件
- `1 <= nums.length <= 50`
- `0 <= nums[i] <= 50`
- `1 <= k <= nums.length`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Data Structures] ➔ [Hashing]`

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ 定长滑动窗口模拟 O(n * k)                              │
│ 枚举所有长度为 k 的窗口，用 set 去重后统计全局窗口频数 │
└───────────────────────────┬────────────────────────────┘
                            │ 数学结构分析 (窗口覆盖规律)
                            ▼
┌────────────────────────────────────────────────────────┐
│ 分类讨论 O(n) 极限常数时间优化                          │
│ • k == 1: 统计全局出现恰好 1 次的最大元素             │
│ • k == n: 取整个数组的最大值                          │
│ • 1 < k < n: 只有端点 nums[0] 和 nums[-1] 可能恰被1个  │
│   长度为 k 的子数组覆盖                                │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

根据长度为 $k$ 的子数组在数组中的覆盖分布：
1. **$k = 1$**：每个子数组长度为 1，题目转化为“寻找在全局 `nums` 中只出现过 1 次的最大值”。
2. **$k = n$**：全数组只有唯一 1 个大小为 $n$ 的子数组，因此该子数组包含数组所有元素，每个元素都恰好只出现在这 1 个子数组中，答案即为全局最大值 $\max(nums)$。
3. **$1 < k < n$**：
   - 内部元素 $nums[1 \dots n-2]$ 会被至少 2 个连续的长度为 $k$ 的子数组覆盖，不可能“恰好只出现在 1 个子数组中”。
   - 只有端点元素 $nums[0]$（仅被首个窗口 $[0, k-1]$ 覆盖）和 $nums[n-1]$（仅被末尾窗口 $[n-k, n-1]$ 覆盖）可能满足条件（前提是它们在全局没有出现其它副本）。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码（定长滑窗模拟与分类优化法）解析：

```python
# 方案 1: 通用定长滑动窗口模拟法
class Solution:
    def largestAlmostMissingInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window_counts = Counter()

        for i in range(n - k + 1):
            window = set(nums[i : i + k]) # 窗口内部去重
            for num in window:
                window_counts[num] += 1

        candidates = [num for num, count in window_counts.items() if count == 1]
        return max(candidates) if candidates else -1

# 方案 2: O(n) 分类讨论优化法
class SolutionOptimal:
    def largestAlmostMissingInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter(nums)

        if k == 1:
            candidates = [x for x, c in cnt.items() if c == 1]
            return max(candidates) if candidates else -1

        if k == n:
            return max(nums)

        # 1 < k < n: 仅考虑两端点
        ans = -1
        if cnt[nums[0]] == 1:
            ans = max(ans, nums[0])
        if cnt[nums[-1]] == 1:
            ans = max(ans, nums[-1])
        return ans
```

1. **定长滑窗模拟**：
   - 遍历每个起点 `i`，截取窗口 `set(nums[i:i+k])`。
   - 对窗口内出现的数字在 `window_counts` 中累加 1。
   - 筛选出 `count == 1` 的所有候选值，返回最大值或 `-1`。
2. **分类讨论优化**：
   - $k=1$ 找唯一频数；$k=n$ 找最大值；其余只检查两端点 $nums[0]$ 和 $nums[-1]$ 是否全局唯一。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么在 $1 < k < n$ 时，中间的元素绝对不可能恰好出现在 1 个子数组中？”*
  - **Candidate Response**: 对于下标 $i \in [1, n-2]$，它至少会被包含在以 $i$ 结尾的窗口 $[i-k+1, i]$ 和以 $i$ 开头的窗口 $[i, i+k-1]$（以及其间的滑动窗口）中。当 $1 < k < n$ 时，覆盖 $nums[i]$ 的窗口总数至少为 $\min(k, n-k+1, i+1, n-i) \ge 2$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 同一窗口内重复元素计入多次 | 错误增加窗口计数 | 题目问的是“出现在几个子数组中”，同一子数组内多次出现只算 1 个窗口 | 统计前必须使用 `set(nums[i:i+k])` 去重 |
| 忽略两端点值相同的情况 | 当 $nums[0] == nums[-1]$ 时误判 | 若两端点值相等，则该值全局频数为 2，被 2 个不同端点窗口覆盖 | 分类讨论时使用 `cnt[nums[0]] == 1` 进行全局唯一性校验 |

### Complete Dry-Run Table / 实例推演表

输入: `nums = [3, 9, 2, 1, 7], k = 3`

| Window Range | Window Elements | Unique Set | Window Counts Updated |
|:---:|:---:|:---:|:---:|
| `[0:3]` | `[3, 9, 2]` | `{2, 3, 9}` | 2: 1, 3: 1, 9: 1 |
| `[1:4]` | `[9, 2, 1]` | `{1, 2, 9}` | 1: 1, 2: 2, 9: 2 |
| `[2:5]` | `[2, 1, 7]` | `{1, 2, 7}` | 1: 2, 2: 3, 7: 1 |

候选频数为 1 的数字: `{3, 7}`，最大为 `7`。返回 `7`。

---

## 6. Complexity Analysis / 复杂度分析

| Approach | Time Complexity | Space Complexity | Rationale |
|---|---|---|---|
| **Sliding Window Simulation** | $O(n \cdot k)$ | $O(n)$ | 共有 $n-k+1$ 个窗口，每个窗口去重和更新耗时 $O(k)$。 |
| **Mathematical Classification** | $O(n)$ | $O(n)$ | 一次全局频数统计后直接以 $O(1)$ 常数时间完成分类逻辑。 |
