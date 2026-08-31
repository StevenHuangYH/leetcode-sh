# LC 0167: Two Sum II - Input Array Is Sorted | 两数之和 II - 输入有序数组

- **LeetCode ID**: LC 0167
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 01: Two Pointers)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/two-sum-ii---input-array-is-sorted/)
- **Solution File**: [`03-lc-0167-two-sum-ii-input-array-is-sorted.py`](problems/luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.

### [CN] 中文描述
给你一个下标从 1 开始的整数数组 `numbers` ，该数组已按非递减顺序排列 ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。

### Constraints / 约束条件
2 <= numbers.length <= 3 * 10^4, -1000 <= numbers[i] <= 1000

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Two Pointer]`

```
┌────────────────────────────────────────────────────────┐
│ 相向双指针对撞: sum < target -> left++; sum > target -> right-- │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
单调性逼近：利用有序性两端相向移动指针收缩解空间。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(numbers):
            other = target - item
            if other in cache:
                return(cache[other]+1,i+1)
            cache[item] = i


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer approach
        left = 0
        right = len(numbers) - 1
        while left != right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return[left+1, right+1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1


#two pointer approach is more efficient than hash table approach in this case 
# because the input list is sorted. The two pointer approach has a time complexity of O(n) 
# and a space complexity of O(1), while the hash table approach has a time complexity of O(n) 
# but a space complexity of O(n) due to the additional storage used for the hash table.
            
            
#note:
#if the list is already sorteed
#two pointer approach is the general methond
```

1. 基于 `03-lc-0167-two-sum-ii-input-array-is-sorted.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何做到 O(1) 空间？”*
  - **Candidate**: 采用相向双指针代替哈希表。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 下标未 +1 | 返回 0-based 索引 | 题目要求 1-based | 输出时统一 +1 |

### Complete Dry-Run Table / 实例推演表

输入: `numbers=[2,7,11,15], target=9` -> `[1,2]`

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 左右指针相向单调移动。 |
| **Space Complexity** | $O(1)$ | 仅需双指针（源码若用哈希则为 O(n)）。 |
