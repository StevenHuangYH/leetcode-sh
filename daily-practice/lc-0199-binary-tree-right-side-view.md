# LeetCode 199. Binary Tree Right Side View (二叉树的右视图)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (树形遍历 / DFS 根右左逆序优先 / 层级与结果集长度对齐 / BFS 层序末尾抽取)
- **Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
- **Corresponding Python File:** [`daily-practice/lc-0199-binary-tree-right-side-view.py`](daily-practice/lc-0199-binary-tree-right-side-view.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.
* **[CN]** 给定一个二叉树的 根节点 `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

### Constraints / 约束条件
* 二叉树中的节点数目在范围 $[0, 100]$ 内。
* $-100 \le \text{Node.val} \le 100$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 视图的数学本质 (Mathematical Invariant of Right-View):                  │
│    • 右视图中每一层 (Level / Depth) 恰好且必须选出且仅选出 1 个节点。        │
│    • 该节点是当前层从左向右看【最靠右】的非空物理节点。                     │
│ 2. DFS 根-右-左优先遍历 (Root-Right-Left DFS Order):                         │
│    • 优先递归右子树，再递归左子树。                                         │
│    • 核心性质: 每一层中第一个被访问到的节点，必定是该层最靠右的节点。        │
│ 3. 动态长度对齐不变量 (Depth-Length Invariant):                             │
│    • 当前层号 depth == len(ans) 成立时，说明这是本层首访节点，执行 append。  │
│    • 后续访问同层左侧节点时，因 depth < len(ans)，自动忽略，天然实现去重。    │
│ 4. 双重范式对比 (DFS vs BFS):                                                │
│    • DFS 递归栈简洁优雅，空间消耗为 O(H)；BFS 层序队列取每层末尾，直观稳定。 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 二叉树层级视图思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Binary Tree View & Level Traversal Lineage (二叉树层级视图思维谱系图)    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Full Level Collection): LC 102 Binary Tree Level Order Traversal  │
│  └─ 全量层序收集: 队列 BFS 收集每一层的全部节点值 [[1], [2, 3], [4, 5]]     │
│        │                                                                    │
│        ▼ [演进 Twist: 每层仅过滤保留最右侧端点元素 (Rightmost Filter)]       │
│  Level 2 (Single Element per Level): LC 199 Right Side View (本题★)        │
│  ├─ DFS 范式: 根-右-左遍历，利用 depth == len(ans) 捕获首访节点              │
│  └─ BFS 范式: 层序遍历队列，每次提取当前层数组的最后一个元素 level[-1]       │
│        │                                                                    │
│        ▼ [演进 Twist: 扩展为左边界 + 全部叶子 + 逆序右边界复合扫描]         │
│  Level 3 (Composite Boundary): LC 545 Boundary of Binary Tree               │
│  └─ 边界缝合: Left Boundary + Leaves + Reversed Right Boundary              │
│        │                                                                    │
│        ▼ [演进 Twist: 引入 2D 平面坐标哈希与纵向垂线投影 (Vertical Proj)]   │
│  Level 4 (2D Spatial Coordinates): LC 987 Vertical Order Traversal          │
│  └─ 空间投影: (row, col) 坐标系哈希桶 + 自定义多关键字排序                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 形式化逻辑推演 (Depth-Length Alignment Invariant)

设树的深度为 $H$，结果集为列表 $	ext{ans}$：
1. 初始状态：$	ext{ans} = []$，长度为 $0$。
2. 当遍历到深度为 $d$ ($d \ge 0$) 的节点时：
   * 若此前尚未收录深度为 $d$ 的任何节点，此时 $	ext{len}(	ext{ans}) = d$。
   * 因为递归遍历顺序为**先右后左**（`node.right` 优先于 `node.left`），所以深度 $d$ 处第一个触发 $d == 	ext{len}(	ext{ans})$ 的节点**必然是该层最靠右的节点**。
   * 将该节点值追加至 $	ext{ans}$ 后，$	ext{len}(	ext{ans})$ 增加为 $d + 1$。
   * 随后无论同一深度 $d$ 还有多少个位于左侧的兄弟或堂兄弟节点被访问，其深度 $d < 	ext{len}(	ext{ans})$ 恒成立，因而不会被错误覆盖或重复追加。

---

### 🎨 ASCII 遍历时序与结果集状态迁移图解

以树 `root = [1, 2, 3, null, 5, null, 4]` 为例：

```
                 (1)               <--- depth 0: 看到节点 1
               /     \
             (2)     (3)           <--- depth 1: 看到节点 3
               \       \
               (5)     (4)         <--- depth 2: 看到节点 4

═════════════════════════════════════════════════════════════════════
DFS 根-右-左时序追踪 (Depth-First Search Execution Flow):

Step 1: 访问节点 (1), depth = 0
  • depth(0) == len(ans)(0) -> ans.append(1) -> ans = [1]
  • 触发右递归 -> 访问节点 (3)

Step 2: 访问节点 (3), depth = 1
  • depth(1) == len(ans)(1) -> ans.append(3) -> ans = [1, 3]
  • 节点 (3) 无左子树，触发右递归 -> 访问节点 (4)

Step 3: 访问节点 (4), depth = 2
  • depth(2) == len(ans)(2) -> ans.append(4) -> ans = [1, 3, 4]
  • 节点 (4) 为叶子节点，返回回溯

Step 4: 回溯至根节点 (1)，触发左递归 -> 访问节点 (2), depth = 1
  • depth(1) == len(ans)(3) 不成立 (1 < 3) -> 跳过 (右侧 3 已遮挡 2)
  • 触发节点 (2) 的右递归 -> 访问节点 (5), depth = 2

Step 5: 访问节点 (5), depth = 2
  • depth(2) == len(ans)(3) 不成立 (2 < 3) -> 跳过 (右侧 4 已遮挡 5)

最终结果: [1, 3, 4]
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-0199-binary-tree-right-side-view.py`](daily-practice/lc-0199-binary-tree-right-side-view.py) 中的实现进行逐行深入解析：

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 1. 初始化结果集容器
        ans = []

        # 2. 定义前序变形递归函数 (Root -> Right -> Left)
        def f(node: Optional[TreeNode], depth: int) -> None:
            # 递归基 (Base Case): 遇到空节点直接返回
            if node is None:
                return
            
            # 核心不变量: 若当前层号首次达到结果集长度，说明此节点为该层最先被访问的“最右节点”
            if depth == len(ans):
                ans.append(node.val)
            
            # 3. 严格优先遍历右子树 (确保右侧节点先被登记)
            f(node.right, depth + 1)
            # 4. 后续遍历左子树 (同层左侧节点仅在右侧缺失时才会满足 depth == len(ans))
            f(node.left, depth + 1)

        # 5. 从根节点启动，根节点深度定义为 0
        f(root, 0)
        return ans
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 如何使用广度优先遍历 (BFS) 队列实现？与 DFS 相比有何优劣？

* **面试官**：DFS 解法非常精妙。但工程实践中很多人第一反应是 BFS 层序遍历。能否写出 BFS 解法并对比时空开销？
* **候选人解析**：
  * **BFS 思路**：使用双端队列 `collections.deque`。按层扫描，对于每一层循环 `for _ in range(len(queue))`，每层的最后一个节点（或在入队时最右弹出的节点）即为右视图元素。
  * **优劣对比**：
    * **DFS 空间优势**：空间复杂度为树高 $\mathcal{O}(H)$。在平衡树下仅需 $\mathcal{O}(\log N)$ 栈空间。
    * **BFS 直观优势**：不依赖递归调用栈，避免大树深度时的栈溢出风险，但最差情况下队列需要存储二叉树最底层的全部叶子节点，空间复杂度为最大宽度 $\mathcal{O}(W) = \mathcal{O}(N)$。

```python
# 附: BFS 层序遍历队列解法 (Queue BFS Template)
from collections import deque
from typing import List, Optional

class SolutionBFS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                # 记录当前层的最后一个节点
                if i == level_len - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return ans
```

---

### 追问 2: 如果面试官要求返回“左视图” (Left Side View)，代码如何最小化修改？

* **面试官**：如果改为要求二叉树的左视图 (Left Side View)，DFS 与 BFS 代码应如何调整？
* **候选人解析**：
  * **DFS 方案**：仅需调换递归顺序，改为**先左后右**：
    ```python
    f(node.left, depth + 1)   # 先左
    f(node.right, depth + 1)  # 后右
    ```
    这样每层最先被访问的必定是左侧节点，其余保持 `depth == len(ans)` 不变。
  * **BFS 方案**：在层序遍历中，每次取当前层的第一个元素 `if i == 0: ans.append(node.val)` 即可。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **子树遍历顺序颠倒 (先左后右)** | 左子树较深时，较深层的左侧节点被正确捕获，但较浅层捕获成了左侧节点 | 写成了常规前序遍历 (`node.left` 优先)，导致左节点先触发 `depth == len(ans)` | 右视图必须严格保证 `f(node.right, ...)` 在 `f(node.left, ...)` 之前调用 |
| **误以为右视图仅由一路 `root.right` 构成** | 当左子树比右子树更深时（如左子树有 4 层，右子树只有 2 层），底层节点缺失 | 右视图并非单指右子树边缘，而是整个二叉树每一层“最右”可见节点 | 必须全树遍历，右树缺位时左树对应深度的节点必然露出来 |
| **空树未做保护** | 输入 `root = []` 时抛出异常或死循环 | 递归基未正确判断 `if node is None: return` | 保证递归入口对 `None` 安全返回，直接返回 `[]` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 结构特征 (Topology) | 递归访问时序 (DFS Order) | 结果集变化过程 (Trace) | 输出 (Output) |
| :--- | :--- | :--- | :--- | :---: |
| **空树 `root = []`** | 无任何节点 | `f(None, 0)` 直接 return | `ans = []` | `[]` |
| **单节点 `[1]`** | 仅根节点 | 访问 `(1, depth=0)` | `[1]` | `[1]` |
| **左斜树较深 `[1,2,null,3]`** | 右子树为空，左子树伸展 | 访问 `1 (d=0)` $ightarrow$ 访问 `2 (d=1)` $ightarrow$ 访问 `3 (d=2)` | `[]` $ightarrow$ `[1]` $ightarrow$ `[1,2]` $ightarrow$ `[1,2,3]` | `[1, 2, 3]` |
| **标准用例 `[1,2,3,null,5,null,4]`** | 左右子树均有分支 | `1(d=0)` $ightarrow$ `3(d=1)` $ightarrow$ `4(d=2)` $ightarrow$ `2(d=1,跳过)` $ightarrow$ `5(d=2,跳过)` | `[1]` $ightarrow$ `[1,3]` $ightarrow$ `[1,3,4]` | `[1, 3, 4]` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | 其中 $N$ 为二叉树的节点总数。算法执行严格的 DFS 遍历，每个节点仅被访问且处理恰好一次，单次递归耗时 $\mathcal{O}(1)$，总体时间为 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(H)$ | 其中 $H$ 为二叉树的高度。空间开销由系统递归调用栈决定：<br>• **最好/平均情况 (平衡二叉树)**: 栈深度 $H = \mathcal{O}(\log N)$；<br>• **最坏情况 (完全退化为单链表)**: 栈深度 $H = \mathcal{O}(N)$。<br>*(注: 返回值结果集占用 $\mathcal{O}(H)$ 输出空间)*。 |
