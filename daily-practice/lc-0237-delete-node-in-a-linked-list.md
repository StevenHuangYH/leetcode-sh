# LeetCode 237. Delete Node in a Linked List (删除链表中的节点)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (脑筋急转弯 / 替罪羊覆写 / 借尸还魂)
- **Tags:** Linked List
- **Corresponding Python File:** [`daily-practice/lc-0237-delete-node-in-a-linked-list.py`](daily-practice/lc-0237-delete-node-in-a-linked-list.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** There is a singly-linked list `head` and we want to delete a node `node` in it.
  * You are given the node to be deleted `node`. You will **not be given access** to the first node of `head`.
  * All the values of the linked list are **unique**, and it is guaranteed that the given node `node` is **not the last node** in the linked list.
  * Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
    * The value of the given node should not exist in the linked list.
    * The number of nodes in the linked list should decrease by one.
    * All the values before `node` should be in the same order.
    * All the values after `node` should be in the same order.
* **[CN]** 有一个单链表的 `head`，我们想删除它其中的一个节点 `node`。
  * 给你想删除的节点 `node` 。你将 **无法访问** 第一个节点 `head`。
  * 链表的所有节点的值都是 **唯一** 的，并且可以保证给定的节点 `node` **不是链表中的最后一个节点**。
  * 删除给定的节点。请注意，删除节点并不是指从内存中删除它。这里的意思是：
    * 给定节点的值不应该存在于链表中。
    * 链表中的节点数应该减少 1。
    * `node` 前面的所有值顺序相同。
    * `node` 后面的所有值顺序相同。

### Constraints / 约束条件
* 链表中节点的数目范围是 $[2, 1000]$
* $-1000 \le \text{Node.val} \le 1000$
* 链表中每个节点的值都是 **唯一** 的
* 需要删除的节点 `node` 是链表中的一个 **有效节点** ，且 **不是尾节点**

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 经典破局思维转变 (Paradigm Shift):                                       │
│    • 传统删除: 需要前驱指针 pre，执行 pre.next = cur.next。                 │
│    • 无前驱删除: 将后继节点的值复制过来 (借尸还魂)，然后删除真正的后继节点。 │
│ 2. 替罪羊模型 (The Scapegoat Pattern):                                      │
│    • node.val = node.next.val   (把下一个节点的值偷过来伪装成自己)          │
│    • node.next = node.next.next (把下一个节点架空跳过并移除)                │
│ 3. 约束前提: 题目明确保证 node 不是尾节点 (node.next 绝不为 None)。         │
│ 4. 极致时空: 严格 O(1) 时间，O(1) 空间。                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 链表删除操作思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Linked List Deletion Pattern Lineage (链表删除思维谱系演化树)             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Standard): LC 203 Remove Linked List Elements                     │
│  └─ 不变量 (Invariant): 有 head 指针，哨兵 dummy 维护前驱 pre.next = cur.next│
│        │                                                                    │
│        ▼ [演进 Twist: 倒数第 N 个节点删除，双指针预先拉开间距]              │
│  Level 2 (Two Pointers): LC 19 Remove Nth Node From End of List             │
│  └─ 不变量 (Invariant): 快指针先走 N 步定位待删节点的前驱，再做架空。        │
│        │                                                                    │
│        ▼ [演进 Twist: 无 head 访问权，无法寻址前驱 (本题 ★)]                │
│  Level 3 (Scapegoat): LC 237 Delete Node in a Linked List                   │
│  └─ 不变量 (Invariant): 替罪羊覆写值 + 跨过物理后继节点 (node.val = nxt.val) │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：“替罪羊 / 借尸还魂” ASCII 图解

假设原链表为 `[4] -> [5] -> [1] -> [9]`，需要删除节点 `[5]`（我们只拿到了指向 `[5]` 的指针 `node`，无法访问前面的 `[4]`）：

```
初始状态 (Initial):
    [4] ──► [5] ──► [1] ──► [9] ──► None
             ▲
            node (待删除)

═════════════════════════════════════════════════════════════════════
步骤 1：数值覆写 (node.val = node.next.val)
将下一个节点 [1] 的值复制到当前节点 [5] 上：
    [4] ──► [1] ──► [1] ──► [9] ──► None
             ▲       ▲
            node   node.next

═════════════════════════════════════════════════════════════════════
步骤 2：跳过真正的后继节点 (node.next = node.next.next)
将当前节点直接连接到下下个节点 [9]，架空原先的 [1]：
    [4] ──► [1] ────────────► [9] ──► None
             ▲
            node (现在表现为值 1)

结果：链表变为 [4] -> [1] -> [9]，节点 [5] 被成功“删除”！
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `daily-practice/lc-0237-delete-node-in-a-linked-list.py` 中的标准实现：

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
```

---

```python
        node.val = node.next.val
```

* **[EN] Action:** Copies the value of the succeeding node (`node.next.val`) into the current node (`node.val`).
  * **Mental Model:** The current node disguises itself as the next node.
* **[CN] 动作**：将后继节点的值 `node.next.val` 覆写到当前节点 `node.val`。
  * **思维模型**：当前节点将自身的值替换为下一个节点的值，完成“身份伪装”。

---

```python
        node.next = node.next.next
```

* **[EN] Action:** Bypasses the next node by pointing `node.next` directly to `node.next.next`.
  * **Result:** The original successor node is decoupled from the linked list, effectively deleting it from the sequence.
* **[CN] 动作**：将当前节点的 `next` 指针跨过紧邻的后继节点，直接指向下下个节点 `node.next.next`。
  * **结果**：原本的后继节点被彻底移出链表拓扑，从而使得当前节点成功替换了后继节点并完成了节点删除。

---

## 5. Interview Simulation & Follow-Up Pivots / 面试官现场追问演练

### 🎤 追问 1：如果待删除的节点恰好是链表的最后一个尾节点，这个算法还能工作吗？

* **面试官意图**：考察候选人对边界约束与数据结构物理本质的认知深度。
* **剖析与解答**：
  * **不能工作**。因为如果 `node` 是尾节点，`node.next` 为 `None`，执行 `node.next.val` 会直接抛出 `AttributeError: 'NoneType' object has no attribute 'val'`。
  * **更深层原因**：在**单向链表**中，如果不给头节点 `head`，且待删除节点是尾节点，**在数学上是绝对无法以 $\mathcal{O}(1)$ 时间删除该节点的**（因为没有前驱引用将倒数第二个节点的 `.next` 置为 `None`）。
  * 题目正是因此明确加入了约束：*“保证给定的节点 `node` 不是尾节点”*。

---

### 🎤 追问 2：在 C++ 或底层语言中，这种“替罪羊”写法会有内存泄漏风险吗？

* **面试官意图**：考察工程落地中的内存管理（Memory Management）。
* **工程防线**：
  * 在 Python 中，由于垃圾回收机制（引用计数 Reference Counting），被架空的后继节点因引用归零会被 GC 自动回收。
  * 但在 **C++ / C** 中，直接 `node->next = node->next->next` 会导致原后继节点的堆内存彻底失联并**造成内存泄漏**！
  * **C++ 标准安全写法**：
    ```cpp
    void deleteNode(ListNode* node) {
        ListNode* next_node = node->next;
        node->val = next_node->val;
        node->next = next_node->next;
        delete next_node; // 显式释放被架空节点的内存
    }
    ```

---

### 🎤 追问 3：如果外部其他系统持有了被删节点的指针/引用，这种覆写值的方式会有副作用吗？

* **面试官意图**：考察对“对象同一性 (Identity) 与不变性 (Immutability)”的并发/系统架构认知。
* **副作用分析**：
  * 若外界其他变量持有了 `node` 的引用，在执行覆写后，外界看到的 `node.val` 发生了变化（变成了下一个节点的值），可能破坏调用方的数据一致性。
  * 若外界持有了 `node.next` 的引用，该对象在逻辑上已被删除，但实际仍然独立存活。
  * 因此在严谨的工业级系统设计中，推荐通过包含 `head` 的标准迭代删除保持对象物理实体的纯洁性。

---

## 6. The Error Log & Dry-Run / 错题排查与实例推演

### ⚠️ 错题排查与反模式诊断 (The Error Log: Anti-Patterns & Defensive Fixes)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚠️ 反模式 1：误以为修改局部变量引用即可改变链表拓扑 `node = node.next`                                     │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ❌ 错误写法:                                                                                                │
│    node = node.next  # 致命：这仅仅改变了函数内部局部变量 node 的指向，链表本身的任何节点均未被修改！      │
│                                                                                                             │
│ 🎯 翻车机理 (Root Cause):                                                                                   │
│    Python 中参数传递是“对象的引用传递”（Pass by Object Reference）。重新给形参赋值只是解除了形参绑定，     │
│    没有修改对象属性（如 node.val 或 node.next）。                                                          │
│                                                                                                             │
│ 🛡️ 防御口诀 (Invariant):                                                                                   │
│    【改属性而非改变量】：必须修改 `node.val` 与 `node.next` 属性实体！                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| 常见陷阱 / 易错反模式 (Buggy Pattern / Traps) | 错误现象与测试用例 (Symptom & Fail Case) | 根本原因分析 (Root Cause) | 防御性修复与循环不变量 (Defensive Fix & Invariant) |
| :--- | :--- | :--- | :--- |
| **`node = node.next`** | 链表没有任何改变，评测失败 | 只修改了局部变量指针，未修改链表节点属性 | 必须修改属性 `node.val` 和 `node.next` |
| **误用于尾节点删除** | `AttributeError: 'NoneType' object has no attribute 'val'` | 尾节点的 `node.next` 为 `None` 无法访问 | 前提必须保证 `node.next is not None` |
| **C++ 漏写 `delete next_node`** | 内存持续增长发生 Memory Leak | 跨越指针未显式释放堆内存 | 手动内存管理语言中必须显式 `delete` |

---

### 🎨 实例全程推演表 (Complete Dry-Run)

**输入**：`head = [4, 5, 1, 9]`, `node` 为节点 `[5]`

| 步骤 | 操作 | 当前节点 `node` 状态 | 原后继节点状态 | 链表整体形态 |
| :---: | :--- | :---: | :---: | :--- |
| **初始** | 传入 `node` (值为 5) | `node.val = 5, node.next = Node(1)` | `Node(1).val = 1, next = Node(9)` | `4 -> 5 -> 1 -> 9` |
| **步 1** | `node.val = node.next.val` | `node.val = 1, node.next = Node(1)` | `Node(1).val = 1` | `4 -> 1 -> 1 -> 9` |
| **步 2** | `node.next = node.next.next` | `node.val = 1, node.next = Node(9)` | 引用归零，等待回收 | `4 -> 1 -> 9` |
| **完成** | 退出函数 | — | — | **`[4, 1, 9]` (成功删除 5)** |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 说明与理论支撑 |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(1)$ | 仅执行了 1 次数值赋值与 1 次指针赋值，总共 2 条基本机器指令，耗时严格常数 $\mathcal{O}(1)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 无任何辅助数据结构与函数调用栈开销，原地修改，空间复杂度严格常数 $\mathcal{O}(1)$。 |
