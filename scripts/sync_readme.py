import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

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

def parse_existing_descriptions(readme_text):
    desc_map = {}
    for line in readme_text.split("\n"):
        if line.startswith("| **"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 6:
                num_str = parts[0].replace("*", "")
                if num_str.isdigit():
                    num = int(num_str)
                    desc_map[num] = (parts[1], parts[4], parts[5])
    return desc_map

def generate_top_100_table(existing_desc):
    top_100_dir = REPO_ROOT / "top-100"
    stems = sorted(list(set(f.stem for f in top_100_dir.glob("lc-*"))))
    
    def get_num(stem):
        m = re.search(r"lc-(\d+)", stem)
        return int(m.group(1)) if m else 999999
    
    stems.sort(key=get_num)
    
    lines = [
        "| # | Problem Title | LeetCode Link | Solutions & Notes | Difficulty | Pattern / Core Technique |",
        "| :-: | :--- | :-: | :--- | :-: | :--- |"
    ]
    
    for stem in stems:
        num = get_num(stem)
        num_m = re.search(r"lc-(\d+)", stem)
        slug = stem[len(f"lc-{num_m.group(1)}-"):] if num_m else stem
        py_path = top_100_dir / f"{stem}.py"
        md_path = top_100_dir / f"{stem}.md"
        
        sol_parts = []
        if py_path.exists():
            sol_parts.append(f"[`top-100/{stem}.py`](top-100/{stem}.py)")
        if md_path.exists():
            sol_parts.append(f"[`top-100/{stem}.md`](top-100/{stem}.md)")
        sol_str = "<br>".join(sol_parts)
        
        if num in existing_desc:
            title, diff, tech = existing_desc[num]
        else:
            title = slug.replace("-", " ").title()
            diff = KNOWN_DIFFICULTIES.get(num, "Medium")
            tech = "High-Frequency Top 100 Pattern"
            
        lines.append(f"| **{num}** | {title} | [LC {num}](https://leetcode.com/problems/{slug}/) | {sol_str} | {diff} | {tech} |")
        
    return "\n".join(lines)

def sync_luffy_in_section5(readme_text):
    # In Topic 1, ensure 03-lc-0167, 04-lc-0003, 06-lc-0209, 09-lc-0059-alt are present
    # In Topic 3, ensure 10-lc-0303-alt, 10-lc-0303-prefix-sum-practices, 11-prefix-sum-basic-example are present
    # In Topic 6, ensure 20-lc-0020-valid-parentheses-dict is present
    # In Topic 7, ensure 29-lc-0098 variants are present
    
    # 1. Topic 1
    t1_old = "| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py) |"
    t1_new = "| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py)<br>[`luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py`](luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py) |"
    if t1_old in readme_text:
        readme_text = readme_text.replace(t1_old, t1_new)

    t3_old = "| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`top-100/lc-0003-longest-substring-without-repeating-characters.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py) |"
    t3_new = "| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`top-100/lc-0003-longest-substring-without-repeating-characters.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py)<br>[`luffy/04-lc-0003-longest-substring-without-repeating-characters.py`](luffy/04-lc-0003-longest-substring-without-repeating-characters.py) |"
    if t3_old in readme_text:
        readme_text = readme_text.replace(t3_old, t3_new)

    t209_old = "| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py) |"
    t209_new = "| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py)<br>[`luffy/06-lc-0209-minimum-size-subarray-sum.py`](luffy/06-lc-0209-minimum-size-subarray-sum.py) |"
    if t209_old in readme_text:
        readme_text = readme_text.replace(t209_old, t209_new)

    t59_old = "| **59** | Spiral Matrix II | [LC 59](https://leetcode.com/problems/spiral-matrix-ii/) | [`luffy/08-lc-0059-spiral-matrix-ii.py`](luffy/08-lc-0059-spiral-matrix-ii.py) |"
    t59_new = "| **59** | Spiral Matrix II | [LC 59](https://leetcode.com/problems/spiral-matrix-ii/) | [`luffy/08-lc-0059-spiral-matrix-ii.py`](luffy/08-lc-0059-spiral-matrix-ii.py)<br>[`luffy/09-lc-0059-spiral-matrix-ii-alt.py`](luffy/09-lc-0059-spiral-matrix-ii-alt.py) |"
    if t59_old in readme_text:
        readme_text = readme_text.replace(t59_old, t59_new)

    # 2. Topic 3
    t303_old = "| **303** | Range Sum Query - Immutable | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | [`luffy/10-lc-0303-range-sum-query-immutable.py`](luffy/10-lc-0303-range-sum-query-immutable.py) |"
    t303_new = "| **303** | Range Sum Query - Immutable | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | [`luffy/10-lc-0303-range-sum-query-immutable.py`](luffy/10-lc-0303-range-sum-query-immutable.py)<br>[`luffy/10-lc-0303-range-sum-query-immutable-alt.py`](luffy/10-lc-0303-range-sum-query-immutable-alt.py)<br>[`luffy/10-lc-0303-prefix-sum-practices.py`](luffy/10-lc-0303-prefix-sum-practices.py)<br>[`luffy/11-prefix-sum-basic-example.py`](luffy/11-prefix-sum-basic-example.py) |"
    if t303_old in readme_text:
        readme_text = readme_text.replace(t303_old, t303_new)

    # 3. Topic 6
    t20_old = "| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py) |"
    t20_new = "| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py)<br>[`luffy/20-lc-0020-valid-parentheses-dict.py`](luffy/20-lc-0020-valid-parentheses-dict.py) |"
    if t20_old in readme_text:
        readme_text = readme_text.replace(t20_old, t20_new)

    # 4. Topic 7
    t98_old = "| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py) |"
    t98_new = "| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-bounds.py`](luffy/29-lc-0098-validate-binary-search-tree-bounds.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-recursion.py`](luffy/29-lc-0098-validate-binary-search-tree-recursion.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-stack.py`](luffy/29-lc-0098-validate-binary-search-tree-stack.py) |"
    if t98_old in readme_text:
        readme_text = readme_text.replace(t98_old, t98_new)

    return readme_text

def update_readme():
    readme_path = REPO_ROOT / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    
    existing_desc = parse_existing_descriptions(readme_text)
    
    new_top_100_table = generate_top_100_table(existing_desc)
    
    sec3_pattern = r"(## Top 100 Liked Track\n\n[^\n]+\n\n)\| # \| Problem Title \|.*?(\n---|\n## )"
    replacement = f"\\1{new_top_100_table}\\n\\2"
    new_readme = re.sub(sec3_pattern, replacement, readme_text, flags=re.DOTALL)
    
    new_readme = sync_luffy_in_section5(new_readme)
    
    new_readme = re.sub(
        r"Problems_Indexed-\d+\+-brightgreen\.svg",
        "Problems_Indexed-174+-brightgreen.svg",
        new_readme
    )
    
    total_problems = 174
    total_notes = len(list(REPO_ROOT.glob("top-100/*.md"))) + len(list(REPO_ROOT.glob("daily-practice/*.md"))) + len(list(REPO_ROOT.glob("luffy/*.md")))
    
    sec2_table = f"""| Difficulty | Companion Notes Count | Percentage | Total Tracked Solutions / Stubs |
| :--- | :---: | :---: | :---: |
| **Easy** | 31 | ~31% | 31 |
| **Medium** | 62 | ~62% | 134 |
| **Hard** | 7 | ~7% | 9 |
| **Total** | **{total_notes} In-Depth Notes** | **100%** | **{total_problems} Problem Entities** |"""

    new_readme = re.sub(
        r"(\| Difficulty \| Companion Notes Count \|.*?\*\*Total\*\* \|.*?\n)",
        sec2_table + "\n",
        new_readme,
        flags=re.DOTALL
    )
    
    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"Updated README.md with {total_problems} problem entities.")

if __name__ == "__main__":
    update_readme()
