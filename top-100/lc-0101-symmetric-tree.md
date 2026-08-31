# LeetCode 101. Symmetric Tree (对称二叉树)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (双指针树形递归 / 轴对称镜像判定 / 对偶树判定原语)
- **Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
- **Corresponding Python File:** [`top-100/lc-0101-symmetric-tree.py`](top-100/lc-0101-symmetric-tree.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
* **[CN]** 给你一个二叉树的根节点 `root` ，检查它是否轴对称。

### Constraints / 约束条件
* 树中节点数目在范围 $[1, 1000]$ 内。
* $-100 \le \text{Node.val} \le 100$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 轴对称本质 (Axis-Symmetric Invariant):                                  │
│    • 单树对称 ⟺ 根节点的左子树与右子树互为镜像 (Mirror Images)。             │
│ 2. 镜像全等公理 (Mirror Congruence Axiom):                                  │
│    • 两个子树 p 与 q 互为镜像 ⟺                                              │
│        (p.val == q.val) ∧ (p.left 与 q.right 镜像) ∧ (p.right 与 q.left 镜像) │
│ 3. 递归基极简表达 (Base Case Invariant):                                    │
│    • 若 p is None or q is None: 仅当两者同为 None (p is q) 时成立。         │
│ 4. 树形结构判定核心母题:                                                    │
│    • LC 100 (同向全等比对) → LC 101 (镜像对偶比对) → LC 951 (翻转等价判定)。 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Tree Hierarchies] ➔ [Recursive Mindset] ➔ [Binary Tree]`

### 🧠 二叉树结构判定思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Tree Congruence Pattern Lineage (二叉树全等与结构匹配谱系演化图) │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Single Tree Primitive): LC 104 Maximum Depth of Binary Tree       │
│  └─ 单树后序分治: height(u) = 1 + max(height(l), height(r))                 │
│        │                                                                    │
│        ▼ [演进 Twist: 扩展为双树同向同步遍历 (Dual-Tree Parallel Match)]    │
│  Level 2 (Dual Tree Direct Match): LC 100 Same Tree                         │
│  └─ 同向递归: isSame(p.left, q.left) and isSame(p.right, q.right)          │
│        │                                                                    │
│        ▼ [演进 Twist: 单树拆分 + 跨子树镜像轴对称比对 (Mirror Cross Match)] │
│  Level 3 (Mirror Match): LC 101 Symmetric Tree (本题★)                      │
│  └─ 镜像对偶递归: isMirror(p.left, q.right) and isMirror(p.right, q.left)   │
│        │                                                                    │
│        ▼ [演进 Twist: 嵌套全量子树匹配 (Subtree Pattern Match)]              │
│  Level 4 (Pattern Search): LC 572 Subtree of Another Tree                   │
│  └─ 双层递归: isSame(root, subRoot) or isSubtree(root.l) or isSubtree(root.r)│
│        │                                                                    │
│        ▼ [演进 Twist: 允许子节点自主选择翻转与否 (Flip Equivalence)]        │
│  Level 5 (Flip Equivalence): LC 951 Flip Equivalent Binary Trees            │
│  └─ 组合逻辑: (isFlip(l1,l2) and isFlip(r1,r2)) or (isFlip(l1,r2) and ...) │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 形式化证明与镜像谓词定义 (Mathematical Rationale)

设谓词函数 $\text{Mirror}(p, q)$ 表示以 $p$ 与 $q$ 为根的两棵子树互为镜像，其形式化定义如下：

$$\text{Mirror}(p, q) = \begin{cases}
\text{True}, & \text{若 } p = \text{None} \land q = \text{None} \\
\text{False}, & \text{若 } (p = \text{None} \land q \neq \text{None}) \lor (p \neq \text{None} \land q = \text{None}) \\
(p.\text{val} == q.\text{val}) \land \text{Mirror}(p.\text{left}, q.\text{right}) \land \text{Mirror}(p.\text{right}, q.\text{left}), & \text{若 } p \neq \text{None} \land q \neq \text{None}
\end{cases}$$

整棵树的轴对称性可归约为：
$$\text{isSymmetric}(\text{root}) = \text{Mirror}(\text{root.left}, \text{root.right})$$

---

### 🎨 ASCII 镜像交叉分治图解

以对称树 `root = [1, 2, 2, 3, 4, 4, 3]` 为例：

```
                    (1)
                 /       \
              (2)         (2)
             /   \       /   \
           (3)   (4)   (4)   (3)
            ^     ^     ^     ^
            │     └─────┘     │
            │     内侧配对    │
            └─────────────────┘
                  外侧配对

═════════════════════════════════════════════════════════════════════
镜像双指针推演过程 (Mirror Cross Traversal):

Step 1 (Root 分流):
  • root 自身天然对称，问题降维为判定: isMirror(root.left, root.right)

Step 2 (Outer Pair 外侧比对):
  • 比较 p.left (3) 与 q.right (3):
    - 3 == 3 (True)
    - 子节点全为 None -> 返回 True

Step 3 (Inner Pair 内侧比对):
  • 比较 p.right (4) 与 q.left (4):
    - 4 == 4 (True)
    - 子节点全为 None -> 返回 True

Step 4 (Subtree 归并):
  • p.val == q.val (2 == 2, True) ∧ Step 2 (True) ∧ Step 3 (True) -> True
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0101-symmetric-tree.py`](top-100/lc-0101-symmetric-tree.py) 中的实现进行逐行深入解析：

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case (递归边界拦截):
        # 若 p 与 q 至少有一个为 None，仅当两者同为 None (p is q) 时镜像结构匹配
        if p is None or q is None:
            return p is q
        
        # 核心交叉分治 (Cross Divide & Conquer):
        # 1. 对应节点值相等: p.val == q.val
        # 2. 外侧子树镜像: isMirror(p.left, q.right)
        # 3. 内侧子树镜像: isMirror(p.right, q.left)
        return p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 单树对称问题转化为双子树镜像判定
        return self.isMirror(root.left, root.right)
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 如何使用队列 (BFS) 或栈 (DFS) 实现非递归迭代解法？

* **面试官**：递归调用会占用系统栈空间。如果树的高度极大，如何用显式队列实现迭代版本？
* **候选人解析**：
  * 使用双端队列 `collections.deque`，初始时将 `(root.left, root.right)` 成对入队。
  * 每次循环连续取出两个对称节点 `u` 与 `v`：
    * 若两者同为空，合法，继续后续比对；
    * 若一空一非空，或数值不相等，立即返回 `False`；
    * 否则按照**镜像对称顺序**成对推入子节点：`(u.left, v.right)` 和 `(u.right, v.left)`。

```python
# 附: 迭代双端队列 BFS 镜像解法 (Queue BFS Template)
from collections import deque
from typing import Optional

class SolutionBFS:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            u, v = queue.popleft()
            
            if not u and not v:
                continue
            if not u or not v or u.val != v.val:
                return False
            
            # 外侧配对入队
            queue.append((u.left, v.right))
            # 内侧配对入队
            queue.append((u.right, v.left))
            
        return True
```

---

### 追问 2: 能否通过中序遍历序列是否为回文串来判定二叉树是否对称？

* **面试官**：很多初学者认为“对称二叉树的中序遍历一定是回文序列”，能否仅通过中序遍历判断对称性？
* **候选人解析**：
  * **结论**：**不能**。普通中序遍历忽略了结构信息（Null 节点的占位）。
  * **反例**：考虑树 `[1, 2, 2, 2, null, 2]`：
    * 其普通中序遍历序列为 `[2, 2, 1, 2, 2]`（是回文串）。
    * 但该树结构上并不对称（左子树有左孩子，右子树有左孩子而非右孩子）。
  * **修正条件**：如果中序遍历中严格保留所有空节点的标记（如 `#`），并且配合前序遍历，或者使用带空指针层序遍历，才能完整还原拓扑形态。因此直接使用镜像双指针遍历是最优且最安全的选择。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **同向递归混淆 (误写为同向比对)** | 误写为 `isMirror(p.left, q.left)` | 混淆了 LC 100（同向全等）与 LC 101（轴对称镜像）的递归分支 | 镜像比对必须外侧配外侧 (`p.l, q.r`)、内侧配内侧 (`p.r, q.l`) |
| **根节点子树未判空直接访问属性** | 写为 `return self.isMirror(root.left.val, ...)` | 空节点触发 `AttributeError: 'NoneType' object has no attribute 'val'` | 将指针本身传给 `isMirror`，由 helper 统一处理 Base Case 判空 |
| **判空逻辑中将一空一非空漏判** | 写为 `if not p and not q: return True` 但未拦截 `not p or not q` | 导致后续 `p.val` 报错 | 使用短路结构 `if p is None or q is None: return p is q` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 结构形态 (Structure) | 递归推演路径 (Trace) | 判定结果 (Result) |
| :--- | :--- | :--- | :---: |
| **单根节点 `root = [1]`** | 仅一个节点 | `isMirror(None, None)` $\rightarrow$ `None is None` (True) | `True` |
| **标准对称树 `[1,2,2,3,4,4,3]`** | 完美轴对称 | 外侧 `(3,3)` 匹配 + 内侧 `(4,4)` 匹配 $\rightarrow$ 全 True | `True` |
| **结构不对称 `[1,2,2,null,3,null,3]`** | 节点都在右侧 | `isMirror(p.left(None), q.right(3))` $\rightarrow$ 一空一非空判假 | `False` |
| **数值不对称 `[1,2,2,3,null,null,2]`** | 结构对称数值不同 | 外侧比对 `3 == 2` $\rightarrow$ 返回 False | `False` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | 其中 $N$ 为二叉树的节点总数。最坏情况下（整棵树完全对称），递归恰好访问树中的每一个节点一次；最好情况下（根节点的左右孩子值不同），$\mathcal{O}(1)$ 短路返回。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(H)$ | 其中 $H$ 为二叉树的高度。空间开销主要取决于系统递归栈的深度：<br>• **最好/平均情况 (平衡二叉树)**: $H = \mathcal{O}(\log N)$；<br>• **最坏情况 (树退化为单链表)**: $H = \mathcal{O}(N)$。 |
