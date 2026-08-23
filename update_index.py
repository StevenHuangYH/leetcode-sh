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
- LocalStorage persistent review checkmarks & progress counter
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

        sec5_match = re.search(r'(## 📚 Topic-Wise Curriculum & Problem Index.*?)(\n## 🖥️ Interactive Web Viewer|\n## 🚀 How to Run)', readme_text, re.DOTALL)
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
                "category": "🎯 Problem Index",
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
            "category": "📖 Overview",
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
        ("top-100", "🔥 Top 100 Liked Track"),
        ("daily-practice", "📅 Daily Practice Track"),
        ("luffy", "📚 Luffy Curriculum (01-42)"),
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
    """Generates the single-page index.html file with dual split-pane view."""
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
      --bg-panel: #11161d;
      --border-color: #30363d;
      --text-main: #c9d1d9;
      --text-muted: #8b949e;
      --accent: #58a6ff;
      --accent-hover: #1f6feb;
      --card-bg: #1c2128;
      --code-bg: #161b22;
      --diff-easy: #3fb950;
      --diff-medium: #d29922;
      --diff-hard: #f85149;
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
    #sidebar {{
      width: 370px;
      min-width: 370px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      height: 100%;
      z-index: 10;
    }}
    .sidebar-header {{
      padding: 16px 14px 10px;
      border-bottom: 1px solid var(--border-color);
    }}
    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .header-top h1 {{
      font-size: 14.5px;
      font-weight: 700;
      color: #f0f6fc;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .progress-badge {{
      font-size: 11px;
      padding: 2px 7px;
      background: rgba(56, 139, 253, 0.15);
      border: 1px solid rgba(88, 166, 255, 0.3);
      border-radius: 10px;
      color: var(--accent);
      font-weight: 600;
    }}
    .search-box-wrapper {{
      position: relative;
      margin-bottom: 8px;
    }}
    .search-box {{
      width: 100%;
      padding: 7px 10px 7px 30px;
      background-color: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      color: #fff;
      font-size: 12.5px;
      outline: none;
    }}
    .search-icon {{
      position: absolute;
      left: 9px;
      top: 8px;
      color: var(--text-muted);
      font-size: 12px;
    }}
    .search-box:focus {{
      border-color: var(--accent);
    }}
    .filter-pills {{
      display: flex;
      gap: 5px;
      margin-top: 6px;
      flex-wrap: wrap;
    }}
    .pill {{
      padding: 2px 7px;
      font-size: 11px;
      border-radius: 12px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      cursor: pointer;
      user-select: none;
      transition: all 0.15s;
    }}
    .pill.active, .pill:hover {{
      background: var(--accent-hover);
      color: #fff;
      border-color: var(--accent);
    }}
    .pill-diff-easy.active {{ background: rgba(63, 185, 80, 0.25); border-color: #3fb950; color: #3fb950; }}
    .pill-diff-medium.active {{ background: rgba(210, 153, 34, 0.25); border-color: #d29922; color: #d29922; }}
    .pill-diff-hard.active {{ background: rgba(248, 81, 73, 0.25); border-color: #f85149; color: #f85149; }}
    .accordion-controls {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 7px 14px 4px;
      border-bottom: 1px solid rgba(48, 54, 61, 0.4);
      font-size: 11px;
      color: var(--text-muted);
    }}
    .control-btn {{
      background: transparent;
      border: none;
      color: var(--accent);
      font-size: 11px;
      cursor: pointer;
      padding: 2px 4px;
      border-radius: 4px;
    }}
    .control-btn:hover {{
      text-decoration: underline;
    }}
    .nav-list {{
      flex: 1;
      overflow-y: auto;
      padding: 6px 8px 16px;
    }}
    .section-group {{
      margin-bottom: 6px;
    }}
    .section-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      padding: 7px 10px;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      user-select: none;
      border-radius: 6px;
      transition: background-color 0.15s;
    }}
    .section-title:hover {{
      background-color: rgba(177, 186, 196, 0.08);
      color: #f0f6fc;
    }}
    .section-title-left {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .chevron {{
      font-size: 9px;
      display: inline-block;
      transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      color: var(--text-muted);
      width: 12px;
      text-align: center;
    }}
    .section-group.collapsed .chevron {{
      transform: rotate(-90deg);
    }}
    .count-badge {{
      font-size: 10px;
      padding: 1px 6px;
      border-radius: 10px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
    }}
    .section-items {{
      overflow: hidden;
      transition: all 0.2s ease-out;
    }}
    .section-group.collapsed .section-items {{
      display: none;
    }}
    .nav-item {{
      display: flex;
      align-items: center;
      padding: 6px 10px;
      border-radius: 6px;
      color: var(--text-main);
      text-decoration: none;
      font-size: 12.5px;
      cursor: pointer;
      margin-bottom: 2px;
      transition: all 0.15s ease;
      gap: 7px;
      position: relative;
    }}
    .nav-item:hover {{
      background-color: rgba(177, 186, 196, 0.12);
      color: #f0f6fc;
    }}
    .nav-item.active {{
      background-color: rgba(56, 139, 253, 0.15);
      color: var(--accent);
      font-weight: 600;
      border-left: 3px solid var(--accent);
    }}
    .check-box {{
      width: 14px;
      height: 14px;
      border: 1px solid var(--border-color);
      border-radius: 3px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 10px;
      flex-shrink: 0;
      color: transparent;
      transition: all 0.15s;
    }}
    .check-box.checked {{
      background: #238636;
      border-color: #2ea043;
      color: #fff;
    }}
    .diff-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    .diff-Easy {{ background: var(--diff-easy); }}
    .diff-Medium {{ background: var(--diff-medium); }}
    .diff-Hard {{ background: var(--diff-hard); }}
    .diff-All {{ display: none; }}

    /* Main Workspace Container */
    #main-container {{
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      background-color: var(--bg-main);
    }}
    .top-toolbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
      border-bottom: 1px solid var(--border-color);
      background-color: var(--bg-sidebar);
      min-height: 48px;
    }}
    .item-meta {{
      font-size: 13px;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 10px;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }}
    .view-toggles {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .btn {{
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 11.5px;
      transition: all 0.15s;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .btn.active, .btn:hover {{
      background: var(--border-color);
      color: #fff;
      border-color: var(--accent);
    }}
    .btn-primary {{
      background: rgba(56, 139, 253, 0.2);
      border-color: rgba(88, 166, 255, 0.4);
      color: var(--accent);
    }}
    .btn-primary:hover {{
      background: var(--accent-hover);
      color: #fff;
    }}

    /* Split Pane Workspace */
    #workspace {{
      flex: 1;
      display: flex;
      overflow: hidden;
      height: calc(100vh - 48px);
    }}
    .pane {{
      overflow-y: auto;
      height: 100%;
      padding: 28px 36px;
    }}
    #left-pane {{
      flex: 1;
      background-color: var(--bg-main);
      border-right: 1px solid var(--border-color);
    }}
    #right-pane {{
      flex: 1;
      background-color: var(--bg-panel);
      display: flex;
      flex-direction: column;
      padding: 20px 24px;
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
      color: #f0f6fc;
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
  </style>
</head>
<body>

  <!-- Left Sidebar Navigation -->
  <div id="sidebar">
    <div class="sidebar-header">
      <div class="header-top">
        <h1>LeetCode Station</h1>
        <span class="progress-badge" id="progressStats">0 / 0 Done</span>
      </div>
      <div class="search-box-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" id="search" class="search-box" placeholder="Search problems, patterns, numbers... (/)" oninput="filterItems()">
      </div>
      <div class="filter-pills">
        <span class="pill active" onclick="setTrackFilter('all')">All</span>
        <span class="pill" onclick="setTrackFilter('problem-index')">🎯 Index</span>
        <span class="pill" onclick="setTrackFilter('top-100')">🔥 Top 100</span>
        <span class="pill" onclick="setTrackFilter('luffy')">📚 Luffy</span>
        <span class="pill" onclick="setTrackFilter('daily-practice')">📅 Daily</span>
      </div>
      <div class="filter-pills" style="margin-top: 4px;">
        <span class="pill" onclick="setDiffFilter('All')">All Diff</span>
        <span class="pill pill-diff-easy" onclick="setDiffFilter('Easy')">Easy</span>
        <span class="pill pill-diff-medium" onclick="setDiffFilter('Medium')">Medium</span>
        <span class="pill pill-diff-hard" onclick="setDiffFilter('Hard')">Hard</span>
      </div>
    </div>
    <div class="accordion-controls">
      <span>Curriculum Categories</span>
      <div style="display: flex; gap: 8px;">
        <button class="control-btn" onclick="expandAllCategories()">▾ Expand All</button>
        <button class="control-btn" onclick="collapseAllCategories()">▴ Fold All</button>
      </div>
    </div>
    <div class="nav-list" id="navList">
      <!-- Injected dynamically by JavaScript -->
    </div>
  </div>

  <!-- Main Content Workspace (Split-Pane) -->
  <div id="main-container">
    <div class="top-toolbar">
      <div class="item-meta" id="itemMeta">Loading...</div>
      <div class="view-toggles">
        <button class="btn btn-primary" id="btnDual" onclick="setViewMode('dual')">◫ Dual Split</button>
        <button class="btn" id="btnNotes" onclick="setViewMode('notes')">📝 Notes Only</button>
        <button class="btn" id="btnCode" onclick="setViewMode('code')">🐍 Code Only</button>
        <button class="btn" onclick="copyActiveCode()">Copy Code</button>
        <button class="btn" onclick="window.print()">Export</button>
      </div>
    </div>

    <div id="workspace">
      <!-- Left Pane: Notes & Walkthrough -->
      <div class="pane" id="left-pane">
        <div class="markdown-body" id="notesViewer">
          <!-- Markdown Rendered Here -->
        </div>
      </div>

      <!-- Right Pane: Syntax-Highlighted Code -->
      <div class="pane" id="right-pane">
        <div class="pane-header">
          <span class="pane-title" id="codePaneTitle">🐍 Solution Source Code</span>
          <button class="btn" onclick="copyActiveCode()">Copy Python</button>
        </div>
        <div class="code-viewer">
          <pre><code class="language-python" id="codeViewer"># Solution code</code></pre>
        </div>
      </div>
    </div>
  </div>

  <script>
    const items = {items_json};
    let currentKey = "README.md";
    let activeTrack = "all";
    let activeDiff = "All";
    let viewMode = "dual"; // 'dual', 'notes', 'code'
    const collapsedCategories = {{}};
    const reviewedSet = new Set(JSON.parse(localStorage.getItem("reviewedProblems") || "[]"));

    function saveReviewed() {{
      localStorage.setItem("reviewedProblems", JSON.stringify(Array.from(reviewedSet)));
      updateProgressBadge();
    }}

    function toggleReviewed(e, key) {{
      e.stopPropagation();
      if (reviewedSet.has(key)) {{
        reviewedSet.delete(key);
      }} else {{
        reviewedSet.add(key);
      }}
      saveReviewed();
      renderNav();
    }}

    function updateProgressBadge() {{
      const problemKeys = Object.keys(items).filter(k => items[k].type === "problem");
      const doneCount = problemKeys.filter(k => reviewedSet.has(k)).length;
      const pct = problemKeys.length ? Math.round((doneCount / problemKeys.length) * 100) : 0;
      document.getElementById("progressStats").innerText = `${{doneCount}} / ${{problemKeys.length}} (${{pct}}%)`;
    }}

    function setViewMode(mode) {{
      viewMode = mode;
      const leftPane = document.getElementById("left-pane");
      const rightPane = document.getElementById("right-pane");
      
      document.getElementById("btnDual").classList.toggle("active", mode === "dual");
      document.getElementById("btnNotes").classList.toggle("active", mode === "notes");
      document.getElementById("btnCode").classList.toggle("active", mode === "code");

      if (mode === "dual") {{
        leftPane.style.display = "block";
        leftPane.style.flex = "1";
        rightPane.style.display = "flex";
        rightPane.style.flex = "1";
      }} else if (mode === "notes") {{
        leftPane.style.display = "block";
        leftPane.style.flex = "1";
        rightPane.style.display = "none";
      }} else if (mode === "code") {{
        leftPane.style.display = "none";
        rightPane.style.display = "flex";
        rightPane.style.flex = "1";
      }}
    }}

    function setTrackFilter(track) {{
      activeTrack = track;
      document.querySelectorAll(".sidebar-header .filter-pills:first-of-type .pill").forEach(p => {{
        const text = p.innerText.toLowerCase();
        if (track === 'all' && text === 'all') {{
          p.classList.add('active');
        }} else if (track !== 'all' && text.includes(track.replace('-', ' '))) {{
          p.classList.add('active');
        }} else {{
          p.classList.remove('active');
        }}
      }});
      renderNav();
      filterItems();
    }}

    function setDiffFilter(diff) {{
      activeDiff = diff;
      document.querySelectorAll(".sidebar-header .filter-pills:last-of-type .pill").forEach(p => {{
        p.classList.toggle("active", p.innerText.includes(diff));
      }});
      renderNav();
      filterItems();
    }}

    function toggleCategory(groupName) {{
      collapsedCategories[groupName] = !collapsedCategories[groupName];
      renderNav();
    }}

    function expandAllCategories() {{
      for (const k in collapsedCategories) {{
        collapsedCategories[k] = false;
      }}
      renderNav();
    }}

    function collapseAllCategories() {{
      const groups = [
        "🎯 Problem Index",
        "📖 Overview",
        "🔥 Top 100 Liked Track",
        "📅 Daily Practice Track",
        "📚 Luffy Curriculum (01-42)"
      ];
      groups.forEach(g => collapsedCategories[g] = true);
      renderNav();
    }}

    function renderNav() {{
      const navList = document.getElementById("navList");
      const groups = {{
        "🎯 Problem Index": Object.keys(items).filter(k => k.startsWith("topic-")),
        "📖 Overview": Object.keys(items).filter(k => k === "README.md"),
        "🔥 Top 100 Liked Track": Object.keys(items).filter(k => k.startsWith("top-100/")),
        "📅 Daily Practice Track": Object.keys(items).filter(k => k.startsWith("daily-practice/")),
        "📚 Luffy Curriculum (01-42)": Object.keys(items).filter(k => k.startsWith("luffy/"))
      }};

      let html = "";
      for (const [groupName, keys] of Object.entries(groups)) {{
        const filteredKeys = keys.filter(k => {{
          const item = items[k];
          const matchTrack = activeTrack === 'all' || 
            (activeTrack === 'problem-index' && k.startsWith("topic-")) ||
            k.startsWith(activeTrack);
          const matchDiff = activeDiff === 'All' || item.diff === activeDiff || item.diff === 'All';
          return matchTrack && matchDiff;
        }});

        if (filteredKeys.length === 0) continue;

        const isCollapsed = !!collapsedCategories[groupName];
        const collapseClass = isCollapsed ? "collapsed" : "";

        html += `
          <div class="section-group ${{collapseClass}}" id="group-${{groupName.replace(/[^a-zA-Z0-9]/g, '_')}}">
            <div class="section-title" onclick="toggleCategory('${{groupName}}')">
              <div class="section-title-left">
                <span class="chevron">▼</span>
                <span>${{groupName}}</span>
              </div>
              <span class="count-badge">${{filteredKeys.length}}</span>
            </div>
            <div class="section-items">
        `;

        for (const k of filteredKeys) {{
          const item = items[k];
          const activeClass = k === currentKey ? "active" : "";
          const isReviewed = reviewedSet.has(k);
          const checkedClass = isReviewed ? "checked" : "";
          const diffClass = `diff-${{item.diff}}`;

          html += `
            <div class="nav-item ${{activeClass}}" onclick="switchItem('${{k}}')" data-key="${{k}}" data-title="${{item.title}}" data-track="${{item.path.split('/')[0]}}" data-diff="${{item.diff}}">
              ${{item.type === 'problem' ? `<span class="check-box ${{checkedClass}}" onclick="toggleReviewed(event, '${{k}}')" title="Mark as reviewed">✓</span>` : ''}}
              <span class="diff-dot ${{diffClass}}"></span>
              <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1;">${{item.short}}</span>
            </div>
          `;
        }}

        html += `
            </div>
          </div>
        `;
      }}
      navList.innerHTML = html;
    }}

    function switchItem(key) {{
      if (!items[key]) return;
      currentKey = key;
      const item = items[key];

      // Auto expand category
      if (item.category && collapsedCategories[item.category]) {{
        collapsedCategories[item.category] = false;
        renderNav();
      }}

      document.querySelectorAll(".nav-item").forEach(el => {{
        el.classList.toggle("active", el.dataset.key === key);
      }});

      // Top Toolbar Metadata
      document.getElementById("itemMeta").innerHTML = `
        <span>📁 <strong>${{item.path}}</strong></span>
        ${{item.diff !== 'All' ? `<span class="diff-dot diff-${{item.diff}}"></span><span style="font-size: 11px; color: var(--text-muted);">${{item.diff}}</span>` : ''}}
      `;

      // Auto view mode: Full width for docs/overview, dual for problems
      if (item.type === "doc" || !item.code) {{
        setViewMode("notes");
        document.getElementById("btnDual").style.display = "none";
        document.getElementById("btnCode").style.display = "none";
      }} else {{
        document.getElementById("btnDual").style.display = "flex";
        document.getElementById("btnCode").style.display = "flex";
        setViewMode("dual");
      }}

      // Render Markdown
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

      // Smart link interception: clicking internal markdown links navigates inside SPA!
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

    function filterItems() {{
      const q = document.getElementById("search").value.toLowerCase();
      document.querySelectorAll(".nav-item").forEach(item => {{
        const title = item.dataset.title.toLowerCase();
        const key = item.dataset.key.toLowerCase();
        const diff = item.dataset.diff;
        const matchSearch = title.includes(q) || key.includes(q);
        const matchDiff = activeDiff === 'All' || diff === activeDiff || diff === 'All';
        
        let matchTrack = false;
        if (activeTrack === 'all') {{
          matchTrack = true;
        }} else if (activeTrack === 'problem-index') {{
          matchTrack = item.dataset.track === 'problem-index';
        }} else {{
          matchTrack = item.dataset.track === activeTrack;
        }}

        if (matchSearch && matchTrack && matchDiff) {{
          item.style.display = "flex";
        }} else {{
          item.style.display = "none";
        }}
      }});

      // Auto expand categories when search query entered
      if (q.trim().length > 0) {{
        document.querySelectorAll(".section-group").forEach(group => {{
          group.classList.remove("collapsed");
        }});
      }}
    }}

    function copyActiveCode() {{
      const item = items[currentKey];
      if (!item || !item.code) return;
      navigator.clipboard.writeText(item.code).then(() => {{
        const btn = document.querySelector("#right-pane .pane-header button");
        if (btn) {{
          btn.innerText = "✓ Copied!";
          setTimeout(() => btn.innerText = "Copy Python", 1500);
        }}
      }});
    }}

    // Global keyboard shortcuts
    window.addEventListener("keydown", (e) => {{
      if (e.key === "/" && document.activeElement.tagName !== "INPUT") {{
        e.preventDefault();
        document.getElementById("search").focus();
      }} else if (e.key === "Escape") {{
        document.getElementById("search").value = "";
        document.getElementById("search").blur();
        filterItems();
      }}
    }});

    renderNav();
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
