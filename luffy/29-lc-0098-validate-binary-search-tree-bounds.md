# LC 0098: Validate BST (Range Bounds) | 验证二叉搜索树 (区间上下界法)

- **LeetCode ID**: LC 0098
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 07: BST Validation)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/validate-bst-(range-bounds)/)
- **Solution File**: [`29-lc-0098-validate-binary-search-tree-bounds.py`](luffy/29-lc-0098-validate-binary-search-tree-bounds.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the root of a binary tree, determine if it is a valid binary search tree (BST) using pre-order range bounds.

### [CN] 中文描述
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树（采用开区间界限法）。

### Constraints / 约束条件
树中节点数目在范围 [1, 10^4] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Data Structures] ➔ [BST]`

```
┌────────────────────────────────────────────────────────┐
│ 开区间上下界递推: is_valid(node, low, high)            │
│ 约束: low < node.val < high                            │
│ 左子树: is_valid(node.left, low, node.val)             │
│ 右子树: is_valid(node.right, node.val, high)           │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
全局边界传递性：节点值必须严格介于当前祖先链路决定的开区间 $(low, high)$ 内。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-98
#validate binary search tree
from typing import Optional
# Definition for a binary tree 
#A vaild BST
#the left subree of a node contains only nodes with strictly less than the node's key
#the right subtree of a node contains only nodes with keys strictly greater than the ndoe's key
#both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#center-left-right
#先判断再遍历


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode],low_limit:float, high_limit:float) -> bool:
            if not node:
                return True

            #Pruning (剪枝)
            if node.val <=low_limit or node.val >= high_limit:
                return False

            #judge in advance
            left_is_BST=dfs(node.left,low_limit,node.val)
            if not left_is_BST:
                return False
            right_is_BST=dfs(node.right, node.val, high_limit)
            if not right_is_BST:
                return False

            return True

        return dfs(root,float('-inf'), float('inf'))
```

1. 基于 `29-lc-0098-validate-binary-search-tree-bounds.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“只比较 root.val > root.left.val 是否足够？”*
  - **Candidate**: 远远不够。BST 要求左子树中所有节点都小于根，单纯局部比较无法检测到左子树深层节点大于祖先节点的情况（如 `[5, 1, 6, null, null, 3, 7]` 中 3 小于 5 的违规）。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 使用闭区间导致等于号判断错误 | BST 严禁出现重复值 | 相等违背 | 必须严格使用 < 和 > |

### Complete Dry-Run Table / 实例推演表

root=[2,1,3] -> valid(2, -inf, inf) -> left valid(1, -inf, 2), right valid(3, 2, inf) -> True

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 遍历所有节点。 |
| **Space Complexity** | $O(h)$ | 树高递归栈。 |
