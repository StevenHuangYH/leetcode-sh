# Spec 18: Hash Routing Hardening, In-Session Navigation, and Anchor Resolution Integrity

**Triage Label**: `ready-for-agent`

---

## Problem Statement

When learners and maintainers navigate the `leetcode-sh` Study Station via direct URL bookmarks, internal section links, and browser history, routing and reference resolution exhibit edge-case failures and architectural friction:

1. **Lost Standalone Anchor Targets**:
   When users click or bookmark deep section links containing standalone hash fragments (such as `#complexity` or `#the-error-log`), the route resolver strips the leading hash character before forwarding the query to the entity reference resolver. Because the resolver relies on the hash prefix to distinguish anchor-only targets from relative file paths, it misinterprets the anchor as an unindexed file, fails to resolve, and silently discards the deep navigation target.

2. **Missing In-Session History and Hash Change Navigation**:
   URL hash routing currently executes only once during cold application startup. When a learner uses browser back/forward buttons, clicks anchor links in companion notes, or updates the URL hash during an active session, the view state fails to synchronize, leaving the user on a stale problem or section.

3. **Forced View Mode Resets on Invalid Routes**:
   When an invalid, malformed, or unresolvable hash is encountered, the router unconditionally defaults to the workspace overview document. This forcibly overrides the learner's persisted layout preference (such as the interactive roadmap view) and disrupts active recall sessions.

4. **Residual Dead Code in Entity Resolution Pipeline**:
   The entity reference resolver retains unreachable defensive branches attempting to convert `.py` problem files to `.md` companion keys. Because problem items in the Study Station dataset are indexed exclusively by their `.py` source paths, these lookups never succeed and violate YAGNI.

5. **Testing Seam Gaps for Static Documents and Anchors**:
   Compiler integration tests do not verify static documentation references (curriculum topics, problem index catalogs, overview documents) or standalone section anchors at the production execution seam, leaving room for regressions during routing refactors.

---

## Solution

1. **Preserve Standalone Anchor Targets**:
   Update route resolution to pass unmodified or properly classified anchor references to the entity reference resolver, ensuring that standalone section fragments (e.g. `#complexity`) preserve the active document and accurately dispatch smooth DOM scrolling to target headers.

2. **Unify In-Session Navigation with Centralized Hash Listener**:
   Attach a reactive `hashchange` event listener to window navigation that delegates directly to the centralized route resolver, ensuring browser back/forward history navigation and in-page anchor jumps update active items and scroll targets seamlessly without page reloads.

3. **Graceful Fallback without Layout Preference Corruption**:
   Revise route fallback behavior so that unrecognized or malformed hashes gracefully retain the user's current or persisted viewing mode (e.g. Interactive Roadmap vs. Workspace), preventing jarring visual resets.

4. **Eliminate All Residual Dead Extension Swapping**:
   Completely purge all remaining `.py` $\rightarrow$ `.md` item lookups across all stages of the entity reference resolver, enforcing strict unidirectional `.md` $\rightarrow$ `.py` problem mapping.

5. **High-Seam Contract Assertions**:
   Expand integration testing at the single production artifact seam—extracting compiled JavaScript routing functions and executing them in Node.js—to assert standalone anchor resolution, static document key retention, in-session route dispatching, and zero dead code branches.

---

## User Stories

1. As a learner following an in-page section link (such as `#complexity`), I want the client router to scroll directly to the matching section header, so that I can immediately review algorithmic proofs without manually scrolling.
2. As a learner clicking the browser's Back or Forward navigation buttons, I want the active problem and view mode to update instantly to match the URL hash history, so that browser history navigation works seamlessly.
3. As a student studying the Interactive Algorithm Topology Roadmap, I want navigating with an invalid or empty hash to preserve my roadmap view mode, so that my exploration is not abruptly reset to the workspace overview.
4. As a mobile learner switching between problem sections using anchor links, I want the client viewer to smoothly scroll the active note container to the target heading, so that my reading flow is continuous on small screens.
5. As a learner clicking cross-references between curriculum topics and problem catalogs, I want static markdown documents to resolve deterministically without path corruption, so that documentation remains fully accessible.
6. As a code reviewer inspecting the client routing architecture, I want route fallback constants to be defined once, so that default routing avoids duplicated return literals across multiple exit paths.
7. As a platform maintainer, I want all dead reverse `.py` to `.md` resolution checks removed from the resolver pipeline, so that the client bundle remains minimal, performant, and maintainable.
8. As a developer adding new features to the client runtime, I want a single centralized route resolution pipeline that handles both initial cold boot and runtime hash changes, so that routing behavior never diverges between page load and user interaction.
9. As a test engineer running automated compiler validation, I want integration tests to assert standalone anchor handling and static document resolution using production JavaScript extracted from the compiled artifact, so that tests verify true browser behavior.
10. As a QA contributor, I want test suites to verify that no forbidden hardcoded track directory literals or dead extension swapping branches exist in the compiled bundle, so that regressions are automatically blocked.
11. As an AI coding assistant implementing routing updates, I want clear domain contracts between the entity reference resolver and the window routing coordinator, so that modifications maintain repository standards.
12. As a learner bookmarking a specific subsection of a problem note (e.g., `#error-log`), I want loading that bookmarked URL to open the problem in Notes-First mode and scroll straight to the error log table, so that active recall is immediate.

---

## Implementation Decisions

### 1. Standalone Anchor Preservation in Route Resolution
- The route resolution routine will inspect hash inputs for leading anchor fragments before string normalization.
- Standalone anchors (e.g., `#complexity` or `#the-error-log`) will be classified directly as anchor-only targets rather than unindexed file paths.
- When an anchor-only reference is detected, the resolver will retain the currently selected document entity key (or fallback to the default document if none is active) and pass the anchor slug to the DOM scroll scheduler.

### 2. Reactive In-Session Hash Routing
- The client application runtime will register a `hashchange` event listener on the global browser window during initialization.
- When triggered, the event handler will route the updated hash through the centralized route resolver.
- If the resolved route targets a different document entity or view mode, the application will invoke the standard view switching pipeline without reloading the document.
- If the resolved route targets an anchor within the already active document, the router will trigger smooth scrolling directly without re-rendering the note container.

### 3. Non-Destructive Fallback for Invalid Hash Routes
- When a provided URL hash cannot be resolved to a valid document entity key or recognized command mode, route resolution will avoid overwriting the user's active or persisted display mode.
- If the application is currently in Roadmap mode and receives an unrecognized hash, it will remain in Roadmap mode rather than forcibly switching to Workspace mode.
- Fallback route objects will be consolidated into a single reusable structure, eliminating duplicated literal objects across disparate branches.

### 4. Complete Elimination of Dead Reverse Extension Swapping
- All remaining conditional branches checking for `.replace(/\.py$/, ".md")` against the entity collection will be excised from all stages of the entity reference resolver, including direct path resolution and stem lookup.
- The entity reference resolver will enforce strict unidirectional normalization: companion markdown links (`.md`) convert to canonical problem source entities (`.py`), while static markdown documents preserve their native `.md` keys.

### 5. Architectural DRYing of Test Assertions
- The test harness assertions checking for forbidden string literals in compiled routing and resolver routines will be parameterized across inspected functions and pattern lists, eliminating repetitive assertion statements.
- Test suites will incorporate explicit high-seam assertions for static documentation keys and standalone anchor navigation.

---

## Testing Decisions

### What Makes a Good Test
- Tests must assert external observable behavior at the highest possible architectural seam rather than verifying internal helper variables or private implementation mechanics.
- Tests must evaluate the exact compiled script artifact generated by the compiler to prevent divergence between source templates, build outputs, and test expectations.
- Tests must execute extracted production routines within a headless Node.js environment against representative fixtures, covering positive resolution, boundary anchors, and invalid inputs.

### Modules Tested
- **Client Application Runtime**: Evaluated via headless Node.js execution on the compiled single-page application artifact, verifying standalone anchor handling, static document resolution, and route fallback integrity.
- **StudyStationCompiler**: Integration tests in the compiler test suite verifying that compiled output contains clean, dead-code-free runtime functions and valid event listeners.

### Prior Art
- High-seam integration tests in `tests/test_update_index.py` that extract compiled script blocks (`resolveEntityReference`, `resolveInitialRoute`) and execute them via Node.js subprocesses.

---

## Out of Scope

- Modifying original Python problem solutions (`problems/**/*.py`), which remain strictly immutable per Core Rule 1.
- Modifying the centralized track registry schema or Python dataclasses in the compiler backend.
- Altering the visual design, theme colors, or CSS layout of the single-page application.
- Introducing third-party client-side routing libraries or Node.js runtime dependencies into the production bundle.

---

## Further Notes

- This specification directly addresses all findings from the post-Spec 17 two-axis code review.
- Aligns with `CONTEXT.md` Architectural Seam 7 (*Zero-Download In-App Navigation & Notes-First Routing*) and Seam 1 (*Depth over Shallowness*).
- All changes remain 100% backward-compatible with existing URLs, external bookmarks, and internal documentation links.
