# LC 0303: Prefix Sum Basic Calculation | 前缀和基础计算模版

- **LeetCode ID**: LC 0303
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 03: Prefix Sum)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/prefix-sum-basic-calculation/)
- **Solution File**: [`11-prefix-sum-basic-example.py`](problems/luffy/11-prefix-sum-basic-example.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Basic algorithm to construct a cumulative prefix sum array in-place or with auxiliary array.

### [CN] 中文描述
构建前缀和数组的基础函数实现与累加递推。

### Constraints / 约束条件
1 <= arr.length <= 10^5

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ prefixSum[i] = prefixSum[i-1] + arr[i]                 │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
累加递推：$prefix[i] = prefix[i-1] + arr[i]$

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
# function to find the prefix sum array
def prefSum(arr):
    n = len(arr)
    
    # to store the prefix sum
    prefixSum = [0] * n

    # initialize the first element
    prefixSum[0] = arr[0]

    # Adding present element with previous element
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]
    
    return prefixSum

if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    prefixSum = prefSum(arr)
    for i in prefixSum:
        print(i, end=" ")
```

1. 基于 `11-prefix-sum-basic-example.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“原地修改原数组实现前缀和的优缺点？”*
  - **Candidate**: 优点是省去 $O(n)$ 空间；缺点是破坏了原数组数据，只读查询场景需权衡。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 索引越界 | i=0 时访问 i-1 | 边界越界 | i=0 需赋初值 arr[0] |

### Complete Dry-Run Table / 实例推演表

arr=[10, 20, 10, 5] -> prefixSum=[10, 30, 40, 45]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 线性遍历一次。 |
| **Space Complexity** | $O(n)$ | 前缀和数组。 |
