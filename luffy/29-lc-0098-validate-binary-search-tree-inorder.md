# LC 0098: Validate BST (Inorder Monotonicity) | 验证二叉搜索树 (中序单调递增法)

- **LeetCode ID**: LC 0098
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 07: BST Validation)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/validate-bst-(inorder-monotonicity)/)
- **Solution File**: [`29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Validate BST by verifying that its in-order traversal yields a strictly monotonically increasing sequence.

### [CN] 中文描述
通过中序遍历严格单调递增性质验证二叉搜索树。

### Constraints / 约束条件
树中节点数目在范围 [1, 10^4] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 中序单调递增特性: pre_val < cur_node.val               │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
BST 中序遍历等价定理：二叉树是有效 BST 充要条件为其遍历结果严格单调递增。

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


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:Optional[TreeNode], min_limit, max_limit):
            #return bool value

            if node is None:
                return True #cannot return False

            left_is_BST=dfs(node.left, min_limit, node.val)
            right_is_BST=dfs(node.right,node.val,max_limit)

            if left_is_BST and right_is_BST and min_limit < node.val< max_limit:
                return True
            return False

        return dfs(root, float("-inf"),float("inf"))
```

1. 基于 `29-lc-0098-validate-binary-search-tree-inorder.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“中序遍历验证时如何提早短路退出？”*
  - **Candidate**: 发现 `cur_val <= pre_val` 立即返回 `False`，无需继续遍历后续子树。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| pre_val 初值设为 0 | 若节点含负数如 -2^31 则失效 | 初值错误 | pre_val 必须初始化为 -inf |

### Complete Dry-Run Table / 实例推演表

root=[5,1,4,null,null,3,6] -> 中序: 1, 5, 3 (3<=5 违背) -> return False

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 最坏全树，平均提前退出。 |
| **Space Complexity** | $O(h)$ | 栈空间。 |
