# LC 0041: First Missing Positive | 缺失的第一个正数

- **LeetCode ID**: LC 0041
- **Difficulty**: Hard
- **Category**: Luffy Structured Curriculum (Topic 04: In-Place Hashing (Cyclic Sort))
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/first-missing-positive/)
- **Solution File**: [`14-lc-0041-first-missing-positive.py`](luffy/14-lc-0041-first-missing-positive.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an unsorted integer array `nums`. Return the smallest positive integer that is not present in `nums`. You must implement an algorithm that runs in $O(n)$ time and uses $O(1)$ auxiliary space.

### [CN] 中文描述
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

### Constraints / 约束条件
1 <= nums.length <= 10^5, -2^31 <= nums[i] <= 2^31 - 1

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 原地哈希 / 归位法 (Cyclic Sort)                         │
│ 数字 x (1 <= x <= n) 应该放在下标 x - 1 处             │
│ while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:│
│   swap(nums[i], nums[nums[i]-1])                       │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
归位不变量：扫描后 $nums[i] == i + 1$ 成立，首个不满足处即为缺失正整数。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-41-missing-postive

from typing import List
#make array as your hash table

#auxiliary space required
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         i=1
#         while True:
#             if i in nums:
#                 i=i+1
#             else:
#                 return i
#         #o(n)
            


# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         num_sets = set(nums) #O(n) space-> wrong
#         i=1
#         while True:
#             if i in num_sets:
#                 i=i+1
#             else:
#                 return i



class Solution: #partition 归位
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            num=nums[i]
            if i==num-1: #partition
                i=i+1
            else: # not on the right postiton
                if 1<=num<=len(nums) and nums[nums[i]-1] !=nums[i]: # 1 to n, should be in num-1
                    # target=nums[num-1]
                    # nums[num-1]=num
                    # nums[i]=target
                    nums[i], nums[num-1]=nums[num-1], nums[i] #交换写法
                    #right side becomes a tuple
                else: #number that is not qualify for partition
                    i=i+1

        #traversal for the num again
        for i in range(len(nums)):
            if i ==nums[i]-1:
                pass
            else:
                return i+1
        
        return len(nums)+1
```

1. 基于 `14-lc-0041-first-missing-positive.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么 while 循环不会导致 O(n^2) 时间复杂度？”*
  - **Candidate**: 每次有效 swap 都会让至少一个数字回到正确位置，每个数字最多被归位一次，总 swap 次数不超过 $n$ 次，总时间严格为 $O(n)$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 死循环 | swap 两个相同数字 nums[i] == nums[target] | 未防御重复元素 | 条件必须为 nums[nums[i]-1] != nums[i] |

### Complete Dry-Run Table / 实例推演表

nums=[3,4,-1,1] -> 归位后 [1,-1,3,4] -> 下标 1 处为 -1 != 2 -> 返回 2

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个数字最多交换一次。 |
| **Space Complexity** | $O(1)$ | 原地数组哈希。 |
