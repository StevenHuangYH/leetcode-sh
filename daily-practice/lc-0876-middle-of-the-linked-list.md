# LeetCode 876. Middle of the Linked List (链表的中间结点)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (快慢双指针经典原语 / 链表二分中点定位)
- **Tags:** Linked List, Two Pointers
- **Corresponding Python File:** [`daily-practice/lc-0876-middle-of-the-linked-list.py`](daily-practice/lc-0876-middle-of-the-linked-list.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a singly linked list, return the **middle node** of the linked list.
  * If there are two middle nodes (i.e. even number of nodes), return the **second middle** node.
* **[CN]** 给你单链表的头结点 `head` ，请你找出并返回链表的 **中间结点**。
  * 如果有两个中间结点（即链表长度为偶数），则返回 **第二个中间结点**。

### Constraints / 约束条件
* 链表中节点的数目在范围 $[1, 100]$ 内
* $1 \le \text{Node.val} \le 100$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Floyd 快慢指针 (Tortoise & Hare): fast 每次走 2 步，slow 每次走 1 步。   │
│ 2. 步长速率倍率关系: 任意时刻 fast 走过的路程恒为 slow 的 2 倍。           │
│ 3. 循环终止条件: while fast and fast.next（防空指针异常）。                 │
│ 4. 奇偶终态归宿: 奇数停在中点，偶数天然落在第二个中点。                      │
│ 5. 空间极致约束: 单趟遍历 (One-Pass) + 严格常数空间 O(1)。                  │
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
│  Level 1 (Primitive): LC 876 Middle of the Linked List (★ 本题)             │
│  └─ 不变量: slow=1步, fast=2步; fast 到达末尾时 slow 恰好位于链表中点。      │
│        │                                                                    │
│        ├─► [变体 1: 环路检测与入口定位]                                      │
│        │   LC 141 (环形链表检测) ──► LC 142 (寻找入环点 - Floyd 数学证明)   │
│        │                                                                    │
│        ├─► [变体 2: 链表折半拆分与重组]                                      │
│        │   LC 143 (重排链表) = [LC 876 找中点] + [LC 206 翻转] + [交替合并]  │
│        │                                                                    │
│        ├─► [变体 3: 回文链表判定]                                           │
│        │   LC 234 (回文链表) = [LC 876 找中点] + [反转后半] + [双指针比对]   │
│        │                                                                    │
│        └─► [变体 4: 链表归并排序]                                           │
│            LC 148 (排序链表) = [LC 876 找第一中点断开] + [归并递归合并]     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：速率差原理与奇偶终态推演

快慢指针（Tortoise and Hare Algorithm）的核心原理是 **速度差为 2:1**：
* 设慢指针 `slow` 每次前进一步（`slow = slow.next`）。
* 快指针 `fast` 每次前进两步（`fast = fast.next.next`）。
* 当快指针 `fast` 走完全程（到达尾节点或超出末尾 `None`）时，`slow` 所走过的路程恰好是 `fast` 的一半，因此 `slow` 必然精准停在链表的中间位置。

#### 奇数长度链表（Odd Length, 如 $n = 5$）
* 初始：`slow = 1`, `fast = 1`
* 步 1：`slow = 2`, `fast = 3`
* 步 2：`slow = 3`, `fast = 5`（此时 `fast.next` 为 `None`，循环终止）
* **结论**：`slow` 停在节点 `3`（唯一中心点）。

#### 偶数长度链表（Even Length, 如 $n = 6$）
* 初始：`slow = 1`, `fast = 1`
* 步 1：`slow = 2`, `fast = 3`
* 步 2：`slow = 3`, `fast = 5`
* 步 3：`slow = 4`, `fast = None`（此时 `fast` 为 `None`，循环终止）
* **结论**：`slow` 停在节点 `4`（第 2 个中间节点，完美契合题意）。

---

### 🎨 动态指针滑移全流程 ASCII 图解

```
═════════════════════════════════════════════════════════════════════
Case 1: 奇数链表 [1, 2, 3, 4, 5] (n = 5)
初始:   [1] -> [2] -> [3] -> [4] -> [5] -> None
        s,f
Step 1: [1] -> [2] -> [3] -> [4] -> [5] -> None
                s      f
Step 2: [1] -> [2] -> [3] -> [4] -> [5] -> None
                       s             f (fast.next is None, 终止!)
结果: 返回 slow 指向的 [3]

═════════════════════════════════════════════════════════════════════
Case 2: 偶数链表 [1, 2, 3, 4, 5, 6] (n = 6)
初始:   [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> None
        s,f
Step 1: [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> None
                s      f
Step 2: [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> None
                       s             f
Step 3: [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> None
                              s                    f=None (fast is None, 终止!)
结果: 返回 slow 指向的 [4] (第二个中点)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `daily-practice/lc-0876-middle-of-the-linked-list.py` 中的经典实现：

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

---

```python
        slow = head
        fast = head
```

* **[EN] Action:** Initializes both `slow` and `fast` pointers at the `head` node.
  * **Invariant:** At start ($t=0$), distance traveled by `slow` is $0$, distance traveled by `fast` is $0$.
* **[CN] 动作**：将快慢两个指针 `slow` 和 `fast` 同时初始化在链表的头节点 `head`。
  * **不变量**：初始时刻两者均位于原点，步长比满足 $2:1$ 的前提条件。

---

```python
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
```

* **[EN] Action:** Traverses the list with two different speeds until `fast` reaches the end.
  * **Guard Condition `while fast and fast.next`:** 
    * `fast` checks if the current fast pointer is valid (handles even lengths when `fast` lands on `None`).
    * `fast.next` ensures `fast.next.next` will not raise an `AttributeError` (handles odd lengths when `fast` lands on the last node).
  * **Pointer Advances:** `slow` moves forward by 1 step, while `fast` moves forward by 2 steps.
* **[CN] 动作**：两指针以不同速率向前推进，直到快指针触底。
  * **双重防御条件 `while fast and fast.next`**：
    * `fast`：确保当前快指针有效，防止偶数长度下 `fast` 已经跳出链表（到达 `None`）时继续访问引发空指针错误。
    * `fast.next`：确保快指针存在下一个节点，防止奇数长度下在最后一个节点执行 `fast.next.next` 时引发 `AttributeError: 'NoneType' object has no attribute 'next'`。
  * **步进操作**：慢指针前进一步（`slow = slow.next`），快指针前进两步（`fast = fast.next.next`）。

---

```python
        return slow
```

* **[EN] Action:** Returns `slow`, which is guaranteed to be pointing to the middle node (or second middle node for even lengths).
* **[CN] 动作**：返回此时的慢指针 `slow`，该节点即为链表的中点。

---

## 5. Interview Simulation & Follow-Up Pivots / 面试官现场追问演练

### 🎤 追问 1：如果面试官要求“对于偶数长度链表，返回【第一个】中间结点（左中点）”，代码应该如何修改？

* **面试官意图**：考察你对快慢指针边界条件的绝对掌控力。在 **LeetCode 148 (链表归并排序)** 和 **LeetCode 143 (重排链表)** 中，我们需要从中点将链表断开成前后两半，此时必须定位在 **左中点 (First Middle)** 才能正确断开！
* **破局解法 1（改变循环终止条件 - 常用推荐）**：
  ```python
  # 定位左中点 (First Middle Node: [1,2,3,4,5,6] -> 停在 3)
  class SolutionFirstMiddle:
      def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
          slow = head
          fast = head
          # 仅当前方至少还有两个节点时才继续前进
          while fast.next and fast.next.next:
              slow = slow.next
              fast = fast.next.next
          return slow
  ```
* **破局解法 2（让快指针领先一步出发）**：
  ```python
  class SolutionFirstMiddleFastAhead:
      def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
          slow = head
          fast = head.next  # fast 提前领先一步
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
          return slow
  ```

---

### 🎤 追问 2：除了快慢双指针，还有哪些解法？各有什么优缺点？

* **面试官意图**：考察对不同解法在时空复杂度、内存分配、以及遍历趟数上的权衡对比。

```python
# 范式 2: 数组辅助空间法 (Array Lookup - O(n) Space)
class SolutionArray:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        return arr[len(arr) // 2]
```

```python
# 范式 3: 计数两趟遍历法 (Two-Pass Counting - O(1) Space, 2 Passes)
class SolutionTwoPass:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        cur = head
        for _ in range(n // 2):
            cur = cur.next
        return cur
```

---

### 📊 算法范式横向对比矩阵

| 维度 | 范式 1：快慢双指针 (当前解法 - 最优) | 范式 2：数组辅助映射 (Array Index) | 范式 3：长度计数两趟遍历 (Two-Pass) |
| :--- | :--- | :--- | :--- |
| **核心机制** | $2:1$ 速率差，单趟一次扫描到达中点 | 存入 Python 列表，直接根据下标 `len//2` 访问 | 第 1 趟统计总长 $n$，第 2 趟走 $n//2$ 步 |
| **空间复杂度** | $\mathcal{O}(1)$ (仅用两个指针) | $\mathcal{O}(n)$ (需要额外数组存储全部引用) | $\mathcal{O}(1)$ (仅用计数器变量) |
| **时间复杂度** | $\mathcal{O}(n)$ (单趟扫描，步数 $< n$) | $\mathcal{O}(n)$ (单趟扫描 + 数组构建) | $\mathcal{O}(n)$ (遍历 $n + n/2 = 1.5n$ 步) |
| **遍历趟数** | **1 趟 (One-Pass)** | 1 趟 | 2 趟 (Two-Pass) |
| **面试推荐度** | ⭐️⭐️⭐️⭐️⭐️ (标准教科书答案) | ⭐️⭐️⭐️ (违背链表空间设计初衷) | ⭐️⭐️⭐️⭐️ (思路朴素但多了一趟扫描) |

---

## 6. The Error Log & Dry-Run / 错题排查与实例推演

### ⚠️ 错题排查与反模式诊断 (The Error Log: Anti-Patterns & Defensive Fixes)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚠️ 反模式 1：while 条件顺序颠倒写成 `while fast.next and fast:`                                              │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ❌ 错误写法:                                                                                                │
│    while fast.next and fast:  # 灾难：当 fast 为 None 时，先求 fast.next 会直接报 AttributeError！            │
│                                                                                                             │
│ 🎯 翻车机理 (Root Cause):                                                                                   │
│    Python 的逻辑运算符 `and` 具备短路求值特性。必须先校验 `fast` 是否非空，才能安全访问 `fast.next`。       │
│                                                                                                             │
│ 🛡️ 防御口诀 (Invariant):                                                                                   │
│    【先自身，后后继】：必须严格写为 `while fast and fast.next:`                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| 常见陷阱 / 易错反模式 (Buggy Pattern / Traps) | 错误现象与测试用例 (Symptom & Fail Case) | 根本原因分析 (Root Cause) | 防御性修复与循环不变量 (Defensive Fix & Invariant) |
| :--- | :--- | :--- | :--- |
| **`while fast.next and fast:`** | `AttributeError: 'NoneType' object has no attribute 'next'` | 短路求值失效，对 `None` 访问了 `.next` | 严格保持先判自身后判子节点的顺序 `while fast and fast.next:` |
| **混淆左中点与右中点** | 链表折半断开时导致前半段多出一个节点或死循环 | `while fast and fast.next` 会落在第 2 个中点 | 若需断开前截，需用 `while fast.next and fast.next.next:` 定位左中点 |
| **快指针步进写错 `fast = fast.next`** | 慢指针停在链表末尾 | 快慢指针速率相同，失去速率差 | 快指针必须前进 2 步 `fast = fast.next.next` |

---

### ❓ 常见疑难与边界排查 (Boundary FAQs)

* **Q1: 当链表只有 1 个节点 (`[1]`) 时会发生什么？**
  * `fast.next` 为 `None`，`while` 循环一次都不执行，直接返回 `slow`（即节点 `1`），结果正确。
* **Q2: 当链表只有 2 个节点 (`[1, 2]`) 时会发生什么？**
  * 初始：`slow = 1, fast = 1`
  * 循环第 1 次：`slow = 2, fast = None`
  * 循环终止，返回 `slow`（即节点 `2`，第 2 个中点），结果完全正确。
* **Q3: 为什么不需要哨兵哑节点 (`dummyNode`)？**
  * 因为本题只需查询中点指针并返回，不涉及链表头部的修改、插入或删除，因此直接使用 `head` 作为起点最为干净。

---

### 🎨 实例全程推演表 (Complete Dry-Run)

#### 实例 1：奇数长度 `head = [1, 2, 3, 4, 5]`
| 循环轮次 | `slow` 位置 | `fast` 位置 | `fast.next` 状态 | 判定是否继续 |
| :---: | :---: | :---: | :---: | :---: |
| **初始** | `[1]` | `[1]` | `[2]` (有效) | `fast` 与 `fast.next` 均存在 $\rightarrow$ 执行 |
| **第 1 轮** | `[2]` | `[3]` | `[4]` (有效) | `fast` 与 `fast.next` 均存在 $\rightarrow$ 执行 |
| **第 2 轮** | `[3]` | `[5]` | `None` (为空) | `fast.next` 为 `None` $\rightarrow$ 终止循环 |
| **返回值** | `[3]` | — | — | 返回 `slow` 即节点 `[3]` |

#### 实例 2：偶数长度 `head = [1, 2, 3, 4, 5, 6]`
| 循环轮次 | `slow` 位置 | `fast` 位置 | `fast.next` 状态 | 判定是否继续 |
| :---: | :---: | :---: | :---: | :---: |
| **初始** | `[1]` | `[1]` | `[2]` (有效) | `fast` 与 `fast.next` 均存在 $\rightarrow$ 执行 |
| **第 1 轮** | `[2]` | `[3]` | `[4]` (有效) | `fast` 与 `fast.next` 均存在 $\rightarrow$ 执行 |
| **第 2 轮** | `[3]` | `[5]` | `[6]` (有效) | `fast` 与 `fast.next` 均存在 $\rightarrow$ 执行 |
| **第 3 轮** | `[4]` | `None` | — | `fast` 为 `None` $\rightarrow$ 终止循环 |
| **返回值** | `[4]` | — | — | 返回 `slow` 即节点 `[4]` (第 2 个中点) |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 说明与理论支撑 |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 快指针每次走 2 步，最多前进 $\lceil n/2 \rceil$ 次即可遍历完链表；慢指针移动 $\lfloor n/2 \rfloor$ 次；总计访问节点次数不超过 $n$ 次，严格单趟线性时间 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用了 `slow` 和 `fast` 两个辅助指针变量，无任何动态容器内存开销，空间复杂度为严格常数 $\mathcal{O}(1)$。 |
