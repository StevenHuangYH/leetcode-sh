# LC 0077: Combinations | 组合

- **LeetCode ID**: LC 0077
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 08: Backtracking)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/combinations/)
- **Solution File**: [`31-lc-0077-combinations.py`](problems/luffy/31-lc-0077-combinations.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

### [CN] 中文描述
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

### Constraints / 约束条件
1 <= n <= 20, 1 <= k <= n

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

```
┌────────────────────────────────────────────────────────┐
│ 回溯树剪枝: 当剩余候选数不足以填满 k 时立即剪枝        │
│ 上界: i <= n - (k - len(path)) + 1                     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
组合无序性：通过规定后选数字严格大于当前数字（`for i in range(start, ...)`）消除重复排列。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-77
#Combinations


#backtracking algorithm
#N-ary Tree
#pick or don't pick / 0-1 decision tree


from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #like when n=4, nums=[1,2,3,4]
        nums=[i for i in range(1, n+1)]
        result=[]

        def backtrack(path, start_index):
            if len(path)==k:
                result.append(path[:]) #deepcopy
                return


            for i in range (start_index, len(nums)): # in charge horizontal of the n-ary tree
                path.append(nums[i]) #make selection
                                     #recursion in charge the vertical part
                backtrack(path, i+1) #recursive, pass through next index and path 
                #path is a list

                path.pop()#cancel the selection / backtracking


        backtrack([], 0) #empty list for path. as the resusion goes deeper, numbers will be added to it
                         # starting index from 0
        return result 
        


class Solution2:
    def combine(self,n:int , k:int)-> List[List[int]]:
                #like when n=4, nums=[1,2,3,4]
        nums=[i for i in range(1, n+1)]
        result=[]
        path=[]

        def backtrack(start_index):
            if len(path)==k:
                result.append(path[:]) #deepcopy
                return


            for i in range (start_index, len(nums)): # in charge horizontal of the n-ary tree
                path.append(nums[i]) #make selection
                                     #recursion in charge the vertical part
                backtrack( i+1) #recursive, pass through next index and path 
                #path is a list

                path.pop()#cancel the selection / backtracking


        backtrack( 0) #empty list for path. as the resusion goes deeper, numbers will be added to it
                         # starting index from 0
        return result 




#0-1 decision tree
class Solution3:
    def combine(self, n:int, k:int) -> List[List[int]]:
        result=[]
        path=[]

        def backtrack(cur_num): #cur_num -> pointer for tracking num
            if len(path)==k:
                result.append(path[:]) #deepcopy
                return


            if cur_num > n: #edge case for the pointer
                return

            #pick
            path.append(cur_num)
            backtrack(cur_num+1)

            #backtrack
            path.pop()
            
            #not pick
            backtrack(cur_num+1)

        backtrack(1)
        return result
```

1. 基于 `31-lc-0077-combinations.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“组合剪枝的上界是如何推导出来的？”*
  - **Candidate**: 还需选 $k - |path|$ 个数，从 $i$ 到 $n$ 共有 $n - i + 1$ 个数，令 $n - i + 1 \ge k - |path|$ 即可解出 $i \le n - (k - |path|) + 1$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 未做剪枝遍历过多无效分支 | 无剪枝暴搜超时 | 效率低下 | 添加上界剪枝优化 |

### Complete Dry-Run Table / 实例推演表

n=4, k=2 -> [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(C(n, k) \cdot k)$ | 组合数乘以单次复制耗时。 |
| **Space Complexity** | $O(k)$ | 递归路径深度。 |
