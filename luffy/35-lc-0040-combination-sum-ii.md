# LC 0040: Combination Sum II | 组合总和 II

- **LeetCode ID**: LC 0040
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 08: Backtracking)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/combination-sum-ii/)
- **Solution File**: [`35-lc-0040-combination-sum-ii.py`](luffy/35-lc-0040-combination-sum-ii.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations where candidate numbers sum to `target`. Each number may only be used once in the combination.

### [CN] 中文描述
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。candidates 中的每个数字在每个组合中只能使用 一次 。

### Constraints / 约束条件
1 <= candidates.length <= 100, 1 <= candidates[i] <= 50, 1 <= target <= 30

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

```
┌────────────────────────────────────────────────────────┐
│ 树层去重 (Breadth Deduplication)                       │
│ 排序 candidates;                                       │
│ 在同层 for 循环中: if i > start and nums[i] == nums[i-1]: continue │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
树枝可重，树层去重：同一路径可包含原数组中的重复值，但同一分叉层不能选取相同数值开头。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-40
#combination sum 2
from typing import List


#Deduplication

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]

        candidates.sort() #sorting first


        def dfs(starting_index, cur_sum):
            if cur_sum == target:
                result.append(path.copy())   
                return


            for i in range(starting_index, len(candidates)):
                #pruning here:
                if cur_sum+candidates[i]>target:
                    break


                #deduplication 去重
                if i > starting_index and candidates[i]==candidates[i-1]:
                    continue

                #track back here
                path.append(candidates[i])

                #since every number could only used once so i+1
                dfs(i+1,cur_sum+candidates[i]) 
                path.pop()


        dfs(0,0)
        return result
```

1. 基于 `35-lc-0040-combination-sum-ii.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么 `i > start` 能区分树层重复和树枝重复？”*
  - **Candidate**: `i == start` 是当前树枝向下深入探索的第一个元素（允许与前一个数值相同）；`i > start` 则是同一层回溯后的横向切换（禁止选取相同值）。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 误用 i > 0 | 将树枝上的合法相同数也剪掉了 | 过度剪枝 | 必须判定 i > start |

### Complete Dry-Run Table / 实例推演表

candidates=[10,1,2,7,6,1,5], target=8 -> [[1,1,6],[1,2,5],[1,7],[2,6]]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(2^n)$ | 搜索树剪枝。 |
| **Space Complexity** | $O(n)$ | 递归栈。 |
