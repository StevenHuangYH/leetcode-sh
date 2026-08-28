# LC 0200: Number of Islands | 岛屿数量

- **LeetCode ID**: LC 0200
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 09: Flood Fill (DFS/BFS))
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/number-of-islands/)
- **Solution File**: [`38-lc-0200-number-of-islands.py`](luffy/38-lc-0200-number-of-islands.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

### [CN] 中文描述
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

### Constraints / 约束条件
m == grid.length, n == grid[i].length, 1 <= m, n <= 300

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 沉岛策略 / 泛洪填充 (Flood Fill)                       │
│ 遍历每个格子，遇到 '1':                                │
│   ans += 1                                             │
│   DFS/BFS 扩散并将所有相连的 '1' 淹没覆写为 '0'        │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
连通分量计数定理：每次触发 DFS 扩散，恰好将一个完整的连通图全部标记/沉没。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-200
#number of islands

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        counter=0

        def dfs(row, column):
            #offside 
            if row < 0 or row >= rows or column <0 or column >= columns:
                return

            #if is water
            if grid[row][column]=="0":
                return

            #if is land
            grid[row][column]= "0"

            dfs(row-1,column)
            dfs(row+1,column)
            dfs(row,column-1)
            dfs(row,column+1)


        for row in range(rows):
            for column in range(columns):
                if grid[row][column]=="1":
                    counter+=1
                    dfs(row,column)

        return counter
```

1. 基于 `38-lc-0200-number-of-islands.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“DFS 与并查集 (Union-Find) 解决本题有何区别？”*
  - **Candidate**: DFS 实现最简且时间 $O(mn)$；并查集适合动态增删陆地（如 LC 305 动态岛屿）的在线维护场景。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 未标记访问导致死循环 | 相邻格子互相调用递归爆栈 | 无限循环 | 必须在进入时立即 grid[r][c] = '0' |

### Complete Dry-Run Table / 实例推演表

4x5 网格遇到首个 '1' -> 沉没整座岛 -> 答案加 1

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(m \cdot n)$ | 每个格子最多访问常数次。 |
| **Space Complexity** | $O(m \cdot n)$ | 递归栈最坏铺满网格。 |
