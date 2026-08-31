# LeetCode 235. Lowest Common Ancestor of a Binary Search Tree (二叉搜索树的最近公共祖先)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (二叉搜索树性质 / 数值单向分治 / 首次分叉点判定 / O(H) 极速定位)
- **Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree
- **Corresponding Python File:** [`daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py`](daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
  * According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”
* **[CN]** 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先 (LCA)。
  * 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

### Constraints / 约束条件
* 树中节点数目在范围 $[2, 10^5]$ 内。
* $-10^9 \le \text{Node.val} \le 10^9$
* 所有 $\text{Node.val}$ 互不相同（Unique Values）。
* $p \neq q$
* $p$ 和 $q$ 均存在于给定的二叉搜索树中。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 二叉搜索树有序不变量 (BST Ordering Invariant):                          │
│    • 对于 BST 中任意节点 u: left.val < u.val < right.val 严格成立。         │
│ 2. 数值区间包容与分叉判定 (Divergence Point Invariant):                    │
│    • 设区间 I = [min(p.val, q.val), max(p.val, q.val)]。                   │
│    • 若 p.val < u.val 且 q.val < u.val: p, q 均在 u 的左子树 ⟹ 深入左子树； │
│    • 若 p.val > u.val 且 q.val > u.val: p, q 均在 u 的右子树 ⟹ 深入右子树； │
│    • 否则 (一小一大分居两侧，或 u 恰好等于 p 或 q) ⟹ u 就是最近公共祖先★!   │
│ 3. 单向检索无需回溯 (One-Way Path without Backtracking):                    │
│    • 不同于普通二叉树 LC 236 的后序全树双向递归，BST 只需沿单条路径下行，   │
│      时间复杂度从 O(N) 优化到树高 O(H)。                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Tree Hierarchies] ➔ [Data Structures] ➔ [BST]`

### 🧠 二叉搜索树 LCA 思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Search Tree LCA Pattern Lineage (BST 公共祖先谱系演化图)         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Single Value Search): LC 700 Search in a Binary Search Tree       │
│  └─ 单目标值定位: 利用 val < root.val 左拐，val > root.val 右拐             │
│        │                                                                    │
│        ▼ [演进 Twist: 单目标扩展为双目标，寻找路径首次分叉交汇点]           │
│  Level 2 (Dual Value Divergence): LC 235 LCA of BST (本题★)                 │
│  └─ 双值同时比对: 只要 p,q 未分居两侧就继续单向深入；首次分叉处即 LCA        │
│        │                                                                    │
│        ▼ [演进 Twist: 失去 BST 有序性，退化为无序通用二叉树]                │
│  Level 3 (General Binary Tree): LC 236 LCA of Binary Tree                   │
│  └─ 后序四态归并: 无法依数值剪枝，必须使用左右双递归回溯汇聚                │
│        │                                                                    │
│        ▼ [演进 Twist: 多节点集合查询或动态树结构]                          │
│  Level 4 (Advanced LCA): LC 1676 Multi-Node LCA / 倍增跳表法 (Binary Lift) │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 形式化数学证明与分叉点唯一性 (Mathematical Proof)

在二叉搜索树中，设从根节点向下行走的当前节点为 $u$：

1. **情况 1：$p.	ext{val} < u.	ext{val} \land q.	ext{val} < u.	ext{val}$**
   * 根据 BST 性质，$u$ 及其右子树中所有节点的值都严格大于 $u.	ext{val}$，因此 $p$ 和 $q$ 不可能出现在右子树中，只能全部位于左子树。
   * 因此，公共祖先必定位于 $u$ 的左子树中。

2. **情况 2：$p.	ext{val} > u.	ext{val} \land q.	ext{val} > u.	ext{val}$**
   * 同理，$p$ 和 $q$ 均严格大于 $u.	ext{val}$，只能全部位于右子树。
   * 因此，公共祖先必定位于 $u$ 的右子树中。

3. **情况 3：$\min(p.	ext{val}, q.	ext{val}) \le u.	ext{val} \le \max(p.	ext{val}, q.	ext{val})$**
   * 此时要么 $p$ 和 $q$ 分居 $u$ 的左右两侧，要么 $u$ 自身就是 $p$ 或 $q$ 之一。
   * 若深入左子树，则 $q$（或较大的节点）将被排除在外；若深入右子树，则 $p$（或较小的节点）将被排除在外。
   * 因此，$u$ 是能同时覆盖 $p$ 和 $q$ 的**最深节点**，即 $u$ 必为 LCA。

---

### 🎨 ASCII 首次分叉点定位推演图解

以二叉搜索树 `root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]` 为例：

```
                     (6)  <--- Step 1: 比较 (p=2, q=8) 与 6
                   /     \       2 < 6 且 8 > 6 ⟹ 首次分叉! 返回 6 (LCA★)
                (2)       (8)
               /   \     /   \
             (0)   (4)  (7)   (9)
                   / \
                 (3) (5)

═════════════════════════════════════════════════════════════════════
查询用例 2: p = 2, q = 4

Step 1: 比较 (p=2, q=4) 与 root=(6)
  • 2 < 6 且 4 < 6 ⟹ 均在左侧，向左深入至 (2)

Step 2: 比较 (p=2, q=4) 与当前 node=(2)
  • p=(2) 刚好等于当前节点值 2 (不再满足 2 > 2 或 4 < 2)
  • 命中分叉/自包含终止条件 ⟹ 返回 2 (LCA★)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py`](daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py) 中的实现进行逐行深入解析：

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 1. 获取当前根节点的值
        x = root.val

        # 2. 若 p 和 q 的值均严格小于当前节点值，说明两目标节点均在左子树
        if p.val < x and q.val < x:
            return self.lowestCommonAncestor(root.left, p, q)

        # 3. 若 p 和 q 的值均严格大于当前节点值，说明两目标节点均在右子树
        if p.val > x and q.val > x:
            return self.lowestCommonAncestor(root.right, p, q)

        # 4. 首次分叉（p, q 分居两侧）或当前节点恰好为 p/q 自身，当前 root 即为 LCA
        return root
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 如何将该递归解法转换为 $\mathcal{O}(1)$ 额外辅助空间的迭代写法？

* **面试官**：由于每次递归只选择一条单向路径深入，完全没有回溯操作（尾递归）。能否写出迭代解法以避免调用栈开销？
* **候选人解析**：
  * 使用一个简单的 `while root:` 循环更新指针，直接在树上下行，空间复杂度降至绝对的 $\mathcal{O}(1)$。

```python
# 附: O(1) 辅助空间迭代模板 (Iterative Constant Space)
class SolutionIterative:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        return None
```

---

### 追问 2: LC 235 (BST) 与 LC 236 (通用二叉树) 的本质区别是什么？

* **面试官**：LC 236 的通用代码能直接用在 LC 235 吗？为什么我们还要写这道专属于 BST 的解法？
* **候选人解析**：
  * **兼容性**：LC 236 的后序双递归解法在 BST 上**功能完全正确**，可以无缝通过 LC 235。
  * **复杂度与效率差异**：
    * **LC 236 通用解法**：由于无序，无法判断目标在左还是在右，必须执行左右子树的双向遍历，最坏时间复杂度为全树规模 $\mathcal{O}(N)$。
    * **LC 235 专属解法**：充分利用了 BST 的数值大小有序性，每一步都能排除掉一半的子树，只需沿着单条路径下行，时间复杂度仅为树高 $\mathcal{O}(H)$（平衡时为 $\mathcal{O}(\log N)$），平均耗时大幅缩减。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **写成了 `p.val <= x and q.val <= x` 带等号** | 当 `root is p` 时继续向左子树递归，导致返回了错误子节点或抛出 `AttributeError` | 等号情况代表已经命中自身，不应继续向子树深入 | 严格使用严格不等号 `<` 和 `>`，等号直接走 `return root` |
| **误用 LC 236 后序全树双向递归** | 面试中被追问复杂度，未能利用 BST 导向特性 | 没有识别出 BST 可以单向检索，错失最优解法 | 牢记 BST 特性：双小向左，双大向右，分叉即答案 |
| **未对未排序的输入做包容** | 假设了 `p.val < q.val`，当输入 `p.val > q.val` 时逻辑出错 | 题目未保证 $p$ 和 $q$ 的先后大小顺序 | 分支条件中使用 `p.val < x and q.val < x`，对 $p$ 和 $q$ 的顺序天然免疫 |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 数值关系 (Comparison) | 决策分支 (Branch Decision) | 输出 (Output) |
| :--- | :--- | :--- | :---: |
| **两节点分居两侧 `[6,2,8]`, p=2, q=8** | $2 < 6$ 且 $8 > 6$ | 命中 Else 分叉条件 $\rightarrow$ 直接返回根节点 6 | `6` |
| **一节点为另一节点父节点 `[6,2,8,0,4]`, p=2, q=4** | 第 1 步: $2<6 \land 4<6$ (左拐)<br>第 2 步: $2=2 \land 4>2$ (分叉) | 第 1 步进入左子树 (2) $\rightarrow$ 第 2 步命中 `return root` | `2` |
| **两节点极小位于最左深处 `[6,2,8,0,4]`, p=0, q=4** | 第 1 步: $0<6 \land 4<6$ (左拐)<br>第 2 步: $0<2 \land 4>2$ (分叉) | 第 1 步进入 (2) $\rightarrow$ 第 2 步 $0<2$ 且 $4>2$ 命中分叉 | `2` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(H)$ | 其中 $H$ 为二叉搜索树的高度。算法从根节点开始沿着单一路径单向向下移动，每层只访问一个节点：<br>• **最好/平均情况 (平衡二叉搜索树)**: 耗时 $\mathcal{O}(\log N)$；<br>• **最坏情况 (退化为单链表)**: 耗时 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(H)$ / $\mathcal{O}(1)$ | • **递归实现**: 递归栈深度为树的高度 $H$，平均为 $\mathcal{O}(\log N)$，最坏为 $\mathcal{O}(N)$；<br>• **迭代实现**: 仅需常数个指针变量，空间开销严格为 $\mathcal{O}(1)$。 |
