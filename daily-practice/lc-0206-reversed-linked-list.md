# LeetCode 206. Reverse Linked List (反转链表)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (面试超高频 / 链表指针操作基石)
- **Tags:** Linked List, Recursion
- **Corresponding Python File:** [`daily-practice/lc-0206-reversed-linked-list.py`](daily-practice/lc-0206-reversed-linked-list.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a singly linked list, reverse the list, and return the **reversed list's head**.
* **[CN]** 给你单链表的头节点 `head` ，请你反转链表，并返回 **反转后的链表头节点** 。

### Constraints / 约束条件
* 链表中节点的数目范围是 `[0, 5000]`
* $-5000 \le \text{Node.val} \le 5000$
* **进阶 (Follow-up)**：链表可以选用迭代或递归方式完成反转。你能否同时实现这两种方法？

---

## 2. Core Idea & Pointer Progression / 核心解法：双指针/三指针迭代滑移

### 💡 核心机制：三指针协同换向 (`pre`, `cur`, `nxt`)
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

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于你实现的经典迭代代码：

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
```

* **[EN] Action:** Loops while `cur` is not `None`. Caches the next node in temporary variable `nxt`.
  * **Critical Step:** If we immediately modify `cur.next` without caching `cur.next`, we would lose the reference to the remainder of the linked list!
* **[CN] 动作**：当 `cur` 不为空时循环。先用局部变量 `nxt` 暂存 `cur.next`。
  * **关键点**：如果不先存下 `cur.next`，一旦修改了 `cur.next` 的指向，后面的所有节点就彻底断链丢失了！

---

```python
            cur.next = pre
```

* **[EN] Action:** Reverses the pointer of `cur` so that it points backwards to `pre`.
* **[CN] 动作**：将当前节点 `cur` 的 `next` 指针反转，指向前一个节点 `pre`。

---

```python
            pre = cur
            cur = nxt
```

* **[EN] Action:** Advances the pointers one step forward for the next iteration: `pre` moves to `cur`, and `cur` moves to `nxt`.
* **[CN] 动作**：双指针同步右移一步，为下一轮反转做准备：`pre` 前移到当前节点 `cur`，`cur` 前移到暂存的下一个节点 `nxt`。

---

```python
        return pre
```

* **[EN] Action:** When `cur` becomes `None`, the loop ends. `pre` points to the last processed node (the new head of the reversed list). Return `pre`.
* **[CN] 动作**：当 `cur` 为 `None` 遍历结束时，`pre` 精确停留在原链表的末尾节点（即反转后的新头节点），直接返回 `pre`。

---

## 4. Alternative Paradigms & Optimizations / 多种解法深度对比

### 递归解法 (Recursive Approach)
通过递归压栈先走到链表末尾，再在回溯阶段逐层反转指针：

```python
class SolutionRecursive:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归基准终止条件：空节点或单节点无需反转
        if head is None or head.next is None:
            return head
        
        # 递归反转后序子链表，new_head 始终指向原链表的末尾节点
        new_head = self.reverseList(head.next)
        
        # 让 head 的下一个节点反向指向 head (例如 1 -> 2 变为 2 -> 1)
        head.next.next = head
        # 断开原来的正向连接，避免出现环
        head.next = None
        
        return new_head
```

### 迭代法 vs 递归法全方位对比：

| 维度 | 1. 迭代法 (Iterative - 推荐) | 2. 递归法 (Recursive) |
| :--- | :--- | :--- |
| **时间复杂度** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **空间复杂度** | $\mathcal{O}(1)$ (无额外内存开销) | $\mathcal{O}(n)$ (系统函数调用栈深度为 $n$) |
| **栈溢出风险** | 无（任意大长度链表均可安全处理） | 当链表过长时可能导致 `RecursionError: maximum recursion depth exceeded` |
| **代码思维** | 自前往后依次换向（贪心滑移） | 自后往前在回溯阶段换向（分治归纳） |

---

## 5. Step-by-Step Walkthrough with Examples / 样例图解分析

### 样例 1: `head = [1, 2, 3]`

* **初始**：`pre = None`, `cur = Node(1)`
* **第 1 轮**：
  * `nxt = Node(2)`
  * `Node(1).next = None`
  * `pre = Node(1)`, `cur = Node(2)`
* **第 2 轮**：
  * `nxt = Node(3)`
  * `Node(2).next = Node(1)`
  * `pre = Node(2)`, `cur = Node(3)`
* **第 3 轮**：
  * `nxt = None`
  * `Node(3).next = Node(2)`
  * `pre = Node(3)`, `cur = None`
* **终止**：`cur == None`，返回 `pre = Node(3)`。
* **链表结构**：`3 -> 2 -> 1 -> None`，完全正确！

---

## 6. Key FAQs & Edge Cases / 核心答疑与边界分析

### Q1: 空链表 (`head = None`) 和 单节点链表 (`head = [1]`) 是否需要特殊处理？
* **空链表**：`cur = head = None`，`while cur:` 条件直接不成立，直接返回 `pre = None`，完美处理。
* **单节点链表**：进入循环 1 次，`Node(1).next = None`，`pre = Node(1)`，返回 `pre`，完全正确。

### Q2: 为什么 `cur.next = pre` 不会修改 `nxt`？
* 因为在执行 `cur.next = pre` 之前，`nxt = cur.next` 已经将下一个节点的引用赋值给了独立变量 `nxt`。改变 `cur.next` 的属性值并不会改变 `nxt` 所指向的对象实体。

---

## 7. Complexity Analysis / 复杂度分析

| 指标 | 复杂度 | 详解 |
| :--- | :--- | :--- |
| **时间复杂度 (Time)** | $\mathcal{O}(n)$ | 线性单遍扫描链表，每个节点恰好被访问和修改指针一次，其中 $n$ 为链表节点总数。 |
| **空间复杂度 (Space)** | $\mathcal{O}(1)$ | 仅使用 `pre`, `cur`, `nxt` 三个局部指针变量，无任何额外堆栈内存消耗。 |
