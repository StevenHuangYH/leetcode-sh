#!/usr/bin/env python3
"""
=============================================================================
LeetCode Workspace - Automated index.html Builder & Watcher
=============================================================================
This script scans all workspace folders (top-100, daily-practice, luffy,
README.md, INDEX.md), extracts topic-wise problem indexes, and compiles
a standalone, self-contained single-page web app (index.html).

Features:
- Categorized dropdown / pull-up collapsible accordion tabs
- Filter pills (All, 🎯 Problem Index, 🔥 Top 100, 📚 Luffy, 📅 Daily)
- KaTeX math rendering, syntax highlighting, and SPA client-side routing
- Automated git pre-commit hook integration
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

# Resolve base workspace directory
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
    """Scans all folders and builds the complete docs index."""
    all_docs = {}

    def process_file(rel_path: str, category: str, display_title: str, short_label: str):
        full_path = BASE_DIR / rel_path
        ftype = get_file_type(rel_path)
        if not full_path.is_file() and not rel_path.startswith("topic-"):
            return
        try:
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                raw_content = f.read()
        except Exception as e:
            raw_content = f"Error reading file: {e}"

        if ftype == "py":
            content = f"# Python Solution: `{full_path.name}`\n\n```python\n{raw_content}\n```"
        elif ftype == "txt":
            content = f"# Curriculum Topic Marker: `{full_path.name}`\n\n```text\n{raw_content}\n```"
        else:
            content = raw_content

        all_docs[rel_path] = {
            "category": category,
            "title": display_title,
            "short": short_label,
            "path": rel_path,
            "type": ftype,
            "content": content
        }

    # 1. Parse Topic-Wise Problem Index from README.md Section 5
    readme_path = BASE_DIR / "README.md"
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
            readme_text = f.read()

        topic_sections = [
            ("topic-all", "Problem Index: Complete Topic Catalog", "All 11 Topics Combined", None),
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

        sec5_match = re.search(r'(## 5\. Topic-Wise Curriculum & Problem Index.*?)(\n## 6\. How to Run)', readme_text, re.DOTALL)
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

            all_docs[key] = {
                "category": "🎯 Problem Index",
                "title": title,
                "short": short,
                "path": f"problem-index/{key}",
                "type": "md",
                "content": topic_content
            }

    # 2. Overview Documents
    process_file("README.md", "📖 Overview", "LeetCode Self-Practices Overview (README)", "README.md")
    process_file("INDEX.md", "📖 Overview", "Master Problem Database & Curriculum Index (INDEX.md)", "INDEX.md")

    # 3. Top 100 Liked Track
    top100_dir = BASE_DIR / "top-100"
    if top100_dir.exists():
        for f in sorted(os.listdir(top100_dir)):
            if f.startswith("__") or f.endswith(".pyc"):
                continue
            rel = f"top-100/{f}"
            short = f.replace("s-lc-", "LC ").replace("-", " ")
            if short.endswith(".md") or short.endswith(".py"):
                short = short[:-3]
            process_file(rel, "🔥 Top 100 Liked Track", f"Top 100: {f}", short)

    # 4. Daily Practice Track
    daily_dir = BASE_DIR / "daily-practice"
    if daily_dir.exists():
        for f in sorted(os.listdir(daily_dir)):
            if f.startswith("__") or f.endswith(".pyc"):
                continue
            rel = f"daily-practice/{f}"
            short = f.replace("s-lc-", "LC ").replace("-", " ")
            if short.endswith(".md") or short.endswith(".py"):
                short = short[:-3]
            process_file(rel, "📅 Daily Practice Track", f"Daily Practice: {f}", short)

    # 5. Luffy Curriculum
    luffy_dir = BASE_DIR / "luffy"
    if luffy_dir.exists():
        for f in sorted(os.listdir(luffy_dir)):
            if f.startswith("__") or f.endswith(".pyc"):
                continue
            rel = f"luffy/{f}"
            short = f.replace("-lc-", " LC ").replace(".py", "").replace("___", "").replace("_", " ")
            process_file(rel, "📚 Luffy Curriculum (01-42)", f"Luffy Curriculum: {f}", short)

    return all_docs

def build_index_html():
    """Generates the single-page index.html file with collapsible accordion categories."""
    all_docs = collect_workspace_documents()
    docs_json = json.dumps(all_docs)

    html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LeetCode Self-Practices - Problem Index & Workspace Browser</title>
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
      --border-color: #30363d;
      --text-main: #c9d1d9;
      --text-muted: #8b949e;
      --accent: #58a6ff;
      --accent-hover: #1f6feb;
      --card-bg: #1c2128;
      --code-bg: #161b22;
      --tag-md: #238636;
      --tag-py: #1f6feb;
      --tag-txt: #8957e5;
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
      width: 380px;
      min-width: 380px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      height: 100%;
    }}
    .sidebar-header {{
      padding: 16px;
      border-bottom: 1px solid var(--border-color);
    }}
    .sidebar-header h1 {{
      font-size: 15px;
      font-weight: 600;
      color: #f0f6fc;
      margin-bottom: 10px;
      letter-spacing: 0.3px;
    }}
    .search-box {{
      width: 100%;
      padding: 8px 12px;
      background-color: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      color: #fff;
      font-size: 13px;
      outline: none;
    }}
    .search-box:focus {{
      border-color: var(--accent);
    }}
    .filter-pills {{
      display: flex;
      gap: 6px;
      margin-top: 10px;
      flex-wrap: wrap;
    }}
    .pill {{
      padding: 3px 8px;
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
    .accordion-controls {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 14px 4px;
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
      transition: opacity 0.15s;
    }}
    .control-btn:hover {{
      text-decoration: underline;
      color: #79c0ff;
    }}
    .nav-list {{
      flex: 1;
      overflow-y: auto;
      padding: 8px 8px 16px;
    }}
    .section-group {{
      margin-bottom: 6px;
    }}
    .section-title {{
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      padding: 8px 10px;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      user-select: none;
      border-radius: 6px;
      transition: background-color 0.15s, color 0.15s;
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
      padding: 7px 12px;
      border-radius: 6px;
      color: var(--text-main);
      text-decoration: none;
      font-size: 13px;
      cursor: pointer;
      margin-bottom: 2px;
      transition: all 0.15s ease;
      gap: 8px;
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
    .tag {{
      font-size: 9px;
      font-weight: 600;
      padding: 1px 5px;
      border-radius: 4px;
      margin-left: auto;
      text-transform: uppercase;
    }}
    .tag-md {{ background: rgba(35, 134, 54, 0.2); color: #3fb950; border: 1px solid rgba(63, 185, 80, 0.4); }}
    .tag-py {{ background: rgba(31, 111, 235, 0.2); color: #58a6ff; border: 1px solid rgba(88, 166, 255, 0.4); }}
    .tag-txt {{ background: rgba(137, 87, 229, 0.2); color: #bc8cff; border: 1px solid rgba(188, 140, 255, 0.4); }}
    #main-content {{
      flex: 1;
      overflow-y: auto;
      padding: 32px 48px;
      background-color: var(--bg-main);
    }}
    .markdown-body {{
      max-width: 1000px;
      margin: 0 auto;
      line-height: 1.65;
      font-size: 15px;
    }}
    .markdown-body h1, .markdown-body h2, .markdown-body h3 {{
      color: #f0f6fc;
      margin-top: 24px;
      margin-bottom: 12px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 6px;
    }}
    .markdown-body p, .markdown-body ul, .markdown-body ol {{
      margin-bottom: 16px;
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
      margin-bottom: 20px;
      overflow-x: auto;
    }}
    .markdown-body pre code {{
      border: none;
      padding: 0;
      background-color: transparent;
      font-size: 13.5px;
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
    .top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
      max-width: 1000px;
      margin-left: auto;
      margin-right: auto;
    }}
    .doc-meta {{
      font-size: 13px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .btn {{
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 12px;
      transition: all 0.15s;
    }}
    .btn:hover {{
      background: var(--border-color);
      color: #fff;
    }}
  </style>
</head>
<body>

  <div id="sidebar">
    <div class="sidebar-header">
      <h1>LeetCode Workspace</h1>
      <input type="text" id="search" class="search-box" placeholder="Search problems, topics, files..." oninput="filterDocs()">
      <div class="filter-pills">
        <span class="pill active" onclick="setFilter('all')">All</span>
        <span class="pill" onclick="setFilter('problem-index')">🎯 Problem Index</span>
        <span class="pill" onclick="setFilter('top-100')">🔥 Top 100</span>
        <span class="pill" onclick="setFilter('luffy')">📚 Luffy Track</span>
        <span class="pill" onclick="setFilter('daily-practice')">📅 Daily Track</span>
      </div>
    </div>
    <div class="accordion-controls">
      <span>Categories</span>
      <div style="display: flex; gap: 8px;">
        <button class="control-btn" onclick="expandAllCategories()">▾ Expand All</button>
        <button class="control-btn" onclick="collapseAllCategories()">▴ Fold All</button>
      </div>
    </div>
    <div class="nav-list" id="navList">
      <!-- Injected by JavaScript -->
    </div>
  </div>

  <div id="main-content">
    <div class="top-bar">
      <div class="doc-meta" id="docMeta">Loading...</div>
      <div style="display: flex; gap: 8px;">
        <button class="btn" onclick="copyContent()">Copy Content</button>
        <button class="btn" onclick="window.print()">Print / Export</button>
      </div>
    </div>
    <div class="markdown-body" id="docViewer">
      <!-- Markdown Content Injected Here -->
    </div>
  </div>

  <script>
    const docs = {docs_json};
    let currentKey = "topic-all";
    let activeTrack = "all";
    const collapsedCategories = {{}};

    function setFilter(track) {{
      activeTrack = track;
      document.querySelectorAll(".pill").forEach(p => {{
        const text = p.innerText.toLowerCase();
        if (track === 'all' && text.includes('all')) {{
          p.classList.add('active');
        }} else if (track !== 'all' && (text.includes(track) || (track === 'problem-index' && text.includes('problem index')))) {{
          p.classList.add('active');
        }} else {{
          p.classList.remove('active');
        }}
      }});
      renderNav();
      filterDocs();
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
        "🎯 Problem Index": Object.keys(docs).filter(k => k.startsWith("topic-")),
        "📖 Overview": Object.keys(docs).filter(k => k === "README.md" || k === "INDEX.md"),
        "🔥 Top 100 Liked Track": Object.keys(docs).filter(k => k.startsWith("top-100/")),
        "📅 Daily Practice Track": Object.keys(docs).filter(k => k.startsWith("daily-practice/")),
        "📚 Luffy Curriculum (01-42)": Object.keys(docs).filter(k => k.startsWith("luffy/"))
      }};

      let html = "";
      for (const [groupName, keys] of Object.entries(groups)) {{
        const filteredKeys = keys.filter(k => {{
          if (activeTrack === 'all') return true;
          if (activeTrack === 'problem-index') return k.startsWith("topic-");
          return k.startsWith(activeTrack) || (activeTrack === 'README.md' && (k === 'README.md' || k === 'INDEX.md'));
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
          const doc = docs[k];
          const activeClass = k === currentKey ? "active" : "";
          const tagClass = `tag-${{doc.type}}`;
          html += `
            <div class="nav-item ${{activeClass}}" onclick="switchDoc('${{k}}')" data-key="${{k}}" data-title="${{doc.title}}" data-track="${{doc.path.split('/')[0]}}">
              <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${{doc.short}}</span>
              <span class="tag ${{tagClass}}">${{doc.type}}</span>
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

    function switchDoc(key) {{
      if (!docs[key]) return;
      currentKey = key;
      const doc = docs[key];

      // Auto un-collapse the active item's group
      if (doc.category && collapsedCategories[doc.category]) {{
        collapsedCategories[doc.category] = false;
        renderNav();
      }}

      document.querySelectorAll(".nav-item").forEach(el => {{
        el.classList.toggle("active", el.dataset.key === key);
      }});

      document.getElementById("docMeta").innerHTML = `📁 <strong>${{doc.path}}</strong> <span style="color: var(--text-muted);">| ${{doc.title}}</span>`;
      
      marked.setOptions({{
        highlight: function(code, lang) {{
          const language = hljs.getLanguage(lang) ? lang : 'plaintext';
          return hljs.highlight(code, {{ language }}).value;
        }},
        gfm: true,
        breaks: true
      }});

      document.getElementById("docViewer").innerHTML = marked.parse(doc.content);

      document.querySelectorAll('pre code').forEach((el) => {{
        hljs.highlightElement(el);
      }});

      if (window.renderMathInElement) {{
        renderMathInElement(document.getElementById("docViewer"), {{
          delimiters: [
            {{left: "$$", right: "$$", display: true}},
            {{left: "$", right: "$", display: false}}
          ]
        }});
      }}

      // Smart link interception: clicking internal markdown links navigates inside the SPA!
      document.querySelectorAll('#docViewer a').forEach(a => {{
        const href = a.getAttribute('href');
        if (!href) return;
        if (href.startsWith('http://') || href.startsWith('https://')) return;
        if (href.startsWith('#')) return;

        let cleanHref = href.replace(/^(\\.\\/|\\/)/, '');
        if (docs[cleanHref]) {{
          a.onclick = (e) => {{
            e.preventDefault();
            switchDoc(cleanHref);
          }};
        }} else {{
          const matchingKey = Object.keys(docs).find(k => k.endsWith(cleanHref) || cleanHref.endsWith(k));
          if (matchingKey) {{
            a.onclick = (e) => {{
              e.preventDefault();
              switchDoc(matchingKey);
            }};
          }}
        }}
      }});

      document.getElementById("main-content").scrollTop = 0;
    }}

    function filterDocs() {{
      const q = document.getElementById("search").value.toLowerCase();
      document.querySelectorAll(".nav-item").forEach(item => {{
        const title = item.dataset.title.toLowerCase();
        const key = item.dataset.key.toLowerCase();
        const matchSearch = title.includes(q) || key.includes(q);
        let matchTrack = false;
        if (activeTrack === 'all') {{
          matchTrack = true;
        }} else if (activeTrack === 'problem-index') {{
          matchTrack = item.dataset.track === 'problem-index';
        }} else {{
          matchTrack = item.dataset.track === activeTrack;
        }}
        if (matchSearch && matchTrack) {{
          item.style.display = "flex";
        }} else {{
          item.style.display = "none";
        }}
      }});

      // Auto expand categories when search is active
      if (q.trim().length > 0) {{
        document.querySelectorAll(".section-group").forEach(group => {{
          group.classList.remove("collapsed");
        }});
      }}
    }}

    function copyContent() {{
      const doc = docs[currentKey];
      if (!doc) return;
      navigator.clipboard.writeText(doc.content).then(() => {{
        alert("Copied to clipboard!");
      }});
    }}

    renderNav();
    switchDoc(currentKey);
  </script>
</body>
</html>
"""

    output_path = BASE_DIR / "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"✨ [Success] Built {output_path.name} ({len(all_docs)} items indexed: 11 topics + 89 workspace files).")
    return output_path

def open_in_browser():
    """Opens index.html in the default system browser."""
    html_file = BASE_DIR / "index.html"
    if not html_file.exists():
        build_index_html()
    
    # WSL Windows browser launch support
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
