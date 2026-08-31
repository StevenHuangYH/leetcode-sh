# LeetCode 103. Binary Tree Zigzag Level Order Traversal (二叉树的锯齿形层序遍历)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (广度优先搜索 / 锯齿形交替翻转 / 双数组分层遍历 / 奇偶层方向反转)
- **Tags:** Tree, Breadth-First Search, Binary Tree
- **Corresponding Python File:** [`daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py`](daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).
* **[CN]** 给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，下一层从右往左，以此类推，层与层之间交替进行）。

### Constraints / 约束条件
* 树中节点数目在范围 $[0, 2000]$ 内。
* $-100 \le \text{Node.val} \le 100$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 拓扑扫描与数值展示解耦不变量 (Topology BFS vs Value View Decoupling):    │
│    • 拓扑入队顺序绝对不可变: 无论当前层是奇数还是偶数，子节点的扫描与收集     │
│      必须严格恒定为先 node.left 再 node.right 入 nxt 数组，以维持下一层的    │
│      真实物理拓扑顺序。                                                     │
│    • 锯齿方向仅属于“视图层 (View Layer)”: 仅在将当前层 vals 追加至 ans 时，   │
│      根据 even 布尔标志位决定是否执行 vals[::-1] 镜像翻转。                  │
│ 2. 奇偶状态交替不变量 (Parity Toggle Invariant):                             │
│    • Level 0 (根节点层): 从左到右，even = False，直接追加 vals。             │
│    • Level 1: 从右到左，even = True，追加 vals[::-1]。                       │
│    • 每轮循环末尾执行: even = not even，严格维持两状态交替。                 │
│ 3. 双数组状态滚动 (Dual-Buffer State Roll Invariant):                        │
│    • 借助 cur 与 nxt 双列表实现层级物理切分，零 collections 依赖，且无      │
│      list.pop(0) 带来的 O(K) 内存搬移性能退化。                             │
│ 4. 空树前置防御 (Defensive Base Case):                                       │
│    • root is None 时短路返回 []，防止 cur = [None] 造成属性访问崩溃。        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Tree Hierarchies] ➔ [Tree Traversal] ➔ [Level Traverse]`

### 🧠 二叉树锯齿形层序思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Tree Level Traversal Family Tree (二叉树层序遍历谱系演化图)       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Direct BFS Primitive): LC 102 Binary Tree Level Order Traversal   │
│  └─ 标准分层 BFS: 逐层收集节点值 [[L0], [L1], [L2], ...]                     │
│        │                                                                    │
│        ├─► [演进 Twist 1: 水平方向按层奇偶反转 (Zigzag / Snake)]             │
│        │   LC 103 Zigzag Level Order Traversal (本题★)                      │
│        │   └─ 核心: 拓扑遍历依然从左到右，仅在收集输出时偶数层执行 vals[::-1]  │
│        │                                                                    │
│        ├─► [演进 Twist 2: 垂直方向层级收集倒置 (Bottom-Up)]                  │
│        │   LC 107 Binary Tree Level Order Traversal II                      │
│        │   └─ 核心: 正常 BFS 收集完毕后整体 ans.reverse()                    │
│        │                                                                    │
│        └─► [演进 Twist 3: 每层提取单侧极值视图 (Side Projection)]            │
│            LC 199 Binary Tree Right Side View                               │
│            └─ 核心: 每层仅保留最靠右的一个节点值 level_vals[-1]              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 形式化逻辑推演 (Zigzag Transformation Function)

设第 $d$ 层 ($d \ge 0$) 从左到右的节点物理值序列为 $\mathcal{V}_d = [v_1, v_2, \dots, v_k]$。

定义锯齿投影函数 $\mathcal{T}(\mathcal{V}_d, d)$：
$$\mathcal{T}(\mathcal{V}_d, d) = \begin{cases} 
[v_1, v_2, \dots, v_k], & \text{若 } d \equiv 0 \pmod 2 \quad (\text{从左到右}) \\
[v_k, v_{k-1}, \dots, v_1] = \mathcal{V}_d^{\text{rev}}, & \text{若 } d \equiv 1 \pmod 2 \quad (\text{从右到左}) 
\end{cases}$$

在此算法中，布尔变量 `even` 跟踪当前层的翻转状态：
- $d = 0$: `even = False` $\implies$ 追加 `vals` (即 $[v_1, \dots, v_k]$)；
- $d = 1$: `even = True` $\implies$ 追加 `vals[::-1]` (即 $[v_k, \dots, v_1]$)；
- 状态转移: $\text{even}_{d+1} = \neg \text{even}_d$。

---

### 🎨 ASCII 锯齿形遍历状态演进图解

以二叉树 `root = [3, 9, 20, null, null, 15, 7]` 为例：

```
                    ( 3 )                 <--- Level 0 (偶数层 0: 从左到右 ──►)
                  /       \
               ( 9 )     ( 20 )           <--- Level 1 (奇数层 1: ◄── 从右到左)
                         /    \
                      ( 15 )  ( 7 )       <--- Level 2 (偶数层 2: 从左到右 ──►)

═════════════════════════════════════════════════════════════════════
双数组分层与视图翻转执行推演 (Execution Trace):

[Round 0: 初始化]
  cur = [Node(3)], even = False, ans = []

[Round 1: 扫描 Level 0] (even = False)
  • cur 遍历: Node(3)
  • vals = [3]
  • nxt  = [Node(9), Node(20)] (严格先左后右)
  • even 为 False -> ans.append(vals) -> ans = [[3]]
  • 状态推进: cur = nxt, even = True

[Round 2: 扫描 Level 1] (even = True)
  • cur 遍历: Node(9), Node(20)
  • vals = [9, 20]
  • nxt  = [Node(15), Node(7)] (严格先左后右)
  • even 为 True -> ans.append(vals[::-1]) -> ans = [[3], [20, 9]]  <-- 翻转
  • 状态推进: cur = nxt, even = False

[Round 3: 扫描 Level 2] (even = False)
  • cur 遍历: Node(15), Node(7)
  • vals = [15, 7]
  • nxt  = []
  • even 为 False -> ans.append(vals) -> ans = [[3], [20, 9], [15, 7]]
  • 状态推进: cur = [], even = True

[Round 4: 终止]
  • while cur 为空，退出循环。
  • 最终返回: [[3], [20, 9], [15, 7]]
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py`](daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py) 中的实现进行逐行深入解析：

```python
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. 空树防御性拦截
        # 当输入为空节点时，直接返回空列表，避免后续 cur = [None] 引发非法访问
        if root is None:
            return []

        # 2. 初始化结果集、当前层节点列表与奇偶翻转标记
        ans = []
        cur = [root]   # 初始时当前层仅包含根节点
        even = False   # even 标记当前层是否需要翻转 (Level 0 从左往右，不翻转，故为 False)

        # 3. 外层主循环：当 cur 中仍有待处理的节点时继续执行
        while cur:
            nxt = []   # 用于暂存下一层的全部有效子节点
            vals = []  # 收集当前层节点的原始值 (严格保持物理拓扑从左到右)

            # 4. 顺序遍历当前层所有节点
            for node in cur:
                vals.append(node.val)
                # 无论当前层是奇是偶，子节点均按先左后右顺序登记到 nxt 中
                if node.left: 
                    nxt.append(node.left)
                if node.right: 
                    nxt.append(node.right)

            # 5. 层级交接与锯齿形视图注入
            cur = nxt                               # 推进到下一层
            ans.append(vals[::-1] if even else vals) # 若为反向层则切片翻转，否则原样追加
            even = not even                         # 切换下一层的奇偶反转标志

        # 6. 返回最终构建完成的锯齿形二维列表
        return ans
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 切片反转 `vals[::-1]` 会产生额外数组拷贝，如何用 `deque` 实现原位定向填充？

* **面试官**：你的解法在需要反转的层对 `vals` 进行了 `vals[::-1]` 切片操作，这会产生新的列表对象。如果不做任何切片翻转，如何在遍历节点时直接生成正确顺序的层级数组？
* **候选人解析**：
  * 使用双端队列 `collections.deque` 作为每层的 `vals` 容器：
    * 当正向层（`even = False`）时：使用 `vals.append(node.val)`（推入尾部）；
    * 当反向层（`even = True`）时：使用 `vals.appendleft(node.val)`（推入头部）。
  * 这样在遍历完成时，`list(vals)` 的顺序天然已经是锯齿形顺序，无需后置逆序切片。

```python
# 附: 双端队列原位填充解法 (Deque Direct Placement Template)
from collections import deque
from typing import Optional, List

class SolutionDequePlacement:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        q = deque([root])
        is_reverse = False
        
        while q:
            level_size = len(q)
            level_vals = deque()
            
            for _ in range(level_size):
                node = q.popleft()
                
                # 根据当前层方向决定推入头部还是尾部
                if is_reverse:
                    level_vals.appendleft(node.val)
                else:
                    level_vals.append(node.val)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            ans.append(list(level_vals))
            is_reverse = not is_reverse
            
        return ans
```

---

### 追问 2: 如何使用深度优先搜索 (DFS) 递归实现锯齿形层序遍历？

* **面试官**：能否使用 DFS 递归前序遍历携带 `depth` 参数来完成此题？
* **候选人解析**：
  * **DFS 核心逻辑**：
    * 递归函数 `dfs(node, depth)`。
    * 当 `depth == len(ans)` 时，创建并追加当前层的空列表 `ans.append([])`。
    * 核心分流：判断 `depth % 2`：
      * 若 `depth % 2 == 0`（偶数层/正向）：`ans[depth].append(node.val)`（追加到末尾）；
      * 若 `depth % 2 == 1`（奇数层/反向）：`ans[depth].insert(0, node.val)`（插入到头部）。
    * 递归顺序保持先左后右 `dfs(node.left, depth + 1)`，`dfs(node.right, depth + 1)`。

```python
# 附: DFS 深度索引递归解法 (DFS Preorder Template)
class SolutionDFS:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            
            if depth == len(ans):
                ans.append([])
                
            if depth % 2 == 0:
                ans[depth].append(node.val)
            else:
                ans[depth].insert(0, node.val)
                
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 0)
        return ans
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **错误地反向收集子节点** | 试图在 `nxt` 入队时根据奇偶调换 `node.right` 与 `node.left` | 破坏了底层节点的物理拓扑顺序，导致孙子节点的顺序完全错乱 | **拓扑与视图严格解耦**: 子节点入 `nxt` 必须恒为先左后右，仅翻转数值 `vals` |
| **奇偶标志初始值设反** | Level 0 根节点被反转，输出与预期完全相反 | 误以为第 1 层从右往左所以设 `even = True`，忽视了根节点是第 0 层 | 明确根节点层号为 $0$（从左往右），初始值必须设为 `even = False` |
| **空树未做防守导致崩溃** | 输入 `root = None` 时抛出 `AttributeError: 'NoneType' object has no attribute 'val'` | 初始直接 `cur = [root]`，未在入口拦截空指针 | 函数入口首行严格前置：`if root is None: return []` |
| **忘记更新标志位 `even = not even`** | 仅第一层反转，后续所有层全为同一方向 | 循环体末尾遗漏了布尔值取反语句 | 确保每轮 `while` 迭代结束时原子推进 `even = not even` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 拓扑形态 (Topology) | 每轮 `cur` $\rightarrow$ `vals` $\rightarrow$ 翻转判断 | 最终输出 (Output) |
| :--- | :--- | :--- | :---: |
| **空树 `root = []`** | 无任何节点 | 触发 `if root is None` 短路拦截 | `[]` |
| **单根节点 `[1]`** | 仅含一个节点 | R1: `vals=[1], even=False` $\rightarrow$ 追加 `[1]` $\rightarrow$ 结束 | `[[1]]` |
| **完全单斜树 `[1,2,null,3]`** | 深度为 3 的左单斜树 | L0: `[1]` (正向)<br>L1: `[2]` (反向 `[2]`)<br>L2: `[3]` (正向 `[3]`) | `[[1], [2], [3]]` |
| **满二叉树 `[1,2,3,4,5,6,7]`** | 3 层完全对称满树 | L0: `[1]` (正向)<br>L1: `[2,3]` $\rightarrow$ 翻转为 `[3,2]`<br>L2: `[4,5,6,7]` $\rightarrow$ 正向 `[4,5,6,7]` | `[[1], [3, 2], [4, 5, 6, 7]]` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | 其中 $N$ 为二叉树的节点总数。每个节点恰好入 `cur` 数组一次、出 `cur` 数组并读取其值一次。对于每一层，切片翻转 `vals[::-1]` 的时间开销与该层节点数 $K$ 严格成正比。所有层切片耗时之和为 $\sum K_i = N$。因此总时间复杂度严格为线性 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(N)$ | 空间开销由辅助列表 `cur`、`nxt` 和 `vals` 决定。在满二叉树或完全二叉树形态下，底层叶子节点数最多可达 $\lceil N/2 \rceil$ 个，此时辅助列表需容纳 $\mathcal{O}(N)$ 个节点引用。因此辅助空间复杂度为 $\mathcal{O}(N)$。*(注: 最终结果集 `ans` 存储所有节点值，占用 $\mathcal{O}(N)$ 空间)*。 |
