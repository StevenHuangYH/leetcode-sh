# LeetCode 92. Reverse Linked List II (反转链表 II)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (高频面试经典题 / 链表局部区间反转与哨兵节点)
- **Tags:** Linked List
- **Corresponding Python File:** [`daily-practice/lc-0092-reversed-linked-list-2.py`](daily-practice/lc-0092-reversed-linked-list-2.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the **reversed list**.
* **[CN]** 给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 **反转后的链表** 。

### Constraints / 约束条件
* 链表中节点数目为 `n`
* $1 \le n \le 500$
* $-500 \le \text{Node.val} \le 500$
* $1 \le left \le right \le n$
* **进阶 (Follow-up)**：你能否使用一趟扫描 ($\mathcal{O}(n)$ 时间，$\mathcal{O}(1)$ 空间) 解决此问题？

---

## 2. Core Idea & Pointer Progression / 核心解法思路与指针演进

### 💡 核心机制：哨兵哑节点 (`dummyNode`) + 局部三指针反转 (`p0`, `pre`, `cur`, `nxt`)

反转链表局部区间 $[left, right]$ 的核心挑战在于：**如何精准定位反转区间前驱，并在局部反转完成后将反转后的子链表无缝缝合回原链表**。

整个算法分为三步：
1. **阶段 1：定位反转前驱 `p0`**
   * 创建哨兵节点 `dummyNode`（`dummyNode.next = head`），从 `dummyNode` 出发向前走 `left - 1` 步。
   * 停止时，`p0` 恰好停在待反转区间的 **前一个节点**（即第 $left - 1$ 个节点）。
2. **阶段 2：局部标准链表反转（共 $right - left + 1$ 个节点）**
   * 从 `cur = p0.next` 开始，使用经典三指针滑移换向（`pre = None`），循环执行 $right - left + 1$ 次。
   * 循环结束后，`pre` 指向反转子区间的 **新头节点**（原第 $right$ 个节点），`cur` 指向反转子区间的 **后继节点**（原第 $right + 1$ 个节点）。
3. **阶段 3：四点缝合（重连边界指针）**
   * 注意此时 `p0.next` 依然指向原区间的第一个节点（反转后的尾节点！）。
   * `p0.next.next = cur`：将反转后的子链表尾部连接到右侧未反转的后缀链表 `cur`。
   * `p0.next = pre`：将前驱节点 `p0` 连接到反转后的子链表新头部 `pre`。

---

### 🎨 动态指针滑移全流程 ASCII 图解

以链表 `[1, 2, 3, 4, 5]`, `left = 2`, `right = 4` 为例：

```
初始状态 (Initial State):
dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> None
  ↑
 p0 (从 dummy 出发走 left - 1 = 1 步)

阶段 1：定位 p0
dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> None
          ↑      ↑
         p0     cur (p0.next)
                pre = None

阶段 2：局部反转 (执行 right - left + 1 = 3 次换向)
第 1 次: [2] -> None, pre=[2], cur=[3]
第 2 次: [3] -> [2] -> None, pre=[3], cur=[4]
第 3 次: [4] -> [3] -> [2] -> None, pre=[4], cur=[5]

反转结束后的指针分布:
               pre (新子头)     cur (未反转后缀)
                ↓                ↓
dummy -> [1]   [4] -> [3] -> [2] [5] -> None
          ↑                   ↑
         p0                p0.next (原子头/新子尾)

阶段 3：缝合链表 (必须按顺序操作)
Step 3.1: p0.next.next = cur  ==>  [2].next = [5]
Step 3.2: p0.next = pre       ==>  [1].next = [4]

最终结果 (Final List):
dummy -> [1] -> [4] -> [3] -> [2] -> [5] -> None
返回 dummyNode.next 即为 [1, 4, 3, 2, 5]
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `daily-practice/lc-0092-reversed-linked-list-2.py` 中的经典实现：

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
```

---

```python
        dummyNode = ListNode(next = head)
        p0 = dummyNode
```

* **[EN] Action:** Creates a sentinel `dummyNode` pointing to `head` and sets pointer `p0` to `dummyNode`.
  * **Why `dummyNode` is essential:** If $left = 1$, the original `head` is part of the reversed segment and will be replaced. `dummyNode` eliminates edge-case conditionals and provides a stable anchor.
* **[CN] 动作**：创建指向 `head` 的哨兵哑节点 `dummyNode`，并将 `p0` 指针初始化在 `dummyNode`。
  * **为什么必须用哨兵节点？** 当 $left = 1$ 时，原头节点自身就在反转区间内，反转后头节点会发生改变。使用 `dummyNode` 可以统一所有情况，避免针对 `left == 1` 单独写冗长的分支特判。

---

```python
        for _ in range(left - 1):
            p0 = p0.next
```

* **[EN] Action:** Advances `p0` exactly $left - 1$ steps from `dummyNode`.
  * **Result:** `p0` arrives precisely at the node immediately before index $left$ (the $(left - 1)$-th node).
* **[CN] 动作**：让 `p0` 从 `dummyNode` 出发向前移动 $left - 1$ 次。
  * **结果**：`p0` 精确停在反转区间的前驱节点（第 $left - 1$ 个节点）。

---

```python
        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
```

* **[EN] Action:** Standard in-place linked list reversal of length $right - left + 1$.
  * Initializes `pre = None` and `cur = p0.next` (the start of the segment to be reversed).
  * Iterates $right - left + 1$ times, caching `nxt = cur.next`, reversing `cur.next = pre`, then advancing `pre` and `cur`.
  * At loop termination, `pre` points to the new head of the reversed subsegment (node $right$), and `cur` points to the successor node (node $right + 1$).
* **[CN] 动作**：对长度为 $right - left + 1$ 的子链表执行标准局部迭代反转。
  * 初始化 `pre = None`，`cur = p0.next`（待反转区间的第一个节点）。
  * 循环 $right - left + 1$ 次：暂存 `nxt = cur.next`，反转指针 `cur.next = pre`，双指针前移 `pre = cur`，`cur = nxt`。
  * 循环结束时，`pre` 指向反转后的局部新头节点（原第 $right$ 个节点），`cur` 指向原第 $right + 1$ 个节点（后继节点）。

---

```python
        p0.next.next = cur
        p0.next = pre
        return dummyNode.next
```

* **[EN] Action:** Stitches the reversed sublist back into the main list:
  1. `p0.next` still references the original first node (which is now the tail of the reversed sublist). Setting `p0.next.next = cur` connects the reversed sublist tail to the remaining unreversed suffix `cur`.
  2. `p0.next = pre` connects the prefix node `p0` to the new sublist head `pre`.
  3. Returns `dummyNode.next` as the new head of the entire list.
* **[CN] 动作**：将反转后的子链表缝合回原链表：
  1. 此时 `p0.next` 依然保留着反转前的第一个节点（反转后的尾节点！）。执行 `p0.next.next = cur` 将反转子链表的尾部接上未反转的后半截 `cur`。
  2. 执行 `p0.next = pre` 将前驱节点 `p0` 指向反转子链表的新头部 `pre`。
  3. 返回 `dummyNode.next`，即为完整的新链表头节点。

---

## 4. Alternative Paradigms & Comparative Study / 算法范式对比

```
范式 1: 局部双指针反转 + 边界缝合 (当前解法)      范式 2: 头插法 / 穿针引线法 (Head-Insertion)
[1] -> [2] -> [3] -> [4] -> [5]                [1] -> [2] -> [3] -> [4] -> [5]
       └──反转 sublist──┘                             把 [3], [4] 依次拔出插入到 [1] 之后
```

| 维度 | 范式 1：局部反转 + 边界缝合 (推荐) | 范式 2：头插法 (穿针引线) | 范式 3：递归分治法 (Recursion) |
| :--- | :--- | :--- | :--- |
| **核心机制** | 定位 `p0`，标准反转区间，最后两步缝合 | 保持 `p0` 和 `cur` 不动，每次将 `nxt` 移到 `p0` 后面 | 递归缩小规模至反转前 $N$ 个节点 (`reverseN`) |
| **代码直观度** | ⭐️⭐️⭐️⭐️⭐️ (复用 LC 206 标准反转模版) | ⭐️⭐️⭐️ (指针交错修改，需注意指针顺序) | ⭐️⭐️⭐️ (调用栈深，理解稍抽象) |
| **时间复杂度** | $\mathcal{O}(n)$ (一趟扫描) | $\mathcal{O}(n)$ (一趟扫描) | $\mathcal{O}(n)$ |
| **空间复杂度** | $\mathcal{O}(1)$ (严格常数级额外空间) | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ (系统递归调用栈) |

### 范式 2：头插法 (Head-Insertion) 参考代码

```python
class SolutionHeadInsert:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next
        
        cur = p0.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = p0.next
            p0.next = nxt
            
        return dummy.next
```

---

## 5. Key FAQs & Edge Cases / 常见疑难与边界排查

### ❓ Q1: 为什么先执行 `p0.next.next = cur`，再执行 `p0.next = pre`？顺序反了会怎样？
* **解答**：
  * `p0.next` 存储的是反转前子区间的首节点（反转后变成了尾节点）。
  * 如果先执行 `p0.next = pre`，`p0.next` 会被立刻覆盖为 `pre`（新头节点），此时你就彻底丢失了对原尾节点的引用，导致无法再执行 `p0.next.next = cur`！
  * **口诀**：先连尾部（`p0.next.next = cur`），再连头部（`p0.next = pre`）。

---

### ❓ Q2: 当 $left = 1$ 且 $right = n$（整体完全反转）时，算法如何运转？
* `p0` 停留在 `dummyNode`（`range(0)` 不移动）。
* 反转子链表长度为 $n$，整条链表被完全反转。
* 循环结束时 `pre` 为原尾节点，`cur` 为 `None`。
* `p0.next.next = cur` 将原头节点指向 `None`；`p0.next = pre` 将 `dummyNode.next` 指向新头节点 `pre`。
* 返回 `dummyNode.next`，结果完全正确。

---

### ❓ Q3: 当 $left == right$（单节点反转）时会发生什么？
* 循环次数为 $right - left + 1 = 1$。
* 循环仅执行 1 次：`nxt = cur.next`, `cur.next = None`, `pre = cur`, `cur = nxt`。
* `p0.next.next = cur` 重新接回原后继节点，`p0.next = pre` 重新接回当前节点。
* 链表结构保持原样不变，零冗余开销。

---

## 6. Complete Step-by-Step Dry-Run / 实例全程推演

**输入**：`head = [1, 2, 3, 4, 5]`, `left = 2`, `right = 4`

| 步骤 | 变量状态 (`p0`, `pre`, `cur`, `nxt`) | 链表结构与指针变化 | 说明 |
| :---: | :--- | :--- | :--- |
| **初始** | `p0 = dummy`, `head = [1]` | `dummy -> [1] -> [2] -> [3] -> [4] -> [5]` | 创建哨兵节点 |
| **定位** | `p0 = [1]` | `p0` 停在节点 `1` | 移动 $left - 1 = 1$ 步 |
| **准备** | `pre = None`, `cur = [2]` | 子区间起点为 `[2]` | 准备反转 3 个节点 |
| **循环 1** | `pre = [2]`, `cur = [3]`, `nxt = [3]` | `[2] -> None` | 反转节点 2 |
| **循环 2** | `pre = [3]`, `cur = [4]`, `nxt = [4]` | `[3] -> [2] -> None` | 反转节点 3 |
| **循环 3** | `pre = [4]`, `cur = [5]`, `nxt = [5]` | `[4] -> [3] -> [2] -> None` | 反转节点 4 |
| **缝合 1** | `p0.next.next = cur` | `[2].next = [5]` | 将尾部 `[2]` 连到 `[5]` |
| **缝合 2** | `p0.next = pre` | `[1].next = [4]` | 将前驱 `[1]` 连到 `[4]` |
| **返回** | `dummyNode.next` | `[1] -> [4] -> [3] -> [2] -> [5]` | 成功返回目标链表 |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 说明与理论支撑 |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 算法仅需遍历链表一次（定位 $p_0$ 耗时 $\mathcal{O}(left)$，反转子区间耗时 $\mathcal{O}(right - left)$，缝合耗时 $\mathcal{O}(1)$），总遍历节点数不超过 $right \le n$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用了 `dummyNode`、`p0`、`pre`、`cur`、`nxt` 等常数个指针变量，未开辟额外堆内存。 |
