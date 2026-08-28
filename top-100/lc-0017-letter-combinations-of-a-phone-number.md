# LeetCode 17. Letter Combinations of a Phone Number (电话号码的字母组合)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (回溯算法 / 笛卡尔积组合搜索 / 递归树路径构建 / 回溯三问)
- **Tags:** Hash Table, String, Backtracking
- **Corresponding Python File:** [`top-100/lc-0017-letter-combinations-of-a-phone-number.py`](top-100/lc-0017-letter-combinations-of-a-phone-number.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.
* **[CN]** 给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

### Constraints / 约束条件
* $0 \le \text{digits.length} \le 4$
* `digits[i]` 是范围 `['2', '9']` 的一个数字。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 递归回溯的本质 (Dynamic Nesting Invariant):                              │
│    • 固定 2 个数字可以写 2 重 for 循环，但当数字长度 n 不确定时，普通循环     │
│      表达能力受限，必须使用递归实现动态深度为 n 的循环嵌套。                 │
│ 2. 经典「回溯三问」模型 (The Three Core Questions of Backtracking):         │
│    • ① 当前操作？ 枚举当前位置 path[i] 所要填入的映射字母。                 │
│    • ② 子问题？   构造由下标 >= i 的数字所生成的所有可能字母串。              │
│    • ③ 下一个子问题？ 构造由下标 >= i + 1 的数字所生成的所有可能字母串。      │
│ 3. 定长路径原位覆盖优化 (In-Place Array Overwrite Invariant):                │
│    • 预先分配定长列表 path = [""] * n，在第 i 层直接执行 path[i] = char，   │
│      递归返回时天然会被新值覆盖，无需额外的 append/pop 回溯显式清理。         │
│ 4. 空输入边界严防 (Empty String Guard):                                      │
│    • 当 digits = "" (n = 0) 时，必须特判直接返回 []，切忌输出 [""]。         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 回溯组合思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Backtracking Combinatorial Family Tree (回溯搜索算法思维谱系图)          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Cartesian Product / Fixed Depth): LC 17 Phone Number (本题★)      │
│  └─ 定长跨集合组合: 每个位置独立从映射表选 1 个字符，仅叶子节点是答案 (i == n) │
│        │                                                                    │
│        ├─► [演进 Twist 1: 同集合子集收集 (Every Node is Answer)]             │
│        │   LC 78 Subsets                                                    │
│        │   └─ 视角 A: 每个元素选或不选 (0/1 二叉树)                          │
│        │   └─ 视角 B: 枚举子集起始下标 j in range(i, n)，每个节点都是答案   │
│        │                                                                    │
│        ├─► [演进 Twist 2: 固定子集长度与剪枝 (Fixed Length Selection)]       │
│        │   LC 77 Combinations                                               │
│        │   └─ 剪枝优化: 剩余可用元素不足时提前 return                       │
│        │                                                                    │
│        ├─► [演进 Twist 3: 无限重复选取与目标和 (Unbounded Sum)]              │
│        │   LC 39 Combination Sum                                            │
│        │   └─ 转移允许递归自身下标 i: dfs(i, current_sum + nums[i])         │
│        │                                                                    │
│        └─► [演进 Twist 4: 全排列与已用标记 (Permutations / Used Mask)]       │
│            LC 46 Permutations                                               │
│            └─ 每次从头搜索整个集合，配合 used 数组或原位交换避免重复使用    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 形式化逻辑推演 (Combinatorial Product Formula)

设输入的数字字符串长度为 $n$，第 $i$ 个字符 `digits[i]` 对应的字母集合为 $\mathcal{S}_i = \text{MAPPING}[\text{digits}[i]]$。

最终结果集 $\mathcal{R}$ 严格等于各集合的笛卡尔积（Cartesian Product）：
$$\mathcal{R} = \mathcal{S}_0 \times \mathcal{S}_1 \times \dots \times \mathcal{S}_{n-1}$$

笛卡尔积的总方案数等于各集合大小之积：
$$|\mathcal{R}| = \prod_{i=0}^{n-1} |\mathcal{S}_i| \le 4^n$$

---

### 🎨 ASCII 搜索树推演图解 (`digits = "23"`)

映射关系：`'2' -> "abc"`, `'3' -> "def"`。

```
                         dfs(0) [Root: 构建 path[0]]
                       /            |            \
                   'a'             'b'             'c'
                  /                 |                 \
             dfs(1)              dfs(1)              dfs(1)
          /    |    \         /    |    \         /    |    \
        'd'   'e'   'f'     'd'   'e'   'f'     'd'   'e'   'f'
        /      |      \     /      |      \     /      |      \
     dfs(2)  dfs(2) dfs(2) dfs(2) dfs(2) dfs(2) dfs(2) dfs(2) dfs(2)
      "ad"    "ae"   "af"   "bd"   "be"   "bf"   "cd"   "ce"   "cf"
      (✓)     (✓)    (✓)    (✓)    (✓)    (✓)    (✓)    (✓)    (✓)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0017-letter-combinations-of-a-phone-number.py`](top-100/lc-0017-letter-combinations-of-a-phone-number.py) 中的实现进行逐行深入解析：

```python
from typing import List, Optional

# 1. 建立全局数字-字母映射表 (0 和 1 无映射，直接用空字符串占位)
MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)
        # 2. 空输入特判拦截：若输入为空，直接返回 [] (若不特判会输出包含空字符串的 [""])
        if n == 0:
            return []

        ans = []
        # 3. 预先开辟定长路径数组，长度固定为 n
        path = [""] * n

        # 4. 定义深度优先搜索函数，i 表示当前正在为 path[i] 选择填入的字母
        def dfs(i):
            # 递归基 (Base Case): 当 i == n 时，说明已经构造完了长度为 n 的完整字符串
            if i == n:
                ans.append("".join(path)) # 将路径数组拼成字符串存入结果集
                return

            # 枚举当前数字 digits[i] 所对应的所有候选字母
            for char in MAPPING[int(digits[i])]:
                path[i] = char  # 原位覆盖 path[i]
                dfs(i + 1)      # 递归深入解决下一个子问题

        # 5. 从下标 0 开始启动递归
        dfs(0)
        return ans
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 原位数组覆盖与字符串参数拼接有何差异？

* **面试官**：你使用了 `path = [""] * n` 并在递归中执行 `path[i] = char`。如果直接在递归函数参数中传递当前字符串（如 `dfs(i, current_str)`），两种写法有什么区别？
* **候选人解析**：
  * **原位覆盖列表法（当前解法）**：全过程仅复用这一个长度为 $n$ 的列表对象，只有触底时执行一次 `"".join(path)`，减少了深层递归过程中的中间临时字符串对象创建，极其高效且内存友好。
  * **参数字符串传递法**：每次调用 `dfs(i + 1, current_str + char)` 会在每次分支时生成新的不可变 `str` 对象，代码极简但增加了中途字符串分配开销。

```python
# 附: 字符串参数传递法模板 (String Parameter Concatenation)
class SolutionStringParam:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        
        def dfs(i: int, cur: str) -> None:
            if i == len(digits):
                ans.append(cur)
                return
            for char in MAPPING[int(digits[i])]:
                dfs(i + 1, cur + char)
                
        dfs(0, "")
        return ans
```

---

### 追问 2: 如何使用广度优先遍历 (BFS) 队列或迭代实现？

* **面试官**：如果不允许使用系统递归栈，如何用迭代或 BFS 队列生成所有字母组合？
* **候选人解析**：
  * 使用双端队列，初始将 `""` 入队。
  * 遍历每个数字 `digit`，读取当前队列长度，将队列中的每一个前缀弹出，分别拼接该数字对应的所有可能字符，重新压入队列。
  * 遍历完所有数字后，队列中的元素即为全量组合。

```python
# 附: BFS 队列迭代解法 (Queue BFS Template)
from collections import deque

class SolutionBFS:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        q = deque([""])
        
        for d in digits:
            chars = mapping[int(d)]
            for _ in range(len(q)):
                prefix = q.popleft()
                for ch in chars:
                    q.append(prefix + ch)
                    
        return list(q)
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **空字符串未拦截** | 输入 `digits = ""` 时输出 `[""]` 判错 | 没有前置判断 `len(digits) == 0`，`dfs(0)` 立即命中 `0 == 0` 并追加空串 | 函数首行必须守卫：`if not digits: return []` |
| **递归触底未写 `return`** | 抛出 `IndexError: string index out of range` | 命中 `i == n` 后继续往下执行 `digits[i]` | 命中 Base Case 并 `ans.append` 后必须立即显式 `return` |
| **映射表下标偏移** | 数字 `2` 错误对应到 `"def"` | 映射表未将索引 `0` 和 `1` 填充占位符，导致 `digits[i]` 下标错位 | 使用 `["", "", "abc", ...]` 确保下标与按键数字严格 $1:1$ 对应 |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 特征与边界 | 递归深度与分支数 | 最终输出 (Output) |
| :--- | :--- | :--- | :---: |
| **空字符串 `""`** | 长度 $n=0$ | 直接短路返回 | `[]` |
| **单数字 `"2"`** | 长度 $n=1$ | 1 层递归，3 个分支 | `["a", "b", "c"]` |
| **双数字 `"23"`** | 长度 $n=2$ | 2 层递归，3 × 3 = 9 种组合 | `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]` |
| **含 4 字符按键 `"79"`** | `'7'->4, '9'->4` | 2 层递归，4 × 4 = 16 种组合 | 16 种合法组合 |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(4^n \cdot n)$ | 其中 $n$ 为输入字符串 `digits` 的长度。每个数字最多对应 4 个字母（数字 7 和 9），因此递归树的叶子节点最多为 $4^n$ 个。对于每个叶子节点，执行 `"".join(path)` 需要耗费 $\mathcal{O}(n)$ 时间构建字符串，总时间复杂度严格为 $\mathcal{O}(4^n \cdot n)$。在题目约束 $n \le 4$ 下，最大计算量仅为 $4^4 \times 4 = 1024$ 次操作，耗时 $< 1\text{ms}$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(n)$ | 不计最终保存结果集的输出空间：<br>1. 系统递归调用栈的深度最大为 $n$；<br>2. 辅助路径数组 `path` 的长度固定为 $n$。<br>因此额外辅助空间复杂度严格为线性 $\mathcal{O}(n)$。 |
