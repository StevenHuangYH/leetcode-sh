# LeetCode 513. Find Bottom Left Tree Value (找树左下角的值)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (广度优先搜索 / 逆序层序遍历 / 从右向左流式出队 / 树的最底层最左节点捕获)
- **Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
- **Corresponding Python File:** [`daily-practice/lc-0513-find-bottom-left-tree-value.py`](daily-practice/lc-0513-find-bottom-left-tree-value.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `root` of a binary tree, return the leftmost value in the last row of the tree.
* **[CN]** 给定一个二叉树的 根节点 `root`，请找出该二叉树的 **最底层 最左边** 节点的值。假设二叉树中至少有一个节点。

### Constraints / 约束条件
* 二叉树中节点数目在范围 $[1, 10^4]$ 内。
* $-2^{31} \le \text{Node.val} \le 2^{31} - 1$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 逆序 BFS 单调性不变量 (Right-to-Left Monotonicity Invariant):            │
│    • 正向 BFS (先入左后入右): 最后一层最后一个出队节点 ⟹ 【最底层最右侧节点】│
│    • 逆序 BFS (先入右后入左): 最后一层最后一个出队节点 ⟹ 【最底层最左侧节点】│
│ 2. 状态零开销收敛 (Zero-Buffer Final Node Invariant):                        │
│    • 无需使用 for _ in range(len(q)) 做分层切片，也无需维护层级数组 vals。    │
│    • 全局队列流式推进，while q 循环终止时，最后被弹出的 node 即为最终答案！   │
│ 3. 防御性初始化与作用域保障 (Defensive Initialization Guard):                │
│    • 前置判空: if not root: return 0 抵御异常输入。                          │
│    • 显式赋值: node = root 消除静态类型分析器关于变量作用域未绑定的警告。    │
│ 4. 树形层序遍历思维谱系中的极值筛选原语:                                    │
│    • LC 102 (全量收集) → LC 199 (每层最右) → LC 513 (全树最底最左 本题★)。   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Tree Hierarchies] ➔ [Tree Traversal] ➔ [Level Traverse]`

### 🧠 二叉树层序视图思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Tree Level Traversal & Extremum Lineage (二叉树层序极值谱系演化图) │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Full Level Collection): LC 102 Binary Tree Level Order Traversal  │
│  └─ 全量分层 BFS: 队列收集每一层的全部节点 [[L0], [L1], [L2]]               │
│        │                                                                    │
│        ├─► [演进 Twist 1: 每层仅筛选最右端点 (Rightmost per Level)]          │
│        │   LC 199 Binary Tree Right Side View                               │
│        │   ├─ BFS 方案: 取每层队列末尾元素 level_vals[-1]                   │
│        │   └─ DFS 方案: 根-右-左优先，利用 depth == len(ans) 捕获首访       │
│        │                                                                    │
│        └─► [演进 Twist 2: 全树仅筛选最底层最左端点 (Global Bottom-Left)]     │
│            LC 513 Find Bottom Left Tree Value (本题★)                       │
│            ├─ 逆序 BFS 方案: 先入右后入左，全树【最后弹出的节点】即为答案     │
│            ├─ 正向 BFS 方案: 标准分层 BFS，记录最后一层的首个节点 vals[0]    │
│            └─ DFS 方案: 根-左-右优先，记录 max_depth 首次被突破时的节点值   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 形式化逻辑推演 (Reverse BFS Deque Invariant)

设二叉树的拓扑深度为 $H$，第 $d$ 层 ($0 \le d < H$) 包含 $k_d$ 个物理节点，从左至右记为：
$$\mathcal{L}_d = [u_{d, 1}, u_{d, 2}, \dots, u_{d, k_d}]$$

目标是求解最底层最左侧节点的值：$\text{Target} = u_{H-1, 1}.\text{val}$。

在**逆序 BFS** 中，对于任意父节点 $u$，入队顺序严格为**先右子节点后左子节点**：
1. **跨层访问单调性**：层号较浅的节点严格在层号较深的节点之前出队。即 $\forall d_1 < d_2$，$\mathcal{L}_{d_1}$ 的所有节点均先于 $\mathcal{L}_{d_2}$ 出队。
2. **同层访问单调性**：在同一深度 $d$ 内，右侧节点严格先于左侧节点入队与出队。即出队序列为：
$$u_{d, k_d}, u_{d, k_d - 1}, \dots, u_{d, 2}, u_{d, 1}$$
3. **全局最终出队节点**：
根据 (1) 和 (2)，整个 BFS 遍历过程中，**全树最后进入队列并最后被 `popleft()` 弹出的节点**必为：
$$\text{Last Node} = u_{H-1, 1}$$
因此，当 `while q:` 循环终止时，`node.val` 恒等于 $u_{H-1, 1}.\text{val}$！

---

### 🎨 ASCII 逆序 BFS 队列状态迁移图解

以树 `root = [1, 2, 3, 4, null, 5, 6, null, null, 7]` 为例：

```
                     ( 1 )                  <--- Depth 0
                   /       \
                ( 2 )     ( 3 )             <--- Depth 1
                /         /   \
              ( 4 )     ( 5 ) ( 6 )         <--- Depth 2
                         /
                       ( 7 )                <--- Depth 3 (最底最左节点: 7)

═════════════════════════════════════════════════════════════════════
逆序 BFS (从右往左入队) 执行时序追踪表:

Step 0: 初始化
  • Queue: [Node(1)]

Step 1: 弹出 Node(1)
  • 右孩子 3 入队，左孩子 2 入队 ──► Queue: [Node(3), Node(2)]

Step 2: 弹出 Node(3)
  • 右孩子 6 入队，左孩子 5 入队 ──► Queue: [Node(2), Node(6), Node(5)]

Step 3: 弹出 Node(2)
  • 无右孩子，左孩子 4 入队 ──────► Queue: [Node(6), Node(5), Node(4)]

Step 4: 弹出 Node(6)
  • 无子节点 ─────────────────────► Queue: [Node(5), Node(4)]

Step 5: 弹出 Node(5)
  • 无右孩子，左孩子 7 入队 ──────► Queue: [Node(4), Node(7)]

Step 6: 弹出 Node(4)
  • 无子节点 ─────────────────────► Queue: [Node(7)]

Step 7: 弹出 Node(7)  <── 【最后被弹出的节点！】
  • 无子节点 ─────────────────────► Queue: []

Step 8: 循环结束，返回 node.val = 7。
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-0513-find-bottom-left-tree-value.py`](daily-practice/lc-0513-find-bottom-left-tree-value.py) 中的实现进行逐行深入解析：

```python
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # 1. 前置防御性判空
        # 若传入空树，直接返回 0，确保系统鲁棒性
        if not root:
            return 0

        # 2. 初始化双端队列并将根节点入队
        q = deque([root])

        # 3. 显式初始化 node 指针为 root
        # 消除静态检查器关于 "node 可能未绑定" 的变量作用域警告
        node = root

        # 4. 逆序 BFS 主循环 (从右向左流式出队)
        while q:
            node = q.popleft() # 弹出当前队首节点 (最后弹出的必定是最底层最左节点)

            # 5. 核心：严格先推入右孩子，后推入左孩子
            # 确保在同层中，右侧节点先被处理，左侧节点更晚出队
            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)

        # 6. 循环结束时，node 自然驻留在全树最后一个出队的节点上，直接返回其数值
        return node.val
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 如果使用正向分层 BFS（从左到右），代码该如何组织？两种 BFS 有何优劣？

* **面试官**：逆序 BFS 非常精妙。如果让你用传统的正向分层 BFS（`for _ in range(len(q))` 先左后右）实现，该怎么写？
* **候选人解析**：
  * **正向分层 BFS**：利用 `len(q)` 将层与层严格隔离。在每一层处理开始时，记录第 0 个弹出的节点 `if i == 0: ans = node.val`。随着层级向下推进，`ans` 会被更深层的首个节点不断覆盖，最终保留最后一层的首个节点。
  * **优劣对比**：
    * **逆序 BFS (User's Solution)**：代码行数极少（无内层循环），无需维护 `ans` 变量，逻辑浑然天成。
    * **正向分层 BFS**：更符合通用层序遍历模板，易于扩展到需要按层做统计的变体题目中。

```python
# 附: 正向分层 BFS 模板 (Standard Level-by-Level BFS)
class SolutionStandardBFS:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        ans = root.val
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                # 记录当前层的第一个节点值 (最左侧节点)
                if i == 0:
                    ans = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return ans
```

---

### 追问 2: 能否使用深度优先搜索 (DFS) 递归解决？时空复杂度与 BFS 相比如何？

* **面试官**：如何用 DFS 递归前序遍历寻找树左下角的值？
* **候选人解析**：
  * **DFS 核心思想**：
    * 采用**根 $\rightarrow$ 左 $\rightarrow$ 右**的前序遍历顺序。
    * 维护全局变量 `max_depth` 与 `ans`。
    * 当且仅当递归触达更深层（`cur_depth > max_depth`）时，**由于左子树优先被访问**，此时遇到的第一个节点必定是该新深度的最左节点，立即更新 `max_depth = cur_depth` 与 `ans = node.val`。
    * 后续同层右侧节点即便被访问，因 `cur_depth == max_depth`（不满足严格大于），不会被错误覆盖。
  * **时空对比**：
    * **DFS 空间优势**：栈深度仅为 $\mathcal{O}(H)$，在平衡二叉树下仅占用 $\mathcal{O}(\log N)$ 空间，优于 BFS 队列的 $\mathcal{O}(W)$ 宽度空间。

```python
# 附: DFS 深度优先递归模板 (DFS Preorder Depth Tracking)
class SolutionDFS:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        ans = root.val
        
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            nonlocal max_depth, ans
            if not node:
                return
            
            # 首次触达更深的一层，且由左子树先达，记录最左节点值
            if depth > max_depth:
                max_depth = depth
                ans = node.val
                
            dfs(node.left, depth + 1)  # 严格先左
            dfs(node.right, depth + 1) # 后右
            
        dfs(root, 0)
        return ans
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **逆序 BFS 中入队顺序写反** | 错误写为 `if node.left: q.append` 先入队，导致输出最底层最右侧节点 | 混淆了逆序入队的方向单调性，先入左会导致左节点先出队，右节点最后出队 | 逆序 BFS 必须严格保证 `if node.right:` 在 `if node.left:` 前入队 |
| **DFS 递归顺序写反** | 误写为 `dfs(node.right)` 优先于 `dfs(node.left)` | 导致最深层最先触发 `depth > max_depth` 的变成最右节点 | DFS 寻找最左节点必须使用**先左后右**的前序遍历 |
| **正向 BFS 未分层导致误取** | 不写 `len(q)` 循环，在流式弹出中取首节点 | 每次出队都会更新 `ans`，最终退化为取到最后一层的最右节点 | 正向 BFS 必须显式维护 `len(q)` 并在 `i == 0` 时单点采样 |
| **局部变量未初始化警告** | 在某些 IDE 中提示 `node` 变量可能在循环外未绑定 | `node` 仅在 `while q:` 内部赋值 | 循环前显式赋值 `node = root` 增强代码健壮性 |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 拓扑形态 (Topology) | 逆序出队序列 (Popped Sequence) | 最终输出 (Output) |
| :--- | :--- | :--- | :---: |
| **单根节点 `[1]`** | 仅含一个节点 | `1` 出队，循环结束 | `1` |
| **完全左单斜树 `[1, 2, null, 3]`** | 深度为 3 的左斜链表 | `1` $\rightarrow$ `2` $\rightarrow$ `3` | `3` |
| **完全右单斜树 `[1, null, 2, null, 3]`** | 深度为 3 的右斜链表 | `1` $\rightarrow$ `2` $\rightarrow$ `3` | `3` |
| **标准二叉树 `[2, 1, 3]`** | 完美对称二叉树 | `2` $\rightarrow$ `3` $\rightarrow$ `1` (最后弹出 `1`) | `1` |
| **不平衡底层 `[1,2,3,4,null,5,6,null,null,7]`** | 最底层 7 位于节点 5 的左孩子 | `1` $\rightarrow$ `3` $\rightarrow$ `2` $\rightarrow$ `6` $\rightarrow$ `5` $\rightarrow$ `4` $\rightarrow$ `7` | `7` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | 其中 $N$ 为二叉树的节点总数。算法执行标准的流式广度优先遍历，树中的每一个节点 $u \in V$ 恰好入队一次并出队一次。队列的入队与出队操作耗时均为 $\mathcal{O}(1)$，因此整体运行时间严格为线性 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(W) = \mathcal{O}(N)$ | 其中 $W$ 为二叉树的最大层宽。空间开销取决于双端队列 `q` 中同时存储的最大节点数。在最坏情况下（如满二叉树 Full Binary Tree），底层叶子节点数目为 $\lceil N/2 \rceil$，队列最多同时容纳 $\mathcal{O}(N)$ 个节点引用；在最好情况下（单链表树），空间开销降为 $\mathcal{O}(1)$。 |
