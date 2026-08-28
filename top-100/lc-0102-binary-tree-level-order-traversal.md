# LeetCode 102. Binary Tree Level Order Traversal (二叉树的层序遍历)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (广度优先搜索 / 双数组分层迭代 / 队列层序遍历 / 树形结构分层切片)
- **Tags:** Tree, Breadth-First Search, Binary Tree
- **Corresponding Python File:** [`top-100/lc-0102-binary-tree-level-order-traversal.py`](top-100/lc-0102-binary-tree-level-order-traversal.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).
* **[CN]** 给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

### Constraints / 约束条件
* 树中节点数目在范围 $[0, 2000]$ 内。
* $-1000 \le \text{Node.val} \le 1000$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 层级隔离不变量 (Level-by-Level Isolation Invariant):                     │
│    • 普通流式 BFS 只保证节点按距离单调出队，但模糊了“层与层”之间的物理边界。 │
│    • 层序遍历必须显式划定层级切片，将同一深度 depth 的节点值打包为独立子列表。│
│ 2. 状态滚动双数组模型 (Dual-Buffer State Roll Invariant):                    │
│    • cur: 容纳当前层全部有效非空节点引用。                                   │
│    • nxt: 在遍历 cur 过程中实时收集所有子节点 (node.left, node.right)。     │
│    • 层级交接: 当前层处理完毕后，执行 ans.append(vals) 与 cur = nxt 滚动。   │
│ 3. 空树前置防御 (Defensive Guard Invariant):                                 │
│    • 若 root is None，必须立即短路返回空列表 []，避免 cur = [None] 污染迭代。│
│ 4. 树形层序母题基石地位:                                                    │
│    • LC 102 是层序遍历全谱系（LC 107 自底向上 / LC 103 之字形 / LC 199 视图 / │
│      LC 513 最底层最左 / LC 116 同层指针连接）的母题源头。                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 二叉树层序遍历思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Tree Level Traversal Pattern Lineage (二叉树层序思维谱系演化图)   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Single Node / Depth): LC 104 Maximum Depth of Binary Tree         │
│  └─ 树高递归统计: depth(u) = 1 + max(depth(l), depth(r))                    │
│        │                                                                    │
│        ▼ [演进 Twist: 引入跨层广度优先扫描，按深度严格分块 (Level Chunking)]│
│  Level 2 (Standard Level BFS): LC 102 Binary Tree Level Order (本题★)       │
│  ├─ 范式 A: 双数组滚动法 (cur + nxt) —— 极致轻量、零 deque 开销              │
│  ├─ 范式 B: 单队列快照法 (len(queue) BFS) —— 经典队列定长迭代                │
│  └─ 范式 C: DFS 深度索引法 (dfs(node, depth)) —— 前序递归层级收集           │
│        │                                                                    │
│        ├─► [演进 Twist: 纵向层级收集顺序倒置 (Bottom-Up)]                   │
│        │   LC 107 Binary Tree Level Order Traversal II                      │
│        │   └─ 策略: 收集完成后 ans.reverse() 或 ans.insert(0, vals)         │
│        │                                                                    │
│        ├─► [演进 Twist: 横向遍历方向按层奇偶交替 (Zigzag Alternate)]         │
│        │   LC 103 Binary Tree Zigzag Level Order Traversal                  │
│        │   └─ 策略: 根据层号奇偶执行 vals.reverse() 或双端队列交替入队      │
│        │                                                                    │
│        ├─► [演进 Twist: 每层仅保留单侧极值端点 (Extreme Boundary Filter)]    │
│        │   LC 199 Right Side View / LC 513 Bottom-Left Value                │
│        │   └─ 策略: 提取每层 vals[-1] (右视图) 或最后一层 vals[0] (左下角)   │
│        │                                                                    │
│        └─► [演进 Twist: 同层兄弟节点横向指针物理串联 (Physical Linkage)]    │
│            LC 116 / LC 117 Populating Next Right Pointers in Each Node      │
│            └─ 策略: 遍历当前层时为 node.left.next = node.right 建立链表     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 形式化逻辑推演 (Dual-Buffer Level BFS Invariant)

设二叉树每一层的节点集合为 $\mathcal{L}_d = \{ u \in V \mid \text{depth}(u) = d \}$，其中根节点所在层 $\mathcal{L}_0 = \{\text{root}\}$。

下一层节点集合 $\mathcal{L}_{d+1}$ 严格满足如下子节点并集转移方程：
$$\mathcal{L}_{d+1} = \bigcup_{u \in \mathcal{L}_d} \Big( \text{Children}(u) \setminus \{\text{None}\} \Big)$$

双数组迭代算法的状态转移机制：
1. **初始状态**：`cur` 赋值为包含根节点的单元素列表 $[\text{root}]$；结果集 `ans = []`。
2. **每轮迭代**：
   * 构造临时缓存：`nxt = []` 用于存储 $\mathcal{L}_{d+1}$；`vals = []` 用于存储 $\mathcal{L}_d$ 的节点值。
   * 遍历 `cur` 中的每一个节点 $u \in \mathcal{L}_d$：
     * `vals.append(u.val)`
     * 若 $u.\text{left} \neq \text{None}$，则 `nxt.append(u.left)`
     * 若 $u.\text{right} \neq \text{None}$，则 `nxt.append(u.right)`
   * 将当前层数值数组入库：`ans.append(vals)`。
   * 状态无缝迁移：`cur = nxt`。
3. **终止条件**：当某一层的所有节点均无子节点时，`nxt` 为空列表，此时下一轮 `while cur` 条件不满足，循环平稳退出。

---

### 🎨 ASCII 双数组分层收集与状态迭代图解

以树 `root = [3, 9, 20, null, null, 15, 7]` 为例：

```
                    ( 3 )                 <--- Level 0
                  /       \
               ( 9 )     ( 20 )           <--- Level 1
                         /    \
                      ( 15 )  ( 7 )       <--- Level 2

═════════════════════════════════════════════════════════════════════
双数组分层迭代状态演进表 (State Roll Execution Trace):

[Round 0: 初始化]
  cur = [Node(3)]
  ans = []

[Round 1: 扫描 Level 0]
  • 遍历 cur 中的 Node(3):
      vals = [3]
      nxt  = [Node(9), Node(20)]
  • 提交层级数据: ans.append(vals) -> ans = [[3]]
  • 状态滚动: cur = nxt -> cur = [Node(9), Node(20)]

[Round 2: 扫描 Level 1]
  • 遍历 cur 中的 Node(9):
      vals = [9]
      nxt  = [] (Node(9) 无子节点)
  • 遍历 cur 中的 Node(20):
      vals = [9, 20]
      nxt  = [Node(15), Node(7)]
  • 提交层级数据: ans.append(vals) -> ans = [[3], [9, 20]]
  • 状态滚动: cur = nxt -> cur = [Node(15), Node(7)]

[Round 3: 扫描 Level 2]
  • 遍历 cur 中的 Node(15) 和 Node(7):
      vals = [15, 7]
      nxt  = [] (均为叶子节点)
  • 提交层级数据: ans.append(vals) -> ans = [[3], [9, 20], [15, 7]]
  • 状态滚动: cur = nxt -> cur = []

[Round 4: 终止判断]
  • while cur 判定为 False，循环结束。
  • 返回 ans = [[3], [9, 20], [15, 7]]。
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0102-binary-tree-level-order-traversal.py`](top-100/lc-0102-binary-tree-level-order-traversal.py) 中的双解法实现进行逐行深入解析：

### 解法一：双数组滚动状态转移法 (`Solution`)

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # 1. 空树防御性拦截 (Base Case Guard)
        # 若根节点为空，直接返回空列表 []，避免将 [None] 存入 cur 引起后续属性报错
        if root is None:
            return []

        # 2. 初始化结果集与当前层节点容器
        ans = []
        cur = [root]  # 初始数组 cur 只有 root

        # 3. 外层主循环：当 cur 数组非空时，说明仍有未处理的层级
        while cur:
            nxt = []   # 用于暂存下一层的全部有效子节点
            vals = []  # 用于收集当前层所有节点的数值

            # 4. 遍历当前层的每一个节点 (保证严格自左向右)
            for node in cur:
                # 记录当前节点值
                vals.append(node.val)

                # 将非空左、右孩子顺序加入下一层数组 nxt
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)

            # 5. 层级交接与状态推进
            cur = nxt        # 将 cur 替换为下一层节点数组 nxt
            ans.append(vals) # 将当前层收集完的数值数组加入最终结果 ans

        # 6. 返回层序遍历总结果
        return ans
```

---

### 解法二：双端队列与定长快照法 (`Solution2`)

```python
from collections import deque

# use queue
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. 空树防护
        if root is None:
            return []

        # 2. 初始化结果容器与双端队列
        ans = []
        q = deque([root])

        # 3. 队列非空时持续按层处理
        while q:
            vals = []
            # 核心: 固定当前层的节点数量 len(q)，循环 len(q) 次严格出队当前层节点
            for _ in range(len(q)):
                node = q.popleft()     # O(1) 弹出队首节点
                vals.append(node.val)  # 记录数值
                # 按左、右顺序将下一层节点推入队尾
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # 当前层所有节点出队并收集完毕后，打包追加进 ans
            ans.append(vals)

        return ans
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 双数组法与经典单队列 `collections.deque` 解法有何异同与优劣？

* **面试官**：你使用的双数组滚动法非常简洁。如果用经典的 `collections.deque` 单队列配合 `len(queue)` 快照，该如何实现？两种实现有什么性能权衡？
* **候选人解析**：
  * **单队列快照法**：每次外层循环先读取 `level_size = len(queue)`，然后内层严格循环 `level_size` 次，弹出队头并压入左右子节点。
  * **对比分析**：
    * **空间与执行效率**：双数组法使用原生 Python `list`，在现代 Python 解释器中具有极致的局部性（Locality of Reference）和更低的内存分配开销；`deque` 是双向链表块结构，单次 `popleft()` 虽为 $\mathcal{O}(1)$，但有额外指针维护成本。
    * **代码简洁性**：双数组法无需引入 `collections` 模块，也避免了对 `popleft()` 下标和边界的思考，逻辑更自然直观。

```python
# 附: 经典单队列快照法模板 (Single Deque BFS Template)
from collections import deque
from typing import List, Optional

class SolutionDequeBFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            vals = []
            
            for _ in range(level_size):
                node = queue.popleft()
                vals.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans.append(vals)
            
        return ans
```

---

### 追问 2: 能否使用深度优先搜索 (DFS) 递归解决层序遍历？

* **面试官**：层序遍历本质是广度优先。如果不允许使用显式队列或迭代循环，如何用 DFS 递归实现层序遍历？
* **候选人解析**：
  * **DFS 解法核心**：在递归函数中携带深度参数 `depth`。
  * **动态扩容不变量**：当 `depth == len(ans)` 时，说明首次触达新的一层，此时向 `ans` 追加一个空子列表 `ans.append([])`。
  * **归位收集**：将 `node.val` 追加到对应的层级容器 `ans[depth].append(node.val)` 中，随后按“先左后右”递归子树即可保持同层自左向右的顺序。

```python
# 附: DFS 深度索引递归法模板 (DFS Preorder Level Grouping)
class SolutionDFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            
            # 若首次访问到该深度，开辟新的层级子列表
            if depth == len(ans):
                ans.append([])
                
            ans[depth].append(node.val)
            
            # 严格先左后右，保证同层元素自左向右排列
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
| **空树未设防将 `[None]` 入数组** | 输入 `root = None`，循环内执行 `node.val` 抛出异常 | 初始定义 `cur = [root]` 时未检查 `root is None`，导致 `cur = [None]` | 在函数入口必须前置守卫：`if root is None: return []` |
| **层级边界丢失 (扁平化遍历)** | 输出为一维列表 `[3, 9, 20, 15, 7]` 而非二维列表 | 仅维护全局队列但未在每轮循环划分 `nxt` 数组或 `level_size` | 必须为每一层独立分配 `vals` 容器并在外层 `ans.append(vals)` |
| **在 `list` 上使用 `pop(0)`** | 节点较多时耗时急剧上升，运行超时 (TLE) | Python `list.pop(0)` 为 $\mathcal{O}(K)$ 内存平移操作，整层总耗时退化为 $\mathcal{O}(K^2)$ | 采用双数组直接覆盖赋值 `cur = nxt` 或改用 `collections.deque.popleft()` |
| **内层循环未清空 `nxt` 引用** | 导致后序层级无限重复包含前序节点，死循环 / 爆内存 | `nxt` 定义在 `while` 外部未在每轮重置 | `nxt = []` 与 `vals = []` 必须置于 `while cur:` 循环体首行 |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 拓扑特征 (Topology) | 每轮 `cur` $\rightarrow$ `vals` $\rightarrow$ `nxt` 推演 | 最终输出 (Output) |
| :--- | :--- | :--- | :---: |
| **空树 `root = []`** | 无任何节点 | 触发 `if root is None` 短路拦截 | `[]` |
| **单节点 `[1]`** | 仅含根节点 | Round 1: `cur=[1]` $\rightarrow$ `vals=[1], nxt=[]` $\rightarrow$ 结束 | `[[1]]` |
| **完全单斜链表 `[1,2,null,3]`** | 退化为深度为 3 的链表 | R1: `vals=[1]` $\rightarrow$ R2: `vals=[2]` $\rightarrow$ R3: `vals=[3]` | `[[1], [2], [3]]` |
| **标准二叉树 `[3,9,20,null,null,15,7]`** | 左右分支均有 | R1: `[3]` $\rightarrow$ R2: `[9, 20]` $\rightarrow$ R3: `[15, 7]` | `[[3], [9, 20], [15, 7]]` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | 其中 $N$ 为二叉树的节点总数。二叉树中的每一个节点 $u \in V$ 在整个 BFS 遍历过程中被且仅被加入 `cur` 数组一次，并遍历提取值一次。所有内层循环操作（子节点判空、列表 `append`）均为 $\mathcal{O}(1)$，因此整体时间复杂度严格为线性 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(N)$ | 空间开销由辅助数组 `cur` 和 `nxt` 决定。在最坏情况下（例如满二叉树 Full Binary Tree），最后一层的叶子节点数目为 $\lceil N/2 \rceil$，此时 `cur` 需要同时容纳 $\mathcal{O}(N)$ 个节点引用。因此最坏辅助空间复杂度为 $\mathcal{O}(N)$。*(注: 结果集 `ans` 占用 $\mathcal{O}(N)$ 存储空间)*。 |
