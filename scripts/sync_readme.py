import sys
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.compiler.collector import ProblemCollector


def get_problem_difficulty(num: int, collector_items: dict) -> str:
    """Dynamically resolves problem difficulty from collected problem entities."""
    for item in collector_items.values():
        if item.get("type") == "problem":
            lc_num = item.get("lc_num", "")
            m = re.search(r"\d+", lc_num)
            if m and int(m.group(0)) == num:
                diff = item.get("diff")
                if diff and diff != "All":
                    return diff
    return "Medium"


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


def generate_top_100_table(existing_desc, collector_items):
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
            diff = get_problem_difficulty(num, collector_items)
            tech = "High-Frequency Top 100 Pattern"
            
        lines.append(f"| **{num}** | {title} | [LC {num}](https://leetcode.com/problems/{slug}/) | {sol_str} | {diff} | {tech} |")
        
    return "\n".join(lines)


LUFFY_TRACK_REPLACEMENTS = [
    (
        "| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py) |",
        "| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py)<br>[`luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py`](luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py) |"
    ),
    (
        "| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`top-100/lc-0003-longest-substring-without-repeating-characters.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py) |",
        "| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`top-100/lc-0003-longest-substring-without-repeating-characters.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py)<br>[`luffy/04-lc-0003-longest-substring-without-repeating-characters.py`](luffy/04-lc-0003-longest-substring-without-repeating-characters.py) |"
    ),
    (
        "| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py) |",
        "| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py)<br>[`luffy/06-lc-0209-minimum-size-subarray-sum.py`](luffy/06-lc-0209-minimum-size-subarray-sum.py) |"
    ),
    (
        "| **59** | Spiral Matrix II | [LC 59](https://leetcode.com/problems/spiral-matrix-ii/) | [`luffy/08-lc-0059-spiral-matrix-ii.py`](luffy/08-lc-0059-spiral-matrix-ii.py) |",
        "| **59** | Spiral Matrix II | [LC 59](https://leetcode.com/problems/spiral-matrix-ii/) | [`luffy/08-lc-0059-spiral-matrix-ii.py`](luffy/08-lc-0059-spiral-matrix-ii.py)<br>[`luffy/09-lc-0059-spiral-matrix-ii-alt.py`](luffy/09-lc-0059-spiral-matrix-ii-alt.py) |"
    ),
    (
        "| **303** | Range Sum Query - Immutable | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | [`luffy/10-lc-0303-range-sum-query-immutable.py`](luffy/10-lc-0303-range-sum-query-immutable.py) |",
        "| **303** | Range Sum Query - Immutable | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | [`luffy/10-lc-0303-range-sum-query-immutable.py`](luffy/10-lc-0303-range-sum-query-immutable.py)<br>[`luffy/10-lc-0303-range-sum-query-immutable-alt.py`](luffy/10-lc-0303-range-sum-query-immutable-alt.py)<br>[`luffy/10-lc-0303-prefix-sum-practices.py`](luffy/10-lc-0303-prefix-sum-practices.py)<br>[`luffy/11-prefix-sum-basic-example.py`](luffy/11-prefix-sum-basic-example.py) |"
    ),
    (
        "| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py) |",
        "| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py)<br>[`luffy/20-lc-0020-valid-parentheses-dict.py`](luffy/20-lc-0020-valid-parentheses-dict.py) |"
    ),
    (
        "| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py) |",
        "| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-bounds.py`](luffy/29-lc-0098-validate-binary-search-tree-bounds.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-recursion.py`](luffy/29-lc-0098-validate-binary-search-tree-recursion.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-stack.py`](luffy/29-lc-0098-validate-binary-search-tree-stack.py) |"
    )
]


def sync_luffy_in_section5(readme_text):
    """Synchronizes companion luffy track references in README Section 5."""
    for old_snip, new_snip in LUFFY_TRACK_REPLACEMENTS:
        if old_snip in readme_text:
            readme_text = readme_text.replace(old_snip, new_snip)
    return readme_text


def update_readme():
    readme_path = REPO_ROOT / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    
    collector_items = ProblemCollector.collect(REPO_ROOT, use_cache=False)
    existing_desc = parse_existing_descriptions(readme_text)
    
    new_top_100_table = generate_top_100_table(existing_desc, collector_items)
    
    sec3_pattern = r"(## Top 100 Liked Track\n\n[^\n]+\n\n)\| # \| Problem Title \|.*?(\n---|\n## )"
    replacement = f"\\1{new_top_100_table}\\n\\2"
    new_readme = re.sub(sec3_pattern, replacement, readme_text, flags=re.DOTALL)
    
    new_readme = sync_luffy_in_section5(new_readme)
    
    problem_entities = [v for v in collector_items.values() if v.get("type") == "problem"]
    total_problems = len(problem_entities)

    easy_problems = len([p for p in problem_entities if p.get("diff") == "Easy"])
    medium_problems = len([p for p in problem_entities if p.get("diff") == "Medium"])
    hard_problems = len([p for p in problem_entities if p.get("diff") == "Hard"])

    notes_entities = [p for p in problem_entities if p.get("md_file") or (p.get("notes") and len(p.get("notes").strip()) > 0)]
    total_notes = len(notes_entities)

    easy_notes = len([p for p in notes_entities if p.get("diff") == "Easy"])
    medium_notes = len([p for p in notes_entities if p.get("diff") == "Medium"])
    hard_notes = len([p for p in notes_entities if p.get("diff") == "Hard"])

    easy_pct = round((easy_notes / total_notes * 100)) if total_notes else 0
    medium_pct = round((medium_notes / total_notes * 100)) if total_notes else 0
    hard_pct = round((hard_notes / total_notes * 100)) if total_notes else 0

    new_readme = re.sub(
        r"Problems_Indexed-\d+\+-brightgreen\.svg",
        f"Problems_Indexed-{total_problems}+-brightgreen.svg",
        new_readme
    )

    sec2_table = f"""| Difficulty | Companion Notes Count | Percentage | Total Tracked Solutions / Stubs |
| :--- | :---: | :---: | :---: |
| **Easy** | {easy_notes} | ~{easy_pct}% | {easy_problems} |
| **Medium** | {medium_notes} | ~{medium_pct}% | {medium_problems} |
| **Hard** | {hard_notes} | ~{hard_pct}% | {hard_problems} |
| **Total** | **{total_notes} In-Depth Notes** | **100%** | **{total_problems} Problem Entities** |"""

    new_readme = re.sub(
        r"(\| Difficulty \| Companion Notes Count \|.*?\*\*Total\*\* \|.*?\n)",
        sec2_table + "\n",
        new_readme,
        flags=re.DOTALL
    )

    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"Updated README.md with {total_problems} problem entities ({total_notes} companion notes).")


if __name__ == "__main__":
    update_readme()
