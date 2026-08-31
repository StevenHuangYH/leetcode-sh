# LC 0303: Prefix Sum Practice & Class Structure | 前缀和与 OOP 面向对象实践

- **LeetCode ID**: LC 0303
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 03: OOP & Prefix Sum)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/prefix-sum-practice-&-class-structure/)
- **Solution File**: [`10-lc-0303-prefix-sum-practices.py`](luffy/10-lc-0303-prefix-sum-practices.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Object-oriented class structure and foundational principles for cumulative data modeling.

### [CN] 中文描述
面向对象类构造及累加数据建模基础。

### Constraints / 约束条件
OOP 基础规范

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Array Basics] ➔ [Prefix Sum]`

```
┌────────────────────────────────────────────────────────┐
│ 面向对象类封装与状态维护                               │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
实例属性封装：`self.attr` 隔离实例内部状态。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Employee:
    empCount = 0



    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
```

1. 基于 `10-lc-0303-prefix-sum-practices.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“类变量与实例变量的区别？”*
  - **Candidate**: 类变量为所有实例共享，实例变量通过 `self` 绑定于独立实例。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 修改类变量误伤全部实例 | 通过 self 修改类变量产生遮蔽 | 作用域混淆 | 类属性统一由类名访问 |

### Complete Dry-Run Table / 实例推演表

Employee('Zara', 2000) -> empCount=1

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(1)$ | 构造与访问。 |
| **Space Complexity** | $O(1)$ | 对象内存。 |
