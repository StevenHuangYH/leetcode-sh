# LC 0078: Subsets | 子集

- **LeetCode ID**: LC 0078
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 08: Backtracking)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/subsets/)
- **Solution File**: [`33-lc-0078-subsets.py`](luffy/33-lc-0078-subsets.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

### [CN] 中文描述
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

### Constraints / 约束条件
1 <= nums.length <= 10, -10 <= nums[i] <= 10

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 子集生成两大流派:                                      │
│ 1. 选/不选二叉树 (0-1 Pick / Skip)                     │
│ 2. 枚举下一个元素多叉树 (Every Node is a Solution)     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
幂集完全性：长度为 $n$ 的集合恰好存在 $2^n$ 个互异子集。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-78
#subsets


from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[] 

        def dfs(i):
            if i>=len(nums):
                result.append(path.copy())
                return
            #pick
            path.append(nums[i])
            dfs(i+1)

            #backtrack
            path.pop()

            #not pick
            dfs(i+1)


        dfs(0)
        return result
```

1. 基于 `33-lc-0078-subsets.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何用二进制位掩码 (Bitmask) 非递归生成子集？”*
  - **Candidate**: 遍历 $0$ 到 $2^n - 1$ 的每一个整数 $mask$，若第 $i$ 位为 1 则将 $nums[i]$ 放入当前子集。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 忘记 path.copy() | 追加引用导致最终全是空列表 | 浅拷贝失误 | ans.append(path.copy()) |

### Complete Dry-Run Table / 实例推演表

nums=[1,2,3] -> 8 个子集

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(2^n \cdot n)$ | 共 $2^n$ 个子集，复制每个耗时 $O(n)$。 |
| **Space Complexity** | $O(n)$ | 路径栈。 |
