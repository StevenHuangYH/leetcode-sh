# LeetCode 142. Linked List Cycle II (环形链表 II)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (快慢双指针经典题 / 数学追及相遇与入环点定位)
- **Tags:** Linked List, Two Pointers, Math, Hash Table
- **Corresponding Python File:** [`top-100/lc-0142-linked-list-cycle-ii.py`](top-100/lc-0142-linked-list-cycle-ii.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a linked list, return the **node where the cycle begins**. If there is no cycle, return `null`.
  * There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.
  * Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that `pos` is not passed as a parameter**.
  * **Do not modify** the linked list.
* **[CN]** 给定一个链表的头节点  `head` ，返回链表开始 **入环的第一个节点**。 如果链表无环，则返回 `null`。
  * 如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。
  * 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 `pos` 是 `-1`，则在该链表中没有环。**注意：`pos` 不作为参数进行传递**，仅仅是为了标识链表的实际情况。
  * **不允许修改** 链表。

### Constraints / 约束条件
* 链表中节点的数目范围在范围 $[0, 10^4]$ 内
* $-10^5 \le \text{Node.val} \le 10^5$
* `pos` 的值为 `-1` 或者链表中的一个有效索引
* **进阶 (Follow-up)**：你能否使用 $\mathcal{O}(1)$（即，常量）内存解决此问题？

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 两阶段判定法则 (Two-Phase Algorithm):                                     │
│    • 阶段 1: 快慢双指针检测是否存在碰撞点 (fast is slow)。                   │
│    • 阶段 2: 单步同速指针追及定位入环点 (head 与 slow 同步走 a 步相遇)。     │
│ 2. 核心数学恒等式: a = (k - 1)(b + c) + c  ==>  当 k=1 时, a = c。          │
│ 3. 内存地址同一性约束: 校验使用 is / is not，严禁使用数值 == 比较。          │
│ 4. 空间与结构约束: 严禁修改链表结构，空间严格常数 O(1)。                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 快慢双指针算法思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Fast-Slow Two Pointer Pattern Lineage (快慢双指针思维谱系演化树)          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Primitive): LC 876 Middle of the Linked List                      │
│  └─ 不变量 (Invariant): 2:1 速度差定位无环链表中点。                         │
│        │                                                                    │
│        ▼ [演进 Twist: 闭环追及相遇检测]                                      │
│  Level 2 (Collision): LC 141 Linked List Cycle                              │
│  └─ 不变量 (Invariant): 相对速度为 1，环内有限步内必在同一节点发生物理碰撞。 │
│        │                                                                    │
│        ▼ [演进 Twist: 碰撞后通过数学等式定位【入环第一个节点】(本题 ★)]      │
│  Level 3 (Math Loc):  LC 142 Linked List Cycle II                           │
│  └─ 不变量 (Invariant): a = (k-1)(b+c) + c，head 与 slow 同速相遇于入环点。 │
│        │                                                                    │
│        ▼ [演进 Twist: 将隐式数组映射为链表图，利用判环寻找数组重复数]        │
│  Level 4 (Array Graph): LC 287 Find the Duplicate Number                    │
│  └─ 不变量 (Invariant): 将 nums[i] 视作 next 指针，在值域图中寻找环入口。     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心数学原理推导：为什么相遇后同步走必在入口相遇？

这是面试中**被提问频率极高的经典数学推导题**：

```
链表结构拓扑与距离定义:

      head (起点)
        │
      a │ (非环部分长度)
        ▼
     [入环点] ◄──────────────┐
        │                    │
      b │ (入环点到相遇点)    │ c (相遇点回环到入环点)
        ▼                    │
     [相遇点] ───────────────┘
     (slow, fast 重合处)
     
环周长 = b + c
```

#### 📐 严密代数推导过程 (Mathematical Proof)
1. **设各个路段长度**：
   * 链表头 `head` 到入环点的距离为 $a$。
   * 入环点顺时针走到两指针初次相遇点的距离为 $b$。
   * 相遇点继续顺时针走到入环点的剩余距离为 $c$。
   * 显然，整个环的周长为 $L = b + c$。

2. **列出初次相遇时的路程方程**：
   * 慢指针 `slow` 走的距离：$d_{\text{slow}} = a + b$（慢指针在进环后走的第一圈内必定被快指针追上，因此慢指针在环内走过的距离恰为 $b$）。
   * 快指针 `fast` 走的距离：$d_{\text{fast}} = a + k(b + c) + b$（其中 $k \ge 1$ 表示快指针在环内转了 $k$ 圈）。

3. **利用快指针速度是慢指针 2 倍列等式**：
   $$d_{\text{fast}} = 2 \cdot d_{\text{slow}}$$
   $$a + k(b + c) + b = 2(a + b)$$
   $$a + k(b + c) + b = 2a + 2b$$
   $$a + b = k(b + c)$$
   $$a = k(b + c) - b$$
   $$a = (k - 1)(b + c) + (b + c) - b$$
   $$a = (k - 1)(b + c) + c$$

4. **数学结论与物理意义**：
   * 公式 $a = (k - 1)(b + c) + c$ 的物理含义非常直观：
     * 从链表头 `head` 走 $a$ 步到达入环点；
     * 从相遇点出发走 $c$ 步（加上可能在环内多转的 $k - 1$ 整圈），也**刚好到达入环点**！
   * **破局动作**：相遇后，将指针 `head` 和相遇点的指针 `slow` **以相同的速度（每次 1 步）向前推进**，两指针最终**必定在入环点发生二次相遇**！

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `top-100/lc-0142-linked-list-cycle-ii.py` 中的标准实现：

```python
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

---

```python
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
```

* **[EN] Action (Phase 1):** Detects if a cycle exists using Floyd's Tortoise and Hare algorithm.
  * `slow` moves 1 step, `fast` moves 2 steps.
  * When `fast is slow`, collision occurs inside the cycle.
* **[CN] 动作 (阶段 1)**：使用 Floyd 快慢双指针进行碰撞检测。
  * `slow` 步长为 1，`fast` 步长为 2。
  * 当 `fast is slow` 成立时，说明快慢指针在环内发生物理碰撞，成功证实环的存在。

---

```python
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
```

* **[EN] Action (Phase 2):** Locates the entry node of the cycle based on $a = (k-1)(b+c) + c$.
  * Advances `head` and `slow` concurrently at speed 1 step per iteration.
  * When `slow is head`, both pointers have met exactly at the cycle entry node.
  * Returns `slow` (the entry node).
* **[CN] 动作 (阶段 2)**：根据数学定理 $a = c$ 同步定位入环点。
  * 保持 `slow` 停在相遇点，将 `head` 作为另一个起点探针。
  * 两者同时以每次 1 步的恒定速度向前走。
  * 当 `slow is head` 时，两指针在入环点相遇，返回该节点。

---

```python
        return None
```

* **[EN] Action:** If `fast` or `fast.next` reaches `None`, the list is acyclic, so returns `None`.
* **[CN] 动作**：如果快指针触底到达链表末尾，说明无环，直接返回 `None`。

---

## 5. Interview Simulation & Follow-Up Pivots / 面试官现场追问演练

### 🎤 追问 1：如果面试官要求用哈希表实现，代码如何写？为什么快慢指针更受大厂青睐？

* **哈希表实现代码**：
  ```python
  # 范式 2: 哈希集合记录节点引用 (Hash Set - O(n) Space)
  class SolutionHashSet:
      def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
          visited = set()
          cur = head
          while cur:
              if cur in visited:
                  return cur  # 首次重复访问的节点即为入环点
              visited.add(cur)
              cur = cur.next
          return None
  ```
* **架构权衡解析**：
  * 哈希表法需要维护一个集合保存所有节点引用，空间复杂度为 $\mathcal{O}(n)$。在包含上万个节点的工业级链表上会产生可观的内存分配与哈希碰撞开销。
  * 快慢指针法将空间复杂度压缩至严格的常数 $\mathcal{O}(1)$，且无需任何内存分配，体现了极致的算法工程素养。

---

### 🎤 追问 2：为什么慢指针 `slow` 进环之后，在走完第一圈之内就必然与快指针相遇？

* **面试官意图**：考察对环内追及细节与严格上界的掌握。
* **严格证明**：
  * 当 `slow` 刚到达入环点时，`fast` 已经在环内的某个位置，两者在环内的追及距离 $d < b+c$（小于 1 圈周长）。
  * 相对速度为 $1$ 节点/步，因此最多只需要 $d$ 步（即小于 1 圈）快指针就能追上慢指针。
  * 慢指针每步只走 1 个节点，因此在走完第一圈之前（即走过距离 $< b+c$）必定与快指针相遇！

---

### 🎤 追问 3：这套双指针数学模型如何无缝迁移解决 LeetCode 287 (寻找重复数)？

* **面试官意图**：考察算法模型的抽象与横向迁移能力。
* **破局思路**：
  * 在数组 `nums` 中，将索引 $i$ 视作节点，将数值 `nums[i]` 视作指向下一个节点的指针 `node.next`。
  * 因为存在重复数，必然有两个不同的下标指向同一个数值节点，从而在值域图中**构成闭环**！
  * 重复数恰好就是值域图的**环入口点**！直接套用本题的双指针模版，即可在 $\mathcal{O}(1)$ 空间且不修改原数组的前提下找到重复数。

---

## 6. The Error Log & Dry-Run / 错题排查与实例推演

### ⚠️ 错题排查与反模式诊断 (The Error Log: Anti-Patterns & Defensive Fixes)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚠️ 反模式 1：阶段 2 循环比较时误用数值比较 `while slow.val != head.val:`                                     │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ❌ 错误写法:                                                                                                │
│    while slow.val != head.val:  # 灾难：若非环节点与入环前节点数值相同，会导致提前在非入环点误相遇！        │
│        slow = slow.next                                                                                     │
│        head = head.next                                                                                     │
│                                                                                                             │
│ 🎯 翻车机理 (Root Cause):                                                                                   │
│    单链表中多个节点可以拥有完全相同的数值。只有内存地址 `is / is not` 才能代表链表拓扑上的同一物理节点。   │
│                                                                                                             │
│ 🛡️ 防御口诀 (Invariant):                                                                                   │
│    【寻入口比对象同一性，绝不比值】：严格使用 `while slow is not head:`                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| 常见陷阱 / 易错反模式 (Buggy Pattern / Traps) | 错误现象与测试用例 (Symptom & Fail Case) | 根本原因分析 (Root Cause) | 防御性修复与循环不变量 (Defensive Fix & Invariant) |
| :--- | :--- | :--- | :--- |
| **`while slow.val != head.val:`** | 重复值链表在入环前提前误返回 | 混淆了数值相等与节点同一性 | 严格使用对象同一性判断 `while slow is not head:` |
| **阶段 2 快指针仍以 2 步速度走** | 两指针不断在环内错开，无法在入环点相遇 | 违背了 $a = c$ 的单步同速数学前提 | 阶段 2 两指针速度必须**严格均为 1 步** |
| **未判空直接访问 `head.next`** | `AttributeError: 'NoneType' object has no attribute 'next'` | 空链表或单节点无环防御不足 | 依赖 `while fast and fast.next:` 作为守卫条件 |

---

### ❓ 常见疑难与边界排查 (Boundary FAQs)

* **Q1: 若整个链表就是一个完整的纯大环（$a = 0$，即 `pos = 0`）会怎样？**
  * 相遇后，`head` 就在入环点，`slow` 走 $c = 0$ 步后两者立即重合，`while slow is not head:` 一次都不执行，直接返回 `head`，完全正确。
* **Q2: 链表仅有 1 个自环节点 (`[1] -> [1]`, `pos = 0`) 会怎样？**
  * 阶段 1：`slow` 和 `fast` 走 1 步后均停在节点 1，判定相遇。
  * 阶段 2：`slow` 与 `head` 均在节点 1，直接返回节点 1，完全正确。
* **Q3: 无环链表 (`pos = -1`) 会怎样？**
  * 快指针 `fast` 遇到 `None`，跳出 `while` 循环返回 `None`，完全正确。

---

### 🎨 实例全程推演表 (Complete Dry-Run)

**输入**：`head = [3, 2, 0, -4]`, `pos = 1`（尾节点 `-4` 连向索引 1 的节点 `2`；$a = 1, b = 2, c = 1$）

| 阶段 | 步骤 | `slow` 位置 | `fast` / `head` 位置 | 说明 |
| :---: | :---: | :---: | :---: | :--- |
| **阶段 1：碰撞检测** | 初始 | `[3]` | `fast = [3]` | 快慢双指针在起点就位 |
| | 步 1 | `[2]` | `fast = [0]` | `slow` 进环，`fast` 跨 2 步 |
| | 步 2 | `[0]` | `fast = [2]` | `fast` 环内追及 |
| | 步 3 | `[-4]` | `fast = [-4]` | **`fast is slow` 成立！在节点 `[-4]` 碰撞！** |
| **阶段 2：定位入环点** | 初始 | `[-4]` (相遇点) | `head = [3]` (起点) | 启动单步同步追及 |
| | 步 1 | `[2]` | `head = [2]` | `slow` 走 $c=1$ 步到达 `[2]`，`head` 走 $a=1$ 步到达 `[2]` |
| | 判定 | `[2]` | `[2]` | **`slow is head` 成立！在入环点 `[2]` 相遇！** |
| **最终返回** | — | — | — | 返回节点 `[2]` (值为 2，正确) |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 说明与理论支撑 |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 1. **阶段 1**：慢指针在环内走不超过 1 圈（$< n$ 步）即与快指针相遇，耗时 $\le 2n$ 步。<br>2. **阶段 2**：两指针各走 $a \le n$ 步在入环点相遇，耗时 $\le n$ 步。<br>总步数不超过 $3n$，严格线性时间 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用了 `slow` 和 `fast` 辅助指针变量，无任何哈希表或动态数组开销，满足进阶严格常数空间要求。 |
