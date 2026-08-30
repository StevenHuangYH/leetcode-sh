# CONTEXT.md — Domain Model & Architectural Context

This file serves as the single source of truth for domain vocabulary and architectural seams within leetcode-sh.

---

## Domain Vocabulary & Glossary

### 1. Core Compilers & Generators
* **StudyStationCompiler**: The central deep module responsible for discovering workspace problem entities, parsing curriculum/roadmap topologies, injecting template assets, and compiling the self-contained index.html Single Page Application (SPA).
* **DocumentEntity**: The primary domain data model representing a tracked problem, curriculum topic, or roadmap document. Holds metadata (slug, difficulty, tags, category, short title), paired source code, and Markdown walkthrough content.
* **CurriculumParser**: The parsing engine that scans README.md and extracts 11 standard curriculum topics, mapping problem links to their underlying track locations.
* **RoadmapParser**: The topological parser that reads ROADMAP.md and generates hierarchical phase-topic-problem graphs.
* **TemplateBundler**: The asset bundler that inlines modular CSS, JS, and HTML template sources in Python memory without requiring external Node.js/npm dependencies.

### 2. Integrity & Quality Guardians
* **NoteStructureValidator**: The quality enforcement module that audits companion .md notes against the standard 7-Section Active Recall template mandated by AGENTS.md.
* **ValidationResult**: The structured result object returned by NoteStructureValidator, providing granular diagnostics on missing sections, bilingual tags, error log schemas, and complexity proofs.

### 3. Three Pillars of Algorithmic Mastery
* **Pillar 1: Core Linear Structures & Array Techniques**: Proficient in contiguous memory manipulations, prefix sums, difference arrays, matrices, two-pointer techniques, sliding window mechanics, binary search variants, circular arrays, stacks, queues, and hash-based structures.
* **Pillar 2: Non-Linear Architectures & Tree Hierarchies**: Pointer-based dynamic data structures, linked list manipulation, recursive modeling, binary trees, BSTs, heaps/priority queues, tries, foundational graph theory, and modular object design.
* **Pillar 3: Search Algorithms & Dynamic Problem-Solving Paradigms**: State-space exploration, level-order traversals (BFS, shortest path), recursive tree traversals (DFS, Backtracking), Divide and Conquer, Dynamic Programming, greedy strategies, and applied mathematical logic.

---

## Architectural Seams & Principles

1. **Depth over Shallowness**:
   * Modules present small public interfaces (e.g. compile_study_station(repo_root) and validate_note(content)), concealing filesystem crawlers, regex transformers, and KaTeX protection algorithms behind internal seams.

2. **Strict Baseline Immutability**:
   * Original .py problem files are strictly read-only during documentation generation, preserving the user's algorithmic baseline.

3. **Zero-Dependency Single Page Application**:
   * The output artifact (index.html) is 100% portable, offline-capable, and self-contained with no external build toolchain requirements.
