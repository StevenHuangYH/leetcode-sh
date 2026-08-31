# LC 0059: Spiral Matrix II | 螺旋矩阵 II

- **LeetCode ID**: LC 0059
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 01: Matrix Simulation)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/spiral-matrix-ii/)
- **Solution File**: [`08-lc-0059-spiral-matrix-ii.py`](problems/luffy/08-lc-0059-spiral-matrix-ii.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a positive integer `n`, generate an `n x n` matrix filled with elements from 1 to `n^2` in spiral order.

### [CN] 中文描述
给你一个正整数 `n` ，生成一个包含 1 到 `n^2` 所有元素，且元素按顺时针顺序螺旋排列的 `n x n` 正方形矩阵 `matrix` 。

### Constraints / 约束条件
1 <= n <= 20

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Array Basics] ➔ [2D Array]`

```
┌────────────────────────────────────────────────────────┐
│ 四界收缩法: top, bottom, left, right 顺时针依次推进    │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
边界收缩不变量：每填满一行或一列，对应边界内缩 1 位。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List


# use for loop
# mat[row][column]
# i -> row  up to buttom index
# j -> left to right index
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [
            [0]*n for _ in range(n)
        ]
        count = 1
        init_index = 0

        while not count >= n**2: #跳出循环条件取反
            for j in range(init_index, n-1-init_index):
                mat[init_index][j] = count
                count += 1
            for i in range(init_index, n-1-init_index):
                mat[i][n-1-init_index] = count
                count += 1
            for j in range(n-1-init_index, init_index, -1):
                mat[n-1-init_index][j] = count
                count += 1
            for i in range(n-1-init_index, init_index, -1):
                mat[i][init_index]= count
                count += 1

            init_index += 1
        
        if n%2==1:
            mat[n//2][n//2]=count
        return mat


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
```

1. 基于 `08-lc-0059-spiral-matrix-ii.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何推广到 m x n 矩阵？”*
  - **Candidate**: 逻辑相同，但每边遍历前需加边界重叠判定。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 转角重复填 | 转角格子被多次赋值 | 边界开闭混淆 | 严格使用收缩后的界限 |

### Complete Dry-Run Table / 实例推演表

输入: `n=3` -> 依次填外圈 1-8，中心 9

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n^2)$ | 填满所有格子。 |
| **Space Complexity** | $O(1)$ | 除返回矩阵外常数空间。 |
