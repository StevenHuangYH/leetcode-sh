# LeetCode 110. Balanced Binary Tree (平衡二叉树)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (树形递归 / 后序遍历分治 / 自底向上带剪枝高度计算)
- **Tags:** Tree, Depth-First Search, Binary Tree
- **Corresponding Python File:** [`daily-practice/lc-0110-balanced-binary-tree.py`](daily-practice/lc-0110-balanced-binary-tree.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a binary tree, determine if it is **height-balanced**.
  * A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
* **[CN]** 给定一个二叉树，判断它是否是 **高度平衡** 的二叉树。
  * 本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

### Constraints / 约束条件
* 树中的节点数在范围 $[0, 5000]$ 内。
* $-10^4 \le \text{Node.val} \le 10^4$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 平衡二叉树严格定义 (Height-Balanced Invariant):                          │
│    • 对于树中任意节点 u: |height(u.left) - height(u.right)| <= 1             │
│    • 且 u.left 与 u.right 也必须均为平衡二叉树。                             │
│ 2. 避免顶向下重复计算 (Avoid Top-Down O(N^2) Redundancy):                    │
│    • 自顶向下 (先算高度再递归子树) 会导致高度被重复递归计算，退化为 O(N^2)。 │
│    • 自底向上后序遍历 (Bottom-Up Post-Order) 在计算子树高度的同时检验平衡性。 │
│ 3. 哨兵短路剪枝 (Sentinel Short-Circuit Pruning):                           │
│    • 定义 get_height(node) 返回非负整数高度；若子树不平衡则返回哨兵值 -1。    │
│    • 只要左/右子树返回 -1 或高度差 > 1，立即短路向上传递 -1，终止多余遍历。  │
│ 4. 树形 DP 奠基母题:                                                        │
│    • LC 104 (单树深度) → LC 110 (深度+合法性判定) → LC 543 (直径全局更新)。   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Tree Hierarchies] ➔ [Recursive Mindset] ➔ [Binary Tree]`

### 🧠 二叉树后序分治思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Tree Post-Order Divide & Conquer Lineage (二叉树后序分治谱系图)   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Pure Metric): LC 104 Maximum Depth of Binary Tree                 │
│  └─ 基础后序分治: height(u) = 1 + max(height(l), height(r))                 │
│        │                                                                    │
│        ▼ [演进 Twist: 附加合法性约束与短路剪枝 (Sentinel Early-Return)]      │
│  Level 2 (Metric + Predicate Pruning): LC 110 Balanced Binary Tree (本题★) │
│  └─ 状态合并: 若 |h_l - h_r| > 1 或已失衡则返回 -1，否则返回真实高度         │
│        │                                                                    │
│        ▼ [演进 Twist: 边计算深度边维护跨子树全局最长路径 (Global Path)]     │
│  Level 3 (Metric + Global Path Optimization): LC 543 Diameter of Tree       │
│  └─ 全局更新: max_diameter = max(max_diameter, h_l + h_r)                   │
│        │                                                                    │
│        ▼ [演进 Twist: 允许包含负权节点与局部截断贡献 (Max Path Sum)]        │
│  Level 4 (DP + Gain Truncation): LC 124 Binary Tree Maximum Path Sum        │
│  └─ 贡献截断: max_gain(u) = u.val + max(0, gain_l) + max(0, gain_r)         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 状态转移与形式化数学证明 (Mathematical Rationale)

定义递归函数 $\text{getHeight}(u)$，其值域为 $\{-1\} \cup \mathbb{N}$：

$$\text{getHeight}(u) = \begin{cases}
0, & \text{若 } u = \text{None} \\
-1, & \text{若 } \text{getHeight}(u.\text{left}) = -1 \\
-1, & \text{若 } \text{getHeight}(u.\text{right}) = -1 \\
-1, & \text{若 } |\text{getHeight}(u.\text{left}) - \text{getHeight}(u.\text{right})| > 1 \\
\max(\text{getHeight}(u.\text{left}), \text{getHeight}(u.\text{right})) + 1, & \text{其他情况 (平衡)}
\end{cases}$$

最终整棵树的平衡性判断为：
$$\text{isBalanced}(\text{root}) \iff \text{getHeight}(\text{root}) \neq -1$$

---

### 🎨 ASCII 自底向上后序高度计算与剪枝图解

以不平衡树 `root = [1, 2, 2, 3, 3, null, null, 4, 4]` 为例：

```
                 (1)
                /   \
              (2)   (2)
             /   \
           (3)   (3)
          /   \
        (4)   (4)

═════════════════════════════════════════════════════════════════════
自底向上短路推演过程 (Bottom-Up Post-Order Trace):

Step 1:
  • 节点 (4): 左高度 0，右高度 0 -> 返回 max(0,0)+1 = 1

Step 2:
  • 节点 (3): 左子树 (4) 高度 1，右子树 (4) 高度 1 -> 返回 max(1,1)+1 = 2

Step 3:
  • 节点 (2) (左侧):
    - 左子树 (3) 高度 = 2
    - 右子树 (3) 高度 = 2
    - abs(2 - 2) <= 1 -> 返回 max(2,2)+1 = 3

Step 4:
  • 节点 (2) (右侧):
    - 左子树 None 高度 0，右子树 None 高度 0 -> 返回 1

Step 5:
  • 根节点 (1):
    - 左子树高度 = 3
    - 右子树高度 = 1
    - 高度差 |3 - 1| = 2 > 1 -> 触发失衡! 立即返回 -1

Step 6:
  • 顶层判定: getHeight(root) == -1 -> 返回 False (非平衡树)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-0110-balanced-binary-tree.py`](daily-practice/lc-0110-balanced-binary-tree.py) 中的实现进行逐行深入解析：

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(node):
            # 递归基 (Base Case): 空节点高度为 0
            if node is None:
                return 0

            # 1. 递归计算左子树高度 (Left Subtree Height)
            left_height = get_height(node.left)
            # 短路剪枝: 若左子树已失衡，直接向上传递 -1，无需计算右子树
            if left_height == -1:
                return -1

            # 2. 递归计算右子树高度 (Right Subtree Height)
            right_height = get_height(node.right)
            # 短路剪枝: 若右子树已失衡，或当前节点左右子树高度差 > 1，标记失衡返回 -1
            if right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            # 3. 左右均平衡，返回当前子树的真实高度: max(left, right) + 1
            return max(left_height, right_height) + 1

        # 若根节点高度计算未触发 -1 哨兵，则整棵树高度平衡
        return get_height(root) != -1
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 为什么不用自顶向下 (Top-Down) 的两重递归解法？两者的复杂度差异是什么？

* **面试官**：如果我写一个 `maxDepth(root)` 函数，然后主函数写 `abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)`，这样写有什么缺陷？
* **候选人解析**：
  * **缺陷分析**：这是典型的**自顶向下暴力解法 (Top-Down Brute Force)**。
  * **重复计算**：每个节点的高度在父节点、祖父节点遍历时都会被重复计算。对于一棵退化为链表的二叉树，根节点计算深度访问 $N$ 个节点，其子节点访问 $N-1$ 个节点……总时间复杂度退化至 $\mathcal{O}(N^2)$。
  * **自底向上 (Bottom-Up) 优势**：采用后序遍历，每个节点仅被访问恰好一次，高度计算与平衡校验在单次遍历中合并完成，时间复杂度严格收敛至最优的 $\mathcal{O}(N)$。

---

### 追问 2: 如果不使用 `-1` 作为哨兵值，还有哪些优雅的状态传递范式？

* **面试官**：在工业级代码或强类型语言中，混合含义的 `-1` 可能被误当做正常高度。如何重构状态表达？
* **候选人解析**：
  * **方案 1：元组返回值 `Tuple[bool, int]` (显式状态传递)**
    * 辅助函数返回 `(is_balanced: bool, height: int)`，语义极其清晰。
  * **方案 2：自定义数据结构 `Result`**
    * 在 Java/C++ 中定义 `class TreeInfo { boolean isBalanced; int height; }`。

```python
# 附: 元组显式多返回值模板 (Explicit State Tuple)
class SolutionTuple:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode]) -> tuple[bool, int]:
            if not node:
                return True, 0
            
            left_balanced, left_h = check(node.left)
            if not left_balanced:
                return False, 0
            
            right_balanced, right_h = check(node.right)
            if not right_balanced:
                return False, 0
            
            balanced = abs(left_h - right_h) <= 1
            return balanced, max(left_h, right_h) + 1
        
        return check(root)[0]
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **自顶向下两重递归导致超时** | 在极端大用例 ($N=5000$) 下执行超时 TLE | 顶层节点重复计算子树高度，时间复杂度退化至 $\mathcal{O}(N^2)$ | 坚决使用后序遍历自底向上计算，在高度函数中集成 `-1` 哨兵 |
| **遗漏子树失衡短路传播** | 左右子树失衡但返回了 `-1`，父节点直接做 `max(-1, 0) + 1 = 1` 误判为平衡 | 未先对 `left_height == -1` 或 `right_height == -1` 进行拦截 | 计算完子树后第一步必须校验是否为 `-1`，失衡立即向上传递 `-1` |
| **高度差比较漏写绝对值 `abs`** | 左高右低判断正确，右高左低时 `left - right <= 1` 漏判失衡 | 忽略了高度差是双向的 | 严格使用 `abs(left_height - right_height) > 1` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 结构形态 (Structure) | 递归推演路径 (Trace) | 判定结果 (Result) |
| :--- | :--- | :--- | :---: |
| **空树 `root = []`** | `None` | `get_height(None)` 返回 0 $\rightarrow$ `0 != -1` | `True` |
| **单节点 `root = [1]`** | 仅根节点 | 左右子树均为 0，`abs(0-0) <= 1`，返回 1 $\rightarrow$ `1 != -1` | `True` |
| **完美平衡树 `[3,9,20,null,null,15,7]`** | 满二叉子树 | 左子树高度 1，右子树高度 2，高度差 1 $\le 1$，根返回 3 | `True` |
| **极左倾斜链表 `[1,2,null,3,null,4]`** | 退化为单链表 | 节点 (3) 高度 2，右为 0，高度差 2 > 1，立即触发 `-1` 短路 | `False` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | 其中 $N$ 为二叉树中的节点总数。后序遍历自底向上访问每个节点恰好一次；若遇到失衡节点，短路剪枝机制会立刻终止后续子树遍历，平均与最坏时间均为 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(H)$ | 其中 $H$ 为二叉树的高度。主要空间开销为系统递归调用栈：<br>• **最好/平均情况 (平衡二叉树)**: $H = \mathcal{O}(\log N)$；<br>• **最坏情况 (完全退化为单链表)**: $H = \mathcal{O}(N)$。 |
