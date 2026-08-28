# LC 0098: Validate BST (Postorder Min/Max Range) | 验证二叉搜索树 (后序极值汇总)

- **LeetCode ID**: LC 0098
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 07: BST Validation)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/validate-bst-(postorder-min/max-range)/)
- **Solution File**: [`29-lc-0098-validate-binary-search-tree-recursion.py`](luffy/29-lc-0098-validate-binary-search-tree-recursion.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Validate BST using post-order tree DP returning (min_val, max_val) sub-tree bounds.

### [CN] 中文描述
使用后序遍历自底向上返回子树 `(min_val, max_val)` 极值范围验证 BST。

### Constraints / 约束条件
树中节点数目在范围 [1, 10^4] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 后序自底向上: 返回 (is_bst, min_val, max_val)          │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
子树极值包络性：`node.val` 必须大于左子树的最大值，且小于右子树的最小值。

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
        def dfs(node: Optional[TreeNode],low_limit:float, high_limit:float) -> bool:
            if not node:
                return True

            #Pruning (剪枝)
            if node.val <=low_limit or node.val >= high_limit:
                return False

            #judge in advance
            left_is_BST=dfs(node.left,low_limit,node.val)
            right_is_BST=dfs(node.right, node.val, high_limit)

            return left_is_BST and right_is_BST

        return dfs(root,float('-inf'), float('inf'))
```

1. 基于 `29-lc-0098-validate-binary-search-tree-recursion.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“后序极值法与前序区间法相比有何特点？”*
  - **Candidate**: 后序法自底向上汇总，利于转化为求解最大 BST 子树（LC 333）等扩展问题。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 空节点极值反向初始化错误 | 空节点 min/max 设置反了 | 极值反转 | 空节点 min=inf, max=-inf |

### Complete Dry-Run Table / 实例推演表

空节点返回 (inf, -inf)，叶子节点返回 (val, val)

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个节点遍历一次。 |
| **Space Complexity** | $O(h)$ | 树高。 |
