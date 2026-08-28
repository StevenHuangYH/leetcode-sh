# LC 0102: Binary Tree Level Order Traversal | 二叉树的层序遍历

- **LeetCode ID**: LC 0102
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 07: Tree BFS)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- **Solution File**: [`28-lc-0102-binary-tree-level-order-traversal.py`](luffy/28-lc-0102-binary-tree-level-order-traversal.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the `root` of a binary tree, return the level order traversal of its nodes' values.

### [CN] 中文描述
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。

### Constraints / 约束条件
树中节点数目在范围 [0, 2000] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 队列 BFS / 双缓冲区层序遍历                            │
│ while queue:                                           │
│   for _ in range(len(queue)): 弹出并收集当前层所有节点 │
│   将该层子节点加入队列，结果存入 ans                   │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
层级隔离不变量：通过 `len(queue)` 快照或双列表隔离上一层与下一层节点。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-102

#Binary Tree level order traversal

from collections import deque #底层是double linked list
from typing import Optional, List

#bfs
#breadth-first search bfs

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        res=[]

        while queue:
            n=len(queue)
            cur_level=[]
            for i in range(n):
                node=queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_level)

        return res
```

1. 基于 `28-lc-0102-binary-tree-level-order-traversal.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何用 DFS 递归实现层序遍历？”*
  - **Candidate**: DFS 入参携带 `depth`，若 `depth == len(ans)` 则 `ans.append([])`，将 `node.val` 追加到 `ans[depth]`。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 动态修改队列导致长度变化 | 在 for 循环中未固定当前层长度 | 层级混淆 | 必须使用 for _ in range(len(q)) 快照 |

### Complete Dry-Run Table / 实例推演表

root=[3,9,20,null,null,15,7] -> [[3], [9, 20], [15, 7]]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个节点入队出队一次。 |
| **Space Complexity** | $O(n)$ | 最宽层最多 $n/2$ 个节点。 |
