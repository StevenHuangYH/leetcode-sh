# 02: Reactive In-Session Hash Navigation

**What to build:**
In `templates/src/scripts/app.js`:
- Register a `hashchange` event listener on `window` during application boot.
- When `hashchange` fires:
  - Call `resolveInitialRoute(window.location.hash)` to compute `{ mode, key, anchor }`.
  - If `mode` differs from `mainMode`, update `setMainMode(mode, false)`.
  - If `mode === "workspace"`:
    - If `key !== currentKey`, switch item via `switchItem(key)`.
    - If `anchor` is non-empty:
      - Scroll the note container to the target heading using `findHeadingElement` (with appropriate rendering delay if the item changed, or immediately if staying on the same item).
- Ensure no infinite loops between internal URL updates and hashchange listener.

**Blocked by:** 01-standalone-anchor-preservation-and-route-fallback.md

**Status:** todo

- [ ] Add `window.addEventListener("hashchange", ...)` handler
- [ ] Route hash updates via `resolveInitialRoute`
- [ ] Handle seamless mode switching and item switching on hash navigation
- [ ] Handle smooth scrolling to target anchors when hash changes in-session
