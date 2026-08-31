# LC 1091: Shortest Path in Binary Matrix | 二进制矩阵中的最短路径

- **LeetCode ID**: LC 1091
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 09: 8-Directional BFS)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
- **Solution File**: [`41-lc-1091-shortest-path-in-binary-matrix.py`](problems/luffy/41-lc-1091-shortest-path-in-binary-matrix.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no such path, return -1.

### [CN] 中文描述
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中 最短畅通路径 的长度。如果不存在这样的路径，返回 -1 。

### Constraints / 约束条件
n == grid.length == grid[i].length, 1 <= n <= 100, grid[i][j] 为 0 或 1

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Search Algorithms] ➔ [BFS]`

```
┌────────────────────────────────────────────────────────┐
│ 8 方向 BFS 逐层扩散                                    │
│ 起点 (0,0) 必须为 0，终点 (n-1, n-1) 必须为 0          │
│ queue.append((0, 0, 1)), grid[0][0] = 1                │
│ 首次到达终点返回当前步数                               │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
BFS 最短路公理：无权图中 BFS 首次抵达终点所经过的步数必然为最短路径。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc1091
#shorest path in binary matrix

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]!=0:
            return -1

        rows=len(grid)
        columns=len(grid[0])
        queue=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        #initialize the queue
        queue.append((0,0))
        grid[0][0]=1

        count=1

        while queue:
            size=len(queue)

            for _ in range(size):

                x,y=queue.popleft()

                if x==rows-1 and y==columns-1:
                    return count



                for dx, dy in directions:
                    next_x=x+dx
                    next_y=y+dy

                    if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= columns:
                        continue

                    if grid[next_x][next_y]!=0:
                        continue

                    grid[next_x][next_y]=1
                    queue.append((next_x, next_y))


            count+=1

        return -1
```

1. 基于 `41-lc-1091-shortest-path-in-binary-matrix.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么入队时必须立即标记已访问，而不是出队时标记？”*
  - **Candidate**: 出队时标记会导致同一个格子被相邻多个节点重复推入队列，造成队列空间与计算量指数级爆炸膨胀。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 出队才标记访问 | 导致队列重复入队 O(8^d) 爆内存 | 标记时机错误 | 入队时必须立即 grid[nr][nc] = 1 |

### Complete Dry-Run Table / 实例推演表

grid=[[0,1],[1,0]] -> (0,0)->(1,1) 步长 2

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n^2)$ | 每个格子最多访问一次。 |
| **Space Complexity** | $O(n^2)$ | BFS 队列。 |
