# Problem Metadata Database for Luffy 42-Topic Curriculum

LUFFY_PROBLEMS = {
    "01-lc-2235-add-two-integers": {
        "id": "2235",
        "title_en": "Add Two Integers",
        "title_cn": "两整数相加",
        "diff": "Easy",
        "topic": "Topic 01: Foundations & Arithmetic",
        "en_desc": "Given two integers `num1` and `num2`, return the sum of the two integers.",
        "cn_desc": "给你两个整数 `num1` 和 `num2`，请你返回这两个整数的和。",
        "constraints": "-100 <= num1, num2 <= 100",
        "ascii": """┌────────────────────────────────────────────────────────┐
│ 基础算术基石 (Foundational Arithmetic)                │
│ 直接返回 num1 + num2                                   │
└────────────────────────────────────────────────────────┘""",
        "invariant": "直接代数加法：$$\\text{sum}(num1, num2) = num1 + num2$$",
        "interview_qa": "- **Interviewer**: *“如何不用加号实现？”*\n  - **Candidate**: 利用位运算半加器原理 `a ^ b` 配合进位 `(a & b) << 1` 迭代计算。",
        "anti_patterns": [("整数溢出 (其他语言)", "超出 32 位整型范围", "基础类型越界", "Python 原生支持大整数运算，无溢出")],
        "dry_run": "输入: `num1 = 12, num2 = 5` -> `12 + 5 = 17`",
        "time": ("$O(1)$", "单次硬件加法指令。"),
        "space": ("$O(1)$", "常数级寄存器空间。")
    },
    "02-lc-0001-two-sum": {
        "id": "0001",
        "title_en": "Two Sum",
        "title_cn": "两数之和",
        "diff": "Easy",
        "topic": "Topic 01: Arrays & Hash Table",
        "en_desc": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
        "cn_desc": "给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。",
        "constraints": "2 <= nums.length <= 10^4, -10^9 <= nums[i] <= 10^9, -10^9 <= target <= 10^9",
        "ascii": """┌────────────────────────────────────────────────────────┐
│ 单遍哈希探测 (Single-Pass Hash Map)                    │
│ 遍历 x，计算补数 target - x                            │
│ 若 cache[target - x] 存在 -> 立即返回对应下标对        │
│ 否则存入 cache[x] = i                                  │
└────────────────────────────────────────────────────────┘""",
        "invariant": "前缀补数不变量：对于任意当前元素 $x$，仅需在先前遍历过的集合中寻找 $target - x$。",
        "interview_qa": "- **Interviewer**: *“为什么单遍边查边存优于两遍哈希？”*\n  - **Candidate**: 既能省去一次数组遍历，又能天然防御元素自身与自身匹配的自碰撞 Bug。",
        "anti_patterns": [("自匹配陷阱", "target=6, nums=[3,3] 返回 [0,0]", "查表时未排除自身下标", "单遍扫描边查边存天然防御自匹配")],
        "dry_run": "输入: `nums = [2, 7, 11, 15], target = 9`\n- i=0, item=2, val=7 -> cache={2:0}\n- i=1, item=7, val=2 -> match cache[2]=0 -> return [0, 1]",
        "time": ("$O(n)$", "遍历数组一次，哈希表单次存取平均 $O(1)$。"),
        "space": ("$O(n)$", "哈希表最多存储 $n$ 个键值对。")
    },
    "03-lc-0167-two-sum-ii-input-array-is-sorted": {
        "id": "0167",
        "title_en": "Two Sum II - Input Array Is Sorted",
        "title_cn": "两数之和 II - 输入有序数组",
        "diff": "Medium",
        "topic": "Topic 01: Two Pointers",
        "en_desc": "Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.",
        "cn_desc": "给你一个下标从 1 开始的整数数组 `numbers` ，该数组已按非递减顺序排列 ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。",
        "constraints": "2 <= numbers.length <= 3 * 10^4, -1000 <= numbers[i] <= 1000",
        "ascii": """┌────────────────────────────────────────────────────────┐
│ 双指针对撞 (Inward Two Pointers)                      │
│ left = 0, right = n - 1                                │
│ sum = nums[left] + nums[right]                         │
│ sum < target -> left += 1; sum > target -> right -= 1  │
└────────────────────────────────────────────────────────┘""",
        "invariant": "单调性逼近：利用数组升序性质，左右指针对撞单向收缩搜索空间。",
        "interview_qa": "- **Interviewer**: *“相比无序数组的两数之和，有序数组有何优势？”*\n  - **Candidate**: 可以将空间复杂度由哈希表的 $O(n)$ 降为双指针的 $O(1)$。",
        "anti_patterns": [("下标基准错误", "返回 0-based 下标", "未注意题目 1-indexed 约束", "返回结果时统一 +1")],
        "dry_run": "输入: `numbers = [2, 7, 11, 15], target = 9`\n- left=0(2), right=3(15), sum=17 > 9 -> right=2(11)\n- left=0(2), right=2(11), sum=13 > 9 -> right=1(7)\n- left=0(2), right=1(7), sum=9 == 9 -> return [1, 2]",
        "time": ("$O(n)$", "双指针单向移动，最多相遇一次。"),
        "space": ("$O(1)$", "仅使用两个指针变量。")
    }
}
