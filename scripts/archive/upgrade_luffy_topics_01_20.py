import os
import re
from pathlib import Path
from scripts.generate_luffy_batch import create_note

REPO_ROOT = Path(__file__).parent.parent
LUFFY_DIR = REPO_ROOT / "luffy"

DB = {
    "01-lc-2235-add-two-integers": {
        "id": "2235", "title_en": "Add Two Integers", "title_cn": "两整数相加", "diff": "Easy", "topic": "Topic 01: Foundations & Arithmetic",
        "en_desc": "Given two integers `num1` and `num2`, return the sum of the two integers.",
        "cn_desc": "给你两个整数 `num1` 和 `num2`，请你返回这两个整数的和。",
        "constraints": "-100 <= num1, num2 <= 100",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 直接代数求和: sum = num1 + num2                         │\n└────────────────────────────────────────────────────────┘",
        "invariant": "代数加法公理：$$\\text{sum}(num1, num2) = num1 + num2$$",
        "interview_qa": "- **Interviewer**: *“如何不用加号实现？”*\n  - **Candidate**: 利用位运算 `a ^ b` 结合进位 `(a & b) << 1` 循环累加。",
        "anti_patterns": [("溢出边界", "其他语言 32 位溢出", "整型边界", "Python 原生支持大整数运算")],
        "dry_run": "输入: `num1 = 12, num2 = 5` -> `17`",
        "time": ("$O(1)$", "硬件级加法。"), "space": ("$O(1)$", "常数空间。")
    },
    "02-lc-0001-two-sum": {
        "id": "0001", "title_en": "Two Sum", "title_cn": "两数之和", "diff": "Easy", "topic": "Topic 01: Arrays & Hash Table",
        "en_desc": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
        "cn_desc": "给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。",
        "constraints": "2 <= nums.length <= 10^4, -10^9 <= nums[i] <= 10^9, -10^9 <= target <= 10^9",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 单遍哈希探测 target - x                                 │\n└────────────────────────────────────────────────────────┘",
        "invariant": "前缀补数映射：对于当前 $x$，查先前集合是否存在 $target - x$。",
        "interview_qa": "- **Interviewer**: *“单遍边查边存的优势？”*\n  - **Candidate**: 避免遍历两次并天然消除元素自匹配 Bug。",
        "anti_patterns": [("自匹配陷阱", "target=6, nums=[3,3] 返回 [0,0]", "未排除自身", "单遍哈希边查边存")],
        "dry_run": "输入: `nums=[2,7,11,15], target=9` -> `[0,1]`",
        "time": ("$O(n)$", "遍历一次数组。"), "space": ("$O(n)$", "哈希表大小。")
    },
    "03-lc-0167-two-sum-ii-input-array-is-sorted": {
        "id": "0167", "title_en": "Two Sum II - Input Array Is Sorted", "title_cn": "两数之和 II - 输入有序数组", "diff": "Medium", "topic": "Topic 01: Two Pointers",
        "en_desc": "Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.",
        "cn_desc": "给你一个下标从 1 开始的整数数组 `numbers` ，该数组已按非递减顺序排列 ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。",
        "constraints": "2 <= numbers.length <= 3 * 10^4, -1000 <= numbers[i] <= 1000",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 相向双指针对撞: sum < target -> left++; sum > target -> right-- │\n└────────────────────────────────────────────────────────┘",
        "invariant": "单调性逼近：利用有序性两端相向移动指针收缩解空间。",
        "interview_qa": "- **Interviewer**: *“如何做到 O(1) 空间？”*\n  - **Candidate**: 采用相向双指针代替哈希表。",
        "anti_patterns": [("下标未 +1", "返回 0-based 索引", "题目要求 1-based", "输出时统一 +1")],
        "dry_run": "输入: `numbers=[2,7,11,15], target=9` -> `[1,2]`",
        "time": ("$O(n)$", "左右指针相向单调移动。"), "space": ("$O(1)$", "仅需双指针（源码若用哈希则为 O(n)）。")
    },
    "04-lc-0003-longest-substring-without-repeating-characters": {
        "id": "0003", "title_en": "Longest Substring Without Repeating Characters", "title_cn": "无重复字符的最长子串", "diff": "Medium", "topic": "Topic 01: Sliding Window",
        "en_desc": "Given a string `s`, find the length of the longest substring without duplicate characters.",
        "cn_desc": "给定一个字符串 `s` ，请你找出其中不含有重复字符的最长子串的长度。",
        "constraints": "0 <= s.length <= 5 * 10^4",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 滑动窗口: 右进左出维持窗口内字符无重复                 │\n└────────────────────────────────────────────────────────┘",
        "invariant": "窗口内字符唯一性：集合记录当前窗口内出现的无重复字符。",
        "interview_qa": "- **Interviewer**: *“如何进一步优化左指针移动步长？”*\n  - **Candidate**: 记录字符最后出现下标，遇到重复直接跳转 `left = max(left, last_pos[c] + 1)`。",
        "anti_patterns": [("空串报错", "s='' 未防御", "未初始化 ans=0", "初始化 ans=0")],
        "dry_run": "输入: `s='abcabcbb'` -> max len = 3 ('abc')",
        "time": ("$O(n)$", "每个字符进出集合一次。"), "space": ("$O(|\\Sigma|)$", "字符集大小。")
    },
    "05-lc-0026-remove-duplicates-from-sorted-array": {
        "id": "0026", "title_en": "Remove Duplicates from Sorted Array", "title_cn": "删除有序数组中的重复项", "diff": "Easy", "topic": "Topic 01: In-Place Two Pointers",
        "en_desc": "Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements.",
        "cn_desc": "给你一个非递减序排列的整数数组 `nums` ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。",
        "constraints": "1 <= nums.length <= 3 * 10^4, -100 <= nums[i] <= 100",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 快慢双指针: read 扫描，write 维护不重复前缀            │\n└────────────────────────────────────────────────────────┘",
        "invariant": "有序前缀无重复不变量：$nums[0...write]$ 中所有元素严格单调递增。",
        "interview_qa": "- **Interviewer**: *“如何保留最多 k 个重复项？”*\n  - **Candidate**: 比较条件改为 `nums[read] != nums[write - k]`。",
        "anti_patterns": [("开辟新数组", "违反原地 O(1) 空间要求", "理解偏差", "必须在 nums 上原地覆写")],
        "dry_run": "输入: `nums=[1,1,2]` -> write=1, nums=[1,2,2], return 2",
        "time": ("$O(n)$", "读指针遍历数组一次。"), "space": ("$O(1)$", "原地修改。")
    },
    "06-lc-0209-minimum-size-subarray-sum": {
        "id": "0209", "title_en": "Minimum Size Subarray Sum", "title_cn": "长度最小的子数组", "diff": "Medium", "topic": "Topic 01: Sliding Window",
        "en_desc": "Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0.",
        "cn_desc": "给定一个含有 n 个正整数的数组和一个正整数 target 。找出该数组中满足其总和大于等于 target 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。",
        "constraints": "1 <= target <= 10^9, 1 <= nums.length <= 10^5, 1 <= nums[i] <= 10^4",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 滑动窗口: 右移累加，和 >= target 时持续收缩左边界      │\n└────────────────────────────────────────────────────────┘",
        "invariant": "正整数单调性：窗口扩大和单调增加，窗口缩小和单调减少。",
        "interview_qa": "- **Interviewer**: *“数组含负数时滑动窗口是否成立？”*\n  - **Candidate**: 不成立，因和失去单调性，需改用前缀和 + 单调队列（LC 862）。",
        "anti_patterns": [("初始值错误", "ans=0 导致 min 永远为 0", "极值初始化错误", "必须初始化为 inf")],
        "dry_run": "输入: `target=7, nums=[2,3,1,2,4,3]` -> min len = 2 ([4,3])",
        "time": ("$O(n)$", "每个元素进出窗口最多一次。"), "space": ("$O(1)$", "仅维护指针和求和变量。")
    },
    "07-lc-0704-binary-search": {
        "id": "0704", "title_en": "Binary Search", "title_cn": "二分查找", "diff": "Easy", "topic": "Topic 02: Binary Search",
        "en_desc": "Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.",
        "cn_desc": "给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。",
        "constraints": "1 <= nums.length <= 10^4, -10^4 < nums[i], target < 10^4",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 闭区间二分: left=0, right=n-1, while left <= right     │\n└────────────────────────────────────────────────────────┘",
        "invariant": "搜索区间不变量：目标值若存在必在 $[left, right]$ 中。",
        "interview_qa": "- **Interviewer**: *“为什么循环条件带等号？”*\n  - **Candidate**: 闭区间下 $left == right$ 仍代表区间内包含 1 个有效待检元素。",
        "anti_patterns": [("死循环", "left=mid 导致区间无法缩小", "未加减 1", "闭区间必须 left=mid+1 / right=mid-1")],
        "dry_run": "输入: `nums=[-1,0,3,5,9,12], target=9` -> mid=4 (val=9) -> return 4",
        "time": ("$O(\\log n)$", "每轮折半。"), "space": ("$O(1)$", "常数级指针。")
    },
    "08-lc-0059-spiral-matrix-ii": {
        "id": "0059", "title_en": "Spiral Matrix II", "title_cn": "螺旋矩阵 II", "diff": "Medium", "topic": "Topic 01: Matrix Simulation",
        "en_desc": "Given a positive integer `n`, generate an `n x n` matrix filled with elements from 1 to `n^2` in spiral order.",
        "cn_desc": "给你一个正整数 `n` ，生成一个包含 1 到 `n^2` 所有元素，且元素按顺时针顺序螺旋排列的 `n x n` 正方形矩阵 `matrix` 。",
        "constraints": "1 <= n <= 20",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 四界收缩法: top, bottom, left, right 顺时针依次推进    │\n└────────────────────────────────────────────────────────┘",
        "invariant": "边界收缩不变量：每填满一行或一列，对应边界内缩 1 位。",
        "interview_qa": "- **Interviewer**: *“如何推广到 m x n 矩阵？”*\n  - **Candidate**: 逻辑相同，但每边遍历前需加边界重叠判定。",
        "anti_patterns": [("转角重复填", "转角格子被多次赋值", "边界开闭混淆", "严格使用收缩后的界限")],
        "dry_run": "输入: `n=3` -> 依次填外圈 1-8，中心 9",
        "time": ("$O(n^2)$", "填满所有格子。"), "space": ("$O(1)$", "除返回矩阵外常数空间。")
    },
    "09-lc-0059-spiral-matrix-ii-alt": {
        "id": "0059", "title_en": "Spiral Matrix II (Alternative / Linked List Model)", "title_cn": "螺旋矩阵 II (变体与链表基石)", "diff": "Medium", "topic": "Topic 01: Matrix & Linked List Pre",
        "en_desc": "Foundational node definitions and traversal alternatives for spiral structures and list elements.",
        "cn_desc": "螺旋矩阵与链表基础节点的结构定义及遍历变体模型。",
        "constraints": "1 <= n <= 20",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 链表节点与矩阵结构演进模型                             │\n└────────────────────────────────────────────────────────┘",
        "invariant": "指针单向链式引用不变量：`node.next` 形成单向链条。",
        "interview_qa": "- **Interviewer**: *“链表结构与二维矩阵扁平化的联系？”*\n  - **Candidate**: 二维矩阵在行主序映射下可看作步长为 $n$ 的跳表或链式索引。",
        "anti_patterns": [("空指针异常", "访问 None.val", "未判空", "操作前必须先判空")],
        "dry_run": "ListNode(1) -> ListNode(2)",
        "time": ("$O(1)$", "节点初始化。"), "space": ("$O(1)$", "单个节点分配。")
    },
    "10-lc-0303-range-sum-query-immutable": {
        "id": "0303", "title_en": "Range Sum Query - Immutable", "title_cn": "区域和检索 - 数组不可变", "diff": "Easy", "topic": "Topic 03: Prefix Sum",
        "en_desc": "Given an integer array `nums`, handle multiple queries of the sum of the elements between indices `left` and `right` inclusive.",
        "cn_desc": "给定一个整数数组  `nums`，处理以下类型的多个查询: 计算索引 `left` 和 `right` （包含 `left` 和 `right`）之间的 `nums` 元素的和 ，其中 `left <= right`。",
        "constraints": "1 <= nums.length <= 10^4, -10^5 <= nums[i] <= 10^5, 0 <= left <= right < nums.length",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 前缀和数组: preSum[i] = nums[0] + ... + nums[i-1]      │\n│ query(left, right) = preSum[right + 1] - preSum[left]  │\n└────────────────────────────────────────────────────────┘",
        "invariant": "区间和减法公理：$$\\sum_{i=l}^r nums[i] = preSum[r+1] - preSum[l]$$",
        "interview_qa": "- **Interviewer**: *“为什么 preSum 长度通常设为 n + 1？”*\n  - **Candidate**: 可以让 `preSum[0] = 0`，使 `left = 0` 时无需进行特殊的条件分支特判。",
        "anti_patterns": [("未偏移 1-index", "preSum[right] - preSum[left-1] 在 left=0 越界", "索引越界", "preSum 开 n+1 长度")],
        "dry_run": "nums=[-2,0,3,-5,2,-1] -> preSum=[0,-2,-2,1,-4,-2,-3] -> sum(0,2) = 1 - 0 = 1",
        "time": ("$O(1)$ 查询, $O(n)$ 预处理", "单次查询仅执行一次减法。"), "space": ("$O(n)$", "前缀和数组空间。")
    },
    "10-lc-0303-range-sum-query-immutable-alt": {
        "id": "0303", "title_en": "Range Sum Query - Immutable (Alt Constructor)", "title_cn": "区域和检索 - 数组不可变 (变体构造)", "diff": "Easy", "topic": "Topic 03: Prefix Sum",
        "en_desc": "Prefix sum implementation using n+1 length array constructor.",
        "cn_desc": "使用 n+1 长度前缀和数组构建的不可变区间求和类。",
        "constraints": "1 <= nums.length <= 10^4",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 前缀和 n+1 构造法                                      │\n└────────────────────────────────────────────────────────┘",
        "invariant": "preSum[i+1] = preSum[i] + nums[i]",
        "interview_qa": "- **Interviewer**: *“与暴力相加相比的优势？”*\n  - **Candidate**: 将 $k$ 次查询由 $O(k \\cdot n)$ 优化为 $O(n + k)$。",
        "anti_patterns": [("累加错位", "下标加减混淆", "索引偏移", "统一公式 preSum[r+1] - preSum[l]")],
        "dry_run": "nums=[1,2,3] -> preSum=[0,1,3,6] -> sum(1,2) = 6 - 1 = 5",
        "time": ("$O(1)$", "单次查询。"), "space": ("$O(n)$", "前缀和数组。")
    },
    "10-lc-0303-prefix-sum-practices": {
        "id": "0303", "title_en": "Prefix Sum Practice & Class Structure", "title_cn": "前缀和与 OOP 面向对象实践", "diff": "Easy", "topic": "Topic 03: OOP & Prefix Sum",
        "en_desc": "Object-oriented class structure and foundational principles for cumulative data modeling.",
        "cn_desc": "面向对象类构造及累加数据建模基础。",
        "constraints": "OOP 基础规范",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 面向对象类封装与状态维护                               │\n└────────────────────────────────────────────────────────┘",
        "invariant": "实例属性封装：`self.attr` 隔离实例内部状态。",
        "interview_qa": "- **Interviewer**: *“类变量与实例变量的区别？”*\n  - **Candidate**: 类变量为所有实例共享，实例变量通过 `self` 绑定于独立实例。",
        "anti_patterns": [("修改类变量误伤全部实例", "通过 self 修改类变量产生遮蔽", "作用域混淆", "类属性统一由类名访问")],
        "dry_run": "Employee('Zara', 2000) -> empCount=1",
        "time": ("$O(1)$", "构造与访问。"), "space": ("$O(1)$", "对象内存。")
    },
    "10-oop-pre-main-practice": {
        "id": "0000", "title_en": "OOP Foundations & Object Instantiation", "title_cn": "面向对象基础与实例初始化", "diff": "Easy", "topic": "Topic 11: OOP Foundations",
        "en_desc": "Foundational object-oriented programming practices in Python covering class definitions and constructors.",
        "cn_desc": "Python 面向对象编程基础：类定义、构造函数与对象实例化。",
        "constraints": "Python 3 OOP 语法规范",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ Class Car -> Instance car_1('Toyota', 'Camry', ...)   │\n└────────────────────────────────────────────────────────┘",
        "invariant": "封装性：对象拥有独立的内部属性状态。",
        "interview_qa": "- **Interviewer**: *“__init__ 和 __new__ 的区别？”*\n  - **Candidate**: `__new__` 负责创建并返回实例，`__init__` 负责初始化实例属性。",
        "anti_patterns": [("忘记 self", "def func() 缺少 self 报错", "缺少实例引用", "首个入参必须为 self")],
        "dry_run": "car_1 = Car('Toyota') -> print(car_1.make) -> 'Toyota'",
        "time": ("$O(1)$", "属性存取。"), "space": ("$O(1)$", "对象实例。")
    },
    "11-lc-0560-subarray-sum-equals-k": {
        "id": "0560", "title_en": "Subarray Sum Equals K", "title_cn": "和为 K 的子数组", "diff": "Medium", "topic": "Topic 03: Prefix Sum + Hash Map",
        "en_desc": "Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.",
        "cn_desc": "给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 该数组中和为 `k` 的子数组的个数 。",
        "constraints": "1 <= nums.length <= 2 * 10^4, -1000 <= nums[i] <= 1000, -10^7 <= k <= 10^7",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 前缀和 + 哈希频次表                                    │\n│ s = sum(nums[0...i])                                   │\n│ 若 s - k 在哈希表中，累计出现次数 ans += cnt[s - k]    │\n│ 累加当前前缀和频次 cnt[s] += 1                         │\n└────────────────────────────────────────────────────────┘",
        "invariant": "子数组和转化等式：$$\\text{sum}(i, j) = s_j - s_{i-1} = k \\iff s_{i-1} = s_j - k$$",
        "interview_qa": "- **Interviewer**: *“为什么不能用滑动窗口求解本题？”*\n  - **Candidate**: 数组中包含负数，窗口扩大或缩小不具备和的单调性，必须使用前缀和哈希表。",
        "anti_patterns": [("漏初始前缀和 {0:1}", "前缀和本身等于 k 时漏计", "边界遗漏", "必须初始化 cnt = {0: 1}")],
        "dry_run": "输入: `nums=[1,1,1], k=2` -> s=1(+0), s=2(+1), s=3(+1) -> ans=2",
        "time": ("$O(n)$", "单遍扫描数组。"), "space": ("$O(n)$", "哈希表大小。")
    },
    "11-prefix-sum-basic-example": {
        "id": "0303", "title_en": "Prefix Sum Basic Calculation", "title_cn": "前缀和基础计算模版", "diff": "Easy", "topic": "Topic 03: Prefix Sum",
        "en_desc": "Basic algorithm to construct a cumulative prefix sum array in-place or with auxiliary array.",
        "cn_desc": "构建前缀和数组的基础函数实现与累加递推。",
        "constraints": "1 <= arr.length <= 10^5",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ prefixSum[i] = prefixSum[i-1] + arr[i]                 │\n└────────────────────────────────────────────────────────┘",
        "invariant": "累加递推：$prefix[i] = prefix[i-1] + arr[i]$",
        "interview_qa": "- **Interviewer**: *“原地修改原数组实现前缀和的优缺点？”*\n  - **Candidate**: 优点是省去 $O(n)$ 空间；缺点是破坏了原数组数据，只读查询场景需权衡。",
        "anti_patterns": [("索引越界", "i=0 时访问 i-1", "边界越界", "i=0 需赋初值 arr[0]")],
        "dry_run": "arr=[10, 20, 10, 5] -> prefixSum=[10, 30, 40, 45]",
        "time": ("$O(n)$", "线性遍历一次。"), "space": ("$O(n)$", "前缀和数组。")
    },
    "12-lc-1109-corporate-flight-bookings": {
        "id": "1109", "title_en": "Corporate Flight Bookings", "title_cn": "航班预订统计", "diff": "Medium", "topic": "Topic 03: Difference Array",
        "en_desc": "There are `n` flights labeled from 1 to `n`. Given a list of flight bookings `bookings` where `bookings[i] = [first, last, seats]`, return an array `answer` of length `n` representing total seats booked for each flight.",
        "cn_desc": "这里有 n 个航班，它们分别从 1 到 n 进行编号。有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [first, last, seats] 意味着在从 first 到 last 的每个航班上预订了 seats 个座位。请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位总数。",
        "constraints": "1 <= n <= 2 * 10^4, 1 <= bookings.length <= 2 * 10^4",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 差分数组区间修改: diff[first-1] += seats, diff[last] -= seats│\n│ 前缀和复原原数组: ans[i] = ans[i-1] + diff[i]          │\n└────────────────────────────────────────────────────────┘",
        "invariant": "差分区间累加性：对差分数组进行单点增减可在前缀和还原时等价于对整个区间加值。",
        "interview_qa": "- **Interviewer**: *“差分数组适用于什么场景？”*\n  - **Candidate**: 适用于频繁进行区间增减 $[l, r, val]$，且最终仅需全量查询一次最终状态的高频场景。",
        "anti_patterns": [("1-indexed 越界", "last 越界导致 diff 数组越界", "未校验 last < n", "当 last < n 时才扣减 diff[last]")],
        "dry_run": "n=5, bookings=[[1,2,10],[2,3,20],[2,5,25]] -> diff=[10, 45, -10, 0, -25] -> ans=[10, 55, 45, 25, 25]",
        "time": ("$O(n + m)$", "$m$ 次区间修改 $O(1)$，单次前缀和还原 $O(n)$。"), "space": ("$O(n)$", "差分数组。")
    },
    "13-lc-0056-merge-intervals": {
        "id": "0056", "title_en": "Merge Intervals", "title_cn": "合并区间", "diff": "Medium", "topic": "Topic 04: Intervals",
        "en_desc": "Given an array of `intervals` where `intervals[i] = [start, end]`, merge all overlapping intervals, and return an array of the non-overlapping intervals.",
        "cn_desc": "以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [start, end]` 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组 。",
        "constraints": "1 <= intervals.length <= 10^4, intervals[i].length == 2, 0 <= start <= end <= 10^4",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 排序 + 贪心合并                                        │\n│ 按 start 升序排序                                      │\n│ 若 cur.start <= prev.end: prev.end = max(prev.end, cur.end) │\n│ 否则开启新区间                                         │\n└────────────────────────────────────────────────────────┘",
        "invariant": "左端点有序性：排序后相交区间必在数组中相邻连续出现。",
        "interview_qa": "- **Interviewer**: *“如果区间已经是按右端点排序的，该如何合并？”*\n  - **Candidate**: 可以从后向前遍历反向合并，或者依然提取并检查相邻重叠。",
        "anti_patterns": [("未更新 max(end)", "直接用 cur.end 覆盖导致大区间被缩小", "未取 max", "必须使用 max(ans[-1][1], interval[1])")],
        "dry_run": "[[1,3],[2,6],[8,10]] -> [1,3]+[2,6] -> [1,6], [8,10] 不重叠 -> [[1,6],[8,10]]",
        "time": ("$O(n \\log n)$", "区间排序耗时。"), "space": ("$O(n)$", "存储合并结果。")
    },
    "14-lc-0041-first-missing-positive": {
        "id": "0041", "title_en": "First Missing Positive", "title_cn": "缺失的第一个正数", "diff": "Hard", "topic": "Topic 04: In-Place Hashing (Cyclic Sort)",
        "en_desc": "Given an unsorted integer array `nums`. Return the smallest positive integer that is not present in `nums`. You must implement an algorithm that runs in $O(n)$ time and uses $O(1)$ auxiliary space.",
        "cn_desc": "给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。",
        "constraints": "1 <= nums.length <= 10^5, -2^31 <= nums[i] <= 2^31 - 1",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 原地哈希 / 归位法 (Cyclic Sort)                         │\n│ 数字 x (1 <= x <= n) 应该放在下标 x - 1 处             │\n│ while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:│\n│   swap(nums[i], nums[nums[i]-1])                       │\n└────────────────────────────────────────────────────────┘",
        "invariant": "归位不变量：扫描后 $nums[i] == i + 1$ 成立，首个不满足处即为缺失正整数。",
        "interview_qa": "- **Interviewer**: *“为什么 while 循环不会导致 O(n^2) 时间复杂度？”*\n  - **Candidate**: 每次有效 swap 都会让至少一个数字回到正确位置，每个数字最多被归位一次，总 swap 次数不超过 $n$ 次，总时间严格为 $O(n)$。",
        "anti_patterns": [("死循环", "swap 两个相同数字 nums[i] == nums[target]", "未防御重复元素", "条件必须为 nums[nums[i]-1] != nums[i]")],
        "dry_run": "nums=[3,4,-1,1] -> 归位后 [1,-1,3,4] -> 下标 1 处为 -1 != 2 -> 返回 2",
        "time": ("$O(n)$", "每个数字最多交换一次。"), "space": ("$O(1)$", "原地数组哈希。")
    },
    "15-lc-0206-reverse-linked-list": {
        "id": "0206", "title_en": "Reverse Linked List", "title_cn": "反转链表", "diff": "Easy", "topic": "Topic 05: Linked Lists",
        "en_desc": "Given the `head` of a singly linked list, reverse the list, and return the reversed list.",
        "cn_desc": "给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。",
        "constraints": "节点数介于 0 到 5000",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 三指针迭代反转: prev=None, curr=head                   │\n│ nxt = curr.next; curr.next = prev; prev = curr; curr = nxt│\n└────────────────────────────────────────────────────────┘",
        "invariant": "反转拓扑不变量：`prev` 始终指向已反转链表的新头节点。",
        "interview_qa": "- **Interviewer**: *“如何用递归方式实现？”*\n  - **Candidate**: 递归反转 `head.next` 后让 `head.next.next = head; head.next = None` 并返回新头。",
        "anti_patterns": [("成环丢失", "未断开原头节点 next", "未设 prev=None", "初始 prev 必须为 None")],
        "dry_run": "1->2->3 -> 1<-2 3 -> 1<-2<-3 -> return 3",
        "time": ("$O(n)$", "单遍遍历链表节点。"), "space": ("$O(1)$", "迭代仅需常数级指针。")
    },
    "16-lc-0021-merge-two-sorted-lists": {
        "id": "0021", "title_en": "Merge Two Sorted Lists", "title_cn": "合并两个有序链表", "diff": "Easy", "topic": "Topic 05: Linked Lists",
        "en_desc": "You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list and return its head.",
        "cn_desc": "将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。",
        "constraints": "两个链表的节点数目范围是 [0, 50], -100 <= Node.val <= 100",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 哨兵头节点 + 双指针穿针引线                            │\n│ dummy = ListNode(0), cur = dummy                       │\n│ 比较 list1.val 与 list2.val，较小者接在 cur.next 后面  │\n└────────────────────────────────────────────────────────┘",
        "invariant": "升序缝合不变量：`cur` 始终指向合并链表的当前尾节点。",
        "interview_qa": "- **Interviewer**: *“哨兵节点 dummy 的核心价值是什么？”*\n  - **Candidate**: 消除头节点为空或首次拼接时的特殊条件分支，简化代码逻辑。",
        "anti_patterns": [("遗漏剩余链表", "while 结束后未拼接非空链表", "遗漏拼接", "cur.next = list1 or list2")],
        "dry_run": "l1=[1,2,4], l2=[1,3,4] -> dummy->1->1->2->3->4->4",
        "time": ("$O(n + m)$", "两链表节点总数。"), "space": ("$O(1)$", "原地拼接复用节点。")
    },
    "17-lc-0141-linked-list-cycle": {
        "id": "0141", "title_en": "Linked List Cycle", "title_cn": "环形链表", "diff": "Easy", "topic": "Topic 05: Linked Lists",
        "en_desc": "Given `head`, the head of a linked list, determine if the linked list has a cycle in it.",
        "cn_desc": "给你一个链表的头节点 `head` ，判断链表中是否有环。",
        "constraints": "链表中节点的数目范围是 [0, 10^4]",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ Floyd 快慢指针 (2:1 相对速度追击)                     │\n│ slow 走 1 步，fast 走 2 步                             │\n│ 若有环，相对速度为 1，fast 必在环内追上 slow           │\n└────────────────────────────────────────────────────────┘",
        "invariant": "相对速度追击公理：相对速度为 1 步/轮，两指针距离每轮减少 1，绝不会发生跨越穿透。",
        "interview_qa": "- **Interviewer**: *“为什么快指针每次走 2 步而不是 3 步？”*\n  - **Candidate**: 每次走 2 步相对速度为 1，必相遇；若走 3 步相对速度为 2，偶数步环可能发生跨跃套圈。",
        "anti_patterns": [("空指针异常", "fast.next.next 未判空", "空指针越界", "循环条件必须为 fast and fast.next")],
        "dry_run": "head=[3,2,0,-4], pos=1 -> slow/fast 在环内节点相遇 -> return True",
        "time": ("$O(n)$", "无环 $n/2$ 步退出，有环追击距离小于环长。"), "space": ("$O(1)$", "仅维护两个指针。")
    },
    "18-lc-0142-linked-list-cycle-ii": {
        "id": "0142", "title_en": "Linked List Cycle II", "title_cn": "环形链表 II", "diff": "Medium", "topic": "Topic 05: Linked Lists",
        "en_desc": "Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.",
        "cn_desc": "给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。",
        "constraints": "链表中节点的数目范围在范围 [0, 10^4] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 数学推导与入环点相遇                                   │\n│ 快慢指针相遇时：快指针走 2k 步，慢指针走 k 步          │\n│ 距离关系: a = c + (n-1)(b+c) -> a ≡ c (mod L)          │\n│ 让指针从 head 与 相遇点 同步单步走，必在入环点相遇     │\n└────────────────────────────────────────────────────────┘",
        "invariant": "步长等式定理：从头节点到入环点的距离 $a$ 等于从相遇点到入环点的距离 $c$ 加上若干整圈数。",
        "interview_qa": "- **Interviewer**: *“推导为什么 a = c？”*\n  - **Candidate**: 慢指针路程 $s = a + b$，快指针路程 $f = a + n(b+c) + b = 2(a+b)$，化简得 $a = (n-1)(b+c) + c$。",
        "anti_patterns": [("返回 True 替代节点", "题目要求返回节点引用", "返回值类型错误", "返回相遇节点指针")],
        "dry_run": "相遇后 ptr1=head, ptr2=meetNode -> 同速前进 -> meet at cycle entry",
        "time": ("$O(n)$", "相遇前 $O(n)$，找入环点 $O(n)$。"), "space": ("$O(1)$", "常数指针。")
    },
    "19-lc-0020-valid-parentheses": {
        "id": "0020", "title_en": "Valid Parentheses", "title_cn": "有效的括号", "diff": "Easy", "topic": "Topic 06: Stacks",
        "en_desc": "Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        "cn_desc": "给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。",
        "constraints": "1 <= s.length <= 10^4",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 栈后进先出匹配 (LIFO Matching)                         │\n│ 遇左括号入栈；遇右括号出栈并检查是否与哈希映射匹配     │\n└────────────────────────────────────────────────────────┘",
        "invariant": "后进先出对称性：最近入栈的未闭合左括号必须与当前遇到的第一个右括号严格闭合配对。",
        "interview_qa": "- **Interviewer**: *“奇数长度字符串如何快速短路优化？”*\n  - **Candidate**: 有效括号必须成对出现，若 `len(s) % 2 != 0` 可直接在首行 `return False`。",
        "anti_patterns": [("空栈 pop 异常", "字符串以右括号开头 stack 为空直接 pop", "IndexError", "pop 前必须检查 not stack")],
        "dry_run": "s='()[]{}' -> stack 依次进出 -> 最终 stack 为空 -> return True",
        "time": ("$O(n)$", "遍历每个字符一次。"), "space": ("$O(n)$", "最坏情况全为左括号存入栈中。")
    },
    "20-lc-0020-valid-parentheses-dict": {
        "id": "0739", "title_en": "Daily Temperatures (Monotonic Stack)", "title_cn": "每日温度 (单调栈基石)", "diff": "Medium", "topic": "Topic 06: Monotonic Stack",
        "en_desc": "Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature.",
        "cn_desc": "给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。",
        "constraints": "1 <= temperatures.length <= 10^5, 30 <= temperatures[i] <= 100",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 单调递减栈 (Monotonic Decreasing Stack)                │\n│ 栈内存放下标，保持对应温度单调递减                     │\n│ 遇到更高温度 x 时，持续弹出栈顶元素并结算天数差        │\n└────────────────────────────────────────────────────────┘",
        "invariant": "单调性结算：当前温度高于栈顶温度时，栈顶元素的下一个更大值已被确定为当前索引。",
        "interview_qa": "- **Interviewer**: *“单调栈适合解决什么类别的题目？”*\n  - **Candidate**: 适合在 $O(n)$ 时间内寻找序列中每个元素左侧/右侧的第一个更大/更小元素（Next Greater Element）。",
        "anti_patterns": [("栈内存放数值而非下标", "无法计算下标天数差", "存储内容失误", "栈内应存储元素下标 i")],
        "dry_run": "temperatures=[73,74,75,71,69,72,76,73] -> ans=[1,1,4,2,1,1,0,0]",
        "time": ("$O(n)$", "每个元素入栈出栈最多各一次。"), "space": ("$O(n)$", "单调栈与输出数组。")
    }
}

def generate_all():
    count = 0
    for stem, data in DB.items():
        filename = f"{stem}.md"
        py_filename = f"{stem}.py"
        py_path = LUFFY_DIR / py_filename
        py_code = py_path.read_text(encoding="utf-8") if py_path.exists() else "# Solution code"
        
        walkthrough_steps = [
            f"基于 `{py_filename}` 原版源码拆解核心数据结构与初始化。",
            f"按关键循环与状态转移推进算法主体逻辑。",
            f"维护核心不变状态并返回最终有效解。"
        ]
        
        create_note(
            filename=filename,
            lc_id=data["id"],
            title_en=data["title_en"],
            title_cn=data["title_cn"],
            diff=data["diff"],
            topic=data["topic"],
            en_desc=data["en_desc"],
            cn_desc=data["cn_desc"],
            constraints=data["constraints"],
            ascii_art=data["ascii"],
            invariant=data["invariant"],
            py_code=py_code,
            walkthrough_steps=walkthrough_steps,
            interview_qa=data["interview_qa"],
            anti_patterns=data["anti_patterns"],
            dry_run_table=data["dry_run"],
            time_comp=data["time"],
            space_comp=data["space"]
        )
        count += 1
    print(f"Successfully generated/upgraded {count} notes in Luffy Topics 01-20.")

if __name__ == "__main__":
    generate_all()
