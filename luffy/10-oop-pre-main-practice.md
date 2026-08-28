# LC 0000: OOP Foundations & Object Instantiation | 面向对象基础与实例初始化

- **LeetCode ID**: LC 0000
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 11: OOP Foundations)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/oop-foundations-&-object-instantiation/)
- **Solution File**: [`10-oop-pre-main-practice.py`](luffy/10-oop-pre-main-practice.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Foundational object-oriented programming practices in Python covering class definitions and constructors.

### [CN] 中文描述
Python 面向对象编程基础：类定义、构造函数与对象实例化。

### Constraints / 约束条件
Python 3 OOP 语法规范

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ Class Car -> Instance car_1('Toyota', 'Camry', ...)   │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
封装性：对象拥有独立的内部属性状态。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from  car import Car


car_1 = Car("Toyota", "Camry", 2020, "Blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)


car_1.drive()
car_1.stop()
```

1. 基于 `10-oop-pre-main-practice.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“__init__ 和 __new__ 的区别？”*
  - **Candidate**: `__new__` 负责创建并返回实例，`__init__` 负责初始化实例属性。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 忘记 self | def func() 缺少 self 报错 | 缺少实例引用 | 首个入参必须为 self |

### Complete Dry-Run Table / 实例推演表

car_1 = Car('Toyota') -> print(car_1.make) -> 'Toyota'

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(1)$ | 属性存取。 |
| **Space Complexity** | $O(1)$ | 对象实例。 |
