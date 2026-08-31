# LeetCode 25. Reverse Nodes in k-Group (K 个一组翻转链表)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Hard (链表指针操作终极面试题 / 局部反转与循环缝合)
- **Tags:** Linked List, Recursion
- **Corresponding Python File:** [`problems/daily-practice/lc-0025-reverse-nodes-in-k-group.py`](problems/daily-practice/lc-0025-reverse-nodes-in-k-group.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a singly linked list, reverse the nodes of the list `k` at a time, and return the modified list.
  * `k` is a positive integer and is less than or equal to the length of the linked list.
  * If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.
  * You may not alter the values in the list's nodes, only nodes themselves may be changed.
* **[CN]** 给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。
  * `k` 是一个正整数，它的值小于或等于链表的长度。
  * 如果节点总数不是 `k` 的整数倍，那么最后剩余的节点应当保持原有顺序。
  * 你不能只是单纯的改变节点内部的值，而是需要实际进行节点指针的交换与重连。

### Constraints / 约束条件
* 链表中节点的数目为 `n`
* $1 \le k \le n \le 5000$
* $0 \le \text{Node.val} \le 1000$
* **进阶 (Follow-up)**：你能否设计一个只使用 $\mathcal{O}(1)$ 额外内存空间的算法解决此问题？

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 哨兵哑节点机制 (Sentinel Dummy): 抹平 head 前驱缺失的特例处理。          │
│ 2. 三指针滑动反转 (3-Pointer In-Place Slide): 局部 k 节点无额外空间翻转。    │
│ 3. 跨组四步缝合口诀: 存新尾 -> 连后驱 -> 连前驱 -> 推进锚点。                │
│ 4. 剩余节点保序判定: 严控剩余长度 n >= k，不足 k 节点绝不破坏原有结构。     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Linear Structures] ➔ [Linked List] ➔ [Two Pointer]`

### 🧠 反转链表算法思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Linked List Reversal Pattern Lineage (反转链表思维谱系演化树)             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Primitive): LC 206 Reverse Linked List                            │
│  └─ 不变量 (Invariant): 三指针 (pre, cur, nxt) 就地翻转 100% 链表节点。       │
│        │                                                                    │
│        ▼ [演进 Twist: 引入边界范围 [left, right]]                            │
│  Level 2 (Bounded):   LC 92 Reverse Linked List II                          │
│  └─ 不变量 (Invariant): 哨兵 dummy + 锚点 p0 定位在 left-1，单次局部缝合。    │
│        │                                                                    │
│        ▼ [演进 Twist: 循环 ⌊n/k⌋ 次 + 动态锚点滚动前移 (p0 步进)]             │
│  Level 3 (Cyclic):    LC 25 Reverse Nodes in k-Group (★ 本题)               │
│  └─ 不变量 (Invariant): 预判总长 n + while n>=k 循环翻转 + 动态前驱缝合。    │
│        │                                                                    │
│        ▼ [演进 Twist: 与树/图结合或复杂分组]                                 │
│  Level 4 (Advanced):  LC 24 (两两交换/k=2) / LC 430 扁平化多级链表          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：哨兵哑节点 (`dummyNode`) + 长度预判 + 循环三指针反转与锚点步进 (`p0`)

整个算法的三个核心逻辑支柱：
1. **支柱 1：先探明链表总长度 $n$**
   * 遍历一次链表得到长度 $n$。
   * 每次处理一组时，先检查剩余节点数是否满足 $n \ge k$。若 $n < k$，直接终止循环并保留原有顺序。
2. **支柱 2：局部标准 $k$ 节点反转**
   * 维护一个前驱锚点指针 `p0`（初始位于 `dummyNode`）。
   * `cur = p0.next`，`pre = None`，循环 $k$ 次执行经典三指针翻转（`nxt = cur.next; cur.next = pre; pre = cur; cur = nxt`）。
   * 翻转后，`pre` 是本组反转后的 **新头节点**，`cur` 是下一组的 **起始后继节点**。
3. **支柱 3：四步关键缝合与锚点迁移 (`p0` 步进)**
   * `nxt = p0.next`：**必须先暂存** 原本的组头（反转后变成了本组的新尾节点！）。
   * `p0.next.next = cur`：将本组新尾部连接到下一组的首节点 `cur`。
   * `p0.next = pre`：将上一组的尾部 `p0` 连接到本组新头部 `pre`。
   * `p0 = nxt`：将锚点 `p0` 推进到本组的新尾部，为下一轮 $k$ 组反转做准备！

---

### 🎨 动态指针滑移全流程 ASCII 图解

以链表 `[1, 2, 3, 4, 5]`, `k = 2` 为例（$n = 5$，共反转 $\lfloor 5/2 \rfloor = 2$ 组，余 1 节点保持原样）：

```
初始状态 (Initial State):
dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> None
  ↑
 p0 (初始停在 dummy)

═════════════════════════════════════════════════════════════════════
第一轮循环 (Round 1: 反转第 1 组 [1, 2]):
反转前: p0 -> [1] -> [2] -> [3] ...
反转后: pre=[2], cur=[3], p0.next 仍指向 [1]

四步缝合:
1. nxt = p0.next        ==> nxt 暂存节点 [1] (本组新尾)
2. p0.next.next = cur   ==> [1].next = [3] (新尾连到下组头)
3. p0.next = pre        ==> dummy.next = [2] (前驱连到新头)
4. p0 = nxt             ==> p0 步进到节点 [1]

第一轮后链表形态:
dummy -> [2] -> [1] -> [3] -> [4] -> [5] -> None
                 ↑
                p0 (新锚点)

═════════════════════════════════════════════════════════════════════
第二轮循环 (Round 2: 反转第 2 组 [3, 4]):
反转前: p0 -> [3] -> [4] -> [5] ...
反转后: pre=[4], cur=[5], p0.next 仍指向 [3]

四步缝合:
1. nxt = p0.next        ==> nxt 暂存节点 [3] (本组新尾)
2. p0.next.next = cur   ==> [3].next = [5]
3. p0.next = pre        ==> [1].next = [4]
4. p0 = nxt             ==> p0 步进到节点 [3]

第二轮后链表形态:
dummy -> [2] -> [1] -> [4] -> [3] -> [5] -> None
                               ↑
                              p0

═════════════════════════════════════════════════════════════════════
终止检查: 剩余 n = 1 < k (2)，跳出循环！
最终结果: dummyNode.next 即为 [2, 1, 4, 3, 5]
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `problems/daily-practice/lc-0025-reverse-nodes-in-k-group.py` 中的经典实现：

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
```

---

```python
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
```

* **[EN] Action:** Traverses the entire linked list once to count its total length $n$.
  * **Why count first?** The problem states that if the final segment has fewer than $k$ nodes, it must remain unmodified. Precomputing $n$ allows $\mathcal{O}(1)$ verification (`while n >= k:`) instead of lookahead probes.
* **[CN] 动作**：单次遍历整条链表，统计节点总数 $n$。
  * **为什么先统计长度？** 题目要求不足 $k$ 个的末尾剩余节点保持原序。提前计算 $n$ 可以在后续反转前通过 `while n >= k:` 以 $\mathcal{O}(1)$ 时间精确判定是否需要继续翻转，避免冗余的试探与回溯。

---

```python
        dummyNode = ListNode(next = head)
        p0 = dummyNode
```

* **[EN] Action:** Creates a sentinel `dummyNode` pointing to `head` and initializes anchor pointer `p0` to `dummyNode`.
  * **Role:** `p0` always points to the node **immediately preceding** the current $k$-group being reversed.
* **[CN] 动作**：创建指向 `head` 的哨兵哑节点 `dummyNode`，并将锚点指针 `p0` 初始化在 `dummyNode`。
  * **作用**：`p0` 在每一轮迭代中始终精准指向 **当前待反转 $k$ 节点子区间的前驱节点**。

---

```python
        while n >= k:
            n -= k
            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
```

* **[EN] Action:** Reverses exactly $k$ nodes in the current group.
  * Decrements remaining node count by $k$ (`n -= k`).
  * Reverses $k$ pointers in-place using standard 3-pointer slide (`pre, cur, nxt`).
  * At loop completion: `pre` points to the new group head, and `cur` points to the next unreversed node.
* **[CN] 动作**：对当前组内的 $k$ 个节点执行标准三指针就地反转。
  * 扣减剩余节点数 `n -= k`。
  * 循环 $k$ 次翻转内部指针。循环结束后，`pre` 指向当前组反转后的新头部，`cur` 指向未反转的下一组首节点。

---

```python
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummyNode.next
```

* **[EN] Action:** Stitches the reversed group back and advances the anchor $p_0$:
  1. `nxt = p0.next`: Caches the original head (which is now the tail of the reversed group).
  2. `p0.next.next = cur`: Connects the new group tail to `cur` (the successor group).
  3. `p0.next = pre`: Connects previous group tail `p0` to `pre` (the new group head).
  4. `p0 = nxt`: Moves anchor `p0` to the tail of the current group, ready for the next iteration.
  5. Finally returns `dummyNode.next`.
* **[CN] 动作**：缝合子链表并将锚点 $p_0$ 前移：
  1. `nxt = p0.next`：**暂存新尾节点**（反转前的组头）。
  2. `p0.next.next = cur`：将本组新尾部连接到后续未反转链表 `cur`。
  3. `p0.next = pre`：将前置节点 `p0` 指向本组新头部 `pre`。
  4. `p0 = nxt`：将锚点 `p0` 移动到本组新尾部，作为下一组的前驱节点。
  5. 循环结束后返回 `dummyNode.next`。

---

## 5. Interview Simulation & Follow-Up Pivots / 面试官现场追问演练

### 🎤 追问 1：如果面试官要求“单次遍历 (One-Pass)，禁止预先扫描统计总长度 $n$”，你该如何破局？

* **面试官意图**：考察你是否具备 **“向前探路探测法 (Lookahead Probe)”** 的能力，即在不知道长度的情况下，如何保证剩余不足 $k$ 个节点不被误翻转。
* **破局解法（探路探测法）**：
  * 在翻转每一组前，先用探针指针向前走 $k$ 步。
  * 若中途遇到 `None`，说明剩余不足 $k$ 个节点，直接退出循环！

```python
# 单趟遍历探路法 (One-Pass Lookahead Probe)
class SolutionLookahead:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy

        while True:
            # 1. 探路：向前走 k 步检测是否存在完整的一组
            probe = p0
            for _ in range(k):
                probe = probe.next
                if not probe:
                    return dummy.next  # 剩余不足 k 个，直接返回

            # 2. 存在完整的一组，执行三指针就地翻转
            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            # 3. 缝合与锚点步进
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
```

---

### 🎤 追问 2：如果面试官要求用“递归分治法 (Recursion)”实现，代码结构是怎样的？有什么代价？

* **面试官意图**：考察你对递归调用栈与分治思想的理解，以及能否指出其在内存空间上的权衡代价。
* **破局解法（递归分治法）**：
  * 先探测前 $k$ 个节点，不够则递归基返回 `head`。
  * 翻转前 $k$ 个节点后，原头节点 `head` 变为尾节点，其 `head.next` 指向 `self.reverseKGroup(next_head, k)` 的递归结果。
* **代价分析**：递归栈深度为 $\mathcal{O}(n/k)$，当 $n = 5000, k = 1$ 时消耗 $\mathcal{O}(n)$ 栈空间，违背进阶 $\mathcal{O}(1)$ 空间的要求。

```python
# 递归分治法 (Recursive Approach)
class SolutionRecursion:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 探路 k 步
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next

        # 2. 翻转当前 k 节点
        pre, node = None, head
        for _ in range(k):
            nxt = node.next
            node.next = pre
            pre = node
            node = nxt

        # 3. 递归连接后续子链表
        head.next = self.reverseKGroup(cur, k)
        return pre
```

---

### 📊 算法范式横向对比矩阵

| 维度 | 范式 1：长度预判 + 迭代缝合 (当前解法 - 推荐) | 范式 2：探路探测 + 迭代翻转 (One-Pass) | 范式 3：递归分治法 (Recursion) |
| :--- | :--- | :--- | :--- |
| **核心机制** | 先求总长 $n$，`while n >= k` 循环缝合 | 每轮向前探路 $k$ 步，够 $k$ 步再翻转 | 翻转前 $k$ 个节点，递归解决后续链表 |
| **空间复杂度** | $\mathcal{O}(1)$ (严格常数内存) | $\mathcal{O}(1)$ (严格常数内存) | $\mathcal{O}(n/k)$ (系统递归调用栈) |
| **时间复杂度** | $\mathcal{O}(n)$ (总计遍历节点 $< 2n$) | $\mathcal{O}(n)$ (探路 + 翻转各 1 次) | $\mathcal{O}(n)$ |
| **代码优雅度** | ⭐️⭐️⭐️⭐️⭐️ (复用 LC 92 模版，逻辑最为工整) | ⭐️⭐️⭐️⭐️ (多一层探测循环) | ⭐️⭐️⭐️ (简洁但消耗栈空间) |

---

## 6. The Error Log & Dry-Run / 错题排查与实例推演

### ⚠️ 错题排查与反模式诊断 (The Error Log: Anti-Patterns & Defensive Fixes)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚠️ 反模式 1：缝合时先改写 p0.next，导致新尾节点指针丢失                                                      │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ❌ 错误写法:                                                                                                │
│    p0.next = pre        # 错误：先将 p0.next 指向了新头节点 pre                                             │
│    p0.next.next = cur   # 灾难：此时 p0.next 是 pre，pre.next 变成了 cur，前 k 个节点的翻转结构瞬间被毁！    │
│    p0 = nxt             # 且此时 nxt 未定义或指向错误                                                       │
│                                                                                                             │
│ 🎯 翻车机理 (Root Cause):                                                                                   │
│    翻转后，原本的 p0.next 是这一组的【新尾部】。一旦先给 p0.next 赋值，就永远失去了对新尾部的引用！          │
│                                                                                                             │
│ 🛡️ 防御口诀 (Gold Standard Invariant):                                                                     │
│    ① 存尾 (nxt = p0.next) -> ② 连后 (p0.next.next = cur) -> ③ 连前 (p0.next = pre) -> ④ 步进 (p0 = nxt)  │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| 常见陷阱 / 易错反模式 (Buggy Pattern / Traps) | 错误现象与测试用例 (Symptom & Fail Case) | 根本原因分析 (Root Cause) | 防御性修复与循环不变量 (Defensive Fix & Invariant) |
| :--- | :--- | :--- | :--- |
| **未提前缓存 `p0.next` 即改写** | 链表成环死循环，或仅返回前 2 个节点 | 改写 `p0.next` 破坏了对本组尾部的引用 | 必须在任何指针改写前用 `nxt = p0.next` 暂存尾节点 |
| **反转内部循环计数用 `while cur:`** | 末尾不足 $k$ 个的节点也被强行翻转 | 题目明确要求剩余节点保序 | 严格使用 `while n >= k:` 或探路 probe 控制翻转次数 |
| **忘了更新 `n -= k`** | `while n >= k` 陷入无限死循环 | 计数器未按步长衰减 | 在每组翻转开始时立即执行 `n -= k` |

---

### ❓ 常见疑难与边界排查 (Boundary FAQs)

* **Q1: 当 $k = 1$ 时会发生什么？**
  * 每一轮 $k = 1$，反转单节点子区间。链表结构在逻辑上被完全原样重构，返回与原链表完全相同的顺序，不会出现死循环或空指针异常。
* **Q2: 当 $k = n$ 时会发生什么？**
  * $n \ge k$ 仅成立 1 次。整个链表被作为单一组整体反转，直接返回完全翻转后的单链表。
* **Q3: 当 $k > n$ 时会发生什么？**
  * 初始 $n \ge k$ 为 False，`while` 循环直接不执行，返回 `dummyNode.next` 即原始链表，完美符合题目要求。

---

### 🎨 实例全程推演表 (Complete Dry-Run)

**输入**：`head = [1, 2, 3, 4, 5]`, `k = 2`

| 阶段 | 剩余 $n$ | `p0` 位置 | `pre` (新头) | `cur` (后继) | 链表结构与指针变化 |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **初始** | $5$ | `dummy` | — | — | `dummy -> [1] -> [2] -> [3] -> [4] -> [5]` |
| **第 1 轮反转** | $3$ | `dummy` | `[2]` | `[3]` | `[1] -> None`, `[2] -> [1]` |
| **第 1 轮缝合** | $3$ | `[1]` | `[2]` | `[3]` | `dummy -> [2] -> [1] -> [3] -> [4] -> [5]` |
| **第 2 轮反转** | $1$ | `[1]` | `[4]` | `[5]` | `[3] -> None`, `[4] -> [3]` |
| **第 2 轮缝合** | $1$ | `[3]` | `[4]` | `[5]` | `dummy -> [2] -> [1] -> [4] -> [3] -> [5]` |
| **终止判定** | $1 < 2$ | `[3]` | — | — | 剩余节点不足 $k=2$，保持原序直接跳出 |
| **返回** | — | — | — | — | 返回 `dummyNode.next` 即 `[2, 1, 4, 3, 5]` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 说明与理论支撑 |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 第一遍遍历统计链表长度耗时 $n$ 步；第二遍局部反转各组节点共处理 $\lfloor n/k \rfloor \times k \le n$ 步；总访问节点次数不超过 $2n$ 次，严格线性时间 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅维护了 `dummyNode`、`p0`、`pre`、`cur`、`nxt` 及计数器 `n` 等常数个引用指针，满足进阶要求的严格常数额外空间。 |
