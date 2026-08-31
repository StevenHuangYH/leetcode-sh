# LC 0994: Rotting Oranges | 腐烂的橘子

- **LeetCode ID**: LC 0994
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 09: Multi-source BFS)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/rotting-oranges/)
- **Solution File**: [`40-lc-0994-rotting-oranges.py`](problems/luffy/40-lc-0994-rotting-oranges.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
You are given an `m x n` grid where each cell can have one of three values: 0 empty, 1 fresh orange, 2 rotten orange. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If impossible, return -1.

### [CN] 中文描述
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一: 0 空, 1 新鲜橘子, 2 腐烂橘子。返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

### Constraints / 约束条件
1 <= m, n <= 10

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Search Algorithms] ➔ [BFS]`

```
┌────────────────────────────────────────────────────────┐
│ 多源广度优先搜索 (Multi-source BFS)                   │
│ 1. 将所有初始腐烂橘子 '2' 同时压入队列，统计新鲜数     │
│ 2. 按分钟层序 BFS 扩散腐烂相邻 '1'，fresh -= 1         │
│ 3. 若 fresh == 0 返回 minutes，否则返回 -1             │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
多源波前同步性：所有腐烂源以相同速度向外蔓延，层序步数即为全局最短扩散时间。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-994
#rotting oranges

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        queue=deque()

        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        #count how many fresh orange in total
        fresh_count=0
        for row in range(rows):
            for column in range(columns):
                cur_num = grid[row][column]
                if cur_num==2:
                    queue.append((row,column))
                elif cur_num==1:
                    fresh_count+=1

        minutes=0

        if len(queue)==0 and fresh_count==0:
            return 0

        while queue:
            size=len(queue)
            for _ in range(size):

                row,column=queue.popleft()

                for dx, dy in directions:
                    next_row=row+dx
                    next_column=column+dy

                    #out of boundary
                    if next_row<0 or next_row>=rows or next_column<0 or next_column>= columns:
                        continue     

                    #not fresh orange
                    if grid[next_row][next_column]!=1:
                        continue

                    grid[next_row][next_column]=2
                    fresh_count-=1
                    queue.append((next_row,next_column))

            minutes+=1

        if fresh_count>0:
                return -1

        return minutes-1 #-1 since it would takes one more round to check if there anymore fresh orange.
        

class Solution1:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue=deque()
        minutes=0

        # 统计一共多少新鲜橘子
        fresh_count=0
        for row in range(rows):
            for column in range(columns):
                cur_num=grid[row][column]
                if cur_num==1 :
                    fresh_count+=1
                elif cur_num==2:
                    queue.append((row,column))


        while queue and fresh_count > 0:
            size=len(queue)
            for _ in range(size):
                row,column=queue.popleft()
                for dx,dy in directions:
                    next_row=row+dx
                    next_column=column+dy

                    # 越界
                    if next_row<0 or next_row>=rows or next_column<0 or next_column>=columns:
                        continue

                    # 不是新鲜橘子
                    if grid[next_row][next_column]!=1:
                        continue

                    grid[next_row][next_column]=2
                    fresh_count-=1
                    queue.append((next_row,next_column))

            minutes+=1

        if fresh_count>0:
            return -1

        return minutes
```

1. 基于 `40-lc-0994-rotting-oranges.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果初始没有新鲜橘子，应返回几分钟？”*
  - **Candidate**: 直接返回 0 分钟，初始判空特判 `if fresh == 0: return 0`。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 初始无新鲜橘子返回非 0 | fresh=0 错误返回 minutes | 边界特判 | 初始 fresh==0 直接 return 0 |

### Complete Dry-Run Table / 实例推演表

grid=[[2,1,1],[1,1,0],[0,1,1]] -> 4 分钟全部腐烂

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(m \cdot n)$ | 每个格子最多入队出队一次。 |
| **Space Complexity** | $O(m \cdot n)$ | BFS 队列空间。 |
