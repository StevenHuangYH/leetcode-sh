# LC 0144: Binary Tree Preorder Traversal | 二叉树的前序遍历

- **LeetCode ID**: LC 0144
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 07: Tree Traversal)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- **Solution File**: [`25-lc-0144-binary-tree-preorder-traversal.py`](luffy/25-lc-0144-binary-tree-preorder-traversal.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

### [CN] 中文描述
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

### Constraints / 约束条件
树中节点数目在范围 [0, 100] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Tree Paradigms] ➔ [Recursive Traverse]`

```
┌────────────────────────────────────────────────────────┐
│ 前序遍历 DFS (Root -> Left -> Right)                   │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
根左右递归不变量：根节点值 + 左子树结果 + 右子树结果。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-144
#binary tree preorder traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# pre-order: root-left-right
#in-order: left-root-right
#posterorder: left-right-root
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def f(node: Optional[TreeNode]): #pre-order traversal

           #base case
            if node is None:
                return

            #center:
            res.append(node.val)

            #left
            f(node.left)

            #right
            f(node.right)
            return
        
        f(root)
        return res
```

1. 基于 `25-lc-0144-binary-tree-preorder-traversal.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“Morris 遍历如何做到 O(1) 空间？”*
  - **Candidate**: 利用叶子节点的空闲右指针建立指向中序前驱的线索（Threaded Binary Tree）。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 递归未终止 | 未写 Base Case | 递归溢出 | 递归基检查 if not root |

### Complete Dry-Run Table / 实例推演表

root=[1,null,2,3] -> [1, 2, 3]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 节点总数。 |
| **Space Complexity** | $O(n)$ | 递归调用栈。 |
