# LC 0303: Range Sum Query - Immutable | 区域和检索 - 数组不可变

- **LeetCode ID**: LC 0303
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 03: Prefix Sum)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/range-sum-query---immutable/)
- **Solution File**: [`10-lc-0303-range-sum-query-immutable.py`](problems/luffy/10-lc-0303-range-sum-query-immutable.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an integer array `nums`, handle multiple queries of the sum of the elements between indices `left` and `right` inclusive.

### [CN] 中文描述
给定一个整数数组  `nums`，处理以下类型的多个查询: 计算索引 `left` 和 `right` （包含 `left` 和 `right`）之间的 `nums` 元素的和 ，其中 `left <= right`。

### Constraints / 约束条件
1 <= nums.length <= 10^4, -10^5 <= nums[i] <= 10^5, 0 <= left <= right < nums.length

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Array Basics] ➔ [Prefix Sum]`

```
┌────────────────────────────────────────────────────────┐
│ 前缀和数组: preSum[i] = nums[0] + ... + nums[i-1]      │
│ query(left, right) = preSum[right + 1] - preSum[left]  │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
区间和减法公理：$$\sum_{i=l}^r nums[i] = preSum[r+1] - preSum[l]$$

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums


        

    def sumRange(self, left: int, right: int) -> int: #general way
        my_sum = 0
        for i in range(left, right+1):
            my_sum +=self.nums[i]
        return my_sum
            


if __name__ == '__main__':
    a=NumArray([0,1,2,3,4,5,6])
    a.sumRange(0,2)


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

1. 基于 `10-lc-0303-range-sum-query-immutable.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么 preSum 长度通常设为 n + 1？”*
  - **Candidate**: 可以让 `preSum[0] = 0`，使 `left = 0` 时无需进行特殊的条件分支特判。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 未偏移 1-index | preSum[right] - preSum[left-1] 在 left=0 越界 | 索引越界 | preSum 开 n+1 长度 |

### Complete Dry-Run Table / 实例推演表

nums=[-2,0,3,-5,2,-1] -> preSum=[0,-2,-2,1,-4,-2,-3] -> sum(0,2) = 1 - 0 = 1

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(1)$ 查询, $O(n)$ 预处理 | 单次查询仅执行一次减法。 |
| **Space Complexity** | $O(n)$ | 前缀和数组空间。 |
