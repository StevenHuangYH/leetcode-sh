# LeetCode 104. Maximum Depth of Binary Tree (二叉树的最大深度)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (分治后序递归 / 树形 DP 原语 / 层序 BFS / 迭代显式栈)
- **Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
- **Corresponding Python File:** [`top-100/lc-0104-maximum-depth-of-binary-tree.py`](top-100/lc-0104-maximum-depth-of-binary-tree.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `root` of a binary tree, return *its maximum depth*.
  * A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.
* **[CN]** 给定一个二叉树 `root` ，返回其 **最大深度** 。
  * 二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

### Constraints / 约束条件
* 树中节点的数量在 $[0, 10^4]$ 区间内。
* $-100 \le \text{Node.val} \le 100$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 概念澄清 (Concept Clarification):                                        │
│    • 深度 (Depth): 从根节点向下到当前节点的唯一路径上的节点数 (自顶向下)。    │
│    • 高度 (Height): 从当前节点向下到最远叶子节点的最长路径节点数 (自底向上)。 │
│    • 二叉树的最大深度严格等价于根节点的最大高度 (Max Depth == Height of Root)。│
│ 2. 分治与后序遍历不变量 (Divide & Conquer / Post-order Invariant):          │
│    • 子问题分解: 当前树的最大深度 = 1 + max(左子树深度, 右子树深度)。       │
│    • 递归基 (Base Case): 若当前子树为空 (root is None)，深度贡献为 0。      │
│ 3. 树形 DP 奠基原语: 本题是 LC 110、LC 543、LC 124 等所有树形 DP 的母题。    │
│ 4. 极致时空: 严格单次遍历 O(N) 时间，O(H) 递归栈空间 (H 为树高)。          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 树形递归与树形 DP 思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Tree Post-order Pattern Lineage (二叉树后序/分治思维谱系演化树)   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Foundational Primitive): LC 104 Maximum Depth of Binary Tree (本题★)│
│  └─ 核心原语: height(u) = 1 + max(height(u.left), height(u.right))          │
│        │                                                                    │
│        ▼ [演进 Twist: 引入平衡性判断与 -1 提前剪枝]                         │
│  Level 2 (Constraint Validation): LC 110 Balanced Binary Tree               │
│  └─ 不变量: |height(left) - height(right)| <= 1，否则立即返回 -1 剪枝。     │
│        │                                                                    │
│        ▼ [演进 Twist: 全局最值维护 (穿过当前节点的最长路径)]                 │
│  Level 3 (Global State Aggregation): LC 543 Diameter of Binary Tree         │
│  └─ 不变量: 全局直径 max_d = max(max_d, left_h + right_h)，单侧向上返 height│
│        │                                                                    │
│        ▼ [演进 Twist: 结合带权路径求和与负值剪枝 (Hard)]                     │
│  Level 4 (Tree DP Masterpiece): LC 124 Binary Tree Maximum Path Sum         │
│  └─ 不变量: 负增益剪枝 max(0, side_sum)，全局更新 max_path = l + r + val。 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 二叉树与递归核心思维模型 (Recursive Mental Model & Why It Works)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 💡 如何系统思考二叉树的递归问题 (How to Reason About Tree Recursion)        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 思考整棵树与其左右子树的关系:                                            │
│    • 整棵树的最大深度 = max(左子树的最大深度, 右子树的最大深度) + 1         │
│ 2. 原问题与子问题的自相似性:                                                │
│    • 原问题: 计算以 root 为根的整棵树的最大深度。                           │
│    • 子问题: 计算以 root.left 和 root.right 为根的子树的最大深度。          │
│    • 子问题与原问题在结构上完全相同，执行的代码逻辑也完全一致。             │
│ 3. 为什么必须使用递归而不是简单循环?                                        │
│    • 子问题的计算结果必须自底向上【返回给上一级问题】，由父节点聚合决策。   │
│    • 系统的函数调用栈天然支持“递”下去探索、“归”上来汇总的生命周期。         │
│ 4. 为什么这样写就一定能正确终止? (Base Case & Invariant):                   │
│    • 每次递归调用的子问题规模严格比父问题小（节点数减少）。                 │
│    • 不断向深处“递”下去，终究会到达叶子节点的空指针 (root is None)。         │
│    • 触发边界条件 (Base Case)，直接返回答案 0，随后逐层“归”并汇总。         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 数学归纳与递推机制 (Mathematical Induction)

设以节点 $u$ 为根的子树深度为 $D(u)$：

$$D(u) = \begin{cases} 
0, & \text{若 } u \text{ 为空节点 (None)} \\ 
1 + \max\big(D(u.\text{left}), D(u.\text{right})\big), & \text{若 } u \text{ 存在}
\end{cases}$$

#### 归纳证明：
1. **基础项**：当树为空（节点数为 0）时，叶子节点不存在，返回 0，符合深度定义。
2. **归纳假设**：假设左右子树的递归调用均能正确返回其最大深度 $D(u.\text{left})$ 与 $D(u.\text{right})$。
3. **归纳推导**：从根节点 $u$ 出发，任何一条通向叶子节点的路径必须经过 $u$，随后只能选择走向左子树或右子树。为了使总路径最长，必须贪心选取深度更大的那一侧子树，即 $\max\big(D(u.\text{left}), D(u.\text{right})\big)$，再加上当前节点 $u$ 本身所占的 1 层，总深度严格为 $1 + \max(D_{\text{left}}, D_{\text{right}})$。

---

### 🎨 ASCII 递归分治回溯图解

以二叉树 `root = [3, 9, 20, null, null, 15, 7]` 为例：

```
                 [3]
               /     \
             [9]     [20]
                    /    \
                  [15]   [7]

═════════════════════════════════════════════════════════════════════
自底向上 (Bottom-Up) 递归回溯求高度推演:

Level 3 (叶子节点):
  • [15] -> 1 + max(0, 0) = 1
  • [7]  -> 1 + max(0, 0) = 1

Level 2:
  • [9]  -> 1 + max(0, 0) = 1
  • [20] -> 1 + max(height([15]), height([7])) = 1 + max(1, 1) = 2

Level 1 (根节点):
  • [3]  -> 1 + max(height([9]), height([20])) = 1 + max(1, 2) = 3

最终输出最大深度 = 3
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

本题在 Python 文件中提供了两种互相对偶的经典递归范式：

---

### 范式 1: 自底向上分治后序遍历 (Bottom-Up Post-order / Divide & Conquer)

直接利用函数返回值自底向上层层归并计算子树高度：

```python
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. 递归基 (Base Case): 若当前子树为空节点 (root is None)，深度贡献为 0，触底开始“归”
        if not root:
            return 0
        
        # 2. 递归深入左子树，求解左子树的最大深度 (Left Subtree Max Depth)
        left_depth = self.maxDepth(root.left)
        
        # 3. 递归深入右子树，求解右子树的最大深度 (Right Subtree Max Depth)
        right_depth = self.maxDepth(root.right)
        
        # 4. 后序汇总 (Post-order Conquer): 
        #    当前树的最大深度 = max(左子树深度, 右子树深度) + 1 (当前根节点所贡献的 1 层高度)
        return max(left_depth, right_depth) + 1
```

---

### 范式 2: 自顶向下前序遍历与外部状态维护 (Top-Down Preorder with State Accumulation)

在参数中自顶向下累加深度 `cnt`，并在遍历过程中动态更新全局最大值 `ans`：

```python
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def f(node, cnt):
            # 1. 递归基 (Base Case): 若当前节点为空，直接回退 (防御性修复: 必须检查当前入参 node 而非外部 root)
            if node is None:
                return
            
            # 2. 前序位置: 访问当前节点，路径深度累加 1
            cnt += 1
            nonlocal ans
            # 3. 动态维护全局最大深度
            ans = max(ans, cnt)
            
            # 4. 向左右子树继续深入传递当前深度 cnt
            f(node.left, cnt)
            f(node.right, cnt)
        
        f(root, 0)
        return ans
```

#### 核心机制与对比总结：
* **自底向上 (`Solution`)**：关注“子树的高度是多少”，不需要外部变量，由子节点计算出结果后**通过 `return` 向上返回**给父节点，是树形 DP 与分治算法的核心原语。
* **自顶向下 (`Solution2`)**：关注“从根节点到当前节点的路径深度是多少”，通过**递归入参 `cnt` 向下传递**状态，在前序位置更新全局最优解 `ans`，是回溯与路径搜索的经典范式。

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 如果递归调用栈可能导致栈溢出 (Stack Overflow)，如何用层序遍历 (BFS) 求解？

* **面试官**：在极端倾斜树（例如链状退化树，深度达 $10^4$）或内存受限环境中，递归可能导致 RecursionError。你能写出迭代层序遍历（BFS）解法吗？
* **候选人解析**：
  * 使用双端队列 `collections.deque` 实现标准 BFS。
  * 每次循环按批次弹出当前整层的节点数 `len(queue)`，每消化完整整一层，深度计数器 `depth += 1`。
  * 队列排空时，`depth` 即为二叉树最大深度。

```python
# 附: 层序遍历 BFS 模板 (Level-Order BFS)
from collections import deque

class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            # 严格锁定当前层的节点数量，批量出队
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            
        return depth
```

---

### 追问 2: 能否使用显式栈 (Explicit DFS Stack) 实现前序模拟？

* **面试官**：如果要求必须用深度优先搜索（DFS），但禁止使用隐式系统递归，如何用显式栈模拟？
* **候选人解析**：
  * 栈中存储二元组 `(node, current_depth)`。
  * 遍历过程中维护全局最大深度 `max_d = max(max_d, current_depth)`。

```python
# 附: 显式栈 DFS 模拟 (Iterative DFS with Stack)
class SolutionIterativeDFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, cur_depth = stack.pop()
            max_depth = max(max_depth, cur_depth)
            if node.right:
                stack.append((node.right, cur_depth + 1))
            if node.left:
                stack.append((node.left, cur_depth + 1))
                
        return max_depth
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **辅助函数误判根节点 (`if root is None`)** | 自顶向下前序遍历时抛出 `AttributeError: 'NoneType' object has no attribute 'left'` | 在辅助递归函数 `f(node, cnt)` 内误写了 `if root is None`，当 `root` 非空但 `node` 到达叶子空子节点时无法正确触发 Base Case 拦截 | 辅助递归函数首行必须检查当前递归指针：`if node is None: return` |
| **遗漏空树判空 (`if not root`)** | 输入 `root = []` 时抛出 `AttributeError: 'NoneType' has no attribute 'left'` | 未设置递归终止边界条件，对 `None` 访问子节点 | 递归首行严格保证 `if not root: return 0` |
| **误将 `+ 1` 写在 `max` 内部** | 代码写为 `max(left + 1, right)` 导致计算结果偏小 | 每一层节点自身的深度贡献应当统一加在左右子树最大值之外 | 严格使用 `1 + max(left_depth, right_depth)` |
| **全局变量累加被脏数据污染** | 在全局变量 `self.depth` 上累加但未在多用例间重置 | 力扣判题机制复用同一个 `Solution` 类实例，全局状态跨用例残留 | 优先采用函数纯返回值传递分治结果，避免非必要类属性全局状态 |
| **极度退化链状树递归栈溢出** | 节点数达到 $10^5$ 且呈单链形状时抛出 `RecursionError: maximum recursion depth exceeded` | Python 默认递归深度上限为 1000 | 工业级/超大规模场景采用 BFS 队列或设置 `sys.setrecursionlimit` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 树拓扑形态 (Tree Shape) | 递归调用树与返回值 (Call Tree & Return) | 最终返回值 (Return Value) |
| :--- | :--- | :--- | :--- |
| **空树 `root = []`** | 空指针 `None` | `if not root: return 0` | `0` (通过) |
| **单节点树 `[1]`** | 仅根节点 `[1]` | `left=0, right=0` $\rightarrow$ `1 + max(0, 0) = 1` | `1` (通过) |
| **完全单斜树 `[1, 2, null, 3]`** | 向左退化为链条 | `[3]->1` $\rightarrow$ `[2]->2` $\rightarrow$ `[1]->3` | `3` (通过) |
| **满二叉树 `[1, 2, 3, 4, 5, 6, 7]`** | 深度为 3 的平衡满二叉树 | 左右子树高度均为 2 $\rightarrow$ `1 + max(2, 2) = 3` | `3` (通过) |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | $N$ 为二叉树的节点总数。每个节点恰好被递归访问一次（常数次入栈和出栈操作），无冗余重叠子问题，故时间复杂度严格为 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(H)$ | $H$ 为二叉树的高度。空间消耗主要取决于递归调用栈的深度：<br>• **最佳/平均情况 (平衡二叉树)**: $H = \mathcal{O}(\log N)$；<br>• **最差情况 (退化为单链表)**: $H = \mathcal{O}(N)$。 |
