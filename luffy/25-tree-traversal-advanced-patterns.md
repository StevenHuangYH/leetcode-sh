# LC 0094: Tree Traversal Advanced Patterns | 二叉树高级遍历与构造模式

- **LeetCode ID**: LC 0094
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 07: Advanced Tree Patterns)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/tree-traversal-advanced-patterns/)
- **Solution File**: [`25-tree-traversal-advanced-patterns.py`](luffy/25-tree-traversal-advanced-patterns.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Comprehensive paradigms for tree serialization, iterative traversals, and multi-threaded tree patterns.

### [CN] 中文描述
二叉树迭代遍历、序列化与线索化高级模式汇总。

### Constraints / 约束条件
通用二叉树结构

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 树遍历三大范式: 递归分治 / 显式辅助栈 / Morris 线索化 │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
拓扑结构一致性：遍历序列与树结构一一映射。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List,Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#use stack
#iterative method
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res=[]
        stack=[root]

        while stack:
            node=stack.pop()
            res.append(node.val)

            #pushing logic
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
```

1. 基于 `25-tree-traversal-advanced-patterns.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“哪两种遍历序列组合可以唯一确定一棵二叉树？”*
  - **Candidate**: 前序+中序，或后序+中序（必须包含中序遍历以划分左右子树）。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 前序+后序试图唯一确定一般树 | 非满二叉树存在歧义 | 歧义性 | 必须有中序才能准确定位左右子树 |

### Complete Dry-Run Table / 实例推演表

Tree DFS/BFS 统一调度模板

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 遍历全体节点。 |
| **Space Complexity** | $O(n)$ | 辅助栈。 |
