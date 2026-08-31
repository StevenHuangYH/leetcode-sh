# LC 0560: Subarray Sum Equals K | 和为 K 的子数组

- **LeetCode ID**: LC 0560
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 03: Prefix Sum + Hash Map)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/subarray-sum-equals-k/)
- **Solution File**: [`11-lc-0560-subarray-sum-equals-k.py`](luffy/11-lc-0560-subarray-sum-equals-k.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

### [CN] 中文描述
给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 该数组中和为 `k` 的子数组的个数 。

### Constraints / 约束条件
1 <= nums.length <= 2 * 10^4, -1000 <= nums[i] <= 1000, -10^7 <= k <= 10^7

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Array Basics] ➔ [Prefix Sum]`

```
┌────────────────────────────────────────────────────────┐
│ 前缀和 + 哈希频次表                                    │
│ s = sum(nums[0...i])                                   │
│ 若 s - k 在哈希表中，累计出现次数 ans += cnt[s - k]    │
│ 累加当前前缀和频次 cnt[s] += 1                         │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
子数组和转化等式：$$\text{sum}(i, j) = s_j - s_{i-1} = k \iff s_{i-1} = s_j - k$$

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List

#can not use sliding window
#sliding window is only applicable when the elements are all positive numbers or negative numbers, but not both


#use prefix sum and hashtable to store the prefix sum and its frequency
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            preSum[i+1]= preSum[i]+nums[i]

        
        cache={}
        count=0
        for i, item in enumerate(preSum):
            other = item - k
            if other in cache:
                count+=cache[other]
            cache[item]=cache.get(item,0)+1

        return count
    
#O(n)
```

1. 基于 `11-lc-0560-subarray-sum-equals-k.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么不能用滑动窗口求解本题？”*
  - **Candidate**: 数组中包含负数，窗口扩大或缩小不具备和的单调性，必须使用前缀和哈希表。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 漏初始前缀和 {0:1} | 前缀和本身等于 k 时漏计 | 边界遗漏 | 必须初始化 cnt = {0: 1} |

### Complete Dry-Run Table / 实例推演表

输入: `nums=[1,1,1], k=2` -> s=1(+0), s=2(+1), s=3(+1) -> ans=2

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 单遍扫描数组。 |
| **Space Complexity** | $O(n)$ | 哈希表大小。 |
