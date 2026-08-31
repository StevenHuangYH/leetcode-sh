# LeetCode 19. Remove Nth Node From End of List (删除链表的倒数第 N 个结点)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (经典双指针 / 滑动固定间距窗 / 哨兵虚拟头节点)
- **Tags:** Linked List, Two Pointers
- **Corresponding Python File:** [`top-100/lc-0019-remove-nth-node-from-end-of-list.py`](top-100/lc-0019-remove-nth-node-from-end-of-list.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a linked list, remove the $n^{\\text{th}}$ node from the end of the list and return its head.
* **[CN]** 给你一个链表，删除链表的倒数第 $n$ 个结点，并且返回链表的头结点。

### Constraints / 约束条件
* 链表中结点的数目为 `sz`
* $1 \\le sz \\le 30$
* $0 \\le \\text{Node.val} \\le 100$
* $1 \\le n \\le sz$

### Follow up / 进阶思考
* Could you do this in one pass? / 你能尝试使用一趟扫描实现吗？

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 核心挑战 (Core Challenge):                                               │
│    • 单向链表无法直接倒序寻址，若要删除目标节点，必须定位到其【前驱节点】。 │
│ 2. 哨兵节点 (Sentinel Dummy Node):                                         │
│    • 处理头节点可能被删除的极端边界 (n == sz)。                             │
│    • 统一所有节点的删除逻辑: left.next = left.next.next。                   │
│ 3. 固定间距双指针 (Fixed-Gap Two Pointers):                                 │
│    • 让 right 先从 dummy 出发走 n 步，与 left 之间形成长度为 n 的恒定间距。  │
│    • 随后 left 与 right 同步前进，直至 right 抵达链表最后一个节点。         │
│    • 此时 left 恰好停在【待删除节点的前驱节点】上！                         │
│ 4. 极致时空: 严格一趟扫描 O(L) 时间，O(1) 额外空间。                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Linear Structures] ➔ [Linked List] ➔ [Two Pointer]`

### 🧠 链表快慢/双指针思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Linked List Dual Pointers Pattern Lineage (链表双指针思维谱系演化树)     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Basic Traversal): LC 203 Remove Linked List Elements              │
│  └─ 核心概念: 哨兵 dummy 统一前驱指针删除操作 (pre.next = cur.next)。        │
│        │                                                                    │
│        ▼ [演进 Twist: 倒数定位，引入固定间距窗口 (本题 ★)]                  │
│  Level 2 (Fixed Gap): LC 19 Remove Nth Node From End of List                │
│  └─ 不变量 (Invariant): right 领先 n 步，right 到末尾时 left 恰为待删前驱。 │
│        │                                                                    │
│        ▼ [演进 Twist: 倍速比例窗口 (2:1 速度差)]                            │
│  Level 3 (Proportional Gap): LC 876 Middle of the Linked List               │
│  └─ 不变量 (Invariant): fast 走 2 步，slow 走 1 步，fast 结束时 slow 在中点。│
│        │                                                                    │
│        ▼ [演进 Twist: 拓扑成环与碰撞推导]                                   │
│  Level 4 (Cycle Detection): LC 141 & LC 142 Linked List Cycle I & II         │
│  └─ 不变量 (Invariant): 快慢指针同余相遇，二次同速相遇定位环入口 (a = c)。 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 数学证明与核心机制：为什么 `right` 走 $n$ 步后同步走能准确定位前驱？

设链表节点总数为 $L$。我们将虚拟哨兵节点 `dummy` 记为索引 $0$，链表原节点依次为索引 $1, 2, \\dots, L$。

```
dummy ──► [Node 1] ──► [Node 2] ──► ... ──► [Node L-n+1] ──► ... ──► [Node L] ──► None
  0           1            2                  (待删除)                   L
                                                  ▲
                                         倒数第 n 个节点
```

1. **待删除节点的正数位置**：倒数第 $n$ 个节点是正数第 $L - n + 1$ 个节点。
2. **待删除节点的前驱位置**：前驱节点是正数第 $(L - n + 1) - 1 = L - n$ 个节点。
3. **两指针相对位移推导**：
   * `right` 从 `dummy` (索引 0) 先走 $n$ 步，到达索引 $n$。
   * 此时 `left` 停在 `dummy` (索引 0)，两指针的索引差恒为 $n$（即 $\\text{index}(right) - \\text{index}(left) = n$）。
   * 当 `while right.next:` 终止时，`right` 恰好停在最后一个节点（索引 $L$）。
   * 代入不变量公式：
     $$\\text{index}(left) = \\text{index}(right) - n = L - n$$
   * 索引 $L - n$ 对应的正是 **待删除节点的前驱节点**！
   * 直接执行 `left.next = left.next.next` 即可安全架空并剔除目标节点。

---

### 🎨 ASCII 动态推演过程图解

以 `head = [1, 2, 3, 4, 5]`, $n = 2$ 为例（删除倒数第 2 个节点 `4`）：

```
Step 0: 构建 dummy 哨兵节点，left 与 right 均初始化在 dummy
    dummy ──► [1] ──► [2] ──► [3] ──► [4] ──► [5] ──► None
      ▲
  left, right

═════════════════════════════════════════════════════════════════════
Step 1: right 先向前移动 n = 2 步，拉开间距
    dummy ──► [1] ──► [2] ──► [3] ──► [4] ──► [5] ──► None
      ▲                 ▲
    left              right (先行 2 步，停在 [2])

═════════════════════════════════════════════════════════════════════
Step 2: left 与 right 同时向后平移，直到 right.next 为 None
    平移 1 步: left -> [1], right -> [3]
    平移 2 步: left -> [2], right -> [4]
    平移 3 步: left -> [3], right -> [5] (此时 right.next is None，循环结束)

    dummy ──► [1] ──► [2] ──► [3] ──► [4] ──► [5] ──► None
                                ▲                 ▲
                              left              right (到达末尾)

═════════════════════════════════════════════════════════════════════
Step 3: 架空删除 left.next (节点 [4])
    left.next = left.next.next

    dummy ──► [1] ──► [2] ──► [3] ───────┐
                                         │  (节点 4 被跨过架空)
                                         ▼
                                        [5] ──► None

Step 4: 返回 dummy.next (即新的头节点 [1])
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件中的实现进行逐行深入解析：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 创建哨兵哑节点，其 next 指向链表头节点
        #    作用: 消除“删除头节点”与“删除中间/尾节点”的特判逻辑
        dummy = ListNode(next=head)
        
        # 2. 初始化先行快指针 right，从 dummy 出发
        right = dummy
        
        # 3. 快指针先行 n 步
        #    执行完毕后，right 与 left 之间在拓扑逻辑上拉开严格为 n 个节点的间距
        for _ in range(n):
            right = right.next

        # 4. 初始化慢指针 left，从 dummy 出发
        left = dummy
        
        # 5. 双指针同步向后遍历，循环条件为 right.next 不为空
        #    当 right.next 为 None 时，right 恰好停在末尾节点 (索引 L)
        #    根据间距不变量，left 此时必然停在正数第 L - n 个节点 (待删节点的前驱)
        while right.next:
            left = left.next
            right = right.next
            
        # 6. 执行核心跳过与删除操作: 将前驱的 next 指针指向待删节点的后继
        left.next = left.next.next

        # 7. 返回哨兵的 next (即删除操作后的实际链表头节点)
        return dummy.next
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 双指针一趟扫描法 vs 两次遍历计数法，优劣势是什么？

* **面试官**：如果让你用最朴素的两趟扫描（先算总长度 $L$，再找第 $L-n$ 个节点）来写，和双指针相比有什么差异？
* **候选人解析**：
  * **时间复杂度**：两者理论上都是 $O(L)$。两次遍历总共访问 $L + (L - n)$ 个节点，大约 $2L$ 次访问；双指针一趟扫描总共遍历 $n + (L - n) = L$ 次右指针访问与 $L - n$ 次左指针访问，总访问次数完全相当。
  * **实际性能与工程考量**：单趟扫描最大的优势在于**硬件 CPU 缓存友好（Cache Locality）**与**流式处理（Stream Processing）**。如果链表非常巨大或来自网络流/磁盘读取无法重头再读，一趟双指针窗口滑行可以在不重读数据的情况下直接完成处理。

```python
# 附: 两次遍历解法 (Two-Pass Baseline)
class SolutionTwoPass:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 统计长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
            
        # 2. 找到倒数第 n 个的前驱 (即正数第 length - n 个)
        dummy = ListNode(next=head)
        cur = dummy
        for _ in range(length - n):
            cur = cur.next
            
        cur.next = cur.next.next
        return dummy.next
```

---

### 追问 2: 能否使用纯递归（倒序回溯计数）来解决？

* **面试官**：除了双指针和长度遍历，单链表的天然递归后序遍历具有“倒序出栈”的性质，你能写出递归解法吗？
* **候选人解析**：
  * 递归到底层遇到 `None` 时返回计数器 `0`。
  * 归程中每次回溯计数器 `+ 1`。
  * 当计数器恰好等于 $n$ 时，说明当前递归层返回的节点即为待删除节点，其父层将其跳过。

```python
# 附: 递归后序回溯法 (Recursive Post-order)
class SolutionRecursion:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        
        def helper(node: Optional[ListNode]) -> int:
            if not node:
                return 0
            # 递归深入到链表末尾
            cnt = helper(node.next) + 1
            if cnt == n + 1:
                # node 是待删除节点的前驱
                node.next = node.next.next
            return cnt

        helper(dummy)
        return dummy.next
```
* **复杂度权衡**：递归法空间复杂度为 $O(L)$（系统调用栈开销），而双指针迭代空间为 $O(1)$，因此在面试中优先推崇迭代双指针。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **未引入 `dummy` 哨兵** | 链表长度为 1 或删除头节点时 (`n == sz`)，报错 `AttributeError` 或返回错误头节点 | 删除头节点需要修改 `head` 本身的指向，缺少前驱节点导致无法执行 `pre.next = cur.next` | 统一引入 `dummy = ListNode(next=head)`，无论删谁都具备统一的前驱 |
| **循环终止条件混淆 (`while right:` vs `while right.next:`)** | 删除了待删除节点的下一个节点，或者越界报 `NoneType.next` | 若条件写为 `while right:`，当 `right` 为 `None` 时，`left` 停在待删除节点本身而非前驱 | 牢记不变量：若要修改 `target`，必须停在 `target` 的**前驱**，因此以 `right.next` 为终止条件 |
| **先行步数越界未做校验** | 当题目给定 $n > sz$ 时，`right = right.next` 在 for 循环中抛出 `AttributeError` | 假设了 $n \le sz$；若在工业级代码中需要防御性保护 | 在 for 循环中增加 `if not right: return head` 防御分支 |
| **C/C++ 内存泄漏 (Memory Leak)** | 内存持续占用（力扣/生产环境） | 仅断开了指针引用，未 `delete` 释放被剔除节点的堆内存 | 先暂存 `ListNode* delNode = left->next; left->next = delNode->next; delete delNode;` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

#### 用例 1: 链表仅 1 个节点，删除头节点 (`head = [1]`, $n = 1$)

1. 初始化：`dummy -> [1] -> None`, `left = dummy`, `right = dummy`
2. 先行 1 步：`right = right.next` $\\rightarrow$ `right` 指向 `[1]`
3. `while right.next:`: `right.next` 为 `None`，循环不执行！
4. 删除操作：`left.next = left.next.next` $\\rightarrow$ `dummy.next = None`（节点 `[1]` 被架空）
5. 返回：`dummy.next` 即 `None`（正确！）

#### 用例 2: 链表多节点，删除头节点 (`head = [1, 2]`, $n = 2$)

1. 初始化：`dummy -> [1] -> [2] -> None`, `left = dummy`, `right = dummy`
2. 先行 2 步：`right` 依次移动到 `[1]` 再到 `[2]`
3. `while right.next:`: `right.next` 为 `None`，循环不执行！
4. 删除操作：`left.next = left.next.next` $\\rightarrow$ `dummy.next = dummy.next.next = [2]`（头节点 `[1]` 被删除）
5. 返回：`dummy.next` 即 `[2]`（正确！）

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\\mathcal{O}(L)$ | $L$ 为链表长度。先行快指针移动 $n$ 步，随后快慢指针共同移动 $L - n$ 步。快指针刚好完整遍历整个链表一次，总操作步数严格为 $L$，时间为线性 $\\mathcal{O}(L)$。 |
| **空间复杂度 (Space Complexity)** | $\\mathcal{O}(1)$ | 算法仅创建了一个哨兵 `dummy` 节点与两个指针变量（`left`, `right`），未申请任何依赖输入规模的辅助数据结构，辅助空间复杂度严格为 $\\mathcal{O}(1)$。 |
