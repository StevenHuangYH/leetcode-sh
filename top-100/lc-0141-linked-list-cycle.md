# LeetCode 141. Linked List Cycle (环形链表)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (快慢双指针经典原语 / 龟兔赛跑闭环相遇)
- **Tags:** Linked List, Two Pointers, Hash Table
- **Corresponding Python File:** [`top-100/lc-0141-linked-list-cycle.py`](top-100/lc-0141-linked-list-cycle.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given `head`, the head of a singly linked list, determine if the linked list has a cycle in it.
  * There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.
  * Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
  * Return `true` if there is a cycle in the linked list. Otherwise, return `false`.
* **[CN]** 给你一个链表的头节点 `head` ，判断链表中是否有环。
  * 如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。
  * 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递**。仅仅是为了标识链表的实际情况。
  * 如果链表中存在环，则返回 `true` ；否则，返回 `false` 。

### Constraints / 约束条件
* 链表中节点的数目范围是 $[0, 10^4]$
* $-10^5 \le \text{Node.val} \le 10^5$
* `pos` 为 `-1` 或者链表中的一个 **有效索引**。
* **进阶 (Follow-up)**：你能否使用 $\mathcal{O}(1)$（即，常量）内存解决此问题？

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 相对运动与速率差模型: slow 步长为 1，fast 步长为 2。                      │
│ 2. 闭环必遇数学定理: fast 相对 slow 的相对追及速度恒为 2 - 1 = 1 节点/步。  │
│    在周长为 C 的环内，两者相对距离每步严格递减 1，绝不会出现“跨越错过”。    │
│ 3. 对象同一性判断 (Object Identity): 必须使用 is 或 id() 比对内存地址，    │
│    绝不能仅比对节点数值 (.val)，防止不同节点的数值重复引发误判。            │
│ 4. 双重防越界守卫: while fast and fast.next（防 None.next 异常）。         │
│ 5. 空间极致约束: 摒弃哈希表额外 O(n) 开销，达成进阶严格 O(1) 常数内存。     │
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
│        ▼ [演进 Twist: 链表尾部成环，快慢指针进入闭环追及]                   │
│  Level 2 (Collision): LC 141 Linked List Cycle (★ 本题)                     │
│  └─ 不变量 (Invariant): 相对速度为 1，闭环内有限步内必在同一节点重合相遇。    │
│        │                                                                    │
│        ▼ [演进 Twist: 不仅要判环，还要数学推导寻找【入环第一个节点】]       │
│  Level 3 (Math Loc):  LC 142 Linked List Cycle II                           │
│  └─ 不变量 (Invariant): 相遇后 head 与 slow 同速单步前移，相遇点即为入环点。 │
│        │                                                                    │
│        ▼ [演进 Twist: 将隐式数组映射为链表，利用 Floyd 判环找重复数]         │
│  Level 4 (Array Graph): LC 287 Find the Duplicate Number                    │
│  └─ 不变量 (Invariant): 将 nums[i] 视作 next 指针，在值域图中寻找环入口。     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：Floyd 判圈算法（龟兔赛跑）数学证明

为什么快指针每次走 2 步、慢指针走 1 步，两者在有环时**必定相遇且绝不会跳过彼此**？

#### 📐 严格相对运动学证明 (Proof of Inevitable Collision)
1. **进入环路阶段**：
   * 设链表头部到环起点的非环长度为 $a$，环周长为 $b$。
   * 慢指针走 $a$ 步到达入环点时，快指针已经走了 $2a$ 步，早已在环内循环运动。
2. **环内追及阶段**：
   * 此时设快指针领先慢指针的距离（按顺时针方向追击）为 $d$（$0 \le d < b$）。
   * 将慢指针 `slow` 视为**静止参照系**，快指针 `fast` 每次相对慢指针以速度 $v_{\text{rel}} = 2 - 1 = 1$ 个节点/步进行靠近。
   * 每经过一次循环迭代，快慢指针之间的环内追及距离从 $d \rightarrow d - 1 \rightarrow d - 2 \dots \rightarrow 0$。
3. **必然重合结论**：
   * 因为相对步长差是**严格连续的整数 1**，步长不会产生跳跃。
   * 追及距离 $d$ 必然会在最多 $b$ 次循环内精准减小到 $0$。
   * 因此快慢指针**必定在环内某节点发生指针重合（`fast is slow`）**，绝不可能发生“快指针跨过慢指针却不相遇”的情况。

---

### 🎨 动态指针滑移与闭环追及 ASCII 图解

以链表 `head = [3, 2, 0, -4]`, `pos = 1`（尾部 `-4` 连回节点 `2`，非环长 $a=1$，环长 $b=3$）为例：

```
链表拓扑形态:
  [3] ──► [2] ──► [0]
           ▲       │
           │       ▼
         [-4] ◄────┘

═════════════════════════════════════════════════════════════════════
初始状态 (Initial):
slow 在 [3], fast 在 [3]

Step 1:
slow 前进 1 步 ──► 到达 [2] (入环点)
fast 前进 2 步 ──► 到达 [0]
此时两者均在环内，追及距离 d = 2

Step 2:
slow 前进 1 步 ──► 到达 [0]
fast 前进 2 步 ──► 从 [0] -> [-4] -> [2]
此时 fast 在 [2], slow 在 [0]，追及距离 d = 1

Step 3:
slow 前进 1 步 ──► 到达 [-4]
fast 前进 2 步 ──► 从 [2] -> [0] -> [-4]
此时 slow=[ -4 ], fast=[ -4 ] ──► fast is slow 为 True！
🎉 判定成功，返回 True！
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `top-100/lc-0141-linked-list-cycle.py` 中的标准实现：

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
```

---

```python
        slow = head
        fast = head
```

* **[EN] Action:** Initializes both `slow` and `fast` pointers at `head`.
  * **Role:** `slow` advances 1 step per cycle; `fast` advances 2 steps per cycle.
* **[CN] 动作**：将快慢两指针同时初始化在链表头节点 `head`。
  * **作用**：`slow` 为慢速巡检指针（每次 1 步）；`fast` 为倍速探针（每次 2 步）。

---

```python
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                return True
```

* **[EN] Action:** Traverses the linked list while guarding against null-pointer errors:
  1. `while fast and fast.next:`: Ensures both `fast` and `fast.next` exist so `fast.next.next` is safe.
  2. `slow = slow.next`: Slow moves 1 node forward.
  3. `fast = fast.next.next`: Fast moves 2 nodes forward.
  4. `if fast is slow:`: Checks reference identity (points to the exact same memory address). If true, a cycle is detected immediately.
* **[CN] 动作**：循环推进双指针并进行碰撞检测：
  1. `while fast and fast.next:`：防越界守卫。确保 `fast` 及其后继节点均存在，避免访问 `fast.next.next` 时抛出空指针异常。
  2. `slow = slow.next`：慢指针单步步进。
  3. `fast = fast.next.next`：快指针双步步进。
  4. `if fast is slow:`：内存地址同一性校验。若两指针指向同一个节点对象，则证实存在环，立即返回 `True`。

---

```python
        return False
```

* **[EN] Action:** If `fast` or `fast.next` becomes `None`, the list has reached an end (linear structure with no cycle), so return `False`.
* **[CN] 动作**：如果 `while` 循环正常结束（即快指针触底到达 `None`），说明链表是有尽头的线性无环结构，返回 `False`。

---

## 5. Interview Simulation & Follow-Up Pivots / 面试官现场追问演练

### 🎤 追问 1：如果不用快慢双指针，最直观的哈希表解法如何写？两种解法如何做架构权衡？

* **面试官意图**：考察候选人对时空权衡（Time-Space Trade-off）的理解。
* **哈希表解法实现**：
  ```python
  # 范式 2: 哈希表记录已访问节点集合 (Hash Set)
  class SolutionHashSet:
      def hasCycle(self, head: Optional[ListNode]) -> bool:
          visited = set()
          cur = head
          while cur:
              if cur in visited:
                  return True
              visited.add(cur)
              cur = cur.next
          return False
  ```
* **架构权衡对比**：
  * 哈希表法逻辑极为直观，但需要 $\mathcal{O}(n)$ 辅助内存，违背进阶 $\mathcal{O}(1)$ 常数空间约束。
  * 快慢指针法将空间复杂度从 $\mathcal{O}(n)$ 降为严格的 $\mathcal{O}(1)$，且单趟遍历性能更优。

---

### 🎤 追问 2：为什么判断相遇必须用 `fast is slow`，而不能写 `fast.val == slow.val`？

* **面试官意图**：考察对 Python 引用机制与数据结构本质的理解（Identity vs. Equality）。
* **核心解析**：
  * 链表中完全可以存在**数值相同但处于不同位置的两个独立节点**（例如 `1 -> 1 -> 1 -> None`）。
  * 若写 `fast.val == slow.val`，当快指针走到第 3 个节点（值为 1）、慢指针走到第 2 个节点（值为 1）时，会触发**错误判定为有环（False Positive）**！
  * `is` 操作符比对的是**底层内存地址 `id(fast) == id(slow)`**，只有指针真正指在同一个物理节点上时才成立。

---

### 🎤 追问 3：如果面试官进一步要求“找出环的入口节点 (LC 142)”，你如何拓展？

* **面试官意图**：考察知识体系的横向迁移能力。
* **破局推导**：
  * 设头到入环点距离为 $a$，入环点到初次相遇点距离为 $b$，环剩余长度为 $c$（环长为 $b + c$）。
  * 相遇时：$s = a + b$，$f = 2(a + b) = a + k(b + c) + b$。
  * 化简得：$a = (k - 1)(b + c) + c$。
  * **结论**：相遇后，将一个指针重置回 `head`，另一个指针保持在相遇点，两指针每次同速走 1 步，**再次相遇处必为入环点**！

---

## 6. The Error Log & Dry-Run / 错题排查与实例推演

### ⚠️ 错题排查与反模式诊断 (The Error Log: Anti-Patterns & Defensive Fixes)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚠️ 反模式 1：值比对 (Value Equality) 误替 内存地址同一性比对 (Object Identity)                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ❌ 错误写法:                                                                                                │
│    if fast.val == slow.val:  # 致命：对于无环但存在重复数值的链表 [1, 1, 1] 会误判为有环！                 │
│        return True                                                                                          │
│                                                                                                             │
│ 🎯 翻车机理 (Root Cause):                                                                                   │
│    节点值相同并不代表是同一个节点。只有指针在内存堆空间中指向同一物理地址时，才是拓扑上的同一个节点。       │
│                                                                                                             │
│ 🛡️ 防御口诀 (Invariant):                                                                                   │
│    【判环比地址，绝不比数值】：严格使用 `if fast is slow:` 或 `if id(fast) == id(slow):`                   │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| 常见易错反模式 (Buggy Anti-Pattern) | 翻车现象与症状 (Symptom) | 深层翻车机理 (Root Cause) | 防御性修复策略 (Defensive Invariant) |
| :--- | :--- | :--- | :--- |
| **`if fast.val == slow.val:`** | 重复值无环链表报出错误的 `True` | 误将“节点值相等”当作“拓扑节点重合” | 必须使用对象同一性判断 `if fast is slow:` |
| **`while fast.next and fast:`** | `AttributeError: 'NoneType' object has no attribute 'next'` | 短路求值顺序错误，对 `None` 访问了 `.next` | 严格保持先判自身后判子节点的顺序 `while fast and fast.next:` |
| **快慢指针初始错位未调终止条件** | 初始时若 `fast = head.next` 会漏掉单节点自环 | 初始指针状态与循环守卫不匹配 | 推荐初始两指针都在 `head`，在循环体内做 `if fast is slow:` |

---

### ❓ 常见疑难与边界排查 (Boundary FAQs)

* **Q1: 链表为空 (`head = None`) 时会发生什么？**
  * `slow = None, fast = None`，`while fast and fast.next:` 直接判定为 False，跳出循环返回 `False`，完全正确。
* **Q2: 链表仅有 1 个无环节点 (`[1]`) 时会发生什么？**
  * `fast.next` 为 `None`，`while` 循环不执行，直接返回 `False`，完全正确。
* **Q3: 链表仅有 1 个自环节点 (`[1] -> [1]`) 时会发生什么？**
  * 步 1：`slow` 前进一步仍在节点 1，`fast` 前进两步也仍在节点 1，`fast is slow` 成立，返回 `True`，完全正确。

---

### 🎨 实例全程推演表 (Complete Dry-Run)

**输入**：`head = [3, 2, 0, -4]`, `pos = 1`（节点 `-4` 连向节点 `2`）

| 轮次 | `slow` 位置 | `fast` 位置 | `fast.next` 存在? | `fast is slow` 判定 | 动作说明 |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **初始** | `[3]` | `[3]` | `[2]` (存在) | — | 双指针在起点就位 |
| **第 1 轮** | `[2]` | `[0]` | `[-4]` (存在) | False (`[0] != [2]`) | `slow` 走 1 步进环，`fast` 走 2 步进环 |
| **第 2 轮** | `[0]` | `[2]` | `[0]` (存在) | False (`[2] != [0]`) | `fast` 在环内追击，相对距离缩减至 1 |
| **第 3 轮** | `[-4]` | `[-4]` | `[2]` (存在) | **True (`[-4] is [-4]`)** | **快慢指针在节点 `[-4]` 精准碰撞！** |
| **返回值** | — | — | — | — | 立即返回 **`True`** |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 说明与理论支撑 |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 1. **无环情况**：快指针每次走 2 步，在 $\lfloor n/2 \rfloor$ 步内直接走到链表末尾，耗时 $\mathcal{O}(n)$。<br>2. **有环情况**：慢指针在走完非环部分 $a$ 步后进环，进环后最多在 1 圈周长 $b$ 步内与快指针相遇；总步数 $a + b = n \le \mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅维护了 `slow` 与 `fast` 两个节点指针变量，没有任何集合、哈希表或动态数组等辅助容器开销，满足进阶严格常数内存 $\mathcal{O}(1)$。 |
