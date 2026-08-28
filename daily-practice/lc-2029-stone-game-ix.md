# LC 2029: Stone Game IX | 石子游戏 IX

- **LeetCode ID**: LC 2029
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/stone-game-ix/)
- **Solution File**: [lc-2029-stone-game-ix.py](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-2029-stone-game-ix.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Alice and Bob continue their games with stones. There is a row of `n` stones, and each stone has an associated value represented by an array `stones`.
Alice and Bob take turns, with Alice starting first. On each turn, the player removes any stone from the row, and adds its value to their running total sum. If the running sum becomes divisible by 3 after a move (excluding the empty sum before the first move), the player loses immediately.
If all stones are removed without the sum becoming divisible by 3, Bob wins.
Assuming both players play optimally, return `true` if Alice wins, or `false` if Bob wins.

### [CN] 中文描述
Alice 和 Bob 再次设计了一款新的石子游戏。现有一行 `n` 个石子，每个石子都有一个表示其价值的整数，这些整数放在数组 `stones` 中。
Alice 和 Bob 轮流进行自己的回合，Alice 先手。每一回合，玩家需要从 `stones` 中移除任一石子，并将石子的价值加到他们的累积和中。如果移除石子后，累积总和可以被 3 整除（第一次回合前的空总和除外），则当前玩家输掉游戏。
如果所有石子都被移除，且总和未被 3 整除，则 Bob 获胜。
假设双方都采取 最优策略 ，如果 Alice 获胜，返回 `true` ；如果 Bob 获胜，返回 `false` 。

### Constraints / 约束条件
- `1 <= stones.length <= 10^5`
- `1 <= stones[i] <= 10^4`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ 博弈搜索 / Minimax 对抗搜索                             │
│ 状态空间 $O(3^n)$ 巨大，直接搜索必超时                 │
└───────────────────────────┬────────────────────────────┘
                            │ 模 3 同余分类与奇偶性转化
                            ▼
┌────────────────────────────────────────────────────────┐
│ 模 3 余数博弈模型 (Remainder Modulo 3 Game)            │
│ 关键性质: 只有余数 0, 1, 2 影响当前和同余状态          │
│ • 余数 0 的石子是换手牌（改变先后手奇偶性）            │
│ • 序列只能以 1-1-2-1-2... 或 2-2-1-2-1... 形式交替延伸 │
└───────────────────────────┬────────────────────────────┘
                            │ 导出分类讨论充要条件
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 2029 极简 O(n) 同余博弈决策 (本题)                  │
│ • 若 cnt0 为偶数: Alice 选较多者必胜 (cnt1>=1 且 cnt2>=1)
│ • 若 cnt0 为奇数: Alice 需差值绝对值 > 2 才能获胜      │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

每个石子的具体数值不重要，只有 `val % 3` 决定局势：
- `cnt0`: 模 3 余 0 的石子。取它不改变当前模 3 的总和，相当于**把轮次转移给对方**（消耗回合）。
- `cnt1`: 模 3 余 1 的石子。
- `cnt2`: 模 3 余 2 的石子。

游戏开局规则：
Alice 先手不能选 0（否则总和为 0 模 3 为 0 直接输）。Alice 只能选 1 或 2：
1. **若 `cnt0` 为偶数**：0 的总数是偶数，0 对双方是均等的。只要 `cnt1 >= 1` 且 `cnt2 >= 1`，Alice 选择较小数量的一方开局，后续通过交替选择就能迫使 Bob 面对死局，Alice 必胜。
2. **若 `cnt0` 为奇数**：0 的存在破坏了回合对称性，相当于 Bob 拥有多一次换手机会。Alice 要想获胜，`cnt1` 和 `cnt2` 数量差必须大于 2（即 `abs(cnt1 - cnt2) > 2`）。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            rem = val % 3
            if rem == 0:
                cnt0 += 1
            elif rem == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        else:
            return abs(cnt1 - cnt2) > 2
```

1. **统计模 3 频数**：
   - 线性扫描统计 `cnt0, cnt1, cnt2`。
2. **偶数 `cnt0` 分支**：
   - `if cnt0 % 2 == 0: return cnt1 >= 1 and cnt2 >= 1`。
3. **奇数 `cnt0` 分支**：
   - `else: return abs(cnt1 - cnt2) > 2`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么在所有石子取完后若没有发生整除，规则规定 Bob 获胜？”*
  - **Candidate Response**: 这是博弈规则的终止条件。因为 Alice 先手，若直到取空石子双方都没有触犯整除 3 的规则，说明 Alice 无法通过最优策略主动击败 Bob，按规则判 Bob 获胜。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 尝试使用递归回溯模拟博弈 | `TimeLimitExceeded` | 数组长度 $10^5$，对抗搜索状态爆炸 | 必须基于同余数学性质进行 $O(n)$ 降维 |
| 奇数 0 场景下误将阈值写为 `> 1` | 特殊用例判错 | Bob 可以利用唯一的 0 反制领先 1 或 2 个石子的优势，需至少相差 3 个 | 严格判定 `abs(cnt1 - cnt2) > 2` |

### Complete Dry-Run Table / 实例推演表

输入: `stones = [2, 1, 2, 4, 3]` -> `cnt0 = 1, cnt1 = 2 (1, 4), cnt2 = 2 (2, 2)`

| Check | Value | Condition | Outcome |
|:---:|:---:|:---:|:---:|
| `cnt0 % 2` | 1 (奇数) | 进入奇数分支 | - |
| `abs(cnt1 - cnt2)` | `abs(2 - 2) = 0` | `0 > 2` 为 False | 返回 `False` (Bob 必胜) |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 仅单次遍历数组统计模 3 频数，分类判断为 $O(1)$。 |
| **Space Complexity** | $O(1)$ | 仅使用 3 个整型计数器 `cnt0, cnt1, cnt2`。 |
