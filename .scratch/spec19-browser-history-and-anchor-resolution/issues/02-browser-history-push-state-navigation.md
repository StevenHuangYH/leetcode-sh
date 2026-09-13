# Ticket 02: Browser History Push-State Navigation & Reactive History Synchronization

**Spec**: `specs/19-browser-history-push-state-navigation-and-generic-anchor-resolution-hardening.md`
**Status**: Completed
**Blocked By**: `01-generic-syntax-anchor-resolution-and-allowlist-elimination.md`

---

## Description
Currently, `updateUrlHash` in `templates/src/scripts/app.js` unconditionally calls `history.replaceState`. As a result, when learners click problem links, sidebar items, or note headings, no new history entries are created, preventing browser Back and Forward navigation buttons from traversing visited problems and sections.

## Requirements
1. Enhance `updateUrlHash(hashKey, { replace = false } = {})`:
   - When `replace` is `false`, invoke `history.pushState({ key: hashKey }, "", "#" + hashKey)`.
   - When `replace` is `true`, invoke `history.replaceState({ key: hashKey }, "", "#" + hashKey)`.
2. Update navigation dispatchers:
   - In `switchItem(key, syncHash = true, { replaceHistory = false } = {})`:
     - When called from user-initiated interactions (sidebar click, search selection, topic catalog navigation), push state (`replaceHistory: false`).
     - Pass `replaceHistory` parameter to `updateUrlHash`.
   - In `initLinkInterceptor`:
     - Clicking internal note anchor links should call `updateUrlHash(anchor, { replace: false })` so heading jumps are pushable.
   - In `handleHashChange`:
     - Navigating via `hashchange` (triggered by browser Back/Forward) must NOT push a redundant history entry. It should use `switchItem(resolved.key, false)` and/or `updateUrlHash(..., { replace: true })`.
   - In initial cold boot:
     - Route normalization should use `replace: true` to avoid polluting the history stack on first load.
