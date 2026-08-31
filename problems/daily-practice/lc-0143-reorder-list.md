# LeetCode 143. Reorder List (重排链表)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (链表组合拳巅峰三合一 / 寻找中点 + 后半反转 + 双向交错合并)
- **Tags:** Linked List, Two Pointers, Stack, Recursion
- **Corresponding Python File:** [`problems/daily-practice/lc-0143-reorder-list.py`](problems/daily-practice/lc-0143-reorder-list.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** You are given the head of a singly linked-list:
  $$L_0 \rightarrow L_1 \rightarrow \dots \rightarrow L_{n-1} \rightarrow L_n$$
  Reorder the list to be on the following form:
  $$L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \rightarrow L_2 \rightarrow L_{n-2} \rightarrow \dots$$
  * You may not modify the values in the list's nodes. Only nodes themselves may be changed.
* **[CN]** 给定一个单链表 $L$ 的头节点 `head` ，单链表 $L$ 表示为：
  $$L_0 \rightarrow L_1 \rightarrow \dots \rightarrow L_{n-1} \rightarrow L_n$$
  请将其重新排列后变为：
  $$L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \rightarrow L_2 \rightarrow L_{n-2} \rightarrow \dots$$
  * 不能只是单纯的改变节点内部的值，而是需要实际的进行节点指针的交换与重排。

### Constraints / 约束条件
* 链表的长度范围为 $[1, 5 \cdot 10^4]$
* $1 \le \text{Node.val} \le 1000$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 链表三大经典基石三合一 (The Grand Synthesis):                            │
│    • 模块 1 (LC 876): 快慢双指针 2:1 速率定位链表中点 (Find Mid)。           │
│    • 模块 2 (LC 206): 原地三指针滑移反转后半部分链表 (Reverse 2nd Half)。    │
│    • 模块 3 (Zip-Merge): 双指针双向穿针引线交错缝合 (Interleave Merge)。     │
│ 2. 终止条件巧夺天工: while head2.next 的循环守卫，无需显式截断前半链表尾部，│
│    自然完美兼容奇数长度与偶数长度链表。                                     │
│ 3. 空间极致约束: 摒弃线性辅助数组 O(n) 开销，严格达成 O(1) 原地指针重排。    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Linear Structures] ➔ [Linked List] ➔ [Two Pointer]`

### 🧠 链表综合大题算法思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Linked List Grand Synthesis Pattern Lineage (链表三合一组合拳思维谱系)   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Primitive A: LC 876 Middle of the Linked List                              │
│  └─ 功能: 2:1 快慢指针将链表对半剖分。                                      │
│                                ╲                                            │
│  Primitive B: LC 206 Reverse Linked List                                    │
│  └─ 功能: 原地反转后半段链表，使尾部节点变成 head2 可正向遍历。              │
│                                ╱                                            │
│        ▼ [三合一聚变 Twist: 前半正向 + 后半逆向交错合并 (本题 ★)]            │
│  Synthesis:   LC 143 Reorder List                                           │
│  └─ 逻辑: mid = middle(head) -> head2 = reverse(mid) -> zip_merge()         │
│        │                                                                    │
│        ▼ [变体 Twist: 判断前半与反转后的后半是否完全相等]                   │
│  Variant:     LC 234 Palindrome Linked List (回文链表)                      │
│  └─ 逻辑: 同样找中点 + 反转后半段，然后逐一校验 head.val == head2.val。       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：三阶段无缝重组流水线 (Three-Stage Pipeline)

以链表 `[1, 2, 3, 4, 5]` 为例：

```
═════════════════════════════════════════════════════════════════════
阶段 1：快慢指针定位中点 (Find Middle Node - LC 876)
  [1] ──► [2] ──► [3] ──► [4] ──► [5] ──► None
                   ▲
                  mid (slow 停留在 3)

═════════════════════════════════════════════════════════════════════
阶段 2：原地反转后半段链表 (Reverse Second Half - LC 206)
将 [3] ──► [4] ──► [5] 反转为：
  [5] ──► [4] ──► [3] ──► None
   ▲
 head2

原前半段依然为：
  [1] ──► [2] ──► [3]
   ▲
 head

═════════════════════════════════════════════════════════════════════
阶段 3：穿针引线交错缝合 (Zip-Merge Two Halves)
交替连接：head(1) -> head2(5) -> head(2) -> head2(4) -> (3)
最终结果：[1] ──► [5] ──► [2] ──► [4] ──► [3] ──► None
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于你在 `problems/daily-practice/lc-0143-reorder-list.py` 中的标准实现：

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
```

---

### 模块 1：定位链表中点 (`middleNode`)

```python
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```

* **[EN] Action:** Uses fast and slow pointers. When `fast` finishes, `slow` is located at the exact middle node (for odd lengths, the middle; for even lengths, the second middle).
* **[CN] 动作**：快慢双指针求中点。快指针走 2 步，慢指针走 1 步。当快指针到头时，`slow` 精准停在中间节点（奇数停在正中，偶数停在后半段起点）。

---

### 模块 2：反转后半段链表 (`reverseList`)

```python
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
```

* **[EN] Action:** Reverses the second half sublist in-place using the 3-pointer pattern (`pre`, `cur`, `nxt`), returning `pre` as the new head (`head2`).
* **[CN] 动作**：经典三指针原地反转。将从中点开始的后半段链表彻底翻转，返回翻转后的新头节点 `head2`。

---

### 模块 3：交错穿针引线重排 (`reorderList`)

```python
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)

        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2
```

* **[EN] Action:** 
  1. `mid = self.middleNode(head)`: Finds split node.
  2. `head2 = self.reverseList(mid)`: Reverses the tail half into `head2`.
  3. `while head2.next:`: The brilliant termination condition!
     * `nxt = head.next`, `nxt2 = head2.next`: Saves successors of both halves.
     * `head.next = head2`: Links node from 1st half to node from 2nd half.
     * `head2.next = nxt`: Links 2nd half node back to 1st half's successor.
     * `head = nxt`, `head2 = nxt2`: Advances both pointers.
* **[CN] 动作**：
  1. 获取中点 `mid`。
  2. 从 `mid` 开始反转后半段得到 `head2`。
  3. `while head2.next:` **极其精妙的循环终止守卫**：
     * 先分别暂存两半段的下一个节点 `nxt = head.next` 和 `nxt2 = head2.next`。
     * `head.next = head2`：前半段节点指向后半段节点。
     * `head2.next = nxt`：后半段节点连回前半段下一个节点。
     * `head = nxt, head2 = nxt2`：双指针同步向后跳跃。

---

## 5. Interview Simulation & Follow-Up Pivots / 面试官现场追问演练

### 🎤 追问 1：为什么循环终止条件写 `while head2.next:` 就能同时完美处理奇数和偶数长度？

* **面试官意图**：考察对链表重排指针交错合并终态的微观掌控力。
* **微观图解与数学证明**：
  * **奇数情况 (例如 5 个节点 `[1, 2, 3, 4, 5]`)**：
    * 前半：`1 -> 2 -> 3`，后半反转：`5 -> 4 -> 3 -> None`（节点 3 是共享的尾部）。
    * 第 1 轮：`1 -> 5 -> 2`，`head` 移到 2，`head2` 移到 4。
    * 第 2 轮：`2 -> 4 -> 3`，`head` 移到 3，`head2` 移到 3。
    * 此时 `head2.next` 为 `None`，循环结束！节点 3 自动作为末尾，天然形成 `1 -> 5 -> 2 -> 4 -> 3 -> None`！
  * **偶数情况 (例如 4 个节点 `[1, 2, 3, 4]`)**：
    * 前半：`1 -> 2 -> 3`，后半反转：`4 -> 3 -> None`。
    * 第 1 轮：`1 -> 4 -> 2`，`head` 移到 2，`head2` 移到 3。
    * 此时 `head2.next` 为 `None`，循环结束！节点 2 原本就连着 3，天然形成 `1 -> 4 -> 2 -> 3 -> None`！
  * **结论**：无需像传统写法那样显式执行 `prev_mid.next = None` 切断前半段，代码行数更少、逻辑更紧凑！

---

### 🎤 追问 2：如果面试中允许使用额外空间，最直观的数组下标双指针怎么做？

* **线性数组辅助解法**：
  ```python
  # 范式 2: 线性数组双指针重构 (O(n) Space)
  class SolutionArray:
      def reorderList(self, head: Optional[ListNode]) -> None:
          if not head:
              return
          nodes = []
          cur = head
          while cur:
              nodes.append(cur)
              cur = cur.next
          
          i, j = 0, len(nodes) - 1
          while i < j:
              nodes[i].next = nodes[j]
              i += 1
              if i == j:
                  break
              nodes[j].next = nodes[i]
              j -= 1
          nodes[i].next = None
  ```
* **对比**：数组法耗费 $\mathcal{O}(n)$ 空间；而你的三合一解法做到了严格的 $\mathcal{O}(1)$ 常数辅助空间，是面试的最佳满分解法。

---

## 6. The Error Log & Dry-Run / 错题排查与实例推演

### ⚠️ 错题排查与反模式诊断 (The Error Log: Anti-Patterns & Defensive Fixes)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚠️ 反模式 1：交错连接时漏暂存后继导致断链 (Missing Successor Cache During Zip-Merge)                       │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ❌ 错误写法:                                                                                                │
│    head.next = head2  # 致命：head.next 原先指向的节点丢失！后续 head2 无法连回原前半段！                   │
│                                                                                                             │
│ 🎯 翻车机理 (Root Cause):                                                                                   │
│    合并两个链表时，两边的后继指针都需要被修改。必须在建立新连接前同时暂存 `nxt` 与 `nxt2`。                 │
│                                                                                                             │
│ 🛡️ 防御口诀 (Invariant):                                                                                   │
│    【双存双连双步进】：                                                                                     │
│    nxt, nxt2 = head.next, head2.next                                                                        │
│    head.next = head2; head2.next = nxt                                                                      │
│    head, head2 = nxt, nxt2                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| 常见陷阱 / 易错反模式 (Buggy Pattern / Traps) | 错误现象与测试用例 (Symptom & Fail Case) | 根本原因分析 (Root Cause) | 防御性修复与循环不变量 (Defensive Fix & Invariant) |
| :--- | :--- | :--- | :--- |
| **合并时未双暂存 `nxt` 和 `nxt2`** | 链表在第 2 个节点死循环或截断 | 覆盖 `head.next` 导致丢失后续节点引用 | 必须在连线前同时缓存 `nxt = head.next, nxt2 = head2.next` |
| **合并循环条件误写为 `while head2:`** | 末尾形成自环导致死循环 | 偶数长度下最后一步 `3.next = 3` 造成闭环 | 严格使用 `while head2.next:` 作为守卫 |
| **反转起点选错为 `mid.next`** | 奇数中点被遗漏或指针未覆盖 | 导致中点孤立无法被穿插 | 统一将 `mid` 作为后半段起点进行反转 |

---

### 🎨 实例全程推演表 (Complete Dry-Run)

**输入**：`head = [1, 2, 3, 4]` (偶数长度)

| 阶段 | 步骤 | 指针状态 | 拓扑变化说明 |
| :---: | :---: | :---: | :--- |
| **1. 找中点** | 结束 | `slow = [3]` | `mid = [3]`（后半段为 `[3, 4]`） |
| **2. 翻转后半** | 结束 | `head2 = [4]` | 后半反转为 `[4] -> [3] -> None`，前半为 `[1] -> [2] -> [3]` |
| **3. 交错合并** | 第 1 轮 | `head=[1], head2=[4]`<br>`nxt=[2], nxt2=[3]` | `1.next = 4`<br>`4.next = 2`<br>步进：`head=[2], head2=[3]` |
| | 判定 | `head2.next` 为 `None` | 循环终止！ |
| **最终拓扑** | 结束 | `[1] -> [4] -> [2] -> [3] -> None` | **重排结果完全正确！** |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 说明与理论支撑 |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 1. 找中点扫描 $n/2$ 步：$\mathcal{O}(n)$。<br>2. 反转后半段扫描 $n/2$ 步：$\mathcal{O}(n)$。<br>3. 穿针引线合并扫描 $n/2$ 步：$\mathcal{O}(n)$。<br>总时间为 $3 \times (n/2) = \mathcal{O}(n)$ 严格线性时间。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 全程仅修改已有节点的 `next` 指针，只使用了几个指针辅助变量，无额外容器开销，达成严格常数空间 $\mathcal{O}(1)$。 |
