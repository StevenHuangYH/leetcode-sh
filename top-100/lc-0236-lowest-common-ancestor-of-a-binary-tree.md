# LeetCode 236. Lowest Common Ancestor of a Binary Tree (二叉树的最近公共祖先)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (树形后序分治 / 自底向上信息汇聚 / 四状态归并剪枝 / LCA 经典原语)
- **Tags:** Tree, Depth-First Search, Binary Tree
- **Corresponding Python File:** [`top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
  * According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”
* **[CN]** 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先 (LCA)。
  * 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

### Constraints / 约束条件
* 树中节点数目在范围 $[2, 10^5]$ 内。
* $-10^9 \le \text{Node.val} \le 10^9$
* 所有 $\text{Node.val}$ 互不相同（Unique Values）。
* $p \neq q$
* $p$ 和 $q$ 均存在于给定的二叉树中。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 递归返回值语义契约 (Post-Order Return Contract):                        │
│    • 函数 lowestCommonAncestor(root, p, q) 的返回值定义为:                  │
│      - 若以 root 为根的子树包含 p 或 q 中的节点，返回该匹配节点指针；        │
│      - 若以 root 为根的子树同时包含 p 和 q，返回其最近公共祖先 (LCA) 指针；  │
│      - 若以 root 为根的子树既不含 p 也不含 q，返回 None。                  │
│ 2. 四状态自底向上归并 (4-State Bottom-Up Aggregation):                      │
│    • 状态 1: left 与 right 均非空 ⟺ p 与 q 分居当前 root 的两侧 ⟹ root 为 LCA │
│    • 状态 2: left 非空，right 为空 ⟺ p, q (或 LCA) 均在左子树 ⟹ 返回 left   │
│    • 状态 3: left 为空，right 非空 ⟺ p, q (或 LCA) 均在右子树 ⟹ 返回 right  │
│    • 状态 4: left 与 right 均为空 ⟺ 子树中无目标节点 ⟹ 返回 None             │
│ 3. 递归基自包含短路 (Base Case Self-Containment):                           │
│    • 若 root is None or root is p or root is q: 立即返回 root。            │
│    • 注意: 当 root 自身为 p (或 q) 时，即使 q 在其子树中，p 即为自包含 LCA， │
│      无需继续向下深入遍历，直接向上回溯传递！                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 最近公共祖先 (LCA) 算法思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Lowest Common Ancestor (LCA) Pattern Lineage (公共祖先谱系演化图)       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (BST Value Directionality): LC 235 LCA of BST                      │
│  └─ 二叉搜索树单向分治: 利用数值范围 min(p,q) <= root.val <= max(p,q) 判定  │
│        │                                                                    │
│        ▼ [演进 Twist: 无序通用二叉树，无法凭数值导向，依赖后序分治汇总]     │
│  Level 2 (General Binary Tree Post-Order): LC 236 LCA of Binary Tree (本题★)│
│  └─ 后序四态归并: left, right = LCA(l), LCA(r) -> 双非空即根，单非空即子     │
│        │                                                                    │
│        ▼ [演进 Twist: 扩展为多目标集合或最深叶子集群 LCA]                    │
│  Level 3 (Multi-Node / Deepest LCA): LC 1676 LCA of Multi-Nodes / LC 1123  │
│  └─ 状态扩展: 传递集合计数或返回 (node, max_depth) 元组                     │
│        │                                                                    │
│        ▼ [演进 Twist: 大规模树高频查询 / 静态树多次离线查询]                │
│  Level 4 (Advanced Offline / Binary Lifting): 倍增 LCA (Binary Lifting)    │
│  └─ 算法升维: 预处理 2^k 祖先跳表 up[u][k]，将单次查询从 O(N) 降至 O(log N) │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎨 ASCII 两种核心归并拓扑图解

#### 拓扑场景 A：$p$ 与 $q$ 分居两侧（双子树相遇）
```
                 (3)  <--- left=(5), right=(1) 均非空 ⟹ 返回 3 (LCA★)
               /     \
             (5)     (1)
            /   \   /   \
          (6)   (2)(0)   (8)
          p=(5), q=(1)
```

#### 拓扑场景 B：$p$ 自身就是 $q$ 的祖先（自包含短路）
```
                 (3)  <--- left=(5), right=None ⟹ 向上透传 (5) (LCA★)
               /     \
             (5)     (1)  <--- 命中 root is p ⟹ 立即返回 (5)，无需深入遍历 4
            /   \
          (6)   (2)
                / \
              (7) (4)  <--- q=(4) 在 p 的子树内部
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py) 中的实现进行逐行深入解析：

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 1. 递归基 (Base Case):
        # • 若当前节点为空 (None)，说明到底部未发现 p 或 q，返回 None
        # • 若当前节点就是 p 或 q，说明命中目标节点，直接返回当前 root
        #   (即便另一节点在其子树内，当前节点也是其合法的自包含 LCA)
        if root is None or root is p or root is q:
            return root

        # 2. 后序分治: 分别在左、右子树中寻找 p 和 q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 3. 状态 1 (两侧分居): 左子树和右子树各找到了一个目标节点
        #    说明当前 root 就是二者分叉交汇的最近公共祖先
        if left and right:
            return root

        # 4. 状态 2 (左侧命中): 仅左子树返回非空
        #    说明 p 和 q 都在左子树中，且其 LCA 已由左子树递归得出并向上返回
        if left:
            return left

        # 5. 状态 3 & 4 (右侧命中或双空):
        #    若 right 非空则返回 right；若 right 亦为空则返回 None
        return right
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 如果树的结构允许使用哈希表记录父节点指针，如何用迭代法求解？

* **面试官**：递归虽好，但如果题目要求非递归实现，或者我们可以预先遍历记录父指针，该如何实现？
* **候选人解析**：
  * **哈希父指针法 (Parent Pointer Map)**：
    1. 使用 BFS/DFS 遍历整棵树，使用字典 `parent = {root: None}` 记录每个节点的父节点，直到 $p$ 和 $q$ 均被记录；
    2. 从节点 $p$ 开始，沿着父指针一路向上爬到根节点，将沿途所有祖先节点存入哈希集合 `visited`；
    3. 从节点 $q$ 开始沿父指针向上爬，遇到的第一个出现在 `visited` 集合中的节点即为最近公共祖先。

```python
# 附: 父节点哈希表回溯法 (Parent Pointer Iteration)
from collections import deque

class SolutionParentMap:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = {root: None}
        queue = deque([root])
        
        # 遍历直到找到 p 和 q 的父节点
        while p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
                
        # 记录从 p 到 root 的全路径
        ancestors = set()
        curr = p
        while curr:
            ancestors.add(curr)
            curr = parent[curr]
            
        # q 向上寻找第一个公共交点
        curr = q
        while curr not in ancestors:
            curr = parent[curr]
            
        return curr
```

---

### 追问 2: 如果 $p$ 或 $q$ 可能【不存在】于二叉树中，当前解法会产生什么问题？如何修正？

* **面试官**：原题保证了 $p$ 和 $q$ 均存在。如果 $p$ 存在而 $q$ 不存在，当前代码会返回什么？如何防御性修正？
* **候选人解析**：
  * **缺陷表现**：若 $p$ 在树中而 $q$ 不在树中，遇到 $p$ 时会触发 `if root is p: return root` 短路返回，最终函数会**误将 $p$ 作为 LCA 返回**，而实际上正确答案应为 `None`。
  * **防御性修正**：不能在遇到首个节点时盲目短路；需要完整遍历统计找到的节点计数（`count == 2`），或者在得到候选 LCA 后，单独跑一次验证函数确认另一节点是否确实存在。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **误以为只有 `left and right` 才返回答案** | 当 $p$ 是 $q$ 的父节点时，返回了 `None` 或错误顶层节点 | 忽略了自包含情况：此时一边返回目标节点，另一边返回 `None` | 当单侧返回非空时，必须正确向上透传 `return left if left else right` |
| **在子树递归前未优先判断 `root is p or root is q`** | 代码陷入对目标节点子树的无意义深搜，效率劣化 | 未利用题目“$p, q$ 必定在树中”的先验条件进行剪枝 | 递归首行置入 `if root is None or root is p or root is q: return root` |
| **比较节点时使用值 `root.val == p.val` 而非对象指针** | 在包含重复值或通用树模型中容易产生错误重名匹配 | 树节点比对应该基于对象内存地址唯一性 | Python 中使用 `root is p` 或 `root == p` 引用比对 |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 拓扑关系 (Relationship) | 递归推演路径 (Trace) | 输出 (Output) |
| :--- | :--- | :--- | :---: |
| **两节点分居根的两侧 `[3,5,1]`, p=5, q=1** | 根左侧为 $p$，根右侧为 $q$ | `left` 返回 5, `right` 返回 1 $\rightarrow$ 命中 `left and right` $\rightarrow$ 返回 3 | `3` |
| **一节点为另一节点父节点 `[3,5,1,6,2]`, p=5, q=2** | $p=(5)$ 是 $q=(2)$ 的直接父节点 | 访问到 (5) 时命中 `root is p` 直接返回 (5)；右子树 (1) 返回 None $\rightarrow$ 透传返回 5 | `5` |
| **两节点链式极深 `[1,2,null,3]`, p=2, q=3** | 单链分布在最左侧 | 访问到 (2) 触发返回 2，左子树透传至根 | `2` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | 其中 $N$ 为二叉树的节点总数。最坏情况下（例如 $p$ 和 $q$ 均位于叶子节点且分居最深两侧），递归遍历需要访问树中的每一个节点恰好一次，处理每个节点耗时 $\mathcal{O}(1)$，总耗时为 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(H)$ | 其中 $H$ 为二叉树的高度。空间开销来自系统递归栈深度：<br>• **最好/平均情况 (平衡二叉树)**: 栈深度 $H = \mathcal{O}(\log N)$；<br>• **最坏情况 (二叉树完全退化为链表)**: 栈深度 $H = \mathcal{O}(N)$。 |
