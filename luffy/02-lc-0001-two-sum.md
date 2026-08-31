# LC 0001: Two Sum | 两数之和

- **LeetCode ID**: LC 0001
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 01: Arrays & Hash Table)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/two-sum/)
- **Solution File**: [`02-lc-0001-two-sum.py`](luffy/02-lc-0001-two-sum.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

### [CN] 中文描述
给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。

### Constraints / 约束条件
2 <= nums.length <= 10^4, -10^9 <= nums[i] <= 10^9, -10^9 <= target <= 10^9

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Data Structures] ➔ [Hashing]`

```
┌────────────────────────────────────────────────────────┐
│ 单遍哈希探测 target - x                                 │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
前缀补数映射：对于当前 $x$，查先前集合是否存在 $target - x$。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List

class Solution3: #even better hash table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(nums):
            other = target - item
            if other in cache:
                return [i, cache[other]]
            cache[item] = i
        return []


#when you need to find two numbers in a list that add up to a specific target, 
# you can use a hash table (dictionary) to store the numbers you've seen so far and their indices. This allows you to check in constant time if the complement (the number needed to reach the target) exists in the hash table. The provided code implements this approach efficiently.
```

1. 基于 `02-lc-0001-two-sum.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“单遍边查边存的优势？”*
  - **Candidate**: 避免遍历两次并天然消除元素自匹配 Bug。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 自匹配陷阱 | target=6, nums=[3,3] 返回 [0,0] | 未排除自身 | 单遍哈希边查边存 |

### Complete Dry-Run Table / 实例推演表

输入: `nums=[2,7,11,15], target=9` -> `[0,1]`

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 遍历一次数组。 |
| **Space Complexity** | $O(n)$ | 哈希表大小。 |
