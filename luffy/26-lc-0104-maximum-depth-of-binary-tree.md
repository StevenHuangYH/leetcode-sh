# LC 0104: Maximum Depth of Binary Tree | 二叉树的最大深度

- **LeetCode ID**: LC 0104
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 07: Tree Divide & Conquer)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- **Solution File**: [`26-lc-0104-maximum-depth-of-binary-tree.py`](luffy/26-lc-0104-maximum-depth-of-binary-tree.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the `root` of a binary tree, return its maximum depth.

### [CN] 中文描述
给定一个二叉树 root ，返回其最大深度。

### Constraints / 约束条件
树中节点的数目在范围 [0, 10^4] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Tree Hierarchies] ➔ [Recursive Mindset] ➔ [Binary Tree]`

```
┌────────────────────────────────────────────────────────┐
│ 分治递推: depth = 1 + max(maxDepth(left), maxDepth(right)) │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
深度归纳基石：空树深度为 0，非空树深度为左右子树最大深度加 1。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-104
#maximum depth of binary tree

from typing import  Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#use poster-order
# left-right-center
#        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case 边界条件
        if root is None:
            return 0 #int, need to return a real value

        #iteration
        left=self.maxDepth(root.left) #return the max depth of the left side
        right=self.maxDepth(root.right)

        

        #return
        return max(left,right)+1


#DFS
```

1. 基于 `26-lc-0104-maximum-depth-of-binary-tree.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何用层序遍历 (BFS) 计算最大深度？”*
  - **Candidate**: 使用队列进行 BFS，每处理完一整层 `depth += 1`，直到队列为空返回 `depth`。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| Base Case 遗漏 | root=None 未返回 0 | 死递归 | 首行 if not root: return 0 |

### Complete Dry-Run Table / 实例推演表

root=[3,9,20,null,null,15,7] -> 1 + max(1, 2) = 3

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个节点遍历一次。 |
| **Space Complexity** | $O(h)$ | 树高 $h$ 递归栈。 |
