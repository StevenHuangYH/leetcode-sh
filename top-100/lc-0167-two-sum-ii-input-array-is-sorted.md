# LC 0167: Two Sum II - Input Array Is Sorted | 两数之和 II - 输入有序数组

- **LeetCode ID**: LC 0167
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- **Solution File**: [lc-0167-two-sum-ii-input-array-is-sorted.py](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.
Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

### [CN] 中文描述
给你一个下标从 1 开始的整数数组 `numbers` ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。如果设这两个数分别是 `numbers[index1]` 和 `numbers[index2]` ，则 `1 <= index1 < index2 <= numbers.length` 。
以长度为 2 的整数数组 `[index1, index2]` 的形式返回这两个整数的下标 `index1` 和 `index2`。
你可以假设每个输入只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
你所设计的解决方案必须只使用常量级的额外空间。

### Constraints / 约束条件
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` 按 非递减顺序 排列
- `-1000 <= target <= 1000`
- 仅存在一个有效答案

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Two Pointer]`

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ LC 1 Two Sum (无序哈希表法)                            │
│ 空间复杂度 O(n)，无法满足 O(1) 额外空间约束            │
└───────────────────────────┬────────────────────────────┘
                            │ 利用输入数组单调有序性质
                            ▼
┌────────────────────────────────────────────────────────┐
│ 相向对撞双指针 (Opposite Direction Two Pointers)        │
│ • s = nums[l] + nums[r] > target: 必须减小最大值 r -= 1│
│ • s = nums[l] + nums[r] < target: 必须增大最小值 l += 1│
└───────────────────────────┬────────────────────────────┘
                            │ 升维为三数/四数之和通用基石
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 15 3Sum / LC 16 3Sum Closest / LC 18 4Sum           │
│ 外层枚举固定基准 + 内层有序对撞双指针                  │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

对撞双指针 `left = 0, right = n - 1`：
- 当前和 $s = \text{numbers}[left] + \text{numbers}[right]$。
- 若 $s > target$：由于数组升序，$\text{numbers}[right]$ 与任何左侧元素相加都必定 $> target$。因此 `right` 不可能参与答案构建，安全排除 `right -= 1`。
- 若 $s < target$：$\text{numbers}[left]$ 与任何右侧元素相加都必定 $< target$。因此 `left` 不可能参与答案构建，安全排除 `left += 1`。
- 若 $s == target$：找到唯一解，返回 `[left + 1, right + 1]`。

```
numbers: [ 2,  7, 11, 15 ], target = 9
           ▲          ▲
          left      right   --> sum = 17 > 9, right -= 1
           ▲      ▲
          left  right       --> sum = 9 == 9, MATCH!
```

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        n = len(numbers)
        right = n - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1

        return []
```

1. **指针初始化**：`left = 0, right = n - 1` 分别指向首尾。
2. **对撞循环**：`while left < right:` 确保不重复使用同一元素。
3. **单调性决策**：
   - `if s == target`: 转换为 1-indexed 下标 `[left + 1, right + 1]` 返回。
   - `elif s > target`: 右指针左移 `right -= 1`。
   - `else`: 左指针右移 `left += 1`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果数组长度非常大，但答案相差悬殊，能用二分查找优化双指针移动吗？”*
  - **Candidate Response**: 可以。在 $s > target$ 时，可以直接在 $[left + 1, right - 1]$ 中通过二分查找 `target - numbers[left]` 的上界位置，一次性跳过大段不可能的元素，将每次指针移动的步长从 1 步加速到对数级别。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 忘记 1-indexed 下标要求 | 结果输出 `[0, 1]` 导致用例失败 | 题目要求返回从 1 开始计数的下标 | 返回时统一加 1：`[left + 1, right + 1]` |
| 循环条件误写为 `left <= right` | 当 $2 \times nums[i] = target$ 时重复选同一元素 | 题目要求不可以重复使用相同元素 | 严格维持 `left < right` |

### Complete Dry-Run Table / 实例推演表

输入: `numbers = [2, 7, 11, 15], target = 9`

| Step | `left` (0-idx) | `right` (0-idx) | `numbers[left]` | `numbers[right]` | `s` | Condition | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 3 | 2 | 15 | 17 | `17 > 9` | `right = 2` |
| 2 | 0 | 2 | 2 | 11 | 13 | `13 > 9` | `right = 1` |
| 3 | 0 | 1 | 2 | 7 | 9 | `9 == 9` | 返回 `[0+1, 1+1] = [1, 2]` |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 左右指针相向而行，每次循环至少一个指针移动 1 步，最多遍历 $n$ 次。 |
| **Space Complexity** | $O(1)$ | 仅使用两个整型指针与临时和变量，满足常数额外空间要求。 |
