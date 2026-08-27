# Spec: Search Architecture Refactoring & Fowler Code Smells Fix

**Triage Label:** `ready-for-agent`

---

## Problem Statement

When using the LeetCode study station search bar in `index.html`, users experience performance jitter, duplicated parsing overhead, and occasional search gaps:
1. Search matching repeatedly executes raw regexes and string slicing across multiple functions for every item and keystroke (Primitive Obsession & Duplicated Code).
2. Typing quickly triggers immediate DOM layout churn, history mutations, and split-pane re-renders on every intermediate keystroke (e.g. typing `104` triggers two unwanted view switches before reaching the target problem) (Feature Envy / Tight Coupling).
3. Search indexing relies on arbitrary character truncation and hardcoded heuristics (`token + "sum"`), risking missed keyword matches in long notes.
4. Pressing `Enter` blurs the search box but leaves the keyboard focus stranded rather than transitioning it to the note reader pane.

---

## Solution

Refactor the search engine and workspace item model to resolve the Fowler code smells cleanly:
1. **Domain Model Normalization**: Extract problem numbers, clean slugs, bilingual titles, tags, and search tokens once during workspace indexing in Python and expose them as clean first-class attributes (`item.lc_num`, `item.slug`, `item.search_blob`).
2. **Decoupled Search & Debounced Auto-Navigation**: Separate pure search filtering from active view switching. Introduce a lightweight 150ms debounce for auto-switching during typing, while keeping tree item filtering instantaneous.
3. **Robust Token Matching**: Replace hardcoded suffix checks with universal word-boundary regex patterns and comprehensive metadata indexing.
4. **Fluid Keyboard Navigation**: When pressing `Enter` in the search box, immediately select the top matched problem, smoothly scroll it into view, and transfer DOM focus to `#notesPane` for immediate keyboard reading.

---

## User Stories

1. As a developer studying algorithm problems, I want typing in the search box to filter sidebar results instantaneously without lag, so that I can quickly explore matching problems.
2. As a developer typing a multi-digit problem number (such as `104`), I want the interface to avoid flickering through intermediate problems (`1` -> `10`) while I am actively typing, so that my view remains stable.
3. As a developer searching by problem number (`100`, `lc 100`, `1`, `19`), I want exact problem number matching without false-positive directory name collisions (e.g. searching `100` should not match all problems under `top-100/`), so that I only see relevant results.
4. As a developer searching by Chinese algorithm terms (e.g. `相同的树`, `无重复字符`, `滑动窗口`, `双指针`), I want all relevant problems to appear accurately regardless of where the term appears in the note metadata, so that I can study by topic and concept.
5. As a developer pressing `Enter` on the search input, I want the top matching note to immediately open and receive keyboard focus, so that I can start reading and scrolling with arrow keys without using the mouse.
6. As a developer pressing `Escape` in the search box, I want the search query to clear and the sidebar tree to restore its previous structure cleanly.
7. As a developer searching for a non-existent query, I want a clear, minimal empty state message, so that I immediately know no problems matched.
8. As a developer reviewing codebase quality, I want search logic to avoid duplicated regex parsing across functions, so that the code is maintainable and adheres to Fowler clean architecture standards.

---

## Implementation Decisions

1. **Workspace Data Ingestion (Python Pipeline)**:
   - In `collect_workspace_documents()`, pre-compute and store:
     - `lc_num`: canonical integer string (e.g. `"100"`, `"1"`, `"104"`).
     - `slug`: clean problem title slug without prefixes (e.g. `"same tree"`).
     - `cn_title`: Chinese title extracted from markdown headers.
     - `tags`: tag list extracted from markdown metadata.
     - `search_blob`: unified lowercase search string containing clean slug, Chinese title, tags, difficulty, and problem description keywords.

2. **Pure Search Predicate (JavaScript)**:
   - `matchesSearchQuery(item, query)` operates purely on pre-indexed domain attributes (`item.lc_num`, `item.slug`, `item.search_blob`).
   - Suffix and word checks use generic regex word boundaries (`\b\d+\b` or `\b<word>\b`) instead of hardcoded problem-specific strings.
   - Numeric tokens strictly match `item.lc_num` or explicit word boundaries in the slug.

3. **Debounced View Synchronization**:
   - Immediate rendering of filtered sidebar items on every `input` event (`renderTree(val)`).
   - 150ms debounced auto-switch of the main view (`switchItem(firstMatch, false)`) to prevent visual jitter during typing.
   - Immediate pane switch on explicit user actions (`Enter` key press or mouse click).

4. **DOM Focus Transition**:
   - On `Enter` key in search:
     - `switchItem(firstMatchedKey, true)`
     - `search.blur()`
     - Transfer focus to `#notesPane` with `tabIndex = -1` attribute to allow keyboard scrolling.

---

## Testing Decisions

1. **High-Level Functional Verification Seams**:
   - Verify search accuracy against high-frequency queries (`1`, `100`, `lc 100`, `3sum`, `相同的树`, `滑动窗口`, `二叉树`, `binary tree 104`, `nonexistent`).
   - Verify that directory names (e.g. `top-100`) do not cause false-positive matches when searching for problem `100`.
   - Verify `index.html` static generation without errors or duplicate regex warnings.

---

## Out of Scope

- Introducing external search dependencies or server-side search microservices (must remain 100% offline static SPA).
- Modifying problem solution code in `.py` files (strictly immutable per AGENTS.md Core Rule 1).

---

## Further Notes

- Maintains 100% compliance with `AGENTS.md` and repository standards.
- Preserves monochromatic SVG aesthetic and dual split-pane layout.
