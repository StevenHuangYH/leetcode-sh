#!/usr/bin/env python3
"""
update_index.py - Automated Compiler for LeetCode Study Station SPA (index.html)

Features:
- Scans top-100/, daily-practice/, and luffy/ folders.
- Dynamically parses README.md curriculum topics and ROADMAP.md visual phases.
- Compiles a fast, zero-dependency SPA with Dual Split-Pane and KaTeX math protection.
"""

import os
import re
import json
import time
import argparse
import subprocess
from pathlib import Path
from dataclasses import dataclass, asdict

BASE_DIR = Path(__file__).parent.resolve()
TEMPLATE_PATH = BASE_DIR / "templates" / "station_template.html"

@dataclass
class DocumentEntity:
    key: str
    category: str
    title: str
    short: str
    slug: str
    cn_title: str
    tags: str
    lc_num: str
    search_blob: str
    path: str
    type: str = "problem"
    notes: str = ""
    code: str = ""
    diff: str = "All"
    py_file: str = ""
    md_file: str = ""

def normalize_slug(text: str) -> str:
    """Normalizes problem title to a clean slug for searching."""
    text = re.sub(r'[\(\)\[\]\{\}\.,:;!\?`\'"]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip().lower()

def build_search_blob(tokens: list, text_content: str = "") -> str:
    """Builds a normalized, space-separated searchable string."""
    combined = " ".join(tokens)
    if text_content:
        clean_text = re.sub(r'[\r\n\t]+', ' ', text_content)
        clean_text = re.sub(r'[#\*`_\[\]\(\)\{\}\.,:;!\?\'"]', ' ', clean_text)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        combined += " " + clean_text[:3000]
    return normalize_slug(combined)

def read_file(path: Path) -> str:
    """Safely reads a text file."""
    try:
        return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    except Exception as e:
        return f"Error reading file: {e}"

def parse_curriculum_topics(readme_text: str) -> dict:
    """Extracts curriculum topic document items from README.md Section 5."""
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
    
    sec5_match = re.search(r'(## (?:📚 )?Topic-Wise Curriculum & Problem Index.*?)(\n## (?:🖥️ )?Interactive Web Viewer|\n## (?:🚀 )?How to Run|\Z)', readme_text, re.DOTALL)
    sec5_text = sec5_match.group(1) if sec5_match else readme_text

    topic_docs = {}
    for key, title, short, header in topic_sections:
        if key == "topic-all":
            topic_content = f"# Problem Index: Complete Topic-Wise Catalog\n\n{sec5_text}"
        else:
            match = re.search(re.escape(header) + r'(.*?)(\n### |\n---|\n## |\Z)', readme_text, re.DOTALL)
            topic_content = f"# Problem Index — {title}\n\n{header}\n{match.group(1).strip()}" if match else f"# Problem Index — {title}\n\nNo content parsed."

        slug = normalize_slug(title)
        topic_docs[key] = asdict(DocumentEntity(
            key=key, category="Problem Index", title=title, short=short, slug=slug,
            cn_title="", tags="topic curriculum problem index", lc_num="",
            search_blob=build_search_blob([title, short, slug, "problem index topic"], topic_content),
            path=f"problem-index/{key}", type="doc", notes=topic_content, diff="All"
        ))
    return topic_docs

def parse_roadmap_data(roadmap_text: str = "") -> list:
    """Dynamically parses phases, topics, and problem links from ROADMAP.md."""
    if not roadmap_text:
        roadmap_text = read_file(BASE_DIR / "ROADMAP.md")
    if not roadmap_text:
        return []
    
    phases = []
    phase_blocks = re.findall(r'## Phase (\d+):\s*([^\n]+)\n+(.*?)(?=\n## Phase \d+|\n---|\Z)', roadmap_text, re.DOTALL)
    
    for phase_num_str, phase_title, block in phase_blocks:
        phase_num = int(phase_num_str)
        topic_blocks = re.findall(r'### Topic (\d+):\s*([^\n]+)\n+(.*?)(?=\n### Topic \d+|\Z)', block, re.DOTALL)
        topics = []
        
        for topic_num_str, topic_title, topic_body in topic_blocks:
            formula_match = re.search(r'┌─+┐\n│\s*([^\n]+)\n├─+┤\n(.*?)\n└─+┘', topic_body, re.DOTALL)
            formula_summary = formula_match.group(1).strip() if formula_match else f"Topic {topic_num_str} Core Patterns"
            
            problems = []
            for row in re.findall(r'\|\s*\*\*LC\s*(\d+)\*\*\s*\|\s*([^\|]+)\|\s*(Easy|Medium|Hard)\s*\|\s*([^\|]+)\|\s*([^\|]+)\|', topic_body):
                lc_num, name_full, diff, category_name, link_cell = row
                cn_match = re.search(r'\(([\u4e00-\u9fa5A-Za-z0-9\s]+)\)', name_full)
                cn_name = cn_match.group(1) if cn_match else ""
                clean_name = re.sub(r'\(.*?\)', '', name_full).strip()
                
                key_match = re.search(r'\(([^)]+\.py)\)', link_cell)
                key = key_match.group(1) if key_match else f"luffy/{int(lc_num):02d}-lc-{int(lc_num):04d}.py"
                
                problems.append({
                    "num": int(lc_num), "name": clean_name, "cn": cn_name, "diff": diff.capitalize(), "key": key
                })
            
            topics.append({
                "id": f"topic-{topic_num_str}",
                "title": topic_title.split("(")[0].strip(),
                "subtitle": topic_title.split("(")[1].replace(")", "").strip() if "(" in topic_title else topic_title,
                "icon": "layers",
                "formula": formula_summary,
                "problems": problems
            })
            
        phases.append({
            "phase": phase_num,
            "phase_name": f"Phase {phase_num}: {phase_title.strip()}",
            "phase_badge": f"PHASE {phase_num:02d}",
            "phase_desc": f"Master Phase {phase_num} core algorithmic models and problem patterns.",
            "topics": topics
        })
    return phases

def collect_workspace_documents() -> dict:
    """Scans repository folders and aggregates structured problem entities."""
    readme_text = read_file(BASE_DIR / "README.md")
    roadmap_text = read_file(BASE_DIR / "ROADMAP.md")
    
    topic_docs = parse_curriculum_topics(readme_text)
    overview_docs = {
        "README.md": asdict(DocumentEntity(
            key="README.md", category="Overview", title="LeetCode Self-Practices Overview (README)",
            short="README.md", slug="readme overview", cn_title="项目总览", tags="readme overview index",
            lc_num="", search_blob=build_search_blob(["README.md", "overview", "项目总览"], readme_text),
            path="README.md", type="doc", notes=readme_text, diff="All"
        )),
        "ROADMAP.md": asdict(DocumentEntity(
            key="ROADMAP.md", category="Overview", title="Algorithm Master Roadmap (ROADMAP.md)",
            short="ROADMAP.md", slug="algorithm master roadmap", cn_title="算法全景路线图", tags="roadmap",
            lc_num="", search_blob=build_search_blob(["ROADMAP.md", "roadmap", "路线图"], roadmap_text),
            path="ROADMAP.md", type="doc", notes=roadmap_text, diff="All"
        ))
    }

    problems = {}
    tracks = [("top-100", "Top 100 Liked Track"), ("daily-practice", "Daily Practice Track"), ("luffy", "Luffy Curriculum (01-42)")]

    for dir_name, cat_title in tracks:
        track_dir = BASE_DIR / dir_name
        if not track_dir.exists():
            continue

        files = sorted(os.listdir(track_dir))
        stem_groups = {}
        for f in files:
            if f.startswith("__") or f.endswith(".pyc") or f == "file_topics.txt":
                continue
            stem = f[:-3] if f.endswith(".py") or f.endswith(".md") else f
            if stem not in stem_groups:
                stem_groups[stem] = {"py": None, "md": None}
            if f.endswith(".py"):
                stem_groups[stem]["py"] = f
            elif f.endswith(".md"):
                stem_groups[stem]["md"] = f

        for stem, pair in stem_groups.items():
            py_file, md_file = pair["py"], pair["md"]
            py_content = read_file(track_dir / py_file) if py_file else ""
            md_content = read_file(track_dir / md_file) if md_file else ""

            m_num = re.search(r'(?:lc-)?(\d{4})', stem)
            lc_num = f"LC {int(m_num.group(1))}" if m_num else ""
            title = f"{lc_num} {stem}" if lc_num else stem.replace("-", " ").title()
            
            cn_match = re.search(r'# .*?\| ([\u4e00-\u9fa5A-Za-z0-9\s\(\)]+)', md_content) if md_content else None
            cn_title = cn_match.group(1).strip() if cn_match else ""
            
            diff_match = re.search(r'\*\*Difficulty:\*\*\s*(Easy|Medium|Hard)', md_content, re.IGNORECASE) if md_content else None
            diff = diff_match.group(1).capitalize() if diff_match else "Medium"
            
            clean_slug = normalize_slug(f"{stem} {cn_title}")
            search_blob = build_search_blob([stem, title, cn_title, lc_num, diff, dir_name], f"{md_content}\n{py_content}")
            primary_key = f"{dir_name}/{py_file if py_file else md_file}"
            
            problems[primary_key] = asdict(DocumentEntity(
                key=primary_key, category=cat_title, title=title, short=py_file if py_file else md_file,
                slug=clean_slug, cn_title=cn_title, tags=f"{dir_name} {diff.lower()}", lc_num=lc_num,
                search_blob=search_blob, path=f"{dir_name}/{stem}", type="problem", notes=md_content,
                code=py_content, diff=diff, py_file=f"{dir_name}/{py_file}" if py_file else "",
                md_file=f"{dir_name}/{md_file}" if md_file else ""
            ))

    return {**overview_docs, **topic_docs, **problems}

def build_index_html():
    """Generates the single-page index.html file with visual roadmap and dual split-pane view."""
    all_items = collect_workspace_documents()
    roadmap_data = parse_roadmap_data()
    template = read_file(TEMPLATE_PATH)
    if not template:
        raise FileNotFoundError(f"Template not found at {TEMPLATE_PATH}")

    html_content = template.replace("{items_json}", json.dumps(all_items)).replace("{roadmap_json}", json.dumps(roadmap_data))
    output_path = BASE_DIR / "index.html"
    output_path.write_text(html_content, encoding="utf-8")
    print(f"✨ [Success] Built {output_path.name} ({len(all_items)} problem entities & curriculum tracks).")
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Auto-update index.html for LeetCode workspace.")
    parser.add_argument("--open", action="store_true", help="Build and open index.html in browser")
    parser.add_argument("--watch", action="store_true", help="Continuously watch workspace and rebuild on change")
    args = parser.parse_args()

    build_index_html()
    if args.open:
        cmd_exe = Path("/mnt/c/WINDOWS/System32/cmd.exe")
        if cmd_exe.exists():
            subprocess.run([str(cmd_exe), "/c", "start", "", "C:\\Users\\steve\\iCloudDrive\\desktop\\leetcode-sh\\index.html"])

if __name__ == "__main__":
    main()
