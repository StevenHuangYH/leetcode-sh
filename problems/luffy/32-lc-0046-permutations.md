# LC 0046: Permutations | 全排列

- **LeetCode ID**: LC 0046
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 08: Backtracking)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/permutations/)
- **Solution File**: [`32-lc-0046-permutations.py`](problems/luffy/32-lc-0046-permutations.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array `nums` of distinct integers, return all the possible permutations.

### [CN] 中文描述
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。

### Constraints / 约束条件
1 <= nums.length <= 6

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

```
┌────────────────────────────────────────────────────────┐
│ 回溯全排列: used 标记数组 或 原地 swap 交换            │
│ 每层递归选择一个未被 used 的元素加入 path              │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
排列有序性：每个位置均可选取任意未被前序位置占用的元素。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-46

#permutation

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]

        
        def backtrack():
            if len(path)==len(nums):
                result.append(path.copy())
                return



            for i in range(len(nums)):
                if nums[i] in path:
                    continue


                path.append(nums[i])

                backtrack()
                path.pop()


        backtrack()
        return result
    


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]

        used = [False] * len(nums) #hashtable




        def backtrack():
            if len(path)==len(nums):
                result.append(path.copy())
                return



            for i in range(len(nums)):
                if used[i]:
                    continue


                path.append(nums[i])
                used[i]=True
                backtrack()
                path.pop()
                used[i]=False#reset as False  归位


        backtrack()
        return result
```

1. 基于 `32-lc-0046-permutations.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果数组中包含重复数字（LC 47），该如何去重？”*
  - **Candidate**: 先排序，在同一树层遇 `nums[i] == nums[i-1]` 且 `not used[i-1]` 时跳过剪枝。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 忘记 path.pop() 恢复现场 | 回溯状态污染后续分支 | 未回溯 | 递归后必须执行 path.pop() |

### Complete Dry-Run Table / 实例推演表

nums=[1,2,3] -> 6 种全排列

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n! \cdot n)$ | 全排列数 $n!$。 |
| **Space Complexity** | $O(n)$ | 递归栈与 used 标记。 |
