# LC 0079: Word Search | 单词搜索

- **LeetCode ID**: LC 0079
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 09: 2D Grid DFS)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/word-search/)
- **Solution File**: [`37-lc-0079-word-search.py`](problems/luffy/37-lc-0079-word-search.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

### [CN] 中文描述
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

### Constraints / 约束条件
m == board.length, n = board[i].length, 1 <= m, n <= 6, 1 <= word.length <= 15

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

```
┌────────────────────────────────────────────────────────┐
│ 网格 DFS + 原地回溯标记                                │
│ 匹配当前字符: temp = board[r][c]; board[r][c] = '#'    │
│ 向四方向探索: dfs(r+dr, c+dc, k+1)                     │
│ 回溯恢复现场: board[r][c] = temp                       │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
路径不重复性：同一路径在单词匹配过程中不能重复经过同一个网格单元。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-79
#Word Search

from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        columns=len(board[0])


        def dfs(row, column, i):
            #base case

            #if word exists in the grid, return true
            if i == len(word):
                return True

            #index out of bounds
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return False

            #current cell is already used, false
            if board[row][column] == "#":
                return False

            #current cell is not matched, false
            if board[row][column] != word[i]:
                return False

                       
            #mark the current cell is already used
            temp=board[row][column]
            board[row][column]= "#"

            found =(
            dfs(row-1, column, i+1) or #up 
            dfs(row+1, column, i+1) or #down
            dfs(row, column-1, i+1) or #left
            dfs(row, column+1, i+1)    #right
            )

            #backtracking, rest the current cell for other path to use
            board[row][column]=temp

            return found

        #iterate through every cell on the grid to treat it as a potential starting point
        for row in range(rows):
            for column in range(columns):
                #if dfs() starting at this cell successfully fins the word, retrun True
                if board[row][column] == word[0] and dfs(row, column, 0):
                    return True

        return False


    
# # 统计字符串里每个字母的次数
# # Count the frequency of each character in a string
# c1 = Counter("apple")
# print(c1)
# # 输出 (Output): Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})


# # 统计列表里每个元素的次数
# # Count the frequency of each element in a list
# c2 = Counter(['张三', '李四', '张三', '王五'])
# print(c2)
# # 输出 (Output): Counter({'张三': 2, '李四': 1, '王五': 1})


# c = Counter("apple")
# print(c['p'])  # 输出 (Output): 2
# print(c['z'])  # 输出 (Output): 0  (不会报错！这在算法里省去了大量的 if 判断)
#                # (It won't throw an error! This saves a lot of 'if' checks in algorithms)


# c = Counter("apple")           # 现在 p 有 2 个 (Right now 'p' has a count of 2)
# c.update("pineapple")          # 又来了 3 个 p (3 more 'p's just arrived)
# print(c['p'])                  # 输出 (Output): 5


# c1 = Counter("aab")
# c2 = Counter("a")
# # 减法：把 c1 里减去 c2 的字母数量
# # Subtraction: Subtract the character counts of c2 from c1
# print(c1 - c2)
# # 输出 (Output): Counter({'a': 1, 'b': 1})


# c = Counter("abracadabra")
# # 找出出现次数最多的前 2 个元素
# # Find the top 2 most frequently occurring elements
# print(c.most_common(2))
# # 输出 (Output): [('a', 5), ('r', 2)]     (返回的是一个排好序的元组列表)
#                                           # (It returns a sorted list of tuples)

class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        columns=len(board[0])

        #counting the numbers of every letter from the grid
        board_counts=Counter()
        for row in board:
            board_counts.update(row)

        #Count the "demand" of letters required by the word
        word_counts= Counter(word)

        #check if the board's inventory for this specific letter is lees than what the word requires.
        for char, count in word_counts.items():
            if board_counts[char]<count:
                #if yes, return false
                return False

        #if the first letter of the word is abundant in the gird
        #but the last letter is scarce, we reverse the word to seach backwards,
        #this forces the DFS to start from the rare letter, 
        # which can reduces the number of false paths we explore.
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]


        def dfs(row, column, i):
            #base case

            #if word exists in the grid, return true
            if i == len(word):
                return True

            #index out of bounds
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return False

            #current cell is already used, false
            if board[row][column] == "#":
                return False

            #current cell is not matched, false
            if board[row][column] != word[i]:
                return False

                       
            #mark the current cell is already used
            temp=board[row][column]
            board[row][column]= "#"

            found =(
            dfs(row-1, column, i+1) or #up 
            dfs(row+1, column, i+1) or #down
            dfs(row, column-1, i+1) or #left
            dfs(row, column+1, i+1)    #right
            )

            #backtracking, rest the current cell for other path to use
            board[row][column]=temp

            return found

        #iterate through every cell on the grid to treat it as a potential starting point
        for row in range(rows):
            for column in range(columns):
                #if dfs() starting at this cell successfully fins the word, retrun True
                if board[row][column] == word[0] and dfs(row, column, 0):
                    return True

        return False
```

1. 基于 `37-lc-0079-word-search.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何进行词频剪枝优化？”*
  - **Candidate**: 统计网格和目标单词的字符频次，若网格字符不足直接返回 `False`；若单词末尾字符频次少于开头，反转单词可减少初期分叉搜索。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 忘记回溯恢复网格字符 | 网格永远变为 '#' | 状态污染 | 必须在递归返回前 board[r][c] = temp |

### Complete Dry-Run Table / 实例推演表

board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word='ABCCED' -> True

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(M \cdot N \cdot 3^L)$ | 网格每个起点出发 3 方向搜索深度 $L$。 |
| **Space Complexity** | $O(L)$ | 单词长度递归栈。 |
