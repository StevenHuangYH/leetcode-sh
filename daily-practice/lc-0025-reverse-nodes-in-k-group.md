# LeetCode 25. Reverse Nodes in k-Group (K 个一组翻转链表)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Hard (链表指针操作终极面试题 / 局部反转与循环缝合)
- **Tags:** Linked List, Recursion
- **Corresponding Python File:** [`daily-practice/lc-0025-reverse-nodes-in-k-group.py`](daily-practice/lc-0025-reverse-nodes-in-k-group.py)

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

## 2. Core Idea & Mathematical Intuition / 核心解法思路与数学原理

### 💡 核心机制：哨兵哑节点 (`dummyNode`) + 长度预判 + 循环三指针反转与锚点步进 (`p0`)

本题是 **LeetCode 92 (反转链表 II)** 的高阶泛化版。在 LeetCode 92 中，我们只需对单一局部区间 $[left, right]$ 反转一次；而在本题中，我们需要 **连续循环执行 $\lfloor n / k \rfloor$ 次局部反转**，并将各组无缝缝合。

整个算法的三个核心逻辑支柱：
1. **支柱 1：先探明链表总长度 $n$**
   * 遍历一次链表得到长度 $n$。
   * 每次处理一组时，先检查剩余节点数是否满足 $n \ge k$。
   * 若 $n < k$，说明最后一组不足 $k$ 个节点，无需反转，直接终止循环并保留原有顺序。
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

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `daily-practice/lc-0025-reverse-nodes-in-k-group.py` 中的经典实现：

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

## 4. Alternative Paradigms & Comparative Study / 算法范式对比

```
范式 1: 长度预判 + 迭代缝合 (当前解法)          范式 2: 递归分治反转 (Recursion)
p0 -> [Group 1] -> [Group 2] -> [Remainder]      head -> [Reverse k] -> reverseKGroup(next_head, k)
循环迭代，空间严格 O(1)                           自顶向下递归，调用栈占用 O(n/k) 空间
```

| 维度 | 范式 1：长度预判 + 迭代缝合 (推荐) | 范式 2：区间探测 + 迭代反转 | 范式 3：递归分治法 (Recursion) |
| :--- | :--- | :--- | :--- |
| **核心机制** | 先求总长 $n$，`while n >= k` 循环缝合 | 每轮向前走 $k$ 步探路，够 $k$ 步再翻转 | 翻转前 $k$ 个节点，递归调用处理后续链表 |
| **空间复杂度** | $\mathcal{O}(1)$ (严格常数内存) | $\mathcal{O}(1)$ (严格常数内存) | $\mathcal{O}(n/k)$ (系统递归调用栈) |
| **时间复杂度** | $\mathcal{O}(n)$ (总计遍历节点 $< 2n$) | $\mathcal{O}(n)$ (探路 + 翻转各 1 次) | $\mathcal{O}(n)$ |
| **代码优雅度** | ⭐️⭐️⭐️⭐️⭐️ (复用 LC 92 模版，逻辑极为规整) | ⭐️⭐️⭐️⭐️ (多一层探路判断) | ⭐️⭐️⭐️ (简洁但违背进阶 $\mathcal{O}(1)$ 要求) |

---

## 5. Key FAQs & Edge Cases / 常见疑难与边界排查

### ❓ Q1: 为什么必须用临时变量 `nxt` 暂存 `p0.next`？
* **解答**：
  * 在执行 `p0.next = pre` 之后，`p0.next` 会被立刻改写为 `pre`（新头部）。
  * 如果没有提前暂存 `nxt = p0.next`，你就永远失去了本组尾节点的指针，导致无法执行 `p0 = nxt` 推进锚点！
  * **四步黄金口诀**：
    1. 存尾 (`nxt = p0.next`)
    2. 连后 (`p0.next.next = cur`)
    3. 连前 (`p0.next = pre`)
    4. 步进 (`p0 = nxt`)

---

### ❓ Q2: 当 $k = 1$ 时会发生什么？
* 每一轮 $k = 1$，反转单节点子区间。
* 链表结构在逻辑上被完全原样重构，返回与原链表完全相同的顺序，不会出现死循环或空指针异常。

---

### ❓ Q3: 当 $k = n$ 时会发生什么？
* $n \ge k$ 仅成立 1 次。
* 整个链表被作为单一组整体反转，直接返回完全翻转后的单链表。

---

## 6. Complete Step-by-Step Dry-Run / 实例全程推演

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
