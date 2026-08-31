# LeetCode 78. Subsets (子集)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (回溯算法 / 0-1 选或不选二叉决策树 / 枚举元素多叉搜索树 / 幂集构造)
- **Tags:** Array, Backtracking, Bit Manipulation
- **Corresponding Python File:** [`top-100/lc-0078-subsets.py`](top-100/lc-0078-subsets.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an integer array `nums` of **unique** elements, return *all possible subsets (the power set)*. The solution set **must not** contain duplicate subsets. Return the solution in **any order**.
* **[CN]** 给你一个整数数组 `nums` ，数组中的元素 **互不相同** 。返回该数组所有可能的子集（幂集）。解集 **不能** 包含重复的子集。你可以按 **任意顺序** 返回解集。

### Constraints / 约束条件
* $1 \le \text{nums.length} \le 10$
* $-10 \le \text{nums}[i] \le 10$
* `nums` 中的所有元素 **互不相同**。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 子集生成两大经典视角 (Two Classic Paradigms for Subsets):                │
│    • 视角一：【站在输入的视角】(0/1 选或不选二叉树)                          │
│      - 对每个 nums[i]，只有 2 种抉择：不选入 path 或 选入 path。              │
│      - 仅在递归达到边界 i == n (叶子节点) 时将 path.copy() 记录入 ans。       │
│    • 视角二：【站在答案的视角】(枚举子集元素多叉树)                          │
│      - 递归遍历中的「每个节点本身就是一个合法子集」，进入 dfs 时立即记录答案。 │
│      - 循环枚举下一个可选下标 j in range(i, n)，递归下一层传递 dfs(j + 1)。   │
│ 2. 浅拷贝与状态隔离不变量 (Object Reference & Backtracking Invariant):      │
│    • Python 中的列表是引用类型，将路径加入结果集时必须执行 path.copy() 或     │
│      path[:]，否则后续的回溯 pop 操作会修改已存入答案中的列表内容。           │
│ 3. 幂集组合爆炸规模 (Power Set Size):                                       │
│    • 大小为 n 的集合子集总数为 2^n。每个子集平均复制耗时 O(n)。              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

### 🧠 子集与组合回溯思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Power Set & Combinations Pattern Lineage (子集与组合回溯思维谱系图)      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Direct Power Set / Unique Elements): LC 78 Subsets (本题★)        │
│  ├─ 范式 A (选/不选二叉树): dfs(i + 1) + [append -> dfs(i + 1) -> pop]     │
│  ├─ 范式 B (多叉树前序收集): ans.append(path.copy()) + for j in range(i, n) │
│  └─ 范式 C (位运算二进制枚举): 0 <= mask < (1 << n)                         │
│        │                                                                    │
│        ├─► [演进 Twist 1: 包含重复元素 + 树层去重 (Duplicate Candidates)]    │
│        │   LC 90 Subsets II                                                 │
│        │   └─ 策略: 先排序，若 j > i 且 nums[j] == nums[j - 1] 则 continue   │
│        │                                                                    │
│        ├─► [演进 Twist 2: 固定子集长度为 k (Fixed Size Subset)]             │
│        │   LC 77 Combinations                                               │
│        │   └─ 策略: 仅收集 len(path) == k 的节点，配合剩余元素数量剪枝      │
│        │                                                                    │
│        └─► [演进 Twist 3: 元素可重复选取的求和组合 (Unbounded Sum)]          │
│            LC 39 Combination Sum                                            │
│            └─ 策略: 下一层递归传入自身 j (允许复用): dfs(j, target - nums[j])│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎨 两种回溯视角的决策树对比图解 (`nums = [1, 2, 3]`)

#### 视角一：输入的视角（0-1 选或不选二叉决策树）
每个位置 `nums[i]` 都有“不选”与“选”两条分支，共有 $2^n$ 个叶子节点：

```
                           dfs(0) [处理 nums[0]=1]
                         /                         \
                   [不选 1]                       [选 1]
                    /                                \
                dfs(1)                             dfs(1)
              /        \                         /        \
          [不选 2]     [选 2]                 [不选 2]     [选 2]
           /              \                    /              \
        dfs(2)          dfs(2)              dfs(2)          dfs(2)
        /    \          /    \              /    \          /    \
      不选3   选3     不选3   选3          不选3   选3     不选3   选3
       []    [3]      [2]   [2,3]          [1]   [1,3]    [1,2]  [1,2,3]
```

#### 视角二：答案的视角（枚举下一个数是谁的多叉决策树）
每个节点本身都是答案，进入函数时立即记录 `ans.append(path.copy())`：

```
                                  path = [] (✓)
                      /                  |                  \
                 选 nums[0]=1       选 nums[1]=2       选 nums[2]=3
                     /                   |                    \
               path=[1] (✓)          path=[2] (✓)          path=[3] (✓)
              /            \             |
         选 nums[1]=2  选 nums[2]=3 选 nums[2]=3
            /                \           |
      path=[1,2] (✓)   path=[1,3] (✓) path=[2,3] (✓)
          /
     选 nums[2]=3
        /
   path=[1,2,3] (✓)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0078-subsets.py`](top-100/lc-0078-subsets.py) 中的双实现进行逐行深入解析：

### 解法一：站在输入的视角（0/1 选与不选二叉决策）

```python
from typing import List, Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            # 递归基 (Base Case): 已经做完了对所有 n 个元素的选/不选抉择
            if i == n:
                ans.append(path.copy()) # 必须浅拷贝当前 path 列表
                return 

            # 分支 1: 不选当前元素 nums[i]，直接进入下一个元素的决策
            dfs(i + 1)

            # 分支 2: 选当前元素 nums[i]，将其推入路径
            path.append(nums[i])
            dfs(i + 1) # 进入下一个元素的决策
            path.pop() # 回溯：恢复现场，弹出 nums[i]

        # 从第 0 个元素开始递归决策
        dfs(0)
        return ans
```

---

### 解法二：站在答案的视角（枚举子集元素多叉搜索）

```python
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            # 核心机制: 每一个中间状态 path 本身就是一个合法的子集，进入即收集
            ans.append(path.copy())

            # 从当前下标 i 开始向后枚举可以加入 path 的下一个数字 nums[j]
            for j in range(i, n):
                path.append(nums[j]) # 选择 nums[j]
                dfs(j + 1)           # 递归子问题：下一个数只能从下标 >= j + 1 中挑选
                path.pop()           # 回溯：撤销选择

        dfs(0)
        return ans
```

> [!TIP]
> **关于 `Solution2` 的关键实现要点**：
> 1. **全节点收集**：由于每个前缀都是合法子集，`ans.append(path.copy())` 位于 `dfs(i)` 入口首行，无需等 `i == n` 才收集。
> 2. **递增下标推进**：递归子问题应为 `dfs(j + 1)`，确保选完 `nums[j]` 后下一个选的数字必须在 `j` 之后，严格避免生成如 `[1, 2]` 和 `[2, 1]` 的重复排列。

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 如何使用二进制位掩码 (Bit Manipulation) 枚举子集？

* **面试官**：回溯法非常标准。如果要求不使用任何递归或栈，如何用位运算在 $\mathcal{O}(1)$ 额外辅助空间内生成所有子集？
* **候选人解析**：
  * 大小为 $n$ 的集合共有 $2^n$ 个子集。
  * 我们可以用整数 `mask`（范围 $0 \le \text{mask} < 2^n$）代表一种子集状态。
  * 若 `mask` 的第 $k$ 位为 `1`（即 `(mask >> k) & 1 == 1`），表示当前子集包含 `nums[k]`。

```python
# 附: 二进制位运算枚举模板 (Bit Manipulation Template)
class SolutionBitMask:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        # 遍历 0 到 2^n - 1 的每一个状态
        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if (mask >> i) & 1:
                    subset.append(nums[i])
            ans.append(subset)
            
        return ans
```

---

### 追问 2: 如何使用级联迭代法 (Cascading / DP) 构建？

* **面试官**：能否使用类似动态规划的逐步级联方式生成子集？
* **候选人解析**：
  * 初始解集中只包含空集 `ans = [[]]`。
  * 遍历 `nums` 中的每个数字 `num`：对于当前 `ans` 中的每一个已有子集 `curr`，克隆并追加 `num` 形成新子集 `curr + [num]`，再合并回 `ans`。

```python
# 附: 级联迭代法模板 (Cascading Iteration Template)
class SolutionCascading:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [curr + [num] for curr in ans]
        return ans
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **忘记列表浅拷贝** | 最终输出 `[[], [], ..., []]` 全为空列表 | 直接写 `ans.append(path)` 导致存入的是同一个列表引用，回溯 `pop` 清空了所有内容 | 必须存入快照：`ans.append(path.copy())` 或 `ans.append(list(path))` |
| **枚举视角中误传 `dfs(i + 1)`** | 生成了含有重复元素的异常子集 | 多叉树循环变量为 `j`，若误写为 `dfs(i + 1)`，导致内部循环不断从 `i + 1` 重新取数 | 递归推进必须传入 `dfs(j + 1)` |
| **枚举视角中仅在 `i == n` 时收集** | 遗漏了大量非满长度子集，输出只有最长叶子 | 混淆了二叉树（叶子是答案）与多叉树（每个节点都是答案）的收集时机 | 在多叉树 `dfs` 入口首行无条件执行 `ans.append(path.copy())` |
| **回溯遗漏 `path.pop()`** | 路径数据持续累加污染后续分支 | 递归调用后未恢复现场 | 选入元素递归后，必须配对调用 `path.pop()` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 集合大小 $n$ | 幂集总方案数 $2^n$ | 最终输出 (Output) |
| :--- | :--- | :---: | :--- |
| **单元素 `nums = [0]`** | $n = 1$ | $2^1 = 2$ | `[[], [0]]` |
| **双元素 `nums = [1, 2]`** | $n = 2$ | $2^2 = 4$ | `[[], [2], [1], [1, 2]]` |
| **标准三元素 `nums = [1, 2, 3]`** | $n = 3$ | $2^3 = 8$ | `[[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]]` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(2^n \cdot n)$ | 其中 $n$ 为输入数组 `nums` 的长度。大小为 $n$ 的集合共有 $2^n$ 个子集，每个子集在加入结果集时执行 `path.copy()` 需要 $\mathcal{O}(n)$ 的时间复制元素。因此总时间复杂度严格为 $\mathcal{O}(2^n \cdot n)$。在题目约束 $n \le 10$ 时，总操作数 $\le 1024 \times 10 \approx 10^4$，耗时 $< 1\text{ms}$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(n)$ | 不计用于保存最终 $2^n$ 个子集的输出列表：<br>1. 系统递归栈深度最大为 $n$；<br>2. 辅助路径列表 `path` 在任意时刻最多容纳 $n$ 个元素。<br>因此额外辅助空间复杂度严格为 $\mathcal{O}(n)$。 |
