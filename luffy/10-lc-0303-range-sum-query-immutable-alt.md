# LC 0303: Range Sum Query - Immutable (Alt Constructor) | 区域和检索 - 数组不可变 (变体构造)

- **LeetCode ID**: LC 0303
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 03: Prefix Sum)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/range-sum-query---immutable-(alt-constructor)/)
- **Solution File**: [`10-lc-0303-range-sum-query-immutable-alt.py`](luffy/10-lc-0303-range-sum-query-immutable-alt.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Prefix sum implementation using n+1 length array constructor.

### [CN] 中文描述
使用 n+1 长度前缀和数组构建的不可变区间求和类。

### Constraints / 约束条件
1 <= nums.length <= 10^4

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Array Basics] ➔ [Prefix Sum]`

```
┌────────────────────────────────────────────────────────┐
│ 前缀和 n+1 构造法                                      │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
preSum[i+1] = preSum[i] + nums[i]

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List
class NumArray: #new

    def __init__(self, nums: List[int]):
        self.preSum = [0] * (len(nums) + 1) #第i个element的位置储存列表前i个元素的和
        for i in range((len(nums))):
            self.preSum[i+1] = self.preSum[i] + nums[i]



    def sumRange(self, left: int, right: int) -> int: #new
        return self.preSum[right+1] - self.preSum[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
      
            


if __name__ == '__main__':
    a=NumArray([0,1,2,3,4,5,6])
    a.sumRange(0,2)
```

1. 基于 `10-lc-0303-range-sum-query-immutable-alt.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“与暴力相加相比的优势？”*
  - **Candidate**: 将 $k$ 次查询由 $O(k \cdot n)$ 优化为 $O(n + k)$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 累加错位 | 下标加减混淆 | 索引偏移 | 统一公式 preSum[r+1] - preSum[l] |

### Complete Dry-Run Table / 实例推演表

nums=[1,2,3] -> preSum=[0,1,3,6] -> sum(1,2) = 6 - 1 = 5

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(1)$ | 单次查询。 |
| **Space Complexity** | $O(n)$ | 前缀和数组。 |
