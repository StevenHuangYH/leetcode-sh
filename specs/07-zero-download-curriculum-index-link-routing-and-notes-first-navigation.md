# Spec 07: Zero-Download Curriculum Index Link Routing and Notes-First Navigation

## Problem Statement

When learners navigate problem solutions and walkthrough notes from the Topic-Wise Curriculum Index (e.g. `topic-01-arrays-sliding-window`, `topic-all`, or `README.md` topic tables) within the Single Page Application (SPA) Study Station (`index.html`), clicking relative file links (such as `luffy/02-lc-0001-two-sum.py` or `top-100/lc-0015-3sum.md`) causes web browsers to treat them as downloadable file assets. This triggers unexpected browser file downloads or 404 page navigation errors instead of loading the problem entity inside the workspace viewer.

Furthermore, when problem navigation occurs, opening dual split panes or displaying code by default violates the repository's strict Notes-First Active Recall philosophy (mandated by `AGENTS.md` and `CONTEXT.md`), revealing solutions prematurely before learners review the mental models and walkthrough notes.

## Solution

1. **Client-Side Event Delegation Interceptor (`InternalNavigationInterceptor`)**: Attach a global click delegation interceptor on the document that captures all `<a>` anchor clicks within Markdown rendering containers (`#notesViewer`, `#left-pane`), preventing default browser navigation and unwanted file downloads (`e.preventDefault()`).
2. **Resilient Multi-Tier Entity Resolver (`EntityReferenceResolver`)**: Implement an in-memory resolution engine in JavaScript that maps arbitrary relative paths (e.g. `luffy/02-lc-0001-two-sum.py`, `top-100/lc-0015-3sum.md`, `./lc-0015-3sum.py`), swaps extensions (`.md` ↔ `.py`), falls back across tracks (`top-100/`, `daily-practice/`, `luffy/`), extracts LeetCode problem numbers, and maps them directly to registered `DocumentEntity` keys in the `items` manifest.
3. **Strict Notes-First Navigation Policy (`NotesFirstLinkRouting`)**: Whenever an internal problem or topic link is clicked, the SPA strictly activates Notes-Only mode (`viewMode = "notes"` on desktop, `setMobileTab("notes")` on mobile) before loading the problem entity, preserving active recall.
4. **In-Pane Heading Anchor Scroller (`findHeadingElement`)**: Intercept in-page and cross-file hash anchors (e.g. `#table-of-contents`, `#1-arrays-strings-two-pointers--sliding-window`), resolve standard GitHub-compatible slug formats, and smoothly scroll the left notes pane to the target heading without mutating top-level URL hash routing.
5. **External Link Tab Isolation**: Identify external URLs (`http://`, `https://`, `mailto:`, `//`) and automatically assign `target="_blank"` and `rel="noopener noreferrer"` attributes to keep the SPA study session uninterrupted.
6. **Fallback Download Prevention**: If an unindexed or malformed relative file path is clicked, prevent browser download and provide graceful handling rather than triggering native file downloads.

## User Stories

1. As a learner viewing the Curriculum Index catalog (`topic-all`), I want clicking on a problem's solution code link (e.g. `luffy/02-lc-0001-two-sum.py`) to open that problem inside the SPA viewer immediately without triggering a file download.
2. As a learner browsing a topic-specific catalog (e.g. `1. Arrays, Strings & Sliding Window`), I want clicking a walkthrough note link (e.g. `top-100/lc-0015-3sum.md`) to switch the active problem and load the walkthrough note directly in the left pane.
3. As a student practicing active recall, I want any problem link clicked from the curriculum index or inside notes to open strictly in Notes-Only view (`viewMode = "notes"`), so that I can study the problem statement and mental models before choosing to reveal the Python solution.
4. As a mobile user studying algorithms on a smartphone (viewport width <= 768px), I want clicking a problem link to automatically activate the `notes` tab, so that the mobile screen displays the walkthrough without requiring manual tab toggling.
5. As a learner reading a long Markdown guide (such as `README.md`), I want clicking Table of Contents anchors (such as `#table-of-contents` or `#1-arrays-strings-two-pointers--sliding-window`) to smoothly scroll the notes container to that section without jarring the browser viewport.
6. As a student reading a problem note that references another problem (e.g. `LC 206` referenced from `LC 143` in another track directory), I want the cross-track reference to resolve seamlessly regardless of relative folder depth (`../daily-practice/...` or `./...`).
7. As a learner clicking an external LeetCode problem link (e.g. `https://leetcode.com/problems/two-sum/`), I want the link to open in a new browser tab with secure `noopener noreferrer` attributes, keeping my local study station open and uninterrupted.
8. As a user who clicks a `.py` link for a problem that only has a Python script without a Markdown walkthrough, I want the viewer to load the problem entity, display the "Python Solution Available" placeholder in the left pane, and preserve full access to the code pane.
9. As a developer browsing the repository on GitHub, I want all links in `README.md` and Markdown notes to remain standard relative file paths, ensuring 100% native GitHub browsing compatibility without requiring artificial hash anchors in Markdown sources.
10. As an automated continuous integration test runner, I want compiler unit tests in `tests/test_update_index.py` to verify that `EntityReferenceResolver` and `InternalNavigationInterceptor` are successfully bundled into `index.html`.
11. As a contributor, I want all original `.py` problem files on disk to remain strictly immutable and untouched during curriculum link resolution and study station generation.

## Implementation Decisions

### 1. Client-Side Link Interception & Entity Resolution
* **Event Delegation on Document**:
  * Listen for `click` events at the document level and find the closest anchor element: `const link = e.target.closest("a")`.
  * If the link has no `href`, ignore.
* **External Link Isolation**:
  * Pattern: `/^(https?:|\/\/|mailto:)/i`.
  * Automatically append `target="_blank"` and `rel="noopener noreferrer"`.
* **In-Page Anchor Scrolling**:
  * Pattern: `rawHref.startsWith("#")`.
  * If the anchor matches a known `item` key (e.g. `#top-100/lc-0015-3sum.py`), call `switchItem(anchorId)`.
  * Otherwise, query for target heading elements inside `#notesViewer` using a unified helper function `findHeadingElement(container, anchorId)` that tests exact IDs, name attributes, and slugified heading text (`cleanHeading.replace(/[^\w\s-]/g, "").trim().replace(/\s+/g, "-")`).
  * Execute `targetEl.scrollIntoView({ behavior: "smooth", block: "start" })`.
* **Multi-Tier Relative Entity Resolution**:
  * Clean raw href: strip leading `/`, `./`, `../`, and query parameters.
  * Extract hash anchor if present (e.g. `path#section`).
  * Tier 1: Direct key lookup (`items[cleanPath]`).
  * Tier 2: Extension swap (`.md` ↔ `.py`).
  * Tier 3: Problem index / topic documents lookup (`problem-index/${cleanPath}`, `topic-*`).
  * Tier 4: Track directory prefix scan (`top-100/${stem}.(py|md)`, `daily-practice/${stem}.(py|md)`, `luffy/${stem}.(py|md)`).
  * Tier 5: LeetCode problem number (`targetLcNum`) and slug matching across all registered `DocumentEntity` items.
  * Tier 6: Fallback download prevention: If resolution returns `null` for a relative link, prevent default browser download and log a console notice.

### 2. View Mode Enforcement & Mobile Responsiveness
* When any internal problem or document entity is resolved:
  * Prevent default browser behavior (`e.preventDefault()`).
  * On mobile (`window.innerWidth <= 768`): invoke `setMobileTab("notes")`.
  * On desktop (`window.innerWidth > 768`): invoke `setViewMode("notes")`.
  * Switch problem entity: `switchItem(targetKey)`.
  * If a sub-anchor was attached, wait for the DOM render cycle and scroll to the target heading.

### 3. Shared DOM Heading Extraction Helper (`findHeadingElement`)
* Consolidate repeated heading query loops between in-page anchor navigation and cross-file anchor navigation into a single reusable helper function:
  ```javascript
  function findHeadingElement(container, anchorId) {
    if (!container || !anchorId) return null;
    const direct = container.querySelector(`[id="${anchorId}"], [name="${anchorId}"]`);
    if (direct) return direct;
    const cleanAnchor = anchorId.toLowerCase();
    return Array.from(container.querySelectorAll("h1, h2, h3, h4, h5, h6")).find(h => {
      const cleanHeading = h.textContent.trim().toLowerCase();
      const slug1 = cleanHeading.replace(/[^\w\s-]/g, "").trim().replace(/\s+/g, "-");
      const slug2 = cleanHeading.replace(/[^\w\s-]/g, " ").trim().replace(/\s+/g, "-");
      return slug1 === cleanAnchor || slug2 === cleanAnchor || cleanHeading === cleanAnchor;
    }) || null;
  }
  ```

### 4. Clean Variable Scope
* Remove unused local variable declarations (`isPy`, `isMd`) in `initLinkInterceptor` to avoid dead code smells following the consolidation of Notes-Only mode.

## Testing Decisions

### 1. Compiler Bundler & Integrity Test Seam
* **Module Tested**: `scripts.compiler.bundler.TemplateBundler` via `tests/test_update_index.py`.
* **Testing Scope**:
  * Verify that `bundler.bundle(minify=False)` successfully inlines `resolveEntityReference`, `initLinkInterceptor`, and `findHeadingElement`.
  * Verify that `initLinkInterceptor()` is invoked during SPA initialization.
  * Verify that `update_index.py --clean` compiles all 187 problem entities and curriculum topics without bundling syntax errors.

### 2. Entity Resolution & Navigation Contracts
* **Testing Contracts**:
  * Verify exact path resolution: `luffy/02-lc-0001-two-sum.py` → `luffy/02-lc-0001-two-sum.py`.
  * Verify extension swap resolution: `top-100/lc-0015-3sum.md` → `top-100/lc-0015-3sum.py`.
  * Verify cross-track stem resolution: `02-lc-0001-two-sum` → `luffy/02-lc-0001-two-sum.py`.
  * Verify slug & number fallback resolution: `lc-0015` → `top-100/lc-0015-3sum.py`.
  * Verify unindexed link download prevention contract.

## Out of Scope

* Modifying or refactoring original Python (`.py`) problem source code in `top-100/`, `daily-practice/`, or `luffy/` (strictly prohibited by Core Rule 1).
* Modifying external LeetCode problem URLs in `README.md` or problem notes.
* Introducing third-party JavaScript router dependencies or Node.js build dependencies (retaining 100% zero-dependency standalone SPA architecture).

## Further Notes

* **Labels**: `ready-for-agent`, `spec`, `viewer`, `router`
* **Architectural Alignment**: Fully documented in `CONTEXT.md` under Domain Vocabulary (`InternalNavigationInterceptor`, `EntityReferenceResolver`, `NotesFirstLinkRouting`) and Architectural Principle 7 (*Zero-Download In-App Navigation & Notes-First Routing*).
