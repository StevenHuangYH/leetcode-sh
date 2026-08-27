# LeetCode 100. Same Tree (相同的树)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (双指针树形递归 / 结构与数值全等判定 / 对偶树判定原语)
- **Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
- **Corresponding Python File:** [`daily-practice/lc-0100-same-tree.py`](daily-practice/lc-0100-same-tree.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
  * Two binary trees are considered the same if they are **structurally identical**, and the nodes have the **same value**.
* **[CN]** 给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验两棵树是否相同。
  * 如果两个树在 **结构上相同**，并且节点具有 **相同的值**，则认为它们是相同的。

### Constraints / 约束条件
* 两棵树上的节点数目都在范围 $[0, 100]$ 内。
* $-10^4 \le \text{Node.val} \le 10^4$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 全等定义 (Congruence Contract):                                          │
│    • 结构全等 (Structural Identity): p 与 q 的拓扑分支形态必须严格 1:1 对齐。 │
│    • 节点值相等 (Value Equality): 对应位置的节点值 p.val == q.val 必须成立。  │
│ 2. 分治与短路归并 (Divide & Conquer with Short-Circuit):                    │
│    • 两树相同 ⟺ (当前值相等) ∧ (左子树相同) ∧ (右子树相同)。               │
│ 3. 递归基极简表达 (Base Case Invariant):                                    │
│    • 若 p is None or q is None: 仅当两者同为 None (p is q) 时成立。         │
│ 4. 树形结构判定奠基母题:                                                    │
│    • 本题是 LC 101 对称二叉树、LC 572 另一棵树的子树、LC 951 翻转二叉树的基石。 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 二叉树结构判定思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Tree Congruence Pattern Lineage (二叉树全等与结构匹配谱系演化图) │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Single Tree Primitive): LC 104 Maximum Depth of Binary Tree       │
│  └─ 单树后序分治: height(u) = 1 + max(height(l), height(r))                 │
│        │                                                                    │
│        ▼ [演进 Twist: 扩展为双树同步遍历 (Dual-Tree Traversal)]             │
│  Level 2 (Dual Tree Direct Match): LC 100 Same Tree (本题★)                │
│  └─ 同向递归: isSame(p.left, q.left) and isSame(p.right, q.right)          │
│        │                                                                    │
│        ▼ [演进 Twist: 镜像轴对称匹配 (Mirror Inversion)]                     │
│  Level 3 (Mirror Match): LC 101 Symmetric Tree                              │
│  └─ 镜像对偶递归: isMirror(p.left, q.right) and isMirror(p.right, q.left)   │
│        │                                                                    │
│        ▼ [演进 Twist: 嵌套全量子树匹配 (Subtree Pattern Match)]              │
│  Level 4 (Pattern Search): LC 572 Subtree of Another Tree                   │
│  └─ 双层递归: isSame(root, subRoot) or isSubtree(root.l) or isSubtree(root.r)│
│        │                                                                    │
│        ▼ [演进 Twist: 允许单侧镜像翻转 (Equivalent Flip Match)]             │
│  Level 5 (Flip Equivalence): LC 951 Flip Equivalent Binary Trees            │
│  └─ 逻辑分支: (isFlip(l1,l2) and isFlip(r1,r2)) or (isFlip(l1,r2) and ...) │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 递归基与短路布尔逻辑 (Boolean Algebra & Short-Circuit)

设谓词函数为 $	ext{Same}(p, q)$，其严格形式化逻辑定义为：

$$\text{Same}(p, q) = \begin{cases}
\text{True}, & \text{若 } p = \text{None} \land q = \text{None} \\
\text{False}, & \text{若 } (p = \text{None} \land q \neq \text{None}) \lor (p \neq \text{None} \land q = \text{None}) \\
(p.\text{val} == q.\text{val}) \land \text{Same}(p.\text{left}, q.\text{left}) \land \text{Same}(p.\text{right}, q.\text{right}), & \text{若 } p \neq \text{None} \land q \neq \text{None}
\end{cases}$$

#### 优雅的 Python 一行判空技巧：
在 Python 中，当 `p is None or q is None` 为真时，若两指针地址完全相同（同为 `None`），`p is q` 严格求值为 `True`；若一空一非空，`p is q` 严格求值为 `False`。

---

### 🎨 ASCII 双树同步分治图解

以两棵树 `p = [1, 2, 3]`, `q = [1, 2, 3]` 为例：

```
       Tree P:                Tree Q:
         (1)                    (1)
        /   \                  /   \
      (2)   (3)                (2)   (3)

═════════════════════════════════════════════════════════════════════
同步递归判定推演 (Synchronous Divide & Conquer):

Step 1 (Root 比较):
  • p.val == q.val -> 1 == 1 (True)
  • 触发左子树深入: isSameTree(p.left, q.left) -> 比较节点 (2) 与 (2)

Step 2 (Left Child 比较):
  • 2 == 2 (True)
  • isSameTree(None, None) -> True (左空子树匹配)
  • isSameTree(None, None) -> True (右空子树匹配)
  • 节点 (2) 判定结果: True 归并返回

Step 3 (Right Child 比较):
  • 3 == 3 (True)
  • isSameTree(None, None) -> True
  • isSameTree(None, None) -> True
  • 节点 (3) 判定结果: True 归并返回

Step 4 (Root 聚合):
  • True (根值匹配) and True (左子树匹配) and True (右子树匹配) -> True
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件中的实现进行逐行深入解析：

```python
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 思考逻辑 (Core Cognitive Flow):
        # 1. the root must be the same (根节点值必须相等)
        # 2. then check if the left subtrees are the same (随后检验左子树是否相同)
        # 3. then the right subtrees (最后检验右子树是否相同)

        # base case (递归边界):
        # 若 p 与 q 至少有一个为 None，仅当两者同为 None (p is q) 时结构匹配
        if p is None or q is None:
            return p is q
        
        # 分治与短路求值 (Divide & Conquer with Short-Circuit):
        # 必须同时满足: 当前根值相等 ∧ 左子树完全相同 ∧ 右子树完全相同
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 如何使用广度优先遍历 (BFS) 队列实现非递归迭代解法？

* **面试官**：如果两棵树非常深，递归可能导致栈溢出。如何使用迭代队列（BFS）实现同步双树比较？
* **候选人解析**：
  * 使用单个双端队列 `collections.deque`，每次成对压入 `(p_node, q_node)`。
  * 每次循环弹出一对节点进行结构与数值校验，并将左右子节点成对入队。

```python
# 附: 双树同步层序遍历 BFS 模板 (Dual-Queue BFS)
from collections import deque

class SolutionBFS:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        
        while queue:
            node_p, node_q = queue.popleft()
            
            # 两者同为空，结构匹配，跳过深入
            if not node_p and not node_q:
                continue
            # 一空一非空，或数值不等，立即判假
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            
            # 成对推入左右子节点
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))
            
        return True
```

---

### 追问 2: 能否通过树的前序遍历与中序遍历序列化字符串直接比对？

* **面试官**：如果将两棵树分别序列化为包含空节点标记的字符串（如带 `null` 的前序遍历），然后直接比较字符串是否相等，这种方法可行吗？
* **候选人解析**：
  * **可行性**：严格可行。如果序列化过程中显式保留叶子节点的空指针标记（如 `#` 或 `null`），前序序列化结果与二叉树拓扑结构严格一一对应。
  * **优劣对比**：
    * 序列化字符串解法需要开辟额外 $\mathcal{O}(N)$ 空间存储全量字符串，且必须完整遍历两棵树才能完成比对。
    * 同步递归/BFS 解法具备**短路优势**（遇到首个不匹配节点立即 $\mathcal{O}(1)$ 返回），平均时空效率远高于全量序列化。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **直接读取空指针 `p.val == q.val`** | 输入 `p = [1], q = []` 时抛出 `AttributeError: NoneType object has no attribute val` | 未先对 `p` 和 `q` 进行判空就访问属性 | 访问 `.val` 前必须先执行 `if p is None or q is None` 拦截 |
| **判空逻辑遗漏同空情况** | 写为 `if not p and not q: return False` 导致空树被误判不同 | 两个空节点代表空子树在结构上完全相同，应返回 `True` | 严格使用 `if p is None or q is None: return p is q` |
| **左右子树比对交叉混淆** | 误写为 `isSameTree(p.left, q.right)` | 混淆了“相同树”（同向比对）与“对称树”（镜像比对 LC 101）的递归语义 | 同向全等必须严格对齐 `p.left` 配 `q.left`、`p.right` 配 `q.right` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 结构形态 (Structure) | 递归推演路径 (Trace) | 判定结果 (Result) |
| :--- | :--- | :--- | :---: |
| **两树皆为空 `p = [], q = []`** | `None` 与 `None` | 命中 Base Case `p is None or q is None` $\rightarrow$ `p is q` (True) | `True` |
| **一空一非空 `p = [1], q = []`** | `[1]` 与 `None` | 命中 Base Case $\rightarrow$ `p is q` (False) | `False` |
| **结构相同数值不同 `p=[1,2], q=[1,3]`** | 左侧叶子值不同 | 根 `1==1` $\rightarrow$ 左子树 `2==3` 返回 `False`，立即短路退出 | `False` |
| **结构互为镜像 `p=[1,2], q=[1,null,2]`** | 一棵左偏，一棵右偏 | 根 `1==1` $\rightarrow$ 比较 `p.left([2])` 与 `q.left(None)` $\rightarrow$ 判假 | `False` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(\min(N, M))$ | $N$ 和 $M$ 分别为两棵二叉树的节点数。最差情况下（两树完全相同），算法同步遍历两树的每个节点恰好一次，访问节点数为 $\min(N, M)$；最好情况下（根节点值不同或一空一非空），首步即短路退出，耗时 $\mathcal{O}(1)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(\min(H_p, H_q))$ | $H_p$ 与 $H_q$ 分别为两棵树的高度。空间开销由系统递归调用栈决定：<br>• **最好/平均情况 (平衡二叉树)**: $\mathcal{O}(\log(\min(N, M)))$；<br>• **最差情况 (完全退化为单链表)**: $\mathcal{O}(\min(N, M))$。 |
