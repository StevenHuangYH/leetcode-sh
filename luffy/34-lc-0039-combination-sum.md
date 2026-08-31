# LC 0039: Combination Sum | 组合总和

- **LeetCode ID**: LC 0039
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 08: Backtracking)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/combination-sum/)
- **Solution File**: [`34-lc-0039-combination-sum.py`](luffy/34-lc-0039-combination-sum.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations where the chosen numbers sum to `target`.

### [CN] 中文描述
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 。

### Constraints / 约束条件
1 <= candidates.length <= 30, 2 <= candidates[i] <= 40, 1 <= target <= 40

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

```
┌────────────────────────────────────────────────────────┐
│ 可重复选择的组合回溯                                   │
│ 排序后递归: dfs(remain - x, i) (传 i 允许重复选自身)  │
│ 若 remain - x < 0: 立即 break 剪枝                     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
非降序消除排列重复：下一次选择只能从下标 $\ge i$ 的候选数中挑选。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc39

#combination Sum
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]

        def backtrack(cur_sum, starting_index):
            if cur_sum == target:
                result.append(path.copy())
                return


            if cur_sum>target:
                return


            for i in range(starting_index, len(candidates)):
                path.append(candidates[i])
                backtrack(cur_sum+candidates[i], i) 
                #cur_sum + candidates[i]: add the current candidate to cur_sum for updating the current sum
                #i: pass i as the starting index 
                #this is becuase problem allows us to reuse the same number an unlimited number of times


                path.pop()

        backtrack(0,0)
        return result            


#pruning after sorting
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        candidates.sort()

        def backtrack(cur_sum, starting_index):
            if cur_sum == target:
                result.append(path.copy())
                return


            if cur_sum>target:
                return


            for i in range(starting_index, len(candidates)):


                #pruning
                if cur_sum + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(cur_sum+candidates[i], i) 
                #cur_sum + candidates[i]: add the current candidate to cur_sum for updating the current sum
                #i: pass i as the starting index 
                #this is becuase problem allows us to reuse the same number an unlimited number of times


                path.pop()

        backtrack(0,0)
        return result      



#pick or not pick
class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]

        def dfs(i, cur_sum):
            if cur_sum == target:
                result.append(path.copy())
                return

            if  i >= len(candidates):
                return

            if cur_sum >=target:
                return

            path.append(candidates[i])
            dfs(i, cur_sum+candidates[i])
            path.pop()

            dfs(i+1, cur_sum)

        dfs(0,0)
        return result
```

1. 基于 `34-lc-0039-combination-sum.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么传 i 而不是 i + 1？”*
  - **Candidate**: 题目允许同一个数字被无限制重复选取，因此递归入参继续保留当前下标 $i$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 未排序就 break 剪枝 | 无序数组 break 误剪有效分支 | 过早剪枝 | 必须先排序后才能 break |

### Complete Dry-Run Table / 实例推演表

candidates=[2,3,6,7], target=7 -> [2,2,3], [7]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(S)$ | $S$ 为所有可行解长度之和。 |
| **Space Complexity** | $O(target)$ | 最坏全选最小元素递归深度。 |
