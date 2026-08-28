#!/usr/bin/env python3
"""
update_index.py - Automated Compiler for LeetCode Study Station SPA (index.html)

Features:
- Scans top-100/, daily-practice/, and luffy/ folders.
- Indexes README.md, ROADMAP.md, and all curriculum topics.
- Compiles an interactive Visual Roadmap view (inspired by labuladong & EndlessCheng).
- Dual split-pane viewer (Syntax-highlighted Python + Markdown 7-section notes).
- Fast client-side fuzzy search, KaTeX math formula rendering, and responsive design.
"""

import os
import re
import json
import time
import argparse
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

def normalize_slug(text: str) -> str:
    """Normalizes problem title to a clean slug for searching."""
    text = re.sub(r'[\(\)\[\]\{\}\.,:;!\?`\'"]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip().lower()
    return text

def build_search_blob(tokens: list, text_content: str = "") -> str:
    """Builds a normalized, space-separated searchable string."""
    combined = " ".join(tokens)
    if text_content:
        clean_text = re.sub(r'[\r\n\t]+', ' ', text_content)
        clean_text = re.sub(r'[#\*`_\[\]\(\)\{\}\.,:;!\?\'"]', ' ', clean_text)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        combined += " " + clean_text[:3000]
    return normalize_slug(combined)

def create_document_item(key, category, title, short, slug, cn_title, tags, lc_num, search_blob, path, doc_type="problem", notes="", code="", diff="All", py_file="", md_file=""):
    """Helper to construct a standardized document metadata item dictionary."""
    return {
        "key": key,
        "category": category,
        "title": title,
        "short": short,
        "slug": slug,
        "cn_title": cn_title,
        "tags": tags,
        "lc_num": lc_num,
        "search_blob": search_blob,
        "path": path,
        "type": doc_type,
        "notes": notes,
        "code": code,
        "diff": diff,
        "py_file": py_file,
        "md_file": md_file,
    }

def collect_workspace_documents():
    """Scans all folders and builds structured problem entities."""
    raw_files = {}
    problems = {}
    topic_docs = {}

    def read_file_content(full_path):
        try:
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    # 1. Parse Topic-Wise Problem Index from README.md Section 5
    readme_path = BASE_DIR / "README.md"
    readme_text = ""
    if readme_path.exists():
        readme_text = read_file_content(readme_path)

        topic_sections = [
            ("topic-all", "Problem Index: Complete Catalog", "All 11 Topics Combined", None),
            ("topic-01-arrays-sliding-window", "1. Arrays, Strings & Sliding Window", "1. Arrays & Sliding Window", "### 1. Arrays, Strings, Two Pointers & Sliding Window"),
            ("topic-02-binary-search", "2. Binary Search", "2. Binary Search", "### 2. Binary Search"),
            ("topic-03-prefix-sum", "3. Prefix Sum & Difference Arrays", "3. Prefix Sum & Difference", "### 3. Prefix Sum & Difference Arrays"),
            ("topic-04-intervals", "4. Intervals & In-Place Hashing", "4. Intervals & In-Place Hash", "### 4. Intervals & In-Place Array Hashing"),
            ("topic-05-linked-lists", "5. Linked Lists", "5. Linked Lists", "### 5. Linked Lists"),
            ("topic-06-stacks-queues", "6. Stacks & Queues", "6. Stacks & Queues", "### 6. Stacks & Queues"),
            ("topic-07-trees-bst", "7. Trees & Binary Search Trees (BST)", "7. Trees & BST", "### 7. Trees & Binary Search Trees (BST)"),
            ("topic-08-backtracking", "8. Backtracking & Combinatorics", "8. Backtracking", "### 8. Backtracking & Combinatorics"),
            ("topic-09-graphs", "9. Graph Algorithms", "9. Graph Algorithms", "### 9. Graph Algorithms"),
            ("topic-10-dp-math", "10. Dynamic Programming & Math / Game Theory", "10. DP & Game Theory", "### 10. Dynamic Programming & Math / Game Theory"),
            ("topic-11-oop", "11. OOP & Foundations", "11. OOP & Foundations", "### 11. Object-Oriented Programming (OOP) & Foundations"),
        ]

        sec5_match = re.search(r'(## (?:📚 )?Topic-Wise Curriculum & Problem Index.*?)(\n## (?:🖥️ )?Interactive Web Viewer|\n## (?:🚀 )?How to Run)', readme_text, re.DOTALL)
        sec5_text = sec5_match.group(1) if sec5_match else readme_text

        for key, title, short, header in topic_sections:
            if key == "topic-all":
                topic_content = f"# Problem Index: Complete Topic-Wise Catalog\n\n{sec5_text}"
            else:
                pattern = re.escape(header) + r'(.*?)(\n### |\n---|\n## )'
                match = re.search(pattern, readme_text, re.DOTALL)
                if match:
                    topic_content = f"# Problem Index — {title}\n\n{header}\n{match.group(1).strip()}"
                else:
                    topic_content = f"# Problem Index — {title}\n\nNo content parsed."

            clean_topic_slug = normalize_slug(title)
            topic_search_blob = build_search_blob(
                [title, short, clean_topic_slug, "problem index topic curriculum"],
                topic_content
            )
            topic_docs[key] = create_document_item(
                key=key,
                category="Problem Index",
                title=title,
                short=short,
                slug=clean_topic_slug,
                cn_title="",
                tags="topic curriculum problem index",
                lc_num="",
                search_blob=topic_search_blob,
                path=f"problem-index/{key}",
                doc_type="doc",
                notes=topic_content,
                diff="All",
            )

    # 2. Overview Documents (README.md & ROADMAP.md)
    readme_search_blob = build_search_blob(
        ["LeetCode Self-Practices Overview (README)", "README.md", "readme overview", "项目总览", "readme overview index 根文档"],
        readme_text
    )
    overview_docs = {
        "README.md": create_document_item(
            key="README.md",
            category="Overview",
            title="LeetCode Self-Practices Overview (README)",
            short="README.md",
            slug="readme overview",
            cn_title="项目总览",
            tags="readme overview index",
            lc_num="",
            search_blob=readme_search_blob,
            path="README.md",
            doc_type="doc",
            notes=readme_text,
            diff="All",
        )
    }

    roadmap_path = BASE_DIR / "ROADMAP.md"
    if roadmap_path.exists():
        roadmap_text = read_file_content(roadmap_path)
        roadmap_search_blob = build_search_blob(
            ["Algorithm Master Roadmap (ROADMAP)", "ROADMAP.md", "roadmap", "全景路线图", "知识图谱", "算法刷题全景路线图"],
            roadmap_text
        )
        overview_docs["ROADMAP.md"] = create_document_item(
            key="ROADMAP.md",
            category="Overview",
            title="Algorithm Master Roadmap (ROADMAP.md)",
            short="ROADMAP.md",
            slug="algorithm master roadmap",
            cn_title="算法全景路线图",
            tags="roadmap curriculum knowledge graph 路线图",
            lc_num="",
            search_blob=roadmap_search_blob,
            path="ROADMAP.md",
            doc_type="doc",
            notes=roadmap_text,
            diff="All",
        )

    # Canonical difficulty dictionary for known LeetCode problems
    KNOWN_DIFFICULTIES = {
        1: "Easy", 2: "Medium", 3: "Medium", 4: "Hard", 5: "Medium",
        10: "Hard", 11: "Medium", 15: "Medium", 16: "Medium", 17: "Medium",
        19: "Medium", 20: "Easy", 21: "Easy", 22: "Medium", 23: "Hard",
        25: "Hard", 26: "Easy", 31: "Medium", 32: "Hard", 33: "Medium",
        34: "Medium", 39: "Medium", 41: "Hard", 42: "Hard", 46: "Medium",
        48: "Medium", 49: "Medium", 53: "Medium", 55: "Medium", 56: "Medium",
        62: "Medium", 64: "Medium", 70: "Easy", 72: "Hard", 75: "Medium",
        76: "Hard", 78: "Medium", 79: "Medium", 82: "Medium", 83: "Easy", 84: "Hard", 85: "Hard",
        92: "Medium", 94: "Easy", 96: "Medium", 98: "Medium", 100: "Easy", 101: "Easy",
        102: "Medium", 103: "Medium", 104: "Easy", 105: "Medium", 110: "Easy", 114: "Medium", 121: "Easy",
        124: "Hard", 128: "Medium", 130: "Medium", 131: "Medium", 136: "Easy", 139: "Medium",
        141: "Easy", 142: "Medium", 143: "Medium", 144: "Easy", 145: "Easy", 146: "Medium", 148: "Medium",
        152: "Medium", 153: "Medium", 155: "Medium", 160: "Easy", 162: "Medium",
        167: "Medium", 169: "Easy", 198: "Medium", 199: "Medium", 200: "Medium", 206: "Easy",
        207: "Medium", 208: "Medium", 209: "Medium", 215: "Medium", 221: "Medium",
        226: "Easy", 227: "Medium", 232: "Easy", 234: "Easy", 235: "Medium", 236: "Medium",
        237: "Medium", 238: "Medium", 239: "Hard", 240: "Medium", 279: "Medium", 283: "Easy",
        287: "Medium", 297: "Hard", 300: "Medium", 301: "Hard", 303: "Easy", 309: "Medium",
        312: "Hard", 322: "Medium", 337: "Medium", 338: "Easy", 347: "Medium",
        394: "Medium", 399: "Medium", 406: "Medium", 416: "Medium", 437: "Medium",
        438: "Medium", 448: "Easy", 494: "Medium", 513: "Medium", 538: "Medium", 543: "Easy",
        560: "Medium", 581: "Medium", 617: "Easy", 621: "Medium", 647: "Medium",
        704: "Easy", 713: "Medium", 739: "Medium", 876: "Easy", 994: "Medium", 1091: "Medium",
        1109: "Medium", 2029: "Medium", 2235: "Easy", 3090: "Easy", 3471: "Easy"
    }

    # 3. Helper to detect difficulty from markdown content or filename
    def extract_difficulty(text: str, filename: str) -> str:
        match = re.search(r'\*\*Difficulty:\*\*\s*(Easy|Medium|Hard)', text, re.IGNORECASE)
        if match:
            return match.group(1).capitalize()
        match = re.search(r'Difficulty[:\s\*]+(Easy|Medium|Hard)', text, re.IGNORECASE)
        if match:
            return match.group(1).capitalize()

        id_match = re.search(r'(?:lc-)?(\d{4})', filename)
        if id_match:
            lc_num = int(id_match.group(1))
            if lc_num in KNOWN_DIFFICULTIES:
                return KNOWN_DIFFICULTIES[lc_num]

        return "Medium"

    # 4. Process Problem Tracks (top-100, daily-practice, luffy)
    tracks = [
        ("top-100", "Top 100 Liked Track"),
        ("daily-practice", "Daily Practice Track"),
        ("luffy", "Luffy Curriculum (01-42)"),
    ]

    for dir_name, cat_title in tracks:
        track_dir = BASE_DIR / dir_name
        if not track_dir.exists():
            continue

        files = sorted(os.listdir(track_dir))
        stem_groups = {}
        for f in files:
            if f.startswith("__") or f.endswith(".pyc") or f == "file_topics.txt":
                continue
            stem = f
            if stem.endswith(".py"):
                stem = stem[:-3]
            elif stem.endswith(".md"):
                stem = stem[:-3]
            if stem not in stem_groups:
                stem_groups[stem] = {"py": None, "md": None}
            if f.endswith(".py"):
                stem_groups[stem]["py"] = f
            elif f.endswith(".md"):
                stem_groups[stem]["md"] = f

        for stem, pair in stem_groups.items():
            py_file = pair["py"]
            md_file = pair["md"]

            py_content = read_file_content(track_dir / py_file) if py_file else ""
            md_content = read_file_content(track_dir / md_file) if md_file else ""

            # Extract title & metadata
            title = stem.replace("-", " ").title()
            lc_num = ""
            m_num = re.search(r'(?:lc-)?(\d{4})', stem)
            if m_num:
                lc_num = f"LC {int(m_num.group(1))}"

            cn_title = ""
            if md_content:
                cn_match = re.search(r'# .*?\| ([\u4e00-\u9fa5A-Za-z0-9\s\(\)]+)', md_content)
                if cn_match:
                    cn_title = cn_match.group(1).strip()

            diff = extract_difficulty(md_content, stem)
            clean_slug = normalize_slug(f"{stem} {cn_title}")
            search_blob = build_search_blob(
                [stem, title, cn_title, lc_num, diff, dir_name, cat_title],
                f"{md_content}\n{py_content}"
            )

            primary_key = f"{dir_name}/{py_file if py_file else md_file}"
            problems[primary_key] = create_document_item(
                key=primary_key,
                category=cat_title,
                title=f"{lc_num} {stem}" if lc_num else title,
                short=py_file if py_file else md_file,
                slug=clean_slug,
                cn_title=cn_title,
                tags=f"{dir_name} {diff.lower()}",
                lc_num=lc_num,
                search_blob=search_blob,
                path=f"{dir_name}/{stem}",
                doc_type="problem",
                notes=md_content,
                code=py_content,
                diff=diff,
                py_file=f"{dir_name}/{py_file}" if py_file else "",
                md_file=f"{dir_name}/{md_file}" if md_file else "",
            )

    all_items = {**overview_docs, **topic_docs, **problems}
    return all_items

ROADMAP_DATA = [
    {
        "phase": 1,
        "phase_name": "Phase 1: 线性结构与双指针基石",
        "phase_badge": "PHASE 01 · 线性与双指针",
        "phase_desc": "数组、链表、栈与队列是所有高级算法的基石，掌握双指针与滑动窗口可以秒杀 50% 线性搜索问题。",
        "topics": [
            {
                "id": "topic-1",
                "title": "数组与哈希查找",
                "subtitle": "Array, Prefix Sum & Difference Array",
                "icon": "hash",
                "formula": "前缀和 s[i+1]=s[i]+x · 差分 diff[l]+=x · 原地哈希置换",
                "problems": [
                    {"num": 1, "name": "Two Sum", "cn": "两数之和", "diff": "Easy", "key": "luffy/02-lc-0001-two-sum.py"},
                    {"num": 303, "name": "Range Sum Query", "cn": "区域和检索", "diff": "Easy", "key": "luffy/10-lc-0303-range-sum-query-immutable.py"},
                    {"num": 560, "name": "Subarray Sum Equals K", "cn": "和为 K 的子数组", "diff": "Medium", "key": "luffy/11-lc-0560-subarray-sum-equals-k.py"},
                    {"num": 1109, "name": "Corporate Flight Bookings", "cn": "航班预订统计", "diff": "Medium", "key": "luffy/12-lc-1109-corporate-flight-bookings.py"},
                    {"num": 56, "name": "Merge Intervals", "cn": "合并区间", "diff": "Medium", "key": "luffy/13-lc-0056-merge-intervals.py"},
                    {"num": 41, "name": "First Missing Positive", "cn": "缺失的第一个正数", "diff": "Hard", "key": "luffy/14-lc-0041-first-missing-positive.py"},
                ]
            },
            {
                "id": "topic-2",
                "title": "双指针与滑动窗口",
                "subtitle": "Two Pointers & Sliding Window",
                "icon": "columns",
                "formula": "短板贪心对撞 · 动态滑窗 [l, r] · 2-Way 极限剪枝 (3Sum)",
                "problems": [
                    {"num": 11, "name": "Container With Most Water", "cn": "盛最多水的容器", "diff": "Medium", "key": "top-100/lc-0011-container-with-most-water.py"},
                    {"num": 15, "name": "3Sum", "cn": "三数之和", "diff": "Medium", "key": "top-100/lc-0015-3sum.py"},
                    {"num": 16, "name": "3Sum Closest", "cn": "最接近的三数之和", "diff": "Medium", "key": "top-100/lc-0016-3-sum-closest.py"},
                    {"num": 167, "name": "Two Sum II", "cn": "两数之和 II 有序数组", "diff": "Medium", "key": "top-100/lc-0167-two-sum-ii-input-array-is-sorted.py"},
                    {"num": 26, "name": "Remove Duplicates", "cn": "删除有序数组重复项", "diff": "Easy", "key": "luffy/05-lc-0026-remove-duplicates-from-sorted-array.py"},
                    {"num": 3, "name": "Longest Substring", "cn": "无重复字符最长子串", "diff": "Medium", "key": "top-100/lc-0003-longest-substring-without-repeating-characters.py"},
                    {"num": 209, "name": "Minimum Size Subarray Sum", "cn": "长度最小子数组", "diff": "Medium", "key": "top-100/lc-0209-minimum-size-subarray-sum.py"},
                    {"num": 713, "name": "Subarray Product Less Than K", "cn": "乘积小于K子数组", "diff": "Medium", "key": "top-100/lc-0713-subarray-product-less-than-k.py"},
                    {"num": 3090, "name": "Max Substring At Most 2", "cn": "最多2次字符最长子串", "diff": "Easy", "key": "daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py"},
                    {"num": 3471, "name": "Largest Almost Missing Integer", "cn": "最大几乎缺失整数", "diff": "Easy", "key": "daily-practice/lc-3471-find-the-largest-almost-missing-integer.py"},
                ]
            },
            {
                "id": "topic-3",
                "title": "单链表穿针引线与快慢指针",
                "subtitle": "Linked List In-Place Mastery",
                "icon": "link",
                "formula": "哨兵 dummy · 3 指针反转 (prev, cur, nxt) · 快慢指针中点/环入口",
                "problems": [
                    {"num": 206, "name": "Reverse Linked List", "cn": "反转链表", "diff": "Easy", "key": "top-100/lc-0206-reverse-linked-list.py"},
                    {"num": 92, "name": "Reverse Linked List II", "cn": "反转链表 II (局部反转)", "diff": "Medium", "key": "daily-practice/lc-0092-reversed-linked-list-2.py"},
                    {"num": 25, "name": "Reverse Nodes in k-Group", "cn": "K 个一组反转链表", "diff": "Hard", "key": "daily-practice/lc-0025-reverse-nodes-in-k-group.py"},
                    {"num": 876, "name": "Middle of Linked List", "cn": "链表的中间结点", "diff": "Easy", "key": "daily-practice/lc-0876-middle-of-the-linked-list.py"},
                    {"num": 143, "name": "Reorder List", "cn": "重排链表 (中点+反转+归并)", "diff": "Medium", "key": "daily-practice/lc-0143-reorder-list.py"},
                    {"num": 141, "name": "Linked List Cycle", "cn": "环形链表 (2:1 碰撞)", "diff": "Easy", "key": "top-100/lc-0141-linked-list-cycle.py"},
                    {"num": 142, "name": "Linked List Cycle II", "cn": "环形链表 II (入口相遇)", "diff": "Medium", "key": "top-100/lc-0142-linked-list-cycle-ii.py"},
                    {"num": 21, "name": "Merge Two Sorted Lists", "cn": "合并有序链表", "diff": "Easy", "key": "luffy/16-lc-0021-merge-two-sorted-lists.py"},
                    {"num": 19, "name": "Remove Nth Node From End", "cn": "删除倒数第 N 节点", "diff": "Medium", "key": "top-100/lc-0019-remove-nth-node-from-end-of-list.py"},
                    {"num": 82, "name": "Remove Duplicates II", "cn": "删除链表重复元素 II", "diff": "Medium", "key": "daily-practice/lc-0082-remove-duplicates-from-sorted-list.py"},
                    {"num": 83, "name": "Remove Duplicates", "cn": "删除链表重复元素", "diff": "Easy", "key": "daily-practice/lc-0083-remove-duplicates-from-sorted-list.py"},
                    {"num": 237, "name": "Delete Node in Linked List", "cn": "删除节点 (替罪羊覆盖)", "diff": "Medium", "key": "daily-practice/lc-0237-delete-node-in-a-linked-list.py"},
                ]
            },
            {
                "id": "topic-4",
                "title": "栈与队列、单调栈",
                "subtitle": "Stack, Queue & Monotonic Stack",
                "icon": "layers",
                "formula": "栈括号匹配 · 辅助最小栈 MinStack · 前后缀最值柱体储水",
                "problems": [
                    {"num": 20, "name": "Valid Parentheses", "cn": "有效的括号", "diff": "Easy", "key": "luffy/19-lc-0020-valid-parentheses.py"},
                    {"num": 155, "name": "Min Stack", "cn": "最小栈", "diff": "Medium", "key": "luffy/21-lc-0155-min-stack.py"},
                    {"num": 232, "name": "Queue using Stacks", "cn": "用栈实现队列", "diff": "Easy", "key": "luffy/24-lc-0232-implement-queue-using-stacks.py"},
                    {"num": 227, "name": "Basic Calculator II", "cn": "基本计算器 II", "diff": "Medium", "key": "luffy/22-lc-0227-basic-calculator-ii.py"},
                    {"num": 394, "name": "Decode String", "cn": "字符串解码", "diff": "Medium", "key": "luffy/23-lc-0394-decode-string.py"},
                    {"num": 42, "name": "Trapping Rain Water", "cn": "接雨水 (前后缀/双指针)", "diff": "Hard", "key": "top-100/lc-0042-trapping-rain-water.py"},
                ]
            }
        ]
    },
    {
        "phase": 2,
        "phase_name": "Phase 2: 经典二分与极限搜索",
        "phase_badge": "PHASE 02 · 经典二分",
        "phase_desc": "红蓝染色法统一所有二分边界，将对数复杂度应用到旋转数组、峰值极值与二分答案判定中。",
        "topics": [
            {
                "id": "topic-5",
                "title": "二分查找与红蓝染色法",
                "subtitle": "Binary Search & Red-Blue Framework",
                "icon": "git-commit",
                "formula": "开区间 (-1, n) 红蓝收缩 · 万能 lower_bound · nums[-1] 旋转锚点",
                "problems": [
                    {"num": 704, "name": "Binary Search", "cn": "二分查找", "diff": "Easy", "key": "luffy/07-lc-0704-binary-search.py"},
                    {"num": 34, "name": "First & Last Position", "cn": "排序数组查找首末位置", "diff": "Medium", "key": "top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py"},
                    {"num": 33, "name": "Search in Rotated Array", "cn": "搜索旋转排序数组", "diff": "Medium", "key": "top-100/lc-0033-search-in-rotated-sorted-array.py"},
                    {"num": 153, "name": "Find Min in Rotated Array", "cn": "寻找旋转数组最小值", "diff": "Medium", "key": "daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py"},
                    {"num": 162, "name": "Find Peak Element", "cn": "寻找峰值 (爬坡二分)", "diff": "Medium", "key": "top-100/lc-0162-find-peak-element.py"},
                ]
            },
            {
                "id": "topic-6",
                "title": "二分答案与单调性判定",
                "subtitle": "Binary Search on Answer",
                "icon": "target",
                "formula": "单调判定 check(mid) · 最小化最大值 / 最大化最小值",
                "problems": []
            }
        ]
    },
    {
        "phase": 3,
        "phase_name": "Phase 3: 树形结构与递归本原",
        "phase_badge": "PHASE 03 · 树与递归",
        "phase_desc": "树是递归思维的最佳训练场。前序自顶向下、后序自底向上分治、BFS 层序遍历与 BST 有序性质。",
        "topics": [
            {
                "id": "topic-7",
                "title": "二叉树与递归分治",
                "subtitle": "Binary Tree DFS & Divide-and-Conquer",
                "icon": "git-pull-request",
                "formula": "自底向上 1+max(l, r) · 对称镜像 isMirror · LCA 四状态归并",
                "problems": [
                    {"num": 104, "name": "Maximum Depth of Tree", "cn": "二叉树的最大深度", "diff": "Easy", "key": "top-100/lc-0104-maximum-depth-of-binary-tree.py"},
                    {"num": 100, "name": "Same Tree", "cn": "相同的树", "diff": "Easy", "key": "daily-practice/lc-0100-same-tree.py"},
                    {"num": 101, "name": "Symmetric Tree", "cn": "对称二叉树", "diff": "Easy", "key": "top-100/lc-0101-symmetric-tree.py"},
                    {"num": 110, "name": "Balanced Binary Tree", "cn": "平衡二叉树 (-1 剪枝)", "diff": "Easy", "key": "daily-practice/lc-0110-balanced-binary-tree.py"},
                    {"num": 236, "name": "Lowest Common Ancestor", "cn": "二叉树的最近公共祖先", "diff": "Medium", "key": "top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py"},
                    {"num": 105, "name": "Construct Tree Pre/In", "cn": "从前序与中序遍历构造二叉树", "diff": "Medium", "key": "luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py"},
                    {"num": 94, "name": "Inorder Traversal", "cn": "二叉树的中序遍历", "diff": "Easy", "key": "luffy/25-lc-0094-binary-tree-inorder-traversal.py"},
                    {"num": 144, "name": "Preorder Traversal", "cn": "二叉树的前序遍历", "diff": "Easy", "key": "luffy/25-lc-0144-binary-tree-preorder-traversal.py"},
                    {"num": 145, "name": "Postorder Traversal", "cn": "二叉树的后序遍历", "diff": "Easy", "key": "luffy/25-lc-0145-binary-tree-postorder-traversal.py"},
                ]
            },
            {
                "id": "topic-8",
                "title": "广度优先搜索与层序遍历",
                "subtitle": "Binary Tree BFS & Level Order",
                "icon": "list",
                "formula": "单队列快照 len(q) · 双数组滚动 (cur, nxt) · 逆序 BFS (先右后左)",
                "problems": [
                    {"num": 102, "name": "Level Order Traversal", "cn": "二叉树的层序遍历", "diff": "Medium", "key": "top-100/lc-0102-binary-tree-level-order-traversal.py"},
                    {"num": 103, "name": "Zigzag Level Order", "cn": "二叉树的锯齿形层序遍历", "diff": "Medium", "key": "daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py"},
                    {"num": 513, "name": "Find Bottom Left Value", "cn": "找树左下角的值 (逆序 BFS)", "diff": "Medium", "key": "daily-practice/lc-0513-find-bottom-left-tree-value.py"},
                    {"num": 199, "name": "Right Side View", "cn": "二叉树的右视图", "diff": "Medium", "key": "daily-practice/lc-0199-binary-tree-right-side-view.py"},
                ]
            },
            {
                "id": "topic-9",
                "title": "二叉搜索树性质与操作",
                "subtitle": "Binary Search Tree BST",
                "icon": "sliders",
                "formula": "上下界约束 (low, high) · 中序遍历严格单调递增 · BST 值域分流",
                "problems": [
                    {"num": 98, "name": "Validate BST", "cn": "验证二叉搜索树", "diff": "Medium", "key": "luffy/29-lc-0098-validate-binary-search-tree-inorder.py"},
                    {"num": 235, "name": "LCA of BST", "cn": "二叉搜索树的最近公共祖先", "diff": "Medium", "key": "daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py"},
                ]
            }
        ]
    },
    {
        "phase": 4,
        "phase_name": "Phase 4: 暴力搜索与回溯算法",
        "phase_badge": "PHASE 04 · 回溯决策树",
        "phase_desc": "回溯是增量穷举解空间的递归过程。建立「回溯三问」模型，区分 0/1 决策与多叉搜索，精准树层去重。",
        "topics": [
            {
                "id": "topic-10",
                "title": "回溯三问模型与决策树",
                "subtitle": "Backtracking & Search Trees",
                "icon": "shuffle",
                "formula": "回溯三问 · 0-1 选/不选二叉树 vs 多叉树前序收集 · 树层去重 (j > i)",
                "problems": [
                    {"num": 17, "name": "Letter Combinations", "cn": "电话号码字母组合 (笛卡尔积)", "diff": "Medium", "key": "top-100/lc-0017-letter-combinations-of-a-phone-number.py"},
                    {"num": 78, "name": "Subsets", "cn": "子集 (0-1 选/不选 vs 枚举多叉树)", "diff": "Medium", "key": "top-100/lc-0078-subsets.py"},
                    {"num": 77, "name": "Combinations", "cn": "组合 (定长组合 + 剩余剪枝)", "diff": "Medium", "key": "luffy/31-lc-0077-combinations.py"},
                    {"num": 39, "name": "Combination Sum", "cn": "组合总和 (无限复用回溯)", "diff": "Medium", "key": "luffy/34-lc-0039-combination-sum.py"},
                    {"num": 40, "name": "Combination Sum II", "cn": "组合总和 II (排序+树层去重)", "diff": "Medium", "key": "luffy/35-lc-0040-combination-sum-ii.py"},
                    {"num": 46, "name": "Permutations", "cn": "全排列 (used 数组/原地交换)", "diff": "Medium", "key": "luffy/32-lc-0046-permutations.py"},
                    {"num": 131, "name": "Palindrome Partitioning", "cn": "分割回文串 (隔板切分+回文剪枝)", "diff": "Medium", "key": "daily-practice/lc-0131-palindrome-partitioning.py"},
                    {"num": 79, "name": "Word Search", "cn": "单词搜索 (2D 网格 DFS + 回溯)", "diff": "Medium", "key": "luffy/37-lc-0079-word-search.py"},
                ]
            }
        ]
    },
    {
        "phase": 5,
        "phase_name": "Phase 5: 动态规划与进阶算法",
        "phase_badge": "PHASE 05 · 动态规划与进阶",
        "phase_desc": "子问题重叠与最优子结构。从记忆化搜索到递推表格，从经典 Kadane、背包九讲到图论拓扑排序与博弈论。",
        "topics": [
            {
                "id": "topic-11",
                "title": "动态规划核心与子问题递推",
                "subtitle": "Dynamic Programming Foundations",
                "icon": "trending-up",
                "formula": "状态定义 dp[i] · Kadane 最大子数组 · 0-1/完全背包遍历顺序",
                "problems": [
                    {"num": 53, "name": "Maximum Subarray", "cn": "最大子数组和 (Kadane 状态压缩)", "diff": "Medium", "key": "top-100/lc-0053-maximum-subarray.py"},
                    {"num": 130, "name": "Surrounded Regions", "cn": "被围绕的区域 (边界逆向 FloodFill)", "diff": "Medium", "key": "luffy/39-lc-0130-surrounded-regions.py"},
                    {"num": 200, "name": "Number of Islands", "cn": "岛屿数量 (沉岛 DFS / 并查集)", "diff": "Medium", "key": "luffy/38-lc-0200-number-of-islands.py"},
                    {"num": 994, "name": "Rotting Oranges", "cn": "腐烂的橘子 (多源网格 BFS)", "diff": "Medium", "key": "luffy/40-lc-0994-rotting-oranges.py"},
                    {"num": 1091, "name": "Shortest Path in Matrix", "cn": "二进制矩阵最短路 (8 联通 BFS)", "diff": "Medium", "key": "luffy/41-lc-1091-shortest-path-in-binary-matrix.py"},
                ]
            },
            {
                "id": "topic-12",
                "title": "图论拓扑排序与博弈数论",
                "subtitle": "Graph Topology & Game Theory",
                "icon": "share-2",
                "formula": "Kahn 入度表 BFS · 3 色标记 DFS 环检测 · 模 3 同余博弈奇偶分析",
                "problems": [
                    {"num": 207, "name": "Course Schedule", "cn": "课程表 (拓扑排序 Kahn BFS / DFS)", "diff": "Medium", "key": "luffy/42-lc-0207-course-schedule.py"},
                    {"num": 2029, "name": "Stone Game IX", "cn": "石子游戏 IX (模 3 同余分类博弈)", "diff": "Medium", "key": "daily-practice/lc-2029-stone-game-ix.py"},
                ]
            }
        ]
    }
]

def build_index_html():
    """Generates the single-page index.html file with visual roadmap and dual split-pane view."""
    all_items = collect_workspace_documents()
    items_json = json.dumps(all_items)
    roadmap_json = json.dumps(ROADMAP_DATA)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LeetCode-SH | Algorithm Master Station</title>
  <!-- Marked for Markdown Rendering -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <!-- Highlight.js for Syntax Highlighting -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
  <!-- KaTeX for Math Formulas -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <style>
    :root {{
      --bg-main: #0d1117;
      --bg-sidebar: #161b22;
      --bg-panel: #0d1117;
      --border-color: #30363d;
      --border-subtle: #21262d;
      --text-main: #c9d1d9;
      --text-bright: #f0f6fc;
      --text-muted: #8b949e;
      --accent: #58a6ff;
      --accent-hover: #1f6feb;
      --card-bg: #1c2128;
      --code-bg: #161b22;
      --diff-easy: #3fb950;
      --diff-medium: #d29922;
      --diff-hard: #f85149;
      --sidebar-width: 320px;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    /* Minimalist Dark Theme Scrollbars */
    ::-webkit-scrollbar {{
      width: 7px;
      height: 7px;
      background-color: transparent;
    }}
    ::-webkit-scrollbar-track {{
      background-color: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
      background-color: rgba(139, 148, 158, 0.28);
      border-radius: 6px;
      border: 1px solid transparent;
      background-clip: padding-box;
      transition: background-color 0.2s ease;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background-color: rgba(139, 148, 158, 0.55);
    }}
    * {{
      scrollbar-width: thin;
      scrollbar-color: rgba(139, 148, 158, 0.28) transparent;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      display: flex;
      height: 100vh;
      overflow: hidden;
    }}

    /* Mobile Backdrop */
    #sidebar-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background-color: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(3px);
      z-index: 990;
      opacity: 0;
      transition: opacity 0.25s ease;
    }}
    #sidebar-backdrop.active {{
      display: block;
      opacity: 1;
    }}

    /* Left Sidebar Navigation (Tree Explorer) */
    #sidebar {{
      width: var(--sidebar-width);
      min-width: 220px;
      max-width: 650px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      height: 100%;
      position: relative;
      flex-shrink: 0;
      z-index: 20;
      transition: width 0.2s cubic-bezier(0.4, 0, 0.2, 1), margin-left 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.25s ease;
    }}
    #sidebar.collapsed {{
      width: 0 !important;
      min-width: 0 !important;
      max-width: 0 !important;
      margin-left: 0;
      border-right: none;
      overflow: hidden;
      pointer-events: none;
    }}
    #sidebar.collapsed > * {{
      display: none !important;
    }}

    /* Resizer Handle */
    .resizer {{
      position: absolute;
      top: 0;
      right: -3px;
      width: 6px;
      height: 100%;
      cursor: col-resize;
      z-index: 30;
    }}
    .resizer:hover, .resizer.dragging {{
      background-color: var(--accent);
    }}

    /* Sidebar Header & Brand */
    .sidebar-header {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 10px;
      background-color: var(--bg-sidebar);
    }}
    .header-brand {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .brand-title {{
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text-bright);
      display: flex;
      align-items: center;
      gap: 7px;
      letter-spacing: 0.2px;
    }}
    .brand-svg {{
      color: var(--accent);
      flex-shrink: 0;
    }}
    .progress-badge {{
      font-size: 11px;
      font-weight: 600;
      background-color: rgba(56, 139, 253, 0.15);
      color: var(--accent);
      padding: 2px 7px;
      border-radius: 12px;
      border: 1px solid rgba(56, 139, 253, 0.3);
    }}

    /* Search Box */
    .search-box-wrapper {{
      position: relative;
      display: flex;
      align-items: center;
    }}
    .search-icon {{
      position: absolute;
      left: 9px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      pointer-events: none;
    }}
    .search-box {{
      width: 100%;
      background-color: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 6px 28px 6px 28px;
      color: var(--text-bright);
      font-size: 12px;
      outline: none;
      transition: all 0.15s;
    }}
    .search-box:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.18);
    }}
    .search-clear-btn {{
      position: absolute;
      right: 7px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 2px;
      border-radius: 4px;
    }}
    .search-clear-btn:hover {{
      color: var(--text-bright);
      background-color: rgba(139, 148, 158, 0.2);
    }}
    .search-clear-btn.visible {{
      display: flex;
    }}

    /* Explorer Top Bar */
    .explorer-bar {{
      padding: 8px 14px 6px;
      font-size: 10.5px;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .explorer-actions {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .icon-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      padding: 2px 4px;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: color 0.15s;
    }}
    .icon-btn:hover {{
      color: var(--text-bright);
      background-color: rgba(139, 148, 158, 0.2);
    }}

    /* Tree View Container */
    .tree-container {{
      flex: 1;
      overflow-y: auto;
      padding: 6px 0 16px;
    }}
    .tree-folder {{
      user-select: none;
      margin-bottom: 2px;
    }}
    .tree-folder-header {{
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      cursor: pointer;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-main);
      transition: background-color 0.15s, color 0.15s;
    }}
    .tree-folder-header:hover {{
      background-color: rgba(177, 186, 196, 0.12);
      color: var(--text-bright);
    }}
    .folder-arrow {{
      width: 14px;
      height: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-muted);
      transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);
      flex-shrink: 0;
    }}
    .tree-folder.collapsed .folder-arrow {{
      transform: rotate(-90deg);
    }}
    .folder-icon {{
      color: var(--accent);
      display: flex;
      align-items: center;
      flex-shrink: 0;
    }}
    .folder-name {{
      flex: 1;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .folder-count {{
      font-size: 10.5px;
      color: var(--text-muted);
      background: rgba(139, 148, 158, 0.15);
      padding: 1px 5px;
      border-radius: 8px;
      font-weight: 500;
    }}
    .tree-children {{
      display: block;
      padding-left: 20px;
      position: relative;
    }}
    .tree-children::before {{
      content: "";
      position: absolute;
      left: 17px;
      top: 0;
      bottom: 6px;
      width: 1px;
      background-color: rgba(240, 246, 252, 0.12);
    }}
    .tree-folder.collapsed .tree-children {{
      display: none;
    }}

    /* Tree Nav Items */
    .nav-item {{
      display: flex;
      align-items: center;
      gap: 7px;
      padding: 5px 12px 5px 6px;
      font-size: 12px;
      color: var(--text-main);
      cursor: pointer;
      border-radius: 4px;
      margin: 1px 6px 1px 0;
      position: relative;
      transition: all 0.15s;
    }}
    .tree-children > .nav-item::before {{
      content: "";
      position: absolute;
      top: 50%;
      left: -3px;
      width: 6px;
      height: 1px;
      background-color: rgba(240, 246, 252, 0.12);
    }}
    .nav-item.root-leaf {{
      padding-left: 24px;
      margin: 1px 8px 1px 8px;
      position: relative;
    }}
    .nav-item.root-leaf:hover {{
      background-color: rgba(177, 186, 196, 0.12);
      color: var(--text-bright);
    }}
    .nav-item.active {{
      background-color: rgba(56, 139, 253, 0.15);
      color: var(--accent);
      font-weight: 600;
    }}
    .tree-title {{
      flex: 1;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .tree-diff-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      flex-shrink: 0;
      margin-left: auto;
      display: inline-block;
    }}
    .diff-Easy {{
      background-color: var(--diff-easy);
      box-shadow: 0 0 5px rgba(63, 185, 80, 0.45);
    }}
    .diff-Medium {{
      background-color: var(--diff-medium);
      box-shadow: 0 0 5px rgba(210, 153, 34, 0.45);
    }}
    .diff-Hard {{
      background-color: var(--diff-hard);
      box-shadow: 0 0 5px rgba(248, 81, 73, 0.45);
    }}
    .diff-All {{ display: none; }}

    /* Main Container */
    #main-container {{
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      background-color: var(--bg-main);
      min-width: 0;
    }}

    /* Top Toolbar */
    .top-toolbar {{
      height: 46px;
      min-height: 46px;
      background-color: var(--bg-sidebar);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 14px;
      gap: 12px;
      z-index: 10;
    }}
    .toolbar-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 0;
      flex: 1;
    }}
    .toggle-sidebar-btn {{
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      width: 28px;
      height: 28px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }}
    .toggle-sidebar-btn:hover {{
      background: rgba(177, 186, 196, 0.12);
      color: #fff;
      border-color: var(--accent);
    }}

    /* Main Mode Switcher (Roadmap vs Workspace) */
    .main-mode-switcher {{
      display: inline-flex;
      background-color: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 2px;
      gap: 2px;
      flex-shrink: 0;
    }}
    .mode-nav-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 500;
      border-radius: 4px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }}
    .mode-nav-btn:hover {{
      color: var(--text-bright);
      background-color: rgba(255, 255, 255, 0.05);
    }}
    .mode-nav-btn.active {{
      background-color: #238636;
      color: #ffffff;
      font-weight: 600;
      box-shadow: 0 0 8px rgba(35, 134, 54, 0.4);
    }}

    .breadcrumb {{
      display: flex;
      align-items: center;
      gap: 7px;
      font-size: 12.5px;
      color: var(--text-main);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .breadcrumb-folder {{
      color: var(--text-muted);
    }}
    .breadcrumb-sep {{
      color: var(--text-muted);
      opacity: 0.5;
      font-size: 11px;
    }}
    .breadcrumb-file {{
      font-weight: 600;
      color: var(--text-bright);
    }}
    .diff-badge {{
      font-size: 10.5px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 10px;
      margin-left: 4px;
    }}
    .diff-badge.Easy {{
      background-color: rgba(63, 185, 80, 0.15);
      color: var(--diff-easy);
      border: 1px solid rgba(63, 185, 80, 0.3);
    }}
    .diff-badge.Medium {{
      background-color: rgba(210, 153, 34, 0.15);
      color: var(--diff-medium);
      border: 1px solid rgba(210, 153, 34, 0.3);
    }}
    .diff-badge.Hard {{
      background-color: rgba(248, 81, 73, 0.15);
      color: var(--diff-hard);
      border: 1px solid rgba(248, 81, 73, 0.3);
    }}
    .diff-badge.All {{ display: none; }}

    .toolbar-right {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .segmented-control {{
      display: inline-flex;
      background-color: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 2px;
      gap: 2px;
    }}
    .seg-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 4px 9px;
      font-size: 11.5px;
      font-weight: 500;
      border-radius: 4px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }}
    .seg-btn:hover {{
      color: var(--text-bright);
    }}
    .seg-btn.active {{
      background-color: var(--bg-sidebar);
      color: var(--accent);
      font-weight: 600;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    }}
    .action-btn {{
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 4px 10px;
      font-size: 11.5px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }}
    .action-btn:hover {{
      background-color: rgba(177, 186, 196, 0.12);
      color: #fff;
      border-color: var(--text-muted);
    }}

    /* ========================================================= */
    /* Roadmap Master View CSS (labuladong-inspired Layout)     */
    /* ========================================================= */
    #roadmap-view {{
      display: none;
      flex: 1;
      flex-direction: column;
      overflow-y: auto;
      background: radial-gradient(circle at 50% 0%, rgba(56, 139, 253, 0.05) 0%, transparent 50%), var(--bg-main);
      padding: 24px 32px 60px;
    }}
    #roadmap-view.active {{
      display: flex;
    }}
    #workspace.hidden-view {{
      display: none !important;
    }}

    .roadmap-hero {{
      max-width: 1140px;
      margin: 0 auto 28px;
      width: 100%;
      text-align: center;
    }}
    .roadmap-hero .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 14px;
      border-radius: 20px;
      background: rgba(88, 166, 255, 0.12);
      border: 1px solid rgba(88, 166, 255, 0.3);
      color: var(--accent);
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.8px;
      margin-bottom: 12px;
      text-transform: uppercase;
    }}
    .roadmap-hero h1 {{
      font-size: clamp(22px, 2.2vw, 30px);
      font-weight: 800;
      color: var(--text-bright);
      margin-bottom: 8px;
      letter-spacing: -0.5px;
    }}
    .roadmap-hero p {{
      color: var(--text-muted);
      font-size: 14px;
      max-width: 720px;
      margin: 0 auto 18px;
      line-height: 1.6;
    }}
    .phase-filter-bar {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 8px;
      margin-top: 14px;
    }}
    .phase-filter-btn {{
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 5px 13px;
      border-radius: 20px;
      font-size: 12px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .phase-filter-btn:hover {{
      border-color: var(--accent);
      color: var(--text-bright);
    }}
    .phase-filter-btn.active {{
      background: var(--accent);
      color: #0d1117;
      border-color: var(--accent);
      font-weight: 700;
    }}

    .roadmap-phases-container {{
      max-width: 1140px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }}
    .phase-section {{
      background: var(--bg-sidebar);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px 22px;
      position: relative;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    .phase-section:hover {{
      border-color: rgba(88, 166, 255, 0.4);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
    }}
    .phase-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .phase-title-group {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .phase-badge-pill {{
      font-size: 11px;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 12px;
      background: rgba(56, 139, 253, 0.15);
      color: var(--accent);
      border: 1px solid rgba(56, 139, 253, 0.3);
    }}
    .phase-title-text {{
      font-size: 16px;
      font-weight: 700;
      color: var(--text-bright);
    }}
    .phase-desc {{
      font-size: 12.5px;
      color: var(--text-muted);
      margin-bottom: 16px;
      line-height: 1.5;
    }}
    .phase-topics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
      gap: 14px;
    }}

    .topic-card {{
      background: var(--card-bg);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 15px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .topic-card:hover {{
      border-color: var(--accent);
      transform: translateY(-2px);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }}
    .topic-card-top {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 8px;
    }}
    .topic-card-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-bright);
      line-height: 1.3;
    }}
    .topic-card-subtitle {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 2px;
    }}
    .topic-card-count {{
      font-size: 10.5px;
      background: rgba(139, 148, 158, 0.15);
      color: var(--text-main);
      padding: 2px 7px;
      border-radius: 10px;
      white-space: nowrap;
      font-weight: 600;
    }}
    .topic-formula-badge {{
      background: rgba(13, 17, 23, 0.85);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 6px 9px;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 11px;
      color: #7ee787;
      line-height: 1.4;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .topic-formula-badge svg {{
      flex-shrink: 0;
      opacity: 0.8;
    }}
    .topic-pills-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 4px;
    }}
    .topic-problem-pill {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 500;
      background: var(--code-bg);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      text-decoration: none;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .topic-problem-pill:hover {{
      border-color: var(--accent);
      color: var(--accent);
      transform: scale(1.03);
      background: rgba(56, 139, 253, 0.1);
    }}
    .pill-diff-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      flex-shrink: 0;
    }}

    /* ========================================================= */
    /* Workspace Dual Split View                                 */
    /* ========================================================= */
    #workspace {{
      flex: 1;
      display: flex;
      height: calc(100vh - 46px);
      overflow: hidden;
      position: relative;
    }}
    .pane {{
      flex: 1;
      overflow-y: auto;
      padding: 24px 32px 60px;
      display: flex;
      flex-direction: column;
      min-width: 0;
    }}
    #left-pane {{
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
    }}
    #right-pane {{
      background-color: var(--bg-main);
    }}
    .workspace-resizer {{
      width: 5px;
      margin: 0 -2.5px;
      cursor: col-resize;
      background: transparent;
      z-index: 15;
      transition: background-color 0.15s;
    }}
    .workspace-resizer:hover, .workspace-resizer.dragging {{
      background-color: var(--accent);
    }}
    .pane-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }}
    .pane-title {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.6px;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .markdown-body {{
      color: var(--text-main);
      max-width: 860px;
      margin: 0 auto;
      line-height: 1.75;
      font-size: clamp(14px, 0.98vw, 15.5px);
    }}
    .markdown-body h1, .markdown-body h2, .markdown-body h3 {{
      color: #f0f6fc;
      margin-top: 24px;
      margin-bottom: 12px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 6px;
    }}
    .markdown-body p, .markdown-body ul, .markdown-body ol {{
      margin-bottom: 14px;
    }}
    .markdown-body code {{
      background-color: var(--code-bg);
      padding: 2px 6px;
      border-radius: 4px;
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
      font-size: 85%;
      border: 1px solid rgba(240, 246, 252, 0.1);
    }}
    .markdown-body pre {{
      background-color: var(--code-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 18px;
      overflow-x: auto;
    }}
    .markdown-body pre code {{
      border: none;
      padding: 0;
      background-color: transparent;
      font-size: 13px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}
    .markdown-body table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
    }}
    .markdown-body th, .markdown-body td {{
      border: 1px solid var(--border-color);
      padding: 8px 12px;
      text-align: left;
    }}
    .markdown-body th {{
      background-color: var(--bg-sidebar);
      color: #f0f6fc;
    }}
    .markdown-body a {{
      color: var(--accent);
      text-decoration: none;
    }}
    .markdown-body a:hover {{
      text-decoration: underline;
    }}
    .markdown-body blockquote {{
      border-left: 4px solid var(--accent);
      padding: 8px 16px;
      background-color: var(--card-bg);
      border-radius: 0 6px 6px 0;
      margin-bottom: 16px;
      color: #f0f6fc;
    }}

    .code-viewer {{
      flex: 1;
      background-color: var(--code-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      overflow: auto;
      padding: 16px;
    }}
    .code-viewer pre code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: clamp(13px, 0.9vw, 14.5px);
      line-height: 1.65;
    }}

    @media (max-width: 768px) {{
      #sidebar {{
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        width: min(85vw, 340px) !important;
        min-width: unset !important;
        max-width: unset !important;
        z-index: 1000;
        transform: translateX(-100%);
        transition: transform 0.25s ease;
        box-shadow: none;
      }}
      #sidebar.mobile-open {{
        transform: translateX(0);
        box-shadow: 4px 0 30px rgba(0, 0, 0, 0.7);
      }}
      #sidebar.collapsed {{
        transform: translateX(-100%);
        width: min(85vw, 340px) !important;
      }}
      .resizer {{
        display: none !important;
      }}
      .top-toolbar {{
        padding: 0 10px;
      }}
      .breadcrumb {{
        font-size: 11.5px;
      }}
      .seg-label {{
        display: none;
      }}
      #workspace {{
        flex-direction: column;
      }}
      #left-pane {{
        border-right: none;
        border-bottom: 1px solid var(--border-color);
        padding: 16px 20px;
      }}
      #right-pane {{
        padding: 16px 20px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Mobile Backdrop -->
  <div id="sidebar-backdrop" onclick="toggleSidebar(false)"></div>

  <!-- Left Sidebar Navigation (Tree Explorer) -->
  <aside id="sidebar">
    <div class="sidebar-header">
      <div class="header-brand">
        <div class="brand-title">
          <svg class="brand-svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
          <span>LeetCode-SH</span>
        </div>
        <span class="progress-badge" id="progressStats" title="Total Indexed Problems">0 Problems</span>
      </div>
      <div class="search-box-wrapper">
        <span class="search-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></span>
        <input type="text" id="search" class="search-box" placeholder="Search problems, patterns... (/)" oninput="handleSearch(this.value)">
        <button id="searchClear" class="search-clear-btn" onclick="clearSearch()" title="Clear search (Esc)"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button>
      </div>
    </div>

    <div class="explorer-bar">
      <span>EXPLORER</span>
      <div class="explorer-actions">
        <button class="icon-btn" onclick="setAllFoldersCollapsed(false)" title="Expand All Folders">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
        </button>
        <button class="icon-btn" onclick="setAllFoldersCollapsed(true)" title="Collapse All Folders">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 11 12 6 7 11"></polyline><polyline points="17 18 12 13 7 18"></polyline></svg>
        </button>
      </div>
    </div>

    <div class="tree-container" id="treeRoot">
      <!-- Injected dynamically by JavaScript -->
    </div>

    <!-- Draggable Resize Splitter Handle -->
    <div id="resizer" class="resizer" title="Drag to resize sidebar"></div>
  </aside>

  <!-- Main Content Workspace -->
  <main id="main-container">
    <header class="top-toolbar">
      <div class="toolbar-left">
        <button class="toggle-sidebar-btn" id="sidebarToggle" onclick="toggleSidebar()" title="Toggle Sidebar (Cmd+B / Ctrl+B)">
          <svg width="15" height="15" viewBox="0 0 16 16" fill="currentColor">
            <path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 010 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 010 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 000 1.5h12.5a.75.75 0 000-1.5H1.75z"></path>
          </svg>
        </button>

        <!-- Main Mode Switcher: Roadmap vs Workspace -->
        <div class="main-mode-switcher">
          <button class="mode-nav-btn active" id="btnModeRoadmap" onclick="setMainMode('roadmap')" title="Interactive Visual Roadmap">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon><line x1="9" y1="3" x2="9" y2="18"></line><line x1="15" y1="6" x2="15" y2="21"></line></svg>
            <span>Roadmap</span>
          </button>
          <button class="mode-nav-btn" id="btnModeWorkspace" onclick="setMainMode('workspace')" title="Dual-Split Problem Workspace">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            <span>Workspace</span>
          </button>
        </div>

        <div class="breadcrumb" id="itemBreadcrumb">Loading...</div>
      </div>

      <div class="toolbar-right">
        <div class="segmented-control" id="viewSwitcher" style="display: none;">
          <button class="seg-btn" id="btnDual" onclick="setViewMode('dual')" title="Split Dual View">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="21"></line></svg>
            <span class="seg-label">Split</span>
          </button>
          <button class="seg-btn active" id="btnNotes" onclick="setViewMode('notes')" title="Notes Only">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            <span class="seg-label">Notes</span>
          </button>
          <button class="seg-btn" id="btnCode" onclick="setViewMode('code')" title="Code Only">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
            <span class="seg-label">Code</span>
          </button>
        </div>

        <button class="action-btn" id="copyBtn" onclick="copyActiveCode()" title="Copy Python Solution" style="display: none;">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          <span id="copyBtnLabel">Copy Code</span>
        </button>
      </div>
    </header>

    <!-- Roadmap Interactive View -->
    <div id="roadmap-view" class="roadmap-container active">
      <div class="roadmap-hero">
        <div class="hero-badge">CURRICULUM TOPOLOGY</div>
        <h1>算法刷题全景路线图</h1>
        <p>灵茶山艾府基础算法精讲 × labuladong 核心解题框架 · 5 大递进阶段 · 12 核心专题全覆盖</p>
        <div class="phase-filter-bar">
          <button class="phase-filter-btn active" onclick="filterRoadmapPhase('all', this)">全部阶段 (All)</button>
          <button class="phase-filter-btn" onclick="filterRoadmapPhase(1, this)">Phase 1: 线性与双指针</button>
          <button class="phase-filter-btn" onclick="filterRoadmapPhase(2, this)">Phase 2: 经典二分</button>
          <button class="phase-filter-btn" onclick="filterRoadmapPhase(3, this)">Phase 3: 树与递归</button>
          <button class="phase-filter-btn" onclick="filterRoadmapPhase(4, this)">Phase 4: 回溯决策树</button>
          <button class="phase-filter-btn" onclick="filterRoadmapPhase(5, this)">Phase 5: 动态规划与进阶</button>
        </div>
      </div>

      <div class="roadmap-phases-container" id="roadmapPhasesRoot">
        <!-- Rendered via JS -->
      </div>
    </div>

    <!-- Workspace Dual Split View -->
    <div id="workspace" class="hidden-view">
      <!-- Left Pane: Syntax-Highlighted Code -->
      <section class="pane" id="left-pane">
        <div class="pane-header">
          <span class="pane-title"><svg class="pane-svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>Solution Source Code</span>
          <button class="action-btn" onclick="copyActiveCode()">Copy Python</button>
        </div>
        <div class="code-viewer">
          <pre><code class="language-python" id="codeViewer"># Solution code</code></pre>
        </div>
      </section>

      <!-- Draggable Splitter between Code & Notes -->
      <div id="workspace-resizer" class="workspace-resizer" title="Drag to adjust split (Double-click to reset 50/50)"></div>

      <!-- Right Pane: Notes & Walkthrough -->
      <section class="pane" id="right-pane">
        <div class="markdown-body" id="notesViewer">
          <!-- Markdown Rendered Here -->
        </div>
      </section>
    </div>
  </main>

  <script>
    const items = {items_json};
    const roadmapData = {roadmap_json};

    let mainMode = localStorage.getItem("mainMode") || "roadmap";
    let currentKey = "README.md";
    let viewMode = "notes"; // 'dual', 'notes', 'code'
    let workspaceSplitRatio = parseFloat(localStorage.getItem("workspaceSplitRatio") || "50");
    const collapsedFolders = JSON.parse(localStorage.getItem("treeCollapsedFolders") || "{{}}");

    // Check initial URL hash
    if (window.location.hash && window.location.hash.length > 1) {{
      const hashKey = decodeURIComponent(window.location.hash.substring(1));
      if (hashKey === "roadmap") {{
        mainMode = "roadmap";
      }} else if (items[hashKey]) {{
        currentKey = hashKey;
        mainMode = "workspace";
      }}
    }}

    // Tree folder structure definitions matching README.md repo structure
    const treeStructure = [
      {{
        id: "roadmap-doc",
        name: "ROADMAP.md",
        label: "Master Roadmap",
        isLeaf: true,
        filter: k => k === "ROADMAP.md"
      }},
      {{
        id: "overview",
        name: "README.md",
        label: "Overview",
        isLeaf: true,
        filter: k => k === "README.md"
      }},
      {{
        id: "problem-index",
        name: "problem-index/",
        label: "Curriculum Index",
        filter: k => k.startsWith("topic-")
      }},
      {{
        id: "top-100",
        name: "top-100/",
        label: "Top 100 Liked",
        filter: k => k.startsWith("top-100/")
      }},
      {{
        id: "daily-practice",
        name: "daily-practice/",
        label: "Daily Practice",
        filter: k => k.startsWith("daily-practice/")
      }},
      {{
        id: "luffy",
        name: "luffy/",
        label: "Curriculum (01-42)",
        filter: k => k.startsWith("luffy/")
      }}
    ];

    function updateProgressBadge() {{
      const problemKeys = Object.keys(items).filter(k => items[k].type === "problem");
      document.getElementById("progressStats").innerText = `${{problemKeys.length}} Problems`;
    }}

    function applyWorkspaceSplit(ratio) {{
      const leftPane = document.getElementById("left-pane");
      const rightPane = document.getElementById("right-pane");
      if (!leftPane || !rightPane) return;
      if (viewMode === "dual") {{
        const clamped = Math.max(15, Math.min(85, ratio));
        leftPane.style.width = `calc(${{clamped}}% - 2.5px)`;
        leftPane.style.flex = "none";
        rightPane.style.width = `calc(${{100 - clamped}}% - 2.5px)`;
        rightPane.style.flex = "none";
      }}
    }}

    function setViewMode(mode) {{
      viewMode = mode;
      const leftPane = document.getElementById("left-pane");
      const rightPane = document.getElementById("right-pane");
      const resizer = document.getElementById("workspace-resizer");

      document.getElementById("btnDual").classList.toggle("active", mode === "dual");
      document.getElementById("btnNotes").classList.toggle("active", mode === "notes");
      document.getElementById("btnCode").classList.toggle("active", mode === "code");

      if (mode === "dual") {{
        leftPane.style.display = "flex";
        rightPane.style.display = "flex";
        resizer.style.display = "block";
        applyWorkspaceSplit(workspaceSplitRatio);
      }} else if (mode === "code") {{
        leftPane.style.display = "flex";
        leftPane.style.width = "100%";
        leftPane.style.flex = "1";
        rightPane.style.display = "none";
        resizer.style.display = "none";
      }} else {{ // notes only
        leftPane.style.display = "none";
        rightPane.style.display = "flex";
        rightPane.style.width = "100%";
        rightPane.style.flex = "1";
        resizer.style.display = "none";
      }}
    }}

    function setMainMode(mode) {{
      mainMode = mode;
      localStorage.setItem("mainMode", mode);

      const btnRoadmap = document.getElementById("btnModeRoadmap");
      const btnWorkspace = document.getElementById("btnModeWorkspace");
      const roadmapView = document.getElementById("roadmap-view");
      const workspaceView = document.getElementById("workspace");
      const viewSwitcher = document.getElementById("viewSwitcher");
      const copyBtn = document.getElementById("copyBtn");
      const breadcrumb = document.getElementById("itemBreadcrumb");

      if (mode === "roadmap") {{
        btnRoadmap.classList.add("active");
        btnWorkspace.classList.remove("active");
        roadmapView.classList.add("active");
        workspaceView.classList.add("hidden-view");
        viewSwitcher.style.display = "none";
        copyBtn.style.display = "none";
        breadcrumb.innerHTML = `
          <span class="breadcrumb-folder">Curriculum</span>
          <span class="breadcrumb-sep">/</span>
          <span class="breadcrumb-file">Algorithm Master Roadmap</span>
        `;
        if (history.replaceState) {{
          history.replaceState(null, null, "#roadmap");
        }}
      }} else {{
        btnRoadmap.classList.remove("active");
        btnWorkspace.classList.add("active");
        roadmapView.classList.remove("active");
        workspaceView.classList.remove("hidden-view");
        viewSwitcher.style.display = "inline-flex";
        copyBtn.style.display = items[currentKey]?.code ? "inline-flex" : "none";
        switchItem(currentKey, false);
      }}
    }}

    function renderRoadmap(selectedPhase = 'all') {{
      const root = document.getElementById("roadmapPhasesRoot");
      if (!root) return;

      const diffColorMap = {{
        "Easy": "var(--diff-easy)",
        "Medium": "var(--diff-medium)",
        "Hard": "var(--diff-hard)",
      }};

      let html = "";
      roadmapData.forEach(p => {{
        if (selectedPhase !== 'all' && p.phase !== parseInt(selectedPhase)) return;

        let totalProblemsInPhase = 0;
        p.topics.forEach(t => totalProblemsInPhase += t.problems.length);

        html += `
          <section class="phase-section" id="phase-sec-${{p.phase}}">
            <div class="phase-header">
              <div class="phase-title-group">
                <span class="phase-badge-pill">${{p.phase_badge}}</span>
                <h2 class="phase-title-text">${{p.phase_name}}</h2>
              </div>
              <span class="topic-card-count">${{p.topics.length}} 专题 · ${{totalProblemsInPhase}} 题解</span>
            </div>
            <p class="phase-desc">${{p.phase_desc}}</p>
            <div class="phase-topics-grid">
        `;

        p.topics.forEach(t => {{
          html += `
            <div class="topic-card">
              <div class="topic-card-top">
                <div>
                  <h3 class="topic-card-title">${{t.title}}</h3>
                  <div class="topic-card-subtitle">${{t.subtitle}}</div>
                </div>
                <span class="topic-card-count">${{t.problems.length}} 题</span>
              </div>
              <div class="topic-formula-badge" title="Core Mental Model / Formula">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
                <span>${{t.formula}}</span>
              </div>
              <div class="topic-pills-container">
          `;

          t.problems.forEach(prob => {{
            const dotColor = diffColorMap[prob.diff] || "var(--diff-medium)";
            html += `
              <div class="topic-problem-pill" onclick="openProblemFromRoadmap('${{prob.key}}')" title="${{prob.name}} (${{prob.cn}})">
                <span class="pill-diff-dot" style="background-color: ${{dotColor}};"></span>
                <span>LC ${{prob.num}} ${{prob.cn || prob.name}}</span>
              </div>
            `;
          }});

          html += `
              </div>
            </div>
          `;
        }});

        html += `
            </div>
          </section>
        `;
      }});

      root.innerHTML = html;
    }}

    function filterRoadmapPhase(phase, btnEl) {{
      document.querySelectorAll(".phase-filter-btn").forEach(b => b.classList.remove("active"));
      if (btnEl) btnEl.classList.add("active");
      renderRoadmap(phase);
    }}

    function openProblemFromRoadmap(key) {{
      setMainMode("workspace");
      switchItem(key);
    }}

    function getCategoryIcon(catId) {{
      switch(catId) {{
        case "roadmap-doc":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon><line x1="9" y1="3" x2="9" y2="18"></line><line x1="15" y1="6" x2="15" y2="21"></line></svg>`;
        case "overview":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>`;
        case "problem-index":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>`;
        case "top-100":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>`;
        case "daily-practice":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`;
        case "luffy":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>`;
        default:
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>`;
      }}
    }}

    function toggleFolder(folderId) {{
      collapsedFolders[folderId] = !collapsedFolders[folderId];
      localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
      renderTree(document.getElementById("search").value);
    }}

    function setAllFoldersCollapsed(collapsed) {{
      treeStructure.forEach(folder => {{
        if (!folder.isLeaf) {{
          collapsedFolders[folder.id] = collapsed;
        }}
      }});
      localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
      renderTree(document.getElementById("search").value);
    }}

    function matchesSearchQuery(item, query) {{
      if (!query) return true;
      const clean = query.trim().toLowerCase();
      if (!clean) return true;
      const tokens = clean.split(/\\s+/);
      return tokens.every(token => item.search_blob.includes(token));
    }}

    function renderTree(query = "") {{
      const root = document.getElementById("treeRoot");
      if (!root) return;

      const isSearching = Boolean(query && query.trim().length > 0);
      let html = "";
      let totalVisible = 0;

      treeStructure.forEach(folder => {{
        if (folder.isLeaf) {{
          const matchingKey = Object.keys(items).find(k => folder.filter(k));
          if (!matchingKey) return;
          const item = items[matchingKey];
          if (isSearching && !matchesSearchQuery(item, query)) return;

          const isActive = matchingKey === currentKey && mainMode === "workspace";
          const iconSvg = getCategoryIcon(folder.id);

          html += `
            <div class="nav-item root-leaf ${{isActive ? 'active' : ''}}" data-key="${{matchingKey}}" onclick="switchItem('${{matchingKey}}')" title="${{item.title}}">
              <span class="folder-icon" style="margin-right: 2px;">${{iconSvg}}</span>
              <span class="tree-title">${{folder.name}}</span>
            </div>
          `;
          totalVisible++;
          return;
        }}

        const folderKeys = Object.keys(items).filter(k => folder.filter(k));
        const matchingKeys = isSearching 
          ? folderKeys.filter(k => matchesSearchQuery(items[k], query))
          : folderKeys;

        if (matchingKeys.length === 0) return;
        totalVisible += matchingKeys.length;

        const isCollapsed = isSearching ? false : Boolean(collapsedFolders[folder.id]);
        const folderIconSvg = getCategoryIcon(folder.id);

        html += `
          <div class="tree-folder ${{isCollapsed ? 'collapsed' : ''}}" id="folder-${{folder.id}}">
            <div class="tree-folder-header" onclick="toggleFolder('${{folder.id}}')">
              <span class="folder-arrow">
                <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </span>
              <span class="folder-icon">${{folderIconSvg}}</span>
              <span class="folder-name">${{folder.label}}</span>
              <span class="folder-count">${{matchingKeys.length}}</span>
            </div>
            <div class="tree-children">
        `;

        matchingKeys.forEach(itemKey => {{
          const item = items[itemKey];
          const isActive = itemKey === currentKey && mainMode === "workspace";
          const diffClass = `diff-${{item.diff}}`;

          let displayTitle = item.title;
          if (item.category.includes("Luffy")) {{
            displayTitle = item.title.replace(/^LC \\d+\\s*/, "");
          }}

          html += `
            <div class="nav-item ${{isActive ? 'active' : ''}}" data-key="${{itemKey}}" onclick="switchItem('${{itemKey}}')" title="${{item.title}}">
              <span class="tree-title">${{displayTitle}}</span>
              <span class="tree-diff-dot ${{diffClass}}"></span>
            </div>
          `;
        }});

        html += `
            </div>
          </div>
        `;
      }});

      if (totalVisible === 0) {{
        html = `
          <div class="tree-no-results">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <span>No matching problems found</span>
          </div>
        `;
      }}

      root.innerHTML = html;
    }}

    function handleSearch(query) {{
      const clearBtn = document.getElementById("searchClear");
      if (query.trim().length > 0) {{
        clearBtn.classList.add("visible");
      }} else {{
        clearBtn.classList.remove("visible");
      }}
      renderTree(query);
    }}

    function clearSearch() {{
      const input = document.getElementById("search");
      input.value = "";
      document.getElementById("searchClear").classList.remove("visible");
      renderTree("");
      input.focus();
    }}

    function switchItem(key, rerenderSearch = true) {{
      if (!items[key]) return;
      currentKey = key;
      const item = items[key];

      setMainMode("workspace");

      if (history.replaceState) {{
        history.replaceState(null, null, "#" + key);
      }} else {{
        window.location.hash = "#" + key;
      }}

      treeStructure.forEach(folder => {{
        if (folder.filter && folder.filter(key) && collapsedFolders[folder.id]) {{
          collapsedFolders[folder.id] = false;
          localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
        }}
      }});

      if (rerenderSearch) {{
        renderTree(document.getElementById("search").value);
      }} else {{
        document.querySelectorAll(".nav-item").forEach(el => {{
          if (el.getAttribute("data-key") === key) {{
            el.classList.add("active");
          }} else {{
            el.classList.remove("active");
          }}
        }});
      }}

      if (window.innerWidth <= 768) {{
        toggleSidebar(false);
      }}

      const breadcrumb = document.getElementById("itemBreadcrumb");
      let folderLabel = item.category;
      let diffHtml = item.diff !== "All" ? `<span class="diff-badge ${{item.diff}}">${{item.diff}}</span>` : "";

      breadcrumb.innerHTML = `
        <span class="breadcrumb-folder">${{folderLabel}}</span>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-file">${{item.short || item.title}}</span>
        ${{diffHtml}}
      `;

      const codeViewer = document.getElementById("codeViewer");
      if (item.code) {{
        codeViewer.textContent = item.code;
        hljs.highlightElement(codeViewer);
      }} else {{
        codeViewer.textContent = "# No python solution source available for this item.";
      }}

      const notesViewer = document.getElementById("notesViewer");
      if (item.notes) {{
        notesViewer.innerHTML = marked.parse(item.notes);
        notesViewer.querySelectorAll("pre code").forEach(block => {{
          hljs.highlightElement(block);
        }});
        renderMathInElement(notesViewer, {{
          delimiters: [
            {{left: "$$", right: "$$", display: true}},
            {{left: "$", right: "$", display: false}},
            {{left: "\\\\(", right: "\\\\)", display: false}},
            {{left: "\\\\[", right: "\\\\]", display: true}}
          ],
          throwOnError: false
        }});
      }} else {{
        notesViewer.innerHTML = `<p style="color: var(--text-muted);">No documentation notes found for this problem.</p>`;
      }}

      const copyBtn = document.getElementById("copyBtn");
      copyBtn.style.display = item.code ? "inline-flex" : "none";

      document.getElementById("left-pane").scrollTop = 0;
      document.getElementById("right-pane").scrollTop = 0;
    }}

    function copyActiveCode() {{
      const item = items[currentKey];
      if (!item || !item.code) return;

      navigator.clipboard.writeText(item.code).then(() => {{
        const label = document.getElementById("copyBtnLabel");
        const originalText = label.innerText;
        label.innerText = "Copied!";
        setTimeout(() => {{
          label.innerText = originalText;
        }}, 1800);
      }}).catch(err => {{
        console.error("Failed to copy code: ", err);
      }});
    }}

    function toggleSidebar(forceState = null) {{
      const sidebar = document.getElementById("sidebar");
      const backdrop = document.getElementById("sidebar-backdrop");
      const isMobile = window.innerWidth <= 768;

      if (isMobile) {{
        const willOpen = forceState !== null ? forceState : !sidebar.classList.contains("mobile-open");
        sidebar.classList.toggle("mobile-open", willOpen);
        backdrop.classList.toggle("active", willOpen);
      }} else {{
        const isCollapsed = forceState !== null ? !forceState : !sidebar.classList.contains("collapsed");
        sidebar.classList.toggle("collapsed", isCollapsed);
      }}
    }}

    // Sidebar Resizer Dragging
    const resizer = document.getElementById("resizer");
    const sidebar = document.getElementById("sidebar");
    let isResizingSidebar = false;

    resizer.addEventListener("mousedown", (e) => {{
      isResizingSidebar = true;
      resizer.classList.add("dragging");
      document.body.style.cursor = "col-resize";
      document.body.style.userSelect = "none";
    }});

    // Workspace Split Resizer Dragging
    const workspaceResizer = document.getElementById("workspace-resizer");
    let isResizingWorkspace = false;

    workspaceResizer.addEventListener("mousedown", (e) => {{
      isResizingWorkspace = true;
      workspaceResizer.classList.add("dragging");
      document.body.style.cursor = "col-resize";
      document.body.style.userSelect = "none";
    }});

    workspaceResizer.addEventListener("dblclick", () => {{
      workspaceSplitRatio = 50;
      localStorage.setItem("workspaceSplitRatio", "50");
      applyWorkspaceSplit(50);
    }});

    window.addEventListener("mousemove", (e) => {{
      if (isResizingSidebar) {{
        const newWidth = Math.max(220, Math.min(650, e.clientX));
        sidebar.style.width = `${{newWidth}}px`;
        document.documentElement.style.setProperty("--sidebar-width", `${{newWidth}}px`);
      }} else if (isResizingWorkspace) {{
        const workspace = document.getElementById("workspace");
        const rect = workspace.getBoundingClientRect();
        const offsetX = e.clientX - rect.left;
        const totalWidth = rect.width;
        const ratio = (offsetX / totalWidth) * 100;
        workspaceSplitRatio = Math.max(15, Math.min(85, ratio));
        applyWorkspaceSplit(workspaceSplitRatio);
      }}
    }});

    window.addEventListener("mouseup", () => {{
      if (isResizingSidebar) {{
        isResizingSidebar = false;
        resizer.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
      }}
      if (isResizingWorkspace) {{
        isResizingWorkspace = false;
        workspaceResizer.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
        localStorage.setItem("workspaceSplitRatio", workspaceSplitRatio.toString());
      }}
    }});

    // Keyboard Shortcuts
    window.addEventListener("keydown", (e) => {{
      if (e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") {{
        e.preventDefault();
        const searchInput = document.getElementById("search");
        if (sidebar.classList.contains("collapsed")) {{
          toggleSidebar(true);
        }}
        searchInput.focus();
        searchInput.select();
      }} else if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "b") {{
        e.preventDefault();
        toggleSidebar();
      }} else if (e.key === "Escape") {{
        const searchInput = document.getElementById("search");
        if (document.activeElement === searchInput) {{
          clearSearch();
          searchInput.blur();
        }}
      }}
    }});

    // Initialize SPA
    renderTree();
    updateProgressBadge();
    renderRoadmap('all');

    if (mainMode === "roadmap") {{
      setMainMode("roadmap");
    }} else {{
      setMainMode("workspace");
      switchItem(currentKey);
    }}
  </script>
</body>
</html>
"""

    output_path = BASE_DIR / "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"✨ [Success] Built {output_path.name} ({len(all_items)} problem entities & curriculum tracks).")
    return output_path

def open_in_browser():
    """Opens index.html in default system browser."""
    html_file = BASE_DIR / "index.html"
    if not html_file.exists():
        build_index_html()
    
    cmd_exe = Path("/mnt/c/WINDOWS/System32/cmd.exe")
    if cmd_exe.exists():
        win_path = f"C:\\Users\\steve\\iCloudDrive\\desktop\\leetcode-sh\\index.html"
        subprocess.run([str(cmd_exe), "/c", "start", "", win_path])
    else:
        import webbrowser
        webbrowser.open(str(html_file.resolve()))
    print(f"🌐 [Browser] Opened {html_file.name} in default browser.")

def install_git_hook():
    """Installs a git pre-commit hook so index.html updates automatically on git commit."""
    hook_dir = BASE_DIR / ".git" / "hooks"
    if not hook_dir.exists():
        print("❌ [Git Hook] .git/hooks directory not found.")
        return
    
    hook_path = hook_dir / "pre-commit"
    hook_script = f"""#!/bin/sh
# Auto-update index.html before committing
python3 "{BASE_DIR / 'update_index.py'}"
git add "{BASE_DIR / 'index.html'}"
"""
    with open(hook_path, "w", encoding="utf-8") as f:
        f.write(hook_script)
    os.chmod(hook_path, 0o755)
    print(f"✅ [Git Hook] Successfully installed pre-commit hook to {hook_path}")

def watch_workspace(interval: float = 2.0):
    """Monitors workspace directories and rebuilds index.html on file modifications."""
    print("👀 [Watch Mode] Watching leetcode-sh workspace for file changes... (Press Ctrl+C to stop)")
    last_mtimes = {}

    def get_snapshot():
        snapshot = {}
        for root, _, files in os.walk(BASE_DIR):
            if ".git" in root or "__pycache__" in root:
                continue
            for f in files:
                if f == "index.html":
                    continue
                full_path = os.path.join(root, f)
                try:
                    snapshot[full_path] = os.path.getmtime(full_path)
                except OSError:
                    pass
        return snapshot

    last_mtimes = get_snapshot()
    build_index_html()

    try:
        while True:
            time.sleep(interval)
            current_snapshot = get_snapshot()
            if current_snapshot != last_mtimes:
                print("\n🔄 [Change Detected] File added, modified, or removed. Rebuilding index.html...")
                build_index_html()
                last_mtimes = current_snapshot
    except KeyboardInterrupt:
        print("\n🛑 [Watch Mode] Stopped.")

def main():
    parser = argparse.ArgumentParser(description="Auto-update index.html for LeetCode workspace.")
    parser.add_argument("--open", action="store_true", help="Build and open index.html in browser")
    parser.add_argument("--watch", action="store_true", help="Continuously watch workspace and rebuild on change")
    parser.add_argument("--git-hook", action="store_true", help="Install git pre-commit hook for auto-updates")
    args = parser.parse_args()

    if args.git_hook:
        install_git_hook()
    elif args.watch:
        watch_workspace()
    else:
        build_index_html()
        if args.open:
            open_in_browser()

if __name__ == "__main__":
    main()
