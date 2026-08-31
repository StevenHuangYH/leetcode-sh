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
* **ProblemTitleFormatter**: The entity normalization model responsible for stripping raw file prefixes (e.g. `01-lc-2235-` -> `LC 2235`), formatting standard bilingual titles (`LC {num} · {English Title} ({Chinese Title})`), and providing semantic non-problem catalog titles for top breadcrumb and tree display.
* **InternalNavigationInterceptor**: Client-side click delegation interceptor that captures link clicks within rendered notes and curriculum indexes, routing relative file references, in-page anchors, and external links without triggering browser navigation, page reloads, or file downloads.
* **EntityReferenceResolver**: The resilient multi-tier resolution engine that normalizes arbitrary relative paths (`luffy/02-lc-0001-two-sum.py`, `top-100/lc-0015-3sum.md`, `lc-0015-3sum.py`), performs cross-track stem lookup, LC-number extraction, and extension swapping (`.md` ↔ `.py`) to map references directly to in-memory `DocumentEntity` keys.
* **NotesFirstLinkRouting**: Strict notes-first in-app routing policy where clicking problem and curriculum links always opens the target problem directly in Notes-Only view (`viewMode = "notes"` / mobile `notes` tab) to maximize active recall and avoid unintended split/code pane expansion.

### 2. Integrity & Quality Guardians
* **NoteStructureValidator**: The quality enforcement module that audits companion `.md` notes against the standard 7-Section Active Recall template mandated by `AGENTS.md`.
* **ValidationResult**: The structured result object returned by `NoteStructureValidator`, providing granular diagnostics on missing sections, bilingual tags, error log schemas, and complexity proofs.

### 3. 38-Node Compound Algorithmic Topology Hierarchy (38 节点复合算法知识图谱)
* **Root**: `data-structure-algorithm` (Programs = Data Structures + Algorithms).
* **Array Subtree (数组子树体系)**:
  * *`array` Root*: Contiguous buffer with O(1) random access.
  * *`array-operation-group` (Operations 复合容器)*:
    * `diff-array`: O(1) interval boundary increments for frequent range modifications.
    * `2d-array-ops`: 2D matrix transformations, diagonal reflections, and spiral indexing.
    * `prefix-sum`: O(N) preprocessing for O(1) static range sum queries.
  * *`two-pointer-group` (Array Two Pointer 复合容器)*:
    * `two-pointer-array`: Monotonic opposite collision pointers and Two Sum / 3Sum.
    * `sliding-window`: Monotonic [left, right] closed-interval dynamic window bounds.
    * `binary-search`: Halving search spaces by monotonicity (left/right bounds & search by answer).
    * `random`: Reservoir sampling for data streams and Fisher-Yates array shuffling.
  * *`basic-ds-group` (Basic Data Structure 复合容器)*:
    * `cycle-array`: Modulo arithmetic for circular buffers without reallocation.
    * `stack-queue`: Monotonic stacks for Next Greater Element and monotonic queues.
    * `hashing`: O(1) frequency tables, deduplication sets, and in-place sign hashes.
    * `design`: Composite data structure design (LRU / LFU cache with Doubly Linked Lists).
* **Linked List & Tree Subtree (链表与树子树体系)**:
  * *`linked` Root*: Discrete pointer-linked dynamic nodes.
  * *Bridge to Trees*: `two-pointer-linked` (Floyd's Tortoise & Hare) $\rightarrow$ `recursion-ops` (Mathematical Induction Contract) $\rightarrow$ `binary-tree` (Foundational Hierarchy).
  * *`level-order-traverse` Pipeline*: Layer size snapshots (`sz = q.size()`) $\rightarrow$ `bfs` (Wavefront expansion) $\rightarrow$ `shortest-path` (Dijkstra state relaxation).
  * *`advanced-ds-group` (Advanced Data Structure 复合容器)*:
    * `bst`: Invariant Left < Root < Right with logarithmic search and sorted inorder.
    * `heap`: Complete binary tree priority queues with swim/sink operations.
    * `trie`: Multi-way string prefix trees for fast prefix matching and wildcards.
    * `graph`: Adjacency lists, Kahn's topological sort, and Union-Find disjoint sets.
  * *Recursive Traversal Multi-Branching (`recursive-traverse`)*:
    * *`traverse-view-group` (Traverse View 复合容器)*: `dfs` (Connected components & cycle checks) + `backtracking` (Choose $\rightarrow$ Explore $\rightarrow$ Unchoose decision trees).
    * *`subproblem-view-group` (Subproblem View 复合容器)*: `divide-conquer` (Disjoint subproblem merging) + `dp` (Overlapping subproblems & state transitions).
    * *`other-group` (Other 复合容器)*: `math` (Bitwise manipulation & number theory) + `greedy` (Local optimal choices with no aftermath).

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

5. **Notes-First Layout & Declarative View Architecture**:
   * Notes-only default viewing (`viewMode = "notes"`), dual split-pane orientation with notes on the left and code on the right, driven by declarative CSS classes (`.mode-notes`, `.mode-code`, `.mode-dual`) rather than imperative JavaScript mutations.

6. **Semantic Breadcrumb & Bilingual Title Normalization**:
   * Top breadcrumb and UI headers display formatted semantic titles (`LC {num} · {English Title} ({Chinese Title})` for problems, and human-readable topic names for catalogs) with graceful ellipsis truncation and full-title tooltips, completely abstracting disk filenames.

7. **Zero-Download In-App Navigation & Notes-First Routing**:
   * Relative `.py` and `.md` links in curriculum catalogs and markdown notes are dynamically intercepted and routed in memory via `InternalNavigationInterceptor` and `EntityReferenceResolver`, completely preventing unwanted browser file downloads. All internal link clicks strictly open the target problem in Notes-Only view (`viewMode = "notes"`) to preserve distraction-free active recall. External URLs are strictly isolated in new browser tabs.

