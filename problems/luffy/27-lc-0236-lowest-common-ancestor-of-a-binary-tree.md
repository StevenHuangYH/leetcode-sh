# LC 0236: Lowest Common Ancestor of a Binary Tree | 二叉树的最近公共祖先

- **LeetCode ID**: LC 0236
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 07: Tree Post-Order)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- **Solution File**: [`27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](problems/luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

### [CN] 中文描述
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先 (LCA)。

### Constraints / 约束条件
树中节点数目在范围 [2, 10^5] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Data Structures] ➔ [BST]`

```
┌────────────────────────────────────────────────────────┐
│ 后序分治四态判定:                                      │
│ 1. 若 root 是 p 或 q 或 None -> 返回 root              │
│ 2. left 和 right 均非空 -> root 即为 LCA               │
│ 3. 仅一边非空 -> 向上透传该非空子树结果                │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
祖先汇聚判定：首次在左右两侧同时捕获到目标节点的分叉点即为最近公共祖先。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-236
#the lowest common ancestor of a binary tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#DFS
#Poster-order: left-right-root

class Solution:
    #retrun the completed information
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode | None':
        #defind return values:
        #whetrher the current node's subtree contains p / whether the current node is the ancestor of p 
        #whether the current node's subtree contains q 
        #and the address of the lowest common ancestor x


        def dfs(node):
            #base case
            if node is None:
                return False, False, None

            left_has_p, left_has_q, left_x = dfs(node.left)
            right_has_p, right_has_q, right_x = dfs(node.right)

            cur_has_p=left_has_p or right_has_p or node == p
            cur_has_q=left_has_q or right_has_q or node == q

            cur_x = None

            if left_x:
                cur_x=left_x
            elif right_x:
                cur_x=right_x
            elif cur_has_p and cur_has_q:
                cur_x=node

            return cur_has_p, cur_has_q, cur_x

        _,_,x=dfs(root)
        return x
```

1. 基于 `27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果两个节点在同一子树中，算法如何正确返回？”*
  - **Candidate**: 较高层级的节点匹配到 `root in (p, q)` 直接返回自身，天然覆盖了其子树包含另一节点的情况。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 未向上透传单侧非空结果 | 一边为空直接返回 None | 逻辑断裂 | return left or right |

### Complete Dry-Run Table / 实例推演表

root=[3,5,1,6,2,0,8], p=5, q=1 -> left=5, right=1 -> return 3

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 遍历每个节点一次。 |
| **Space Complexity** | $O(h)$ | 递归栈深度。 |
