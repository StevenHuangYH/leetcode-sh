# LC 0105: Construct Binary Tree from Preorder & Inorder | 从前序与中序遍历序列构造二叉树

- **LeetCode ID**: LC 0105
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 07: Tree Construction)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-&-inorder/)
- **Solution File**: [`30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given two integer arrays `preorder` and `inorder`, construct and return the binary tree.

### [CN] 中文描述
给定两个整数数组 preorder 和 inorder ，构造二叉树并返回其根节点。

### Constraints / 约束条件
1 <= preorder.length <= 3000, inorder.length == preorder.length

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Tree Paradigms] ➔ [Recursive Traverse]`

```
┌────────────────────────────────────────────────────────┐
│ 递归分治定位:                                          │
│ preorder[0] 是根节点 root_val                          │
│ 在 inorder 中定位 root_val 索引 k:                     │
│   左子树大小 size = k - in_left                        │
│   左子树: preorder[1...size], inorder[...k-1]          │
│   右子树: preorder[size+1...], inorder[k+1...]         │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
子树划分对偶性：前序序列的根节点在中序序列中精确划分左子树与右子树的节点集合。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-105

#construct binary tree from preorder and inorder traversal
from typing import List,Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



#pre-order root-left-righ
#inorder: left-root-right

#posterorder: left-right-root


#divide and conquer
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val=preorder[0]
        root=TreeNode(val=root_val)

        root_index=inorder.index(root_val) #O(n)



        #left subtree
        root.left=self.buildTree(preorder[1 : 1+root_index],inorder[:root_index])


        #right subtree
        root.right=self.buildTree(preorder[1 + root_index :],inorder[root_index + 1 :])

        return root



class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val:idx for idx,val in enumerate(inorder)} #hashmap for inorder

        def solver(pre_left, pre_right, in_left, in_right)->Optional[TreeNode]:
            if pre_left>pre_right:
                return None

            root_val=preorder[pre_left]
            root=TreeNode(val=root_val)
            root_idx=inorder_map[root_val] 

            left_size=root_idx-in_left

            root.left= solver(pre_left+1, pre_left+left_size, in_left, root_idx-1)
            root.right= solver(pre_left+left_size+1, pre_right, root_idx+1,in_right)

            return root

        return solver(0, len(preorder)-1, 0, len(inorder)-1)
```

1. 基于 `30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何避免递归切片导致的 O(n^2) 时间复杂度？”*
  - **Candidate**: 预先用哈希表记录 `inorder` 各元素下标，递归时仅传递下标范围 `(pre_l, pre_r, in_l, in_r)` 做到 $O(n)$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 数组切片复制开销 | nums[1:k] 产生额外拷贝 | 时间退化 | 采用索引边界传参或哈希表辅助 |

### Complete Dry-Run Table / 实例推演表

preorder=[3,9,20,15,7], inorder=[9,3,15,20,7] -> root=3, left=[9], right=[20,15,7]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 带哈希表索引查询。 |
| **Space Complexity** | $O(n)$ | 哈希表与递归树。 |
