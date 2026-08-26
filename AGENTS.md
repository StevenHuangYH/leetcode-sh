# AGENTS.md - Repository Guidelines & AI Assistant Rules

This file establishes the operational rules and standards for all AI coding assistants (Antigravity, Claude, Copilot, etc.) working within the `leetcode-sh` repository.

---

## 🎯 Repository Overview & Architecture

* **`top-100/`**: High-frequency LeetCode Top 100 Liked problems with paired `.py` solutions and `.md` walkthrough notes.
* **`luffy/`**: Structured 42-topic algorithmic curriculum problems and notes.
* **`daily-practice/`**: Daily challenges, contest problems, and algorithmic practice.
* **`index.html`**: Self-contained Single Page App (SPA) study station with dual split-pane viewer.
* **`update_index.py`**: Automated script that scans the repository, pairs `.py` and `.md` files, and compiles `index.html`.

---

## 🔒 Core Rule 1: Strict Immutability of Original Python (`.py`) Files

> [!IMPORTANT]
> **When creating, updating, or explaining notes (`.md` files), the corresponding Python (`.py`) file is STRICTLY READ-ONLY.**

1. **Zero Modifications During Note Generation**:
   * NEVER modify, reformat, refactor, or overwrite the existing `.py` file when the user asks for a note, walkthrough, explanation, or documentation.
   * NEVER inject alternative classes, comments, or extra template code into the `.py` file unless the user explicitly commands you to modify code in `.py`.
   * The user's original code in `.py` is the authoritative baseline and must be preserved exactly as written.

2. **Intent & Trigger Separation**:
   * **Markdown-Only Tasks** (zero `.py` edits): Prompts containing words like `note`, `notes`, `walkthrough`, `explain`, `document`, `add notes for [problem]`.
   * **Code Modification Tasks** (permits `.py` edits): Prompts explicitly stating `code`, `implement`, `fix code in py`, `refactor py`, `solve [problem]`.

3. **Placement of Optimizations & Alternative Solutions**:
   * Any optimizations, alternative algorithmic paradigms (e.g., 3-interval binary search templates, extreme pruning, recursion vs. iteration), bug fixes, or edge-case handling must be documented **exclusively within the companion `.md` note**, never in the `.py` file.

---

## 📝 Core Rule 2: Standard 7-Section Structure for Companion `.md` Notes (Active & Exam-Oriented Standard)

Every companion `.md` note must adhere to the standard 7-section structure, designed around active recall, mental model mapping, and exam/interview readiness:

1. **Header & File Links**:
   * Problem number, English & Chinese title, difficulty rating, tags, and clickable markdown link to the corresponding `.py` file.
2. **Problem Statement & Constraints (Bilingual)**:
   * English (`[EN]`) and Chinese (`[CN]`) problem statements, plus complete input constraints and edge assumptions.
3. **Core Idea, Mental Model & Pattern Lineage (Visuals & Mathematics)**:
   * **ASCII Pattern Lineage Map (算法思维谱系演化图)**: Visually show how the current problem inherits from foundational primitives (e.g. `LC 206 → LC 92 → LC 25`) and what new twist was introduced.
   * Core insights, mathematical proofs, invariants, and multi-stage ASCII diagrams.
4. **Step-by-Step Code Walkthrough**:
   * Line-by-line breakdown based **strictly on the user's original `.py` implementation**, explaining the rationale, variable roles, and loop invariants.
5. **Interview Simulation: Alternative Paradigms & Follow-up Pivots (面试官追问演练)**:
   * Framed as real-world **Interviewer Follow-ups** (e.g. *"Interviewer: Can you do this in one pass without length pre-counting?"* or *"Interviewer: How would you solve this recursively?"*).
   * Comparative tables and clean code snippets for alternative templates.
6. **The Error Log & Complete Dry-Run (错题排查与实例推演)**:
   * **⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)**: 4-column matrix (*Buggy Pattern / Traps* $\rightarrow$ *Symptom & Fail Case* $\rightarrow$ *Root Cause* $\rightarrow$ *Defensive Fix & Invariant*).
   * Complete step-by-step dry-run table on representative inputs.
   * Key boundary FAQs (single elements, $k=1$, $k=n$, duplicates, empty lists).
7. **Complexity Analysis**:
   * Markdown table detailing Time Complexity and Space Complexity with rigorous mathematical rationales.

---

## 🚀 Core Rule 3: Mandatory 4-Step Push & Walkthrough Protocol

Whenever creating a note, implementing a solution, or preparing to push to GitHub, AI assistants **MUST execute the following 4-step protocol in exact sequence**:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. Note Creation / Verification                                         │
│    • Generate/update companion .md note (strictly preserve .py).        │
│    • Ensure standard zero-padded format: lc-{4-digit-id}-{slug}.(py|md) │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 2. README.md Synchronization                                            │
│    • Update tracking table in ## Top 100 Liked Track or Daily Track.    │
│    • Update topic catalog in ## Topic-Wise Curriculum & Problem Index.  │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 3. Mandatory index.html Rebuild (update_index.py)                       │
│    • Execute: python3 update_index.py                                   │
│    • VERIFY that the new/updated problem is compiled into index.html.   │
│    • NEVER commit or push if index.html has not been regenerated.       │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 4. Stage, Commit & Push                                                 │
│    • git add -A                                                         │
│    • git commit -m "<type>(<scope>): <clear description>"               │
│    • git push origin main                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🎨 Core Rule 4: Visual & Iconography Standards

1. **Strict Prohibition of Distracting Emojis in README & Documentation**:
   * **Zero Distracting Emojis**: NEVER use decorative, random, or distracting emojis in `README.md` (e.g., no emojis in section titles, headings, table headers, table cells, or bullet points such as `🔥`, `🚀`, `✨`, `📁`, `📊`, `📑`, `🟢`, `🟡`, `🔴`).
   * Keep `README.md` and repository documents strictly clean, minimal, typography-focused, and professional.

2. **Clean Monochromatic SVG Iconography on `index.html`**:
   * The web viewer (`index.html`) and automated generator (`update_index.py`) use clean, theme-matched SVG / monochrome icons (VS Code / GitHub Dark aesthetic).
   * **No Multi-Colored Platform Emojis**: Category labels, accordion folders, and navigation nodes must avoid platform-dependent multi-colored emojis to ensure a consistent, developer-focused IDE aesthetic across all operating systems.

---

## 📊 Post-Push Completion Report Standard

Whenever a push is executed, the assistant must provide a structured confirmation report to the user containing:
1. **Commit & Remote Status**: Commit hash, branch target (`main -> origin/main`), and list of modified files.
2. **Viewer Navigation Path**: The exact sidebar path in `index.html` where the note/solution can be viewed (e.g., `Daily Practice Track -> LC 0153 find minimum in rotated sorted array`).
3. **Browser Cache Invalidation Reminder**: Explicit instructions to hard-refresh the browser tab (`Ctrl + Shift + R` or `Cmd + Shift + R`) to bypass cached HTML.

