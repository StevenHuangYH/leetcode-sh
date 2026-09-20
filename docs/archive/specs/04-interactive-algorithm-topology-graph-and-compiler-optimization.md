# Spec: Interactive Algorithm Topology Graph & Compiler Architecture Optimization

**Labels**: `ready-for-agent`, `curriculum-topology`, `compiler-optimization`, `station-spa`

---

## Problem Statement

As the algorithm repository grows in breadth and depth, learners encounter difficulties visualizing how individual LeetCode problems connect back to foundational algorithm primitives and cognitive paradigms (e.g. how Linked List techniques transition through Recursion into Binary Trees, which then branch into Level-Order BFS, Backtracking DFS, and Divide & Conquer DP). 

Previously, learning roadmap tracking was split across a verbose Markdown document (`ROADMAP.md`) and static phase card grids inside the Study Station web viewer (`index.html`). This caused excessive visual clutter, cognitive fatigue, and navigation friction. Furthermore, graph node connections were hardcoded in the frontend, compilation lacked caching (parsing 180+ problems from scratch on every build), and git commits lacked automated pre-commit quality enforcement to guarantee compliance with the 7-section Active Recall standard.

---

## Solution

A fully interactive, directed acyclic graph (DAG) topology viewer integrated directly into the Study Station Single Page Application (SPA), backed by a modernized Python compiler architecture:

1. **Immersive Directed Topology Viewer**: A distraction-free, full-viewport interactive DAG rendered via Cytoscape.js and Dagre layout, modeling the precise dual-subtree algorithmic lineage (Array Pipeline & Linked List/Tree Multi-Branching) with directed edge semantics, node mastery status toggles, and live search synchronization.
2. **Streamlined Minimalist UI**: Elimination of phase cards, subview tab switchers, and redundant roadmap Markdown files in favor of a sleek dark-themed canvas with a floating glassmorphic HUD toolbar and adaptive detail popovers.
3. **Dynamic Topology Compiler**: Decoupling the graph hierarchy into a dedicated Python compiler module that enriches nodes dynamically with real-time problem counts and metadata from workspace entities.
4. **Incremental Manifest Caching**: File-state-based (mtime/size) caching in the compiler collector to enable sub-second incremental builds while providing an explicit clean rebuild bypass.
5. **Automated Pre-Commit Quality Gate**: A pre-commit Git hook that automatically runs note structure linting, unit tests, and SPA compilation before any commit is finalized.

---

## User Stories

1. As an algorithm learner, I want to explore an interactive directed graph of algorithm concepts, so that I can intuitively understand how data structures branch into advanced problem-solving paradigms.
2. As an algorithm learner, I want the algorithm topology to strictly separate the Array lineage from the Linked List & Tree lineage, so that my mental model mirrors core computer science principles.
3. As an algorithm learner, I want to trace the Operations pipeline (Array $\rightarrow$ Prefix Sum $\rightarrow$ Difference Array $\rightarrow$ 2D Matrix), so that I understand interval update patterns progressively.
4. As an algorithm learner, I want to trace the Two Pointers pipeline (Array $\rightarrow$ Array Two Pointers $\rightarrow$ Sliding Window $\rightarrow$ Binary Search $\rightarrow$ Randomized Algorithms), so that I understand monotonicity reduction techniques.
5. As an algorithm learner, I want to trace the Data Structures pipeline (Array $\rightarrow$ Basic Data Structures $\rightarrow$ Advanced Data Structures), so that I master cache design and tree/graph structures.
6. As an algorithm learner, I want to trace the Bridge pipeline (Linked List $\rightarrow$ Linked List Two Pointers $\rightarrow$ Recursion $\rightarrow$ Binary Tree), so that I understand how pointer mechanics foundationally enable tree algorithms.
7. As an algorithm learner, I want to see the Binary Tree node branch into Level-order Traversal (leading to BFS and Shortest Path) and Recursive Traversal, so that I clearly differentiate queue-driven breadth exploration from stack-driven depth exploration.
8. As an algorithm learner, I want the Recursive Traversal node to explicitly branch into Traversal Perspective (Backtracking $\rightarrow$ DFS), Subproblem Perspective (Divide & Conquer $\rightarrow$ Dynamic Programming), and Miscellaneous (Math $\rightarrow$ Greedy), so that I know exactly which mental model to apply during technical interviews.
9. As an algorithm learner, I want directed edges to display clean category labels (e.g. `层序遍历`, `遍历视角`, `子问题视角`), so that the conceptual pivot between nodes is immediately obvious.
10. As an algorithm learner, I want to click any topology node to open an adaptive detail popover, so that I can read the core mental model summary without losing my canvas view.
11. As an algorithm learner, I want to see the count of solved problems associated with each topology node, so that I know the depth of my repository coverage for that topic.
12. As an algorithm learner, I want to toggle a node's mastery status (Mastered, Learning, Unvisited) directly within the popover, so that I can personalize and track my study progress.
13. As an algorithm learner, I want my mastery status selections to persist across browser sessions in local storage, so that my learning progress is not reset on refresh.
14. As an algorithm learner, I want a "View Notes & Source" button on each node popover that immediately switches the SPA to the relevant problem or topic document in the workspace view.
15. As an algorithm learner, I want typing into the global sidebar search bar to automatically highlight matching topology nodes on the graph, so that I can locate relevant algorithm concepts instantly.
16. As an algorithm learner, I want a floating minimal HUD toolbar with quick zoom-in, zoom-out, and auto-fit buttons, so that I can easily navigate large graph structures on any screen size.
17. As an algorithm learner, I want the roadmap view to be free of clunky hero banners and redundant phase matrix cards, so that the screen real estate is maximized for the graph.
18. As a repository maintainer, I want the graph data to be generated dynamically by the Python compiler rather than hardcoded in JavaScript, so that future topic expansions automatically reflect throughout the application.
19. As a repository maintainer, I want the compiler to cache unchanged problem and note files, so that building the study station remains nearly instantaneous as the problem count scales.
20. As a repository maintainer, I want a `--clean` command-line flag to force a full rebuild bypassing the cache when necessary.
21. As a repository maintainer, I want a Git pre-commit hook to audit companion note active recall schemas, execute unit tests, and recompile the SPA, so that broken notes or out-of-sync HTML builds are never committed to version control.
22. As a repository maintainer, I want the repository's domain glossary (`CONTEXT.md`) to accurately document `TopologyGraph`, `TopologyNode`, and `TopologyEdge` entities, so that all AI assistants and contributors share an unambiguous domain vocabulary.

---

## Implementation Decisions

1. **Topology Graph Architecture (Deep Compiler Seam)**:
   - Encapsulate graph generation within a dedicated compiler module.
   - The graph builder consumes collected workspace document entities and outputs a Cytoscape-compatible structure containing structured `TopologyNode` and `TopologyEdge` definitions.
   - Node entities are enriched with problem counts derived from matching repository problem entities.
   - The compiled graph JSON payload is injected into the Single Page Application template via a compiler template replacement token.

2. **Full-Viewport Canvas & HUD Controls**:
   - The roadmap view container occupies 100% of the viewport area with a dark grid background.
   - User controls are concentrated into a single glassmorphic floating HUD pill with status dots and zoom/fit icon actions.
   - Phase cards and static Markdown overview documents for the roadmap are retired to eliminate redundant UI states.

3. **Incremental Manifest Caching**:
   - The document collector maintains a persistent manifest cache storing modification timestamps and file sizes.
   - If both the Python solution file and Markdown companion note for a problem remain unmodified, the collector reuses the cached document entity dictionary directly from memory/disk.
   - The build cache is stored under an ignored cache directory to prevent cache files from polluting version control.
   - A command-line bypass flag (`--clean` / `--force`) allows overriding the cache for clean rebuilds.

4. **Automated Pre-Commit Quality Gate**:
   - A version-controlled pre-commit hook is established within the repository.
   - The hook enforces a three-stage barrier: note structure linting, unit test discovery, and template compilation.
   - If any unit test fails or a companion note exhibits critical structural errors, the commit process is aborted.

5. **Client-Side Progressive Persistence**:
   - Node mastery statuses are stored in browser local storage.
   - On graph initialization, local storage values override default static node statuses, dynamically coloring node status rings without requiring backend state.

---

## Testing Decisions

- **Test Scope**:
  - Tests verify external behaviors and contract invariants rather than internal implementation details.
- **Topology Graph Invariants**:
  - Assert that the generated topology is a valid directed graph where every edge's source and target match an existing node identifier.
  - Assert that no self-loops exist.
  - Assert that key root nodes and downstream leaves exist and possess valid category and label attributes.
  - Assert that passing problem items to the graph builder enriches nodes with non-negative problem counts.
- **Incremental Cache Invariants**:
  - Assert that a cache manifest file is created upon document collection.
  - Assert that subsequent collection runs with caching enabled produce identical entity counts to cold runs.
  - Assert that clean rebuilds with caching disabled function reliably.
- **End-to-End Compilation**:
  - Assert that the compiler pipeline generates a valid, non-empty `index.html` artifact containing both problem items and the compiled topology graph.

---

## Out of Scope

- Multi-user authentication or cloud database synchronization for node mastery progress.
- Arbitrary custom node creation or dynamic graph editing directly inside the browser UI.
- Rewriting or refactoring original Python solution files (`AGENTS.md` Core Rule 1).
- External server-side rendering (SSR) runtimes (maintains strict Zero-Dependency Single Page Application architecture).

---

## Further Notes

- The resulting `index.html` remains fully self-contained, portable, and offline-capable.
- Graph layout uses Dagre hierarchical positioning configured for top-to-bottom flow with smooth edge routing.
