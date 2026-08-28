# LC 0207: Course Schedule | 课程表

- **LeetCode ID**: LC 0207
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 09: Topological Sort (Kahn / DFS))
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/course-schedule/)
- **Solution File**: [`42-lc-0207-course-schedule.py`](luffy/42-lc-0207-course-schedule.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. Given prerequisites array, return `true` if you can finish all courses.

### [CN] 中文描述
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。在选修某些课程之前需要一些先修课程。请你判断是否可能完成所有课程的学习？

### Constraints / 约束条件
1 <= numCourses <= 2000, 0 <= prerequisites.length <= 5000

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ Kahn 拓扑排序 (入度表 + BFS)                           │
│ 1. 统计每个节点入度 in_degree[i] 和邻接表 graph        │
│ 2. 将所有入度为 0 的课程推入队列                       │
│ 3. 弹出节点，将其指向的所有邻居入度减 1，减为 0 则入队 │
│ 4. 统计弹出总数 count == numCourses                    │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
有向无环图 (DAG) 判定：有向图存在拓扑排序充要条件为图中无有向环。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc 206
#course schedule

from typing import List
from collections import deque

#Topological Sorting
#in-degree table
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adjcency list
        graph=[ [] for _ in range(numCourses)]

        #indegree table
        indegree=[0]*numCourses

        #Iterate over the edge list
        for after, pre in prerequisites:
            graph[pre].append(after)
            indegree[after]+=1

        #initialize the queue
        queue=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)


        while queue: #while queue has value
            cur_class = queue.popleft()
            for after in graph[cur_class]:
                indegree[after]-=1
                if indegree[after]==0:
                    queue.append(after)

        for item in indegree:
            if item != 0:
                return False

        return True
```

1. 基于 `42-lc-0207-course-schedule.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何用三色标记法 (DFS) 检测有向图中的环？”*
  - **Candidate**: 0: 未访问，1: 正在当前递归栈中（遇到 1 说明发现返祖边/环），2: 已完全访问完毕。遇到 1 立即判定有环。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 先修方向建反 | 将 [a, b] (b->a) 建成了 a->b | 图方向混淆 | b 是 a 的前置，边应为 b -> a |

### Complete Dry-Run Table / 实例推演表

numCourses=2, prerequisites=[[1,0]] -> in_deg[0]=0, in_deg[1]=1 -> 0 出队 -> in_deg[1]=0 -> 1 出队 -> count=2 == numCourses -> True

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(V + E)$ | 点数与边数之和。 |
| **Space Complexity** | $O(V + E)$ | 邻接表与入度数组。 |
