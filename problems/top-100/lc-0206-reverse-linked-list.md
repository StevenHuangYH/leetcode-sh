# LeetCode 206. Reverse Linked List (反转链表)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (面试超高频 / 链表指针操作基石)
- **Tags:** Linked List, Recursion, Two Pointers
- **Corresponding Python File:** [`problems/top-100/lc-0206-reverse-linked-list.py`](problems/top-100/lc-0206-reverse-linked-list.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a singly linked list, reverse the list, and return the **reversed list's head**.
* **[CN]** 给你单链表的头节点 `head` ，请你反转链表，并返回 **反转后的链表头节点** 。

### Constraints / 约束条件
* 链表中节点的数目范围是 `[0, 5000]`
* $-5000 \le \text{Node.val} \le 5000$
* **进阶 (Follow-up)**：链表可以选用迭代或递归方式完成反转。你能否同时实现这两种方法？

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 链表指针操作母题 (Foundational Primitive): 整个链表体系最核心的基础原语。 │
│ 2. 四步指针滑移节律: 暂存后继 -> 指针换向 -> 前驱步进 -> 当前步进。          │
│ 3. 核心循环不变量 (Loop Invariant):                                         │
│    • pre 始终维护已完全反转的子链表头节点 (初始为 None)。                    │
│    • cur 始终指向当前待反转的节点 (初始为 head)。                            │
│    • nxt 用于提前保全尚未遍历的剩余链表 (防断链丢失)。                       │
│ 4. 边界防御与鲁棒性: 完美自适配空链表与单节点，无任何特判。                  │
│ 5. 极致常数开销: 严格 O(n) 时间，O(1) 原地空间反转。                         │
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
│  Level 1 (Primitive): LC 206 Reverse Linked List (★ 本题)                   │
│  └─ 不变量 (Invariant): 全局单向三指针滑移换向 (pre, cur, nxt)。              │
│        │                                                                    │
│        ▼ [演进 Twist: 局部指定区间 [left, right] 反转]                      │
│  Level 2 (Interval):  LC 92 Reverse Linked List II                          │
│  └─ 不变量 (Invariant): 哨兵 dummy + 步进 p0 定位前驱，局部反转后四步缝合。   │
│        │                                                                    │
│        ▼ [演进 Twist: 每 k 个节点为一组进行全局周期性批量反转]              │
│  Level 3 (Hard Mode): LC 25 Reverse Nodes in k-Group                        │
│  └─ 不变量 (Invariant): 预先长度探测 + 循环组内调用 LC 206 原语 + 组间拼接。 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：三指针协同滑移换向 (`pre`, `cur`, `nxt`)

单向链表的特点是每个节点只有一个指向下一个节点的指针 `next`。
反转链表的核心就在于：**将当前节点 `cur.next` 的指向从原来的下一个节点改为指向前一个节点 `pre`**。

#### 动态指针滑移全流程 ASCII 图解：

```
初始状态 (Initial State):
     pre       cur        nxt
      ↓         ↓          ↓
    None       [1]   ->   [2]   ->   [3]   ->   None

第 1 步：暂存 nxt = cur.next (防止链表后续断裂丢失)
第 2 步：换向 cur.next = pre (指向前面)
第 3 步：前移 pre = cur
第 4 步：前移 cur = nxt

第 1 轮后 (After Iteration 1):
              pre        cur        nxt
               ↓          ↓          ↓
    None  <-  [1]        [2]   ->   [3]   ->   None

第 2 轮后 (After Iteration 2):
                         pre        cur        nxt
                          ↓          ↓          ↓
    None  <-  [1]  <-    [2]        [3]   ->   None

第 3 轮后 (After Iteration 3):
                                    pre        cur (None)
                                     ↓          ↓
    None  <-  [1]  <-    [2]  <-    [3]        None

循环终止：cur 为 None，pre 停在原链表的尾节点（即反转后的新头节点 [3]），直接返回 pre！
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `problems/top-100/lc-0206-reverse-linked-list.py` 中的标准实现：

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
```

* **[EN] Action:** Initializes `pre` pointer to `None` and `cur` pointer to `head`.
  * **Why `pre = None`?** Because the original head node will become the tail node of the reversed list, and a list tail must point to `None`.
* **[CN] 动作**：初始化前驱指针 `pre = None`，当前指针 `cur = head`。
  * **为什么 `pre` 初始为 `None`？** 原链表的头节点反转后将变为新链表的尾节点，而链表尾部必须指向 `None`。

---

```python
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
```

* **[EN] Action:** Loops through every node in the linked list in 4 synchronized steps:
  1. `nxt = cur.next`: Caches the remaining sublist before severing references.
  2. `cur.next = pre`: Inverts the pointer backwards.
  3. `pre = cur`: Advances the reversed sublist's head.
  4. `cur = nxt`: Moves to the next node.
  5. `return pre`: When `cur` becomes `None`, `pre` sits on the new head.
* **[CN] 动作**：四步节奏推进指针并完成换向：
  1. `nxt = cur.next`：**暂存后继**。保全未处理的后续链表，防止指针断裂引发内存丢失。
  2. `cur.next = pre`：**指针换向**。将当前节点的后继指针反转指向前驱。
  3. `pre = cur`：**前驱步进**。将已反转子链表的头指针更新为当前节点。
  4. `cur = nxt`：**当前步进**。当前指针前移到暂存的下一个待处理节点。
  5. `return pre`：当 `cur` 触底到达 `None` 结束时，`pre` 精准停留在反转后的新头节点，直接返回。

---

## 5. Interview Simulation & Follow-Up Pivots / 面试官现场追问演练

### 🎤 追问 1：链表可以选用递归方式完成反转吗？递归与迭代如何做工程权衡？

* **递归实现代码**：
  ```python
  # 范式 2: 递归反转 (Recursive Approach)
  class SolutionRecursive:
      def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          if head is None or head.next is None:
              return head
          
          # 递归深入到链表末尾，new_head 始终锚定原链表的尾节点 (新头节点)
          new_head = self.reverseList(head.next)
          
          # 回溯阶段反转指针：让 head 的下一个节点指向自己
          head.next.next = head
          head.next = None  # 切断原正向链接防成环
          
          return new_head
  ```
* **全方位架构对比**：

| 维度 | 迭代法 (Iterative - 推荐) | 递归法 (Recursive) |
| :--- | :--- | :--- |
| **时间复杂度** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **空间复杂度** | $\mathcal{O}(1)$ (严格常数) | $\mathcal{O}(n)$ (系统调用栈深度为 $n$) |
| **栈溢出风险** | 无（支持任意超长链表） | 当链表过长（如 $>1000$）可能引发栈溢出 |
| **代码思维** | 自前往后滑移换向 | 自后往前在回溯阶段换向 |

---

### 🎤 追问 2：为什么必须在 `cur.next = pre` 之前暂存 `nxt = cur.next`？

* **面试官意图**：考察指针引用赋值的底层机制与对“悬挂指针/断链丢失”的防范意识。
* **核心解析**：
  * 单向链表中的节点只能通过其前驱的 `next` 引用寻址。
  * 如果先执行 `cur.next = pre`，`cur` 的后继指针被立即覆盖。此时原链表后续所有的节点将没有任何指针引用指向它们，导致**整个后续链表在内存中失联断裂（Dangling Sublist）**。
  * 因此必须先使用独立的临时引用 `nxt` 锁住后续节点地址。

---

## 6. The Error Log & Dry-Run / 错题排查与实例推演

### ⚠️ 错题排查与反模式诊断 (The Error Log: Anti-Patterns & Defensive Fixes)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚠️ 反模式 1：未暂存后继直接反转导致断链丢失 (Missing Next Cache)                                            │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ❌ 错误写法:                                                                                                │
│    cur.next = pre  # 致命：cur.next 原先指向的节点丢失！后续 cur = cur.next 变成进入死循环或 None           │
│    pre = cur                                                                                                │
│                                                                                                             │
│ 🎯 翻车机理 (Root Cause):                                                                                   │
│    指针赋值具有破坏性（Destructive Write）。覆盖指针前必须先缓存目标地址。                                 │
│                                                                                                             │
│ 🛡️ 防御口诀 (Invariant):                                                                                   │
│    【先存后断，四步节律】：`nxt = cur.next` -> `cur.next = pre` -> `pre = cur` -> `cur = nxt`               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| 常见陷阱 / 易错反模式 (Buggy Pattern / Traps) | 错误现象与测试用例 (Symptom & Fail Case) | 根本原因分析 (Root Cause) | 防御性修复与循环不变量 (Defensive Fix & Invariant) |
| :--- | :--- | :--- | :--- |
| **未缓存 `cur.next` 先换向** | 链表在第 1 个节点处截断，返回只有 1 个节点 | 破坏了原链表向后寻址的单向引用链 | 严格遵循四步滑移顺序，先取 `nxt = cur.next` |
| **循环条件误写为 `while cur.next:`** | 最后一个尾节点没有被反转，直接丢失新头 | 提前一轮跳出循环，尾节点指针未换向 | 严格使用 `while cur:` 确保所有节点均被处理 |
| **递归法回溯漏写 `head.next = None`** | 链表出现环并在遍历时陷入无限死循环 | 原头节点与第 2 节点形成了双向互相指向 | 递归回溯必加 `head.next = None` 切断原正向链接 |

---

### 🎨 实例全程推演表 (Complete Dry-Run)

**输入**：`head = [1, 2, 3]`

| 轮次 | `cur` 位置 | `pre` 位置 | 暂存 `nxt` | 执行 `cur.next = pre` 后的局部形态 | 步进后 `pre, cur` |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **初始** | `[1]` | `None` | — | `None` | `pre=None, cur=[1]` |
| **第 1 轮** | `[1]` | `None` | `[2]` | `[1] -> None` | `pre=[1], cur=[2]` |
| **第 2 轮** | `[2]` | `[1]` | `[3]` | `[2] -> [1] -> None` | `pre=[2], cur=[3]` |
| **第 3 轮** | `[3]` | `[2]` | `None` | `[3] -> [2] -> [1] -> None` | `pre=[3], cur=None` |
| **终止** | `None` | `[3]` | — | 循环结束，返回 `pre` (`[3]`) | 返回 `[3, 2, 1]` (正确) |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 说明与理论支撑 |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 单趟线性扫描，每个节点执行常数次指针读写与赋值操作，总时间为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用 `pre`, `cur`, `nxt` 三个指针变量，原地修改指针，无额外内存分配。 |
