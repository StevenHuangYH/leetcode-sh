# Spec 19: Browser History Push-State Navigation and Generic Anchor Resolution Hardening

**Triage Label**: `ready-for-agent`

---

## Problem Statement

When learners and maintainers navigate the `leetcode-sh` Study Station via deep links, browser navigation controls, and markdown cross-references, several routing inconsistencies and architectural design smells persist:

1. **In-Session History Traversal Blocked by Unconditional `replaceState`**:
   Although reactive `hashchange` listener support exists, the client application unconditionally executes `history.replaceState` whenever an item is switched or an anchor link is clicked. Consequently, user-driven navigation never pushes new entries onto the browser's history stack, preventing learners from using browser Back and Forward buttons to trace their problem study history.

2. **Bypassed Entity Resolver Seam & Premature Hash Stripping**:
   `resolveInitialRoute` strips the leading hash character (`replace(/^#/, "")`) before forwarding the target to `resolveEntityReference`. Because `resolveEntityReference` relies on the leading `#` prefix (`normalized.startsWith("#")`) to classify anchor-only references targeting the active document, this premature stripping bypasses the resolver's internal classification logic.

3. **Brittle Hardcoded Anchor Allowlist**:
   To compensate for the bypassed resolver seam, a static 17-item `Set` (`STANDALONE_SECTION_ANCHORS`) was introduced. Any valid markdown section anchor outside this hardcoded list (e.g. custom note sections or novel headers) fails route resolution, discarding the deep link target and falling back to `README.md`.

4. **Duplicated Node Binary Resolution in Compiler Tests**:
   The compiler integration test suite duplicates identical Node.js executable discovery and fallback routines across multiple test methods rather than encapsulating discovery behind a single reusable helper.

---

## Solution

1. **Enable Browser History Stack Navigation (`history.pushState`)**:
   Enhance `updateUrlHash` and navigation dispatchers to distinguish between user-initiated navigation (clicking problem links or anchor headings, which must push a new history entry via `history.pushState`) and programmatic/cold-boot URL synchronization (which should replace the current state via `history.replaceState`). Ensure `hashchange` handling navigates smoothly without creating duplicate history entries.

2. **Unify Route Resolution and Respect Resolver Seam**:
   Pass unstripped hash strings directly to `resolveEntityReference`, allowing the entity reference resolver's native `isAnchorOnly` logic to classify standalone fragment references (`#...`) without premature delimiter manipulation or redundant string splitting in `resolveInitialRoute`.

3. **Generic Syntax-Based Anchor Resolution**:
   Completely remove the hardcoded `STANDALONE_SECTION_ANCHORS` allowlist. Anchor-only targets are classified structurally by syntax: any reference beginning with `#` (or resolving to an empty base key with an anchor fragment) targets the currently active document (or fallback default) and forwards the anchor slug to the DOM scroll dispatcher.

4. **Consolidate Test Environment Discovery**:
   Extract Node executable discovery in `tests/test_update_index.py` into a unified `_get_node_binary()` helper method supporting environment variable override (`NODE_BIN`), standard `PATH` discovery, and fallback runtimes. Expand high-seam tests to assert generic anchor navigation and history push state behavior.

---

## User Stories

1. As a learner navigating between multiple problems, I want each problem switch to push a new entry onto my browser history stack, so that clicking the browser Back button returns me to the previous problem.
2. As a learner reviewing a problem and clicking an in-page section link (e.g. `#the-error-log`), I want the section navigation recorded in browser history, so that I can click Back to return to my earlier reading position.
3. As a student navigating browser history using Back/Forward buttons, I want the Study Station view to reactively synchronize without creating redundant duplicate history entries.
4. As a learner bookmarking an arbitrary heading in a companion note, I want any syntax-valid anchor target to resolve to the active problem without requiring registration in a hardcoded allowlist.
5. As a maintainer creating new companion notes with specialized custom headings, I want deep links to those headings to resolve cleanly without modifying a static whitelist in client code.
6. As a developer inspecting client routing, I want `resolveInitialRoute` to delegate reference parsing entirely to `resolveEntityReference`, so that delimiter splitting logic is defined in exactly one place.
7. As a code reviewer, I want the client runtime free of primitive-obsession string sets for document headings, keeping the codebase clean and maintainable.
8. As a test engineer running compiler integration tests, I want a single centralized Node.js discovery utility that respects the `NODE_BIN` environment variable, so that tests run reliably across diverse CI and developer environments.
9. As a QA contributor, I want high-seam integration tests executed against the compiled `index.html` artifact asserting that generic custom anchors resolve and scroll accurately.
10. As a learner opening the application with an unrecognized route, I want the application to gracefully preserve my current or persisted layout mode without throwing runtime errors.

---

## Implementation Decisions

### 1. Dual-Mode History Synchronization (`push` vs `replace`)
- Update `updateUrlHash(hashKey, { replace = false } = {})` in the client application runtime.
- Problem switches from user clicks (sidebar navigation, search results, internal markdown links) call `updateUrlHash` with `replace: false` (pushing history).
- Cold-boot initial route resolution, invalid route fallback, and reactive `hashchange` updates call `updateUrlHash` with `replace: true` (or avoid pushing redundant states).

### 2. Generic Syntax Anchor Classification
- Pass the raw hash string directly from `resolveInitialRoute` into `resolveEntityReference`.
- In `resolveEntityReference`, retain the invariant that any reference beginning with `#` is classified as `isAnchorOnly: true`, binding to the active document key and extracting the trailing slug as `anchor`.
- Delete `STANDALONE_SECTION_ANCHORS` completely from `app.js`.

### 3. Elimination of Delimiter Duplication
- Remove manual `#` splitting in `resolveInitialRoute`. Directly consume `{ key, item, anchor, isAnchorOnly }` returned by `resolveEntityReference`.

### 4. Consolidated Test Discovery Helper
- Implement `_get_node_binary(self)` in `tests/test_update_index.py`.
- Check `os.environ.get("NODE_BIN")`, then `shutil.which("node")` / `shutil.which("nodejs")`, then user environment runtimes (`.local/share/fnm/...`).

---

## Testing Decisions

### What Makes a Good Test
- Tests must assert external observable behavior at the highest possible architectural seam (the compiled `index.html` Single Page Application).
- Tests must execute extracted client routing and navigation routines in a headless Node.js runtime against representative datasets.
- Tests must verify generic syntax anchor resolution for arbitrary heading slugs without hardcoded string checks.

### Modules Tested
- **Client Application Runtime (`templates/src/scripts/app.js` compiled into `index.html`)**: Tested via headless Node.js execution for route resolution, generic anchor recognition, and history management parameters.
- **Compiler Test Harness (`tests/test_update_index.py`)**: Unit and integration tests covering node discovery and compiler integrity.

### Prior Art
- Existing high-seam test suite in `tests/test_update_index.py` extracting production functions and executing them via Node.js subprocesses.

---

## Out of Scope

- Modifying original Python problem files (`problems/**/*.py`), which remain strictly immutable per Core Rule 1.
- Changing the centralized track registry schema or backend compiler models.
- Altering visual design, themes, or CSS classes.
- Introducing external client routing dependencies.

---

## Further Notes

- Directly resolves all findings from the post-Spec 18 two-axis code review.
- Fully backwards-compatible with all existing bookmarks, links, and tests.
