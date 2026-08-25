# AGENTS.md - Repository Guidelines & AI Assistant Rules

This file establishes the operational rules and standards for all AI coding assistants (Antigravity, Claude, Copilot, etc.) working within the `leetcode-sh` repository.

---

## 🎯 Repository Overview & Architecture

* **`top-100/`**: High-frequency LeetCode Top 100 Liked problems with paired `.py` solutions and `.md` walkthrough notes.
* **`luffy/`**: Structured 42-topic algorithmic curriculum problems and notes.
* **`daily-practice/`**: Daily challenges, contest problems, and algorithmic practice.
* **`index.html`**: Self-contained Single Page App (SPA) study station with dual split-pane viewer.
* **`update_index.py`**: Automated script that scans the repository, pairs `.py` and `.md` files, and generates `index.html`.

---

## 🔒 Core Rule: Strict Immutability of Original Python (`.py`) Files

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

## 📝 Standard 7-Section Structure for Companion `.md` Notes

Every companion `.md` note must adhere to the standard 7-section structure:

1. **Header & File Links**:
   * Problem number, English & Chinese title, difficulty rating, tags, and clickable markdown link to the corresponding `.py` file.
2. **Problem Statement & Constraints (Bilingual)**:
   * English (`[EN]`) and Chinese (`[CN]`) problem statements, plus complete input constraints and edge assumptions.
3. **Core Idea & Intuition (Visuals / Mathematical Principles)**:
   * Core insight, slope theorems, mathematical proofs, ASCII diagrams, and pattern classifications (e.g., Red-Blue binary search coloring, two-pointer inward narrowing).
4. **Step-by-Step Code Walkthrough**:
   * Line-by-line breakdown based **strictly on the user's original `.py` implementation**, explaining the rationale, variable roles, and loop invariants.
5. **Alternative Paradigms & Optimizations**:
   * Comparative tables and clean code snippets for alternative templates (e.g. Closed, Left-closed Right-open, Open intervals) or advanced pruning.
6. **Key FAQs & Edge Cases**:
   * Detailed answers to common pitfalls, boundary edge cases (single-element arrays, duplicates, out-of-bounds safety), and step-by-step dry runs on representative examples.
7. **Complexity Analysis**:
   * Markdown table detailing Time Complexity and Space Complexity with clear rationales.

---

## ⚙️ Automated Companion Pipeline

Whenever a problem solution or companion note is added or updated:
1. Ensure both `.py` and `.md` use the standardized zero-padded format: `lc-{4-digit-id}-{problem-slug}.(py|md)`.
2. Update the corresponding tracking table(s) in [`README.md`](README.md):
   * `## 🔥 Top 100 Liked Track`
   * `## 📚 Topic-Wise Curriculum & Problem Index`
3. Execute `python3 update_index.py` to rebuild and synchronize [`index.html`](index.html).
