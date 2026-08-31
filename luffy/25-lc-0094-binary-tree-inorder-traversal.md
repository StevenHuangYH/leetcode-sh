# LC 0094: Binary Tree Inorder Traversal | 二叉树的中序遍历

- **LeetCode ID**: LC 0094
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 07: Tree Traversal)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- **Solution File**: [`25-lc-0094-binary-tree-inorder-traversal.py`](luffy/25-lc-0094-binary-tree-inorder-traversal.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

### [CN] 中文描述
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

### Constraints / 约束条件
树中节点数目在范围 [0, 100] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Tree Paradigms] ➔ [Recursive Traverse]`

```
┌────────────────────────────────────────────────────────┐
│ 中序遍历 DFS (Left -> Root -> Right)                   │
│ 对于 BST，中序遍历结果严格单调递增                     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
左根右递归不变量：左子树遍历结果 + 根节点值 + 右子树遍历结果。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#inordertraversal
#lc-94

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def f(node: Optional[TreeNode]): #pre-order traversal

           #base case
            if node is None:
                return


            f(node.left)


            
            res.append(node.val)


            
            f(node.right)
            return
        
        f(root)
        return res
```

1. 基于 `25-lc-0094-binary-tree-inorder-traversal.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何用迭代栈实现中序遍历？”*
  - **Candidate**: 一路向左将所有左节点压栈；弹出栈顶记录结果，转向其右子树重复此过程。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 空树未防御 | root=None 报错 | 未判空 | 首行 if not root: return [] |

### Complete Dry-Run Table / 实例推演表

root=[1,null,2,3] -> 1 -> 3 -> 2 -> [1, 3, 2]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个节点访问一次。 |
| **Space Complexity** | $O(n)$ | 最坏链状树递归栈深度 $O(n)$。 |
