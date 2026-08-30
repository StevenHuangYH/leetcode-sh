# CONTEXT.md — Domain Model & Architectural Context

This file serves as the single source of truth for domain vocabulary, topological models, and architectural seams within `leetcode-sh`.

---

## Domain Vocabulary & Glossary

### 1. Core Compilers & Generators
* **StudyStationCompiler**: The central deep module responsible for discovering workspace problem entities, parsing curriculum metadata, bundling template assets in Python memory, and compiling the self-contained `index.html` Single Page Application (SPA).
* **DocumentEntity**: The primary domain data model representing a tracked problem, curriculum topic, or project overview document. Holds metadata (slug, difficulty, tags, category, short title), paired source code, and companion Markdown walkthrough content.
* **CurriculumParser**: The parsing engine that scans `README.md` and extracts 11 standard curriculum topics, mapping problem links to their underlying track locations (`top-100/`, `daily-practice/`, `luffy/`).
* **TopologyGraph**: The directed acyclic graph (DAG) domain model representing the algorithm learning lineage. Composed of `TopologyNode` entities (with status markers: `mastered`, `learning`, `unvisited`, and mental model summaries) and `TopologyEdge` entities (with perspective labels: `层序遍历`, `遍历视角`, `子问题视角`, `其他算法`).
* **TemplateBundler**: The asset bundler that inlines modular CSS, JS, and HTML template sources into `index.html` without requiring external Node.js/npm dependencies.

### 2. Integrity & Quality Guardians
* **NoteStructureValidator**: The quality enforcement module that audits companion `.md` notes against the standard 7-Section Active Recall template mandated by `AGENTS.md`.
* **ValidationResult**: The structured result object returned by `NoteStructureValidator`, providing granular diagnostics on missing sections, bilingual tags, error log schemas, and complexity proofs.

### 3. Dual-Subtree Algorithmic Mastery Hierarchy
* **Array Subtree (数组子树)**:
  * *Operations Pipeline*: Contiguous memory, prefix sums, difference arrays, and 2D matrix transformations.
  * *Two Pointers Pipeline*: Fast/slow pointers, collision pointers, sliding window dynamic bounds, binary search variants, and randomized algorithms.
  * *Data Structures Pipeline*: Basic structures (circular arrays, stacks, queues, hash tables, design) transitioning to advanced structures (BSTs, heaps, tries, graph adjacency).
* **Linked List & Tree Subtree (链表与树子树)**:
  * *Bridge to Trees*: Discrete pointers, in-place re-linking, recursion foundations, and binary tree hierarchies.
  * *Level-order Pipeline*: Queue-driven level traversal, breadth-first search (BFS), and shortest path algorithms.
  * *Recursive Traversal Multi-Branching*:
    * *Traversal Perspective (遍历视角)*: Decision tree exploration $\rightarrow$ Backtracking $\rightarrow$ Depth-First Search (DFS).
    * *Subproblem Perspective (子问题视角)*: Disjoint subproblems $\rightarrow$ Divide & Conquer $\rightarrow$ Dynamic Programming (DP).
    * *Miscellaneous (其他算法)*: Mathematical logic, bit manipulation $\rightarrow$ Greedy Algorithms.

---

## Architectural Seams & Principles

1. **Depth over Shallowness**:
   * Modules present small, clean public interfaces (e.g. `compile_study_station(repo_root)` and `validate_note(content)`), concealing filesystem crawlers, regex transformers, and KaTeX protection algorithms behind internal seams.

2. **Strict Baseline Immutability (Core Rule 1)**:
   * Original `.py` problem files are strictly read-only during documentation generation, preserving the user's algorithmic baseline.

3. **Zero-Dependency Single Page Application**:
   * The output artifact (`index.html`) is 100% portable, offline-capable, and self-contained with no local node runtime requirements.

4. **Minimalist IDE Aesthetic & Interactive Topology**:
   * Clean dark theme (`#0d1117` background, `#161b22` cards, `#2dd4bf` teal accents) with full-viewport interactive DAG topology, floating HUD controls, and instant note loading hooks.
