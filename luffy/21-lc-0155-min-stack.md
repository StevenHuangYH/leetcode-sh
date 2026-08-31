# LC 0155: Min Stack | 最小栈

- **LeetCode ID**: LC 0155
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 06: Stacks)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/min-stack/)
- **Solution File**: [`21-lc-0155-min-stack.py`](luffy/21-lc-0155-min-stack.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

### [CN] 中文描述
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

### Constraints / 约束条件
-2^31 <= val <= 2^31 - 1, 最多调用 3 * 10^4 次 push, pop, top, getMin

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Data Structures] ➔ [Stack & Queue]`

```
┌────────────────────────────────────────────────────────┐
│ 双栈法 / 辅助最小栈 (Min Stack Pair)                   │
│ 主栈 stack 存数据，辅助栈 min_stack 同步存当前最小值   │
│ min_stack[-1] 始终为全局最小值                         │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
前缀极值同步性：`min_stack[i]` 严格等于 `min(stack[0...i])`。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-155-min-stack


class MinStack:

    def __init__(self):
        self.data_stack=[]
        self.min_stack=[]

    def push(self, value: int) -> None:
        self.data_stack.append(value)
        if self.min_stack:
            top=self.min_stack[-1]
            min_value=min(value,top)
            self.min_stack.append(min_value)
        else:
            self.min_stack.append(value)

    def pop(self) -> None:
        self.data_stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.data_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

1. 基于 `21-lc-0155-min-stack.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何只用一个栈做到 O(1) 空间支持 getMin？”*
  - **Candidate**: 可以在栈中存入当前值与当前最小值的差值 `diff = val - min_val`，或在栈内压入 `(val, cur_min)` 二元组。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| pop 未同步更新 min | 仅从主栈 pop 导致 min 栈未同步 | 状态脱节 | 主栈与辅助栈必须严格同步 push/pop |

### Complete Dry-Run Table / 实例推演表

push(-2), push(0), push(-3) -> getMin()=-3, pop() -> getMin()=-2

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(1)$ | 所有操作均为常数时间。 |
| **Space Complexity** | $O(n)$ | 辅助栈占用额外空间。 |
