import sys
import re
from pathlib import Path
from collections import Counter
from typing import Dict, List, Tuple, Optional

REPO_ROOT = Path(__file__).parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.compiler.collector import ProblemCollector
from scripts.compiler.track_definitions import TrackRegistry


def format_markdown_link(rel_path: str) -> str:
    """Formats a repository-relative path as a markdown link."""
    return f"[`{rel_path}`]({rel_path})"


def build_difficulty_map(collector_items: dict) -> Dict[int, str]:
    """Pre-builds an integer-keyed difficulty lookup map from collected problem entities."""
    diff_map = {}
    for item in collector_items.values():
        if item.get("type") == "problem":
            lc_num = item.get("lc_num", "")
            m = re.search(r"\d+", lc_num)
            if m:
                diff = item.get("diff")
                if diff and diff != "All":
                    diff_map[int(m.group(0))] = diff
    return diff_map


def build_problem_files_index(collector_items: dict) -> Dict[int, List[str]]:
    """Dynamically maps problem number to repository-relative solution links across all tracks directly from collector entities."""
    py_map: Dict[int, List[str]] = {}
    md_map: Dict[int, List[str]] = {}
    
    def _add_link(target_dict: Dict[int, List[str]], num: int, file_rel: Optional[str]):
        if file_rel and (REPO_ROOT / file_rel).exists():
            link = format_markdown_link(file_rel)
            links = target_dict.setdefault(num, [])
            if link not in links:
                links.append(link)

    for key in sorted(collector_items.keys()):
        item = collector_items[key]
        if item.get("type") != "problem":
            continue
        
        lc_num = item.get("lc_num", "")
        m = re.search(r"\d+", lc_num)
        if not m:
            continue
        num = int(m.group(0))
        
        py_file = item.get("py_file")
        if py_file:
            _add_link(py_map, num, py_file)
        elif key.endswith(".py"):
            _add_link(py_map, num, key)
            
        md_file = item.get("md_file")
        if md_file:
            _add_link(md_map, num, md_file)
        elif key.endswith(".md"):
            _add_link(md_map, num, key)
            
    file_map: Dict[int, List[str]] = {}
    all_nums = set(py_map.keys()) | set(md_map.keys())
    for num in sorted(all_nums):
        file_map[num] = py_map.get(num, []) + md_map.get(num, [])
        
    return file_map



def parse_existing_descriptions(readme_text: str) -> Dict[int, Tuple[str, str, str]]:
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


def generate_top_100_table(existing_desc: dict, diff_map: dict) -> str:
    top_100_track = TrackRegistry.get_track_by_id("top-100")
    if not top_100_track:
        raise RuntimeError("Canonical track 'top-100' is not registered in TrackRegistry.")
    top_100_rel = top_100_track.dir_path
    top_100_dir = REPO_ROOT / top_100_rel
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
            sol_parts.append(format_markdown_link(f"{top_100_rel}/{stem}.py"))
        if md_path.exists():
            sol_parts.append(format_markdown_link(f"{top_100_rel}/{stem}.md"))
        sol_str = "<br>".join(sol_parts)
        
        if num in existing_desc:
            title, diff, tech = existing_desc[num]
        else:
            title = slug.replace("-", " ").title()
            diff = diff_map.get(num, "Medium")
            tech = "High-Frequency Top 100 Pattern"
            
        lines.append(f"| **{num}** | {title} | [LC {num}](https://leetcode.com/problems/{slug}/) | {sol_str} | {diff} | {tech} |")
        
    return "\n".join(lines)


def sync_multi_track_solutions(readme_text: str, file_map: Dict[int, List[str]]) -> str:
    """Dynamically ensures Section 5 curriculum rows include all companion solution links."""
    def replace_row(match):
        num_str = match.group(1)
        if not num_str.isdigit():
            return match.group(0)
        num = int(num_str)
        if num in file_map and len(file_map[num]) > 1:
            title = match.group(2)
            lc_link = match.group(3)
            sol_cell = "<br>".join(file_map[num])
            rest = match.group(5)
            return f"| **{num}** | {title} | {lc_link} | {sol_cell} | {rest}"
        return match.group(0)

    row_pattern = r"\| \*\*(\d+)\*\* \| (.*?) \| (\[LC \d+\].*?) \| (.*?) \| (.*?)(?=\n\||\n\n|\Z)"
    return re.sub(row_pattern, replace_row, readme_text)


def update_readme():
    readme_path = REPO_ROOT / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    
    collector_items = ProblemCollector.collect(REPO_ROOT, use_cache=False)
    diff_map = build_difficulty_map(collector_items)
    file_map = build_problem_files_index(collector_items)
    existing_desc = parse_existing_descriptions(readme_text)
    
    new_top_100_table = generate_top_100_table(existing_desc, diff_map)
    
    sec3_pattern = r"(## Top 100 Liked Track\n\n[^\n]+\n\n)\| # \| Problem Title \|.*?(\n---|\n## )"
    replacement = f"\\1{new_top_100_table}\\n\\2"
    new_readme = re.sub(sec3_pattern, replacement, readme_text, flags=re.DOTALL)
    
    new_readme = sync_multi_track_solutions(new_readme, file_map)
    
    problem_entities = [v for v in collector_items.values() if v.get("type") == "problem"]
    total_problems = len(problem_entities)
    notes_entities = [p for p in problem_entities if p.get("md_file") or (p.get("notes") and len(p.get("notes").strip()) > 0)]
    total_notes = len(notes_entities)

    prob_diffs = Counter(p.get("diff", "Medium") for p in problem_entities)
    notes_diffs = Counter(p.get("diff", "Medium") for p in notes_entities)

    easy_problems, medium_problems, hard_problems = prob_diffs["Easy"], prob_diffs["Medium"], prob_diffs["Hard"]
    easy_notes, medium_notes, hard_notes = notes_diffs["Easy"], notes_diffs["Medium"], notes_diffs["Hard"]

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
