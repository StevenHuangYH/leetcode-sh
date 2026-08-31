# LC 0098: Validate BST (Iterative Stack) | 验证二叉搜索树 (显式栈迭代法)

- **LeetCode ID**: LC 0098
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 07: BST Validation)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/validate-bst-(iterative-stack)/)
- **Solution File**: [`29-lc-0098-validate-binary-search-tree-stack.py`](luffy/29-lc-0098-validate-binary-search-tree-stack.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Validate BST using an explicit stack for in-order traversal to eliminate recursion overhead.

### [CN] 中文描述
使用显式辅助栈进行中序遍历验证 BST，消除函数调用栈开销。

### Constraints / 约束条件
树中节点数目在范围 [1, 10^4] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Data Structures] ➔ [BST]`

```
┌────────────────────────────────────────────────────────┐
│ 显式中序栈: while stack or root -> push all left nodes │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
栈内状态一致性：栈顶元素为当前未访问的最左侧子节点。

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

        pre=float("-inf")

        def inorder(node:Optional[TreeNode])-> bool:
            if node is None:
                return True

            nonlocal pre

            left_is_BST = inorder(node.left)
            if node.val <= pre:
                return False

            right_is_BST = inorder(node.right)
            if not right_is_BST:
                return False

            return left_is_BST and right_is_BST

        return inorder(root)
```

1. 基于 `29-lc-0098-validate-binary-search-tree-stack.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“迭代中序遍历在内存受限系统中的优势？”*
  - **Candidate**: 避免栈溢出风险，且易于在中途终止时手动清理释放堆栈。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| root = root.right 遗漏 | 死循环卡在当前节点 | 指针移动遗漏 | 弹出节点后必须将 root 转向其右孩子 |

### Complete Dry-Run Table / 实例推演表

压左孩子入栈 -> 弹出比较 -> 转右孩子

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 线性时间。 |
| **Space Complexity** | $O(h)$ | 显式栈大小。 |
