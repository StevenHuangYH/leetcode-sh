# LC 0145: Binary Tree Postorder Traversal | 二叉树的后序遍历

- **LeetCode ID**: LC 0145
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 07: Tree Traversal)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- **Solution File**: [`25-lc-0145-binary-tree-postorder-traversal.py`](luffy/25-lc-0145-binary-tree-postorder-traversal.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

### [CN] 中文描述
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

### Constraints / 约束条件
树中节点的数目在范围 [0, 100] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 后序遍历 DFS (Left -> Right -> Root)                   │
│ 分治与树形 DP 的天然遍历顺序                           │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
左右根归纳不变量：必须先收集完左右子树的全部信息，再在根节点进行状态合并。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc 145 
#binary tree postorder traversal

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def f(node:Optional[TreeNode]):
            if node is None:
                return

            f(node.left)

            f(node.right)

            res.append(node.val)


            return

        f(root)
        return res
```

1. 基于 `25-lc-0145-binary-tree-postorder-traversal.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么树形 DP 大多基于后序遍历？”*
  - **Candidate**: 树形 DP 需要子树的计算结果（高度、最优值）自底向上汇总至当前根节点。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 左右子树未完全遍历即返回 | 过早返回局部状态 | 后序逻辑混淆 | 先递归 left/right 再处理 root |

### Complete Dry-Run Table / 实例推演表

root=[1,null,2,3] -> [3, 2, 1]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个节点遍历一次。 |
| **Space Complexity** | $O(n)$ | 递归栈。 |
