# LeetCode 2029. Stone Game IX (石子游戏 IX)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (博弈论 / 模 3 同余分类讨论 / 奇偶性分析 / 贪心决策)
- **Tags:** Array, Math, Greedy, Game Theory
- **Corresponding Python File:** [`daily-practice/lc-2029-stone-game-ix.py`](daily-practice/lc-2029-stone-game-ix.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Alice and Bob play a game with stones. There is a collection of stones with positive integer values. Alice and Bob take turns, with Alice starting first. On each turn, the player makes a move consisting of removing a stone from the pile. A player loses if the sum of the values of all removed stones is divisible by 3. If all stones are removed without the sum becoming divisible by 3, Bob wins. Return `true` if Alice wins, or `false` if Bob wins.
* **[CN]** Alice 和 Bob 再次设计了一款新的石子游戏。现有一包石子，每个石子上都有一个正整数。游戏由 Alice 和 Bob 轮流进行，Alice 先手。在每个回合中，玩家可以从石子堆中选出一个石子并移除。如果移除后所有已被移除石子的总和能被 3 整除，则该玩家输掉游戏。如果所有石子都被移除且总和仍不能被 3 整除，则 Bob 获胜。如果 Alice 赢，返回 `true` ；否则返回 `false` 。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 模 3 同余分类 (Modulo 3 Invariant):                                       │
│    • 每个石子仅取决于 val % 3 的余数：cnt0, cnt1, cnt2。                     │
│ 2. 模 0 石子的充要性质 (Parity Buffer):                                      │
│    • 选 cnt0 不改变当前累加和的模 3 状态，仅用于翻转出牌先后手。             │
│ 3. 极简胜负判定公式 (Decision Invariant):                                    │
│    • 若 cnt0 为偶数: Alice 必胜当且仅当 cnt1 >= 1 且 cnt2 >= 1。             │
│    • 若 cnt0 为奇数: Alice 必胜当且仅当 abs(cnt1 - cnt2) > 2。               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-2029-stone-game-ix.py`](daily-practice/lc-2029-stone-game-ix.py) 中的实现进行逐行深入解析：

```python
class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        # 1. 统计模 3 余数为 0, 1, 2 的石子个数
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            rem = val % 3
            if rem == 0:
                cnt0 += 1
            elif rem == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        # 2. 情况一：cnt0 为偶数（相当于没有 0 类型的石子）
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
            
        # 3. 情况二：cnt0 为奇数（Alice 可以利用 0 的反转破坏 Bob 的策略）
        return abs(cnt1 - cnt2) > 2
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 单次遍历数组统计模 3 频数，后续判定 $\mathcal{O}(1)$，总时间严格为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用 3 个计数器变量。 |
