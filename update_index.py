#!/usr/bin/env python3
"""
=============================================================================
LeetCode Workspace - Automated index.html Builder & Study Station
=============================================================================
This script scans all workspace folders (top-100, daily-practice, luffy,
README.md), organizes problems into paired (Code + Notes) entities,
and compiles a standalone, self-contained single-page web app (index.html).

Features:
- Side-by-side Dual Split View (Left: Markdown Walkthrough, Right: Python Code)
- View mode switcher (Dual Split, Notes Only, Code Only) with resizable pane
- Category Accordions with Expand/Fold All controls
- Difficulty filter tags (Easy, Medium, Hard)
- Dynamic indexed problem count badge
- Keyboard shortcuts (/ for search, Esc to clear)
- Automated Git pre-commit hook integration
=============================================================================
"""

import os
import sys
import re
import json
import time
import argparse
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def get_file_type(filename: str) -> str:
    if filename.endswith(".md") or filename.startswith("topic-"):
        return "md"
    elif filename.endswith(".py") or filename.endswith("py"):
        return "py"
    elif filename.endswith(".txt"):
        return "txt"
    return "other"

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
            ("topic-11-oop", "11. OOP & Foundations", "11. OOP & Foundations", "### 11. OOP & Foundations"),
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

            topic_docs[key] = {
                "key": key,
                "category": "Problem Index",
                "title": title,
                "short": short,
                "path": f"problem-index/{key}",
                "type": "doc",
                "notes": topic_content,
                "code": "",
                "diff": "All"
            }

    # 2. Overview Document (README.md)
    overview_docs = {
        "README.md": {
            "key": "README.md",
            "category": "Overview",
            "title": "LeetCode Self-Practices Overview (README)",
            "short": "README.md",
            "path": "README.md",
            "type": "doc",
            "notes": readme_text,
            "code": "",
            "diff": "All"
        }
    }

    # 3. Helper to detect difficulty from markdown content or filename
    def extract_difficulty(text: str, filename: str) -> str:
        if "Hard" in text:
            return "Hard"
        elif "Easy" in text:
            return "Easy"
        elif "Medium" in text:
            return "Medium"
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
            if f.endswith(".py"):
                stem = f[:-3]
            elif f.endswith(".md"):
                stem = f[:-3]
            stem_groups.setdefault(stem, []).append(f)

        for stem, group_files in stem_groups.items():
            py_file = next((f for f in group_files if f.endswith(".py")), None)
            md_file = next((f for f in group_files if f.endswith(".md")), None)

            py_content = read_file_content(track_dir / py_file) if py_file else ""
            md_content = read_file_content(track_dir / md_file) if md_file else ""

            # Make nice title and short label
            short_name = stem
            if short_name.startswith("lc-"):
                short_name = short_name.replace("lc-", "LC ")
            elif "-lc-" in short_name:
                short_name = short_name.replace("-lc-", " LC ")
            short_name = short_name.replace("-", " ")

            diff = extract_difficulty(md_content, stem)
            problem_key = f"{dir_name}/{stem}"

            problems[problem_key] = {
                "key": problem_key,
                "category": cat_title,
                "title": f"{cat_title}: {short_name}",
                "short": short_name,
                "path": f"{dir_name}/{stem}",
                "type": "problem",
                "notes": md_content,
                "code": py_content,
                "diff": diff,
                "py_file": f"{dir_name}/{py_file}" if py_file else "",
                "md_file": f"{dir_name}/{md_file}" if md_file else ""
            }

    # Aggregate all items
    all_items = {**overview_docs, **topic_docs, **problems}
    return all_items

def build_index_html():
    """Generates the single-page index.html file with dual split-pane view and responsive tree explorer."""
    all_items = collect_workspace_documents()
    items_json = json.dumps(all_items)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LeetCode Study Station - Split Dual View & Interactive Notes</title>
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
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
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
      transition: background-color 0.15s;
    }}
    .resizer:hover, .resizer.dragging {{
      background-color: var(--accent);
    }}

    /* Sidebar Header */
    .sidebar-header {{
      padding: 12px 14px 8px;
      border-bottom: 1px solid var(--border-color);
    }}
    .header-brand {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .brand-title {{
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text-bright);
      display: flex;
      align-items: center;
      gap: 7px;
      user-select: none;
    }}
    .brand-icon {{
      font-size: 15px;
    }}
    .progress-badge {{
      font-size: 11px;
      padding: 2px 7px;
      background: rgba(56, 139, 253, 0.12);
      border: 1px solid rgba(88, 166, 255, 0.25);
      border-radius: 10px;
      color: var(--accent);
      font-weight: 600;
      white-space: nowrap;
    }}
    .search-box-wrapper {{
      position: relative;
      margin-bottom: 2px;
    }}
    .search-box {{
      width: 100%;
      padding: 6px 26px 6px 28px;
      background-color: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      color: #fff;
      font-size: 12px;
      outline: none;
      transition: border-color 0.15s, box-shadow 0.15s;
    }}
    .search-box:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 2px rgba(88, 166, 255, 0.2);
    }}
    .search-icon {{
      position: absolute;
      left: 8px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 11px;
      pointer-events: none;
    }}
    .search-clear-btn {{
      position: absolute;
      right: 7px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 11px;
      cursor: pointer;
      display: none;
      padding: 2px;
      line-height: 1;
    }}
    .search-clear-btn:hover {{
      color: #fff;
    }}

    /* Explorer Bar (Header for Tree) */
    .explorer-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 14px 6px;
      border-bottom: 1px solid var(--border-subtle);
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.5px;
      user-select: none;
    }}
    .explorer-actions {{
      display: flex;
      gap: 4px;
    }}
    .icon-btn {{
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      font-size: 12px;
      cursor: pointer;
      padding: 2px 5px;
      border-radius: 4px;
      line-height: 1;
      transition: all 0.15s;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .icon-btn:hover {{
      background: rgba(177, 186, 196, 0.12);
      color: var(--text-bright);
      border-color: var(--border-color);
    }}

    /* Tree View Container */
    .tree-container {{
      flex: 1;
      overflow-y: auto;
      padding: 6px 8px 20px;
    }}
    .tree-folder {{
      margin-bottom: 2px;
    }}
    .tree-folder-header {{
      display: flex;
      align-items: center;
      padding: 5px 8px;
      border-radius: 6px;
      cursor: pointer;
      user-select: none;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      transition: background-color 0.15s, color 0.15s;
      gap: 6px;
    }}
    .tree-folder-header:hover {{
      background-color: rgba(177, 186, 196, 0.08);
      color: var(--text-bright);
    }}
    .tree-chevron {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 12px;
      color: var(--text-muted);
      transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);
      flex-shrink: 0;
    }}
    .tree-folder.collapsed .tree-chevron {{
      transform: rotate(-90deg);
    }}
    .tree-folder-icon, .tree-file-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      color: var(--text-muted);
    }}
    .tree-file-icon.code-icon {{
      color: #58a6ff;
    }}
    .tree-file-icon.doc-icon {{
      color: #8b949e;
    }}
    .pane-svg {{
      color: var(--accent);
      vertical-align: middle;
      margin-right: 4px;
    }}
    .tree-folder-name {{
      flex: 1;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .tree-count-badge {{
      font-size: 10px;
      padding: 1px 6px;
      border-radius: 10px;
      background: var(--card-bg);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-weight: 500;
      flex-shrink: 0;
    }}
    .tree-children {{
      position: relative;
      margin-left: 13px;
      padding-left: 6px;
      border-left: 1px solid rgba(240, 246, 252, 0.08);
      transition: all 0.2s ease-out;
    }}
    .tree-folder.collapsed .tree-children {{
      display: none;
    }}

    /* Tree Node / Nav Item */
    .nav-item {{
      display: flex;
      align-items: center;
      padding: 5px 8px;
      border-radius: 5px;
      color: var(--text-main);
      text-decoration: none;
      font-size: 12px;
      cursor: pointer;
      margin-bottom: 1px;
      transition: all 0.15s ease;
      gap: 6px;
      position: relative;
    }}
    .nav-item:hover {{
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
    }}
    .diff-Easy {{ background-color: var(--diff-easy); }}
    .diff-Medium {{ background-color: var(--diff-medium); }}
    .diff-Hard {{ background-color: var(--diff-hard); }}
    .diff-All {{ display: none; }}

    /* Main Workspace Container */
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
      padding: 1px 7px;
      border-radius: 10px;
      font-weight: 600;
      margin-left: 4px;
    }}
    .diff-badge.diff-Easy {{ background: rgba(63, 185, 80, 0.15); color: var(--diff-easy); border: 1px solid rgba(63, 185, 80, 0.3); }}
    .diff-badge.diff-Medium {{ background: rgba(210, 153, 34, 0.15); color: var(--diff-medium); border: 1px solid rgba(210, 153, 34, 0.3); }}
    .diff-badge.diff-Hard {{ background: rgba(248, 81, 73, 0.15); color: var(--diff-hard); border: 1px solid rgba(248, 81, 73, 0.3); }}

    /* Toolbar Right Controls */
    .toolbar-right {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}
    .segmented-control {{
      display: inline-flex;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 2px;
      gap: 2px;
    }}
    .seg-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 11.5px;
      padding: 3px 9px;
      border-radius: 4px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      font-weight: 500;
      transition: all 0.15s;
      user-select: none;
    }}
    .seg-btn:hover {{
      color: var(--text-bright);
    }}
    .seg-btn.active {{
      background: rgba(56, 139, 253, 0.18);
      color: var(--accent);
      font-weight: 600;
    }}
    .action-btn {{
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      font-size: 11.5px;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      font-weight: 500;
      transition: all 0.15s;
      user-select: none;
    }}
    .action-btn:hover {{
      background: rgba(177, 186, 196, 0.15);
      color: #fff;
      border-color: var(--accent);
    }}

    /* Split Pane Workspace */
    #workspace {{
      flex: 1;
      display: flex;
      overflow: hidden;
      height: calc(100vh - 46px);
    }}
    .pane {{
      overflow-y: auto;
      height: 100%;
      padding: 28px 36px;
    }}
    #left-pane {{
      flex: 1;
      background-color: var(--bg-panel);
      display: flex;
      flex-direction: column;
      padding: 20px 24px;
      border-right: 1px solid var(--border-color);
      min-width: 0;
    }}
    #right-pane {{
      flex: 1;
      background-color: var(--bg-main);
      overflow-y: auto;
      padding: 28px 36px;
      min-width: 0;
    }}
    .pane-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 12px;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
    }}
    .pane-title {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-bright);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* Markdown Body Styling */
    .markdown-body {{
      max-width: 900px;
      margin: 0 auto;
      line-height: 1.65;
      font-size: 14.5px;
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

    /* Code Pane Viewer */
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
      font-size: 13px;
      line-height: 1.55;
    }}

    /* Responsive Breakpoints & Mobile Drawer */
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
          <span>LeetCode Station</span>
        </div>
        <span class="progress-badge" id="progressStats" title="Total Indexed Problems">0 Problems</span>
      </div>
      <div class="search-box-wrapper">
        <span class="search-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></span>
        <input type="text" id="search" class="search-box" placeholder="Search problems, patterns... (/)" oninput="handleSearch(this.value)">
        <button id="searchClear" class="search-clear-btn" onclick="clearSearch()" title="Clear search (Esc)">✕</button>
      </div>
    </div>

    <div class="explorer-bar">
      <span>EXPLORER</span>
      <div class="explorer-actions">
        <button class="icon-btn" onclick="expandAllFolders()" title="Expand All Folders">⊞</button>
        <button class="icon-btn" onclick="collapseAllFolders()" title="Collapse All Folders">⊟</button>
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
        <div class="breadcrumb" id="itemBreadcrumb">Loading...</div>
      </div>

      <div class="toolbar-right">
        <div class="segmented-control" id="viewSwitcher">
          <button class="seg-btn active" id="btnDual" onclick="setViewMode('dual')" title="Split Dual View">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="21"></line></svg>
            <span class="seg-label">Split</span>
          </button>
          <button class="seg-btn" id="btnNotes" onclick="setViewMode('notes')" title="Notes Only">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            <span class="seg-label">Notes</span>
          </button>
          <button class="seg-btn" id="btnCode" onclick="setViewMode('code')" title="Code Only">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
            <span class="seg-label">Code</span>
          </button>
        </div>

        <button class="action-btn" id="copyBtn" onclick="copyActiveCode()" title="Copy Python Solution">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          <span id="copyBtnLabel">Copy Code</span>
        </button>
      </div>
    </header>

    <div id="workspace">
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
    let currentKey = "README.md";
    let viewMode = "dual"; // 'dual', 'notes', 'code'
    const collapsedFolders = JSON.parse(localStorage.getItem("treeCollapsedFolders") || "{{}}");

    // Check initial URL hash
    if (window.location.hash && window.location.hash.length > 1) {{
      const hashKey = decodeURIComponent(window.location.hash.substring(1));
      if (items[hashKey]) {{
        currentKey = hashKey;
      }}
    }}

    // Tree folder structure definitions
    const treeStructure = [
      {{
        id: "overview",
        name: "Overview",
        filter: k => k === "README.md"
      }},
      {{
        id: "problem-index",
        name: "Problem Index",
        filter: k => k.startsWith("topic-")
      }},
      {{
        id: "top-100",
        name: "Top 100 Liked Track",
        filter: k => k.startsWith("top-100/")
      }},
      {{
        id: "daily-practice",
        name: "Daily Practice Track",
        filter: k => k.startsWith("daily-practice/")
      }},
      {{
        id: "luffy",
        name: "Luffy Curriculum (01-42)",
        filter: k => k.startsWith("luffy/")
      }}
    ];

    function updateProgressBadge() {{
      const problemKeys = Object.keys(items).filter(k => items[k].type === "problem");
      document.getElementById("progressStats").innerText = `${{problemKeys.length}} Problems`;
    }}

    function setViewMode(mode) {{
      viewMode = mode;
      const leftPane = document.getElementById("left-pane");
      const rightPane = document.getElementById("right-pane");
      
      document.getElementById("btnDual").classList.toggle("active", mode === "dual");
      document.getElementById("btnNotes").classList.toggle("active", mode === "notes");
      document.getElementById("btnCode").classList.toggle("active", mode === "code");

      if (mode === "dual") {{
        leftPane.style.display = "flex";
        leftPane.style.flex = "1";
        rightPane.style.display = "block";
        rightPane.style.flex = "1";
      }} else if (mode === "notes") {{
        leftPane.style.display = "none";
        rightPane.style.display = "block";
        rightPane.style.flex = "1";
      }} else if (mode === "code") {{
        leftPane.style.display = "flex";
        leftPane.style.flex = "1";
        rightPane.style.display = "none";
      }}
    }}

    function toggleFolder(folderId) {{
      collapsedFolders[folderId] = !collapsedFolders[folderId];
      localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
      renderTree();
    }}

    function expandAllFolders() {{
      treeStructure.forEach(folder => {{
        collapsedFolders[folder.id] = false;
      }});
      localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
      renderTree();
    }}

    function collapseAllFolders() {{
      treeStructure.forEach(folder => {{
        collapsedFolders[folder.id] = true;
      }});
      localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
      renderTree();
    }}

    function renderTree(searchQuery = "") {{
      const treeRoot = document.getElementById("treeRoot");
      const q = searchQuery.toLowerCase().trim();
      let html = "";

      const docSvg = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>`;
      const codeSvg = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>`;
      const chevronSvg = `<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>`;

      treeStructure.forEach(folder => {{
        const allKeys = Object.keys(items).filter(folder.filter);
        const matchingKeys = q
          ? allKeys.filter(k => {{
              const item = items[k];
              return (item.title && item.title.toLowerCase().includes(q)) ||
                     (item.short && item.short.toLowerCase().includes(q)) ||
                     k.toLowerCase().includes(q);
            }})
          : allKeys;

        if (matchingKeys.length === 0) return;

        // Auto expand if search active, else respect saved state
        const isCollapsed = q ? false : !!collapsedFolders[folder.id];
        const collapseClass = isCollapsed ? "collapsed" : "";
        const folderSvg = isCollapsed
          ? `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>`
          : `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0"></path></svg>`;

        const folderIconHtml = folder.id === 'overview' ? docSvg : folderSvg;

        html += `
          <div class="tree-folder ${{collapseClass}}" id="folder-${{folder.id}}">
            <div class="tree-folder-header" onclick="toggleFolder('${{folder.id}}')">
              <span class="tree-chevron">${{chevronSvg}}</span>
              <span class="tree-folder-icon">${{folderIconHtml}}</span>
              <span class="tree-folder-name">${{folder.name}}</span>
              <span class="tree-count-badge">${{matchingKeys.length}}</span>
            </div>
            <div class="tree-children">
        `;

        matchingKeys.forEach(k => {{
          const item = items[k];
          const isActive = k === currentKey;
          const activeClass = isActive ? "active" : "";
          const diffClass = item.diff && item.diff !== "All" ? `diff-${{item.diff}}` : "diff-All";
          const fileIconHtml = item.type === "doc"
            ? `<span class="tree-file-icon doc-icon">${{docSvg}}</span>`
            : `<span class="tree-file-icon code-icon">${{codeSvg}}</span>`;

          html += `
            <div class="nav-item ${{activeClass}}" onclick="switchItem('${{k}}')" data-key="${{k}}" title="${{item.title || item.short}}">
              ${{fileIconHtml}}
              <span class="tree-title">${{item.short}}</span>
              <span class="tree-diff-dot ${{diffClass}}" title="${{item.diff}}"></span>
            </div>
          `;
        }});

        html += `
            </div>
          </div>
        `;
      }});

      treeRoot.innerHTML = html;
    }}

    function handleSearch(val) {{
      const clearBtn = document.getElementById("searchClear");
      if (clearBtn) clearBtn.style.display = val.trim() ? "block" : "none";
      renderTree(val);
    }}

    function clearSearch() {{
      const input = document.getElementById("search");
      input.value = "";
      handleSearch("");
      input.focus();
    }}

    function switchItem(key) {{
      if (!items[key]) return;
      currentKey = key;
      const item = items[key];

      // Update URL hash
      if (history.replaceState) {{
        history.replaceState(null, null, "#" + key);
      }} else {{
        window.location.hash = "#" + key;
      }}

      // Ensure parent folder is expanded
      treeStructure.forEach(folder => {{
        if (folder.filter(key) && collapsedFolders[folder.id]) {{
          collapsedFolders[folder.id] = false;
          localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
        }}
      }});

      // Re-render tree highlight
      renderTree(document.getElementById("search").value);

      // Auto close sidebar on mobile upon item selection
      if (window.innerWidth <= 768) {{
        toggleSidebar(false);
      }}

      // Scroll active item smoothly into view
      setTimeout(() => {{
        const activeEl = document.querySelector(`.nav-item[data-key="${{CSS.escape(key)}}"]`);
        if (activeEl) {{
          activeEl.scrollIntoView({{ block: "nearest", behavior: "smooth" }});
        }}
      }}, 50);

      // Top Toolbar Breadcrumb
      const pathParts = item.path.split("/");
      const folderPart = pathParts.length > 1 ? pathParts[0] : "root";
      const filePart = pathParts.length > 1 ? pathParts.slice(1).join("/") : pathParts[0];
      const diffBadge = item.diff && item.diff !== "All"
        ? `<span class="diff-badge diff-${{item.diff}}">${{item.diff}}</span>`
        : "";

      document.getElementById("itemBreadcrumb").innerHTML = `
        <span class="breadcrumb-folder">${{folderPart}}</span>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-file">${{filePart}}</span>
        ${{diffBadge}}
      `;

      // Auto view mode: Full width for docs/overview, dual for problems
      if (item.type === "doc" || !item.code) {{
        setViewMode("notes");
        document.getElementById("btnDual").style.display = "none";
        document.getElementById("btnCode").style.display = "none";
        document.getElementById("copyBtn").style.display = "none";
      }} else {{
        document.getElementById("btnDual").style.display = "inline-flex";
        document.getElementById("btnCode").style.display = "inline-flex";
        document.getElementById("copyBtn").style.display = "inline-flex";
        setViewMode("dual");
      }}

      // Render Markdown Notes
      marked.setOptions({{
        highlight: function(code, lang) {{
          const language = hljs.getLanguage(lang) ? lang : 'plaintext';
          return hljs.highlight(code, {{ language }}).value;
        }},
        gfm: true,
        breaks: true
      }});

      document.getElementById("notesViewer").innerHTML = marked.parse(item.notes || "# No Notes Available");

      document.querySelectorAll('#notesViewer pre code').forEach((el) => {{
        hljs.highlightElement(el);
      }});

      if (window.renderMathInElement) {{
        renderMathInElement(document.getElementById("notesViewer"), {{
          delimiters: [
            {{left: "$$", right: "$$", display: true}},
            {{left: "$", right: "$", display: false}}
          ]
        }});
      }}

      // Render Code Pane
      const codeEl = document.getElementById("codeViewer");
      codeEl.textContent = item.code || "# No python solution file directly associated";
      delete codeEl.dataset.highlighted;
      hljs.highlightElement(codeEl);

      // Smart link interception: clicking internal markdown links navigates inside SPA
      document.querySelectorAll('#notesViewer a').forEach(a => {{
        const href = a.getAttribute('href');
        if (!href) return;
        if (href.startsWith('http://') || href.startsWith('https://')) return;
        if (href.startsWith('#')) return;

        let cleanHref = href.replace(/^(\\.\\/|\\/)/, '');
        if (cleanHref.endsWith('.py') || cleanHref.endsWith('.md')) {{
          cleanHref = cleanHref.replace(/\\.(py|md)$/, '');
        }}

        if (items[cleanHref]) {{
          a.onclick = (e) => {{
            e.preventDefault();
            switchItem(cleanHref);
          }};
        }} else {{
          const matchingKey = Object.keys(items).find(k => k.endsWith(cleanHref) || cleanHref.endsWith(k));
          if (matchingKey) {{
            a.onclick = (e) => {{
              e.preventDefault();
              switchItem(matchingKey);
            }};
          }}
        }}
      }});

      document.getElementById("left-pane").scrollTop = 0;
      document.getElementById("right-pane").scrollTop = 0;
    }}

    function copyActiveCode() {{
      const item = items[currentKey];
      if (!item || !item.code) return;
      navigator.clipboard.writeText(item.code).then(() => {{
        const label = document.getElementById("copyBtnLabel");
        if (label) {{
          const original = label.innerText;
          label.innerText = "Copied!";
          setTimeout(() => label.innerText = original, 1500);
        }}
      }});
    }}

    // Sidebar Toggle & Collapse
    function toggleSidebar(forceState) {{
      const sidebar = document.getElementById("sidebar");
      const backdrop = document.getElementById("sidebar-backdrop");
      const isMobile = window.innerWidth <= 768;

      if (isMobile) {{
        const willOpen = forceState !== undefined ? forceState : !sidebar.classList.contains("mobile-open");
        sidebar.classList.toggle("mobile-open", willOpen);
        backdrop.classList.toggle("active", willOpen);
      }} else {{
        const isCollapsed = forceState !== undefined ? !forceState : !sidebar.classList.contains("collapsed");
        sidebar.classList.toggle("collapsed", isCollapsed);
        localStorage.setItem("sidebarCollapsed", isCollapsed);
      }}
    }}

    // Draggable Resizer Logic
    (function initResizer() {{
      const resizer = document.getElementById("resizer");
      const sidebar = document.getElementById("sidebar");
      let isResizing = false;

      // Restore saved width
      const savedWidth = localStorage.getItem("sidebarWidth");
      if (savedWidth && window.innerWidth > 768) {{
        sidebar.style.width = savedWidth + "px";
        sidebar.style.minWidth = savedWidth + "px";
      }}

      // Restore collapsed state on desktop
      const isCollapsed = localStorage.getItem("sidebarCollapsed") === "true";
      if (isCollapsed && window.innerWidth > 768) {{
        sidebar.classList.add("collapsed");
      }}

      resizer.addEventListener("mousedown", (e) => {{
        if (window.innerWidth <= 768) return;
        isResizing = true;
        resizer.classList.add("dragging");
        document.body.style.cursor = "col-resize";
        document.body.style.userSelect = "none";
      }});

      window.addEventListener("mousemove", (e) => {{
        if (!isResizing) return;
        const newWidth = Math.min(Math.max(e.clientX, 220), 650);
        sidebar.style.width = newWidth + "px";
        sidebar.style.minWidth = newWidth + "px";
      }});

      window.addEventListener("mouseup", () => {{
        if (isResizing) {{
          isResizing = false;
          resizer.classList.remove("dragging");
          document.body.style.cursor = "";
          document.body.style.userSelect = "";
          const width = parseInt(sidebar.style.width);
          if (width) localStorage.setItem("sidebarWidth", width);
        }}
      }});
    }})();

    // Global Keyboard Shortcuts
    window.addEventListener("keydown", (e) => {{
      // Cmd+B / Ctrl+B: Toggle sidebar
      if ((e.metaKey || e.ctrlKey) && (e.key === "b" || e.key === "B")) {{
        e.preventDefault();
        toggleSidebar();
      }}
      // /: Focus search
      else if (e.key === "/" && document.activeElement.tagName !== "INPUT") {{
        e.preventDefault();
        const searchInput = document.getElementById("search");
        if (document.getElementById("sidebar").classList.contains("collapsed")) {{
          toggleSidebar(true);
        }}
        searchInput.focus();
      }}
      // Escape: Clear search & blur
      else if (e.key === "Escape") {{
        const searchInput = document.getElementById("search");
        if (document.activeElement === searchInput) {{
          clearSearch();
          searchInput.blur();
        }}
      }}
    }});

    // Initialize
    renderTree();
    updateProgressBadge();
    switchItem(currentKey);
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
