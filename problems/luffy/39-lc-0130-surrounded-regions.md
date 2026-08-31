# LC 0130: Surrounded Regions | 被围绕的区域

- **LeetCode ID**: LC 0130
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 09: 2D Grid DFS)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/surrounded-regions/)
- **Solution File**: [`39-lc-0130-surrounded-regions.py`](problems/luffy/39-lc-0130-surrounded-regions.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an `m x n` matrix `board` containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

### [CN] 中文描述
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：连接所有与 'X' 边缘不相连的 'O' 并替换为 'X'。

### Constraints / 约束条件
1 <= m, n <= 200

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [DFS]`

```
┌────────────────────────────────────────────────────────┐
│ 逆向思维: 从四条边界的 'O' 出发 DFS 标记为 'A' (保活)  │
│ 遍历全图: 'A' 恢复为 'O' (边界相连未被包围)            │
│           'O' 捕获为 'X' (被包围)                      │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
边界连通等价性：任何没有被完全包围的 'O' 必然至少与一条外边界上的某个 'O' 四向连通。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc 130
#surrounded regions
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        columns=len(board[0])

        def dfs(row,column): #replace O as #
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return

            # #if current cell is X, do nothing:
            # if board[row][column]=="X":
            #     return

            # if board[row][column]=="#": 不要走回头路
            #     return   

            if board[row][column]!="O":
                return       

            board[row][column]="#"

            dfs(row-1,column)
            dfs(row+1,column)
            dfs(row,column-1)
            dfs(row,column+1)

        #Boundary Traversal
        for row in range(rows):
            if board[row][0]=="O":
                dfs(row,0)
            if board[row][columns-1]=="O":
                dfs(row,columns-1)

        for column in range(columns):
            if board[0][column]=="O":
                dfs(0,column)
            if board[rows-1][column]=="O":
                dfs(rows-1,column)

        #travel the entire gird, replace # as O, replace O as X
        for row in range(rows):
            for column in range(columns):
                if board[row][column]=="#":
                    board[row][column]="O"
                elif board[row][column]=="O": #reminder: use elif
                    board[row][column]="X"
```

1. 基于 `39-lc-0130-surrounded-regions.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么从边界反向搜索优于从内部正向搜索？”*
  - **Candidate**: 内部正向搜索需要走到边界才能判断是否被包围，状态回溯繁琐；从边界出发只需单向标记，逻辑极为清晰。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 漏扫某条边界 | 只扫描了第一行第一列 | 遗漏四边 | 四条边界需全部启动 DFS |

### Complete Dry-Run Table / 实例推演表

边界 'O' -> 'A' -> 内部 'O' 变 'X' -> 'A' 恢复 'O'

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(m \cdot n)$ | 网格遍历与 DFS 访问。 |
| **Space Complexity** | $O(m \cdot n)$ | DFS 递归栈。 |
