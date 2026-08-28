# LC 0232: Implement Queue using Stacks | 用栈实现队列

- **LeetCode ID**: LC 0232
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 06: Stacks & Queues)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/implement-queue-using-stacks/)
- **Solution File**: [`24-lc-0232-implement-queue-using-stacks.py`](luffy/24-lc-0232-implement-queue-using-stacks.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Implement a first in first out (FIFO) queue using only two stacks.

### [CN] 中文描述
请你仅使用两个栈实现先入先出 (FIFO) 的队列。

### Constraints / 约束条件
最多调用 100 次

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 双栈模拟 (In-Stack & Out-Stack)                        │
│ push: 直接压入 in_stack                                │
│ pop/peek: 若 out_stack 为空，将 in_stack 全部倒入      │
│           再从 out_stack 弹出/查看                     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
倒序抵消原理：两次 LIFO 后进先出等价于一次 FIFO 先入先出。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-232:
#implement queue using stacks


class MyQueue:

    def __init__(self):
        self.input_stack=[]
        self.out_stack=[]
        

    def push(self, x: int) -> None:
        self.input_stack.append(x)
        
        

    def pop(self) -> int:
        if self.out_stack:
            return self.out_stack.pop()
        else:
            while self.input_stack:
                self.out_stack.append(self.input_stack.pop())

            return self.out_stack.pop()
        

    
    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]
        while self.input_stack:
            self.out_stack.append(self.input_stack.pop())
        return self.out_stack[-1]
        

    def empty(self) -> bool:
        if self.input_stack or self.out_stack:
            return False
        else:
            return True

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

1. 基于 `24-lc-0232-implement-queue-using-stacks.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“pop 操作的均摊时间复杂度是多少？”*
  - **Candidate**: 均摊 $O(1)$。每个元素最多进出 `in_stack` 和 `out_stack` 各一次，总步数 $4n$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 每次 push 都倒栈 | push 复杂度退化为 O(n) | 过早搬运 | 仅在 pop/peek 且 out 为空时倒栈 |

### Complete Dry-Run Table / 实例推演表

push(1), push(2) -> in=[1,2], out=[] -> pop() -> in=[], out=[2,1] -> return 1

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | 均摊 $O(1)$ | 每个元素最多被移动 2 次。 |
| **Space Complexity** | $O(n)$ | 两栈总容量。 |
