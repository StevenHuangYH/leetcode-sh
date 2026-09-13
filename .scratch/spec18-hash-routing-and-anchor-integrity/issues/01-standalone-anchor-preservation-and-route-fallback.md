# 01: Standalone Anchor Preservation and Route Fallback Consolidation

**What to build:**
In `templates/src/scripts/app.js`:
- In `resolveInitialRoute(rawHash)`:
  - Do NOT strip the leading `#` before querying `resolveEntityReference`. Standalone anchors (e.g. `#complexity`, `#the-error-log`) require the `#` prefix so that `resolveEntityReference` triggers `isAnchorOnly` logic, keeping `currentKey` (or defaulting to `"README.md"`) and extracting the anchor slug.
  - Consolidate the fallback route object into a single default constant: `DEFAULT_ROUTE = { mode: "workspace", key: "README.md", anchor: "" }`.
  - Ensure non-destructive fallback: If the raw hash is empty or fails to resolve to a valid entity and is not a special mode (like `roadmap`), do not overwrite an active or persisted mode (e.g. if the user is currently exploring roadmap).
- Mirror changes cleanly into `templates/src/scripts/app.js`.

**Blocked by:** None (Frontier)

**Status:** done

- [x] Preserve leading `#` when passing hash to `resolveEntityReference` for anchor-only detection
- [x] Consolidate duplicated `{ mode: "workspace", key: "README.md", anchor: "" }` into a shared constant
- [x] Implement non-destructive route fallback
- [x] Ensure `resolveInitialRoute` returns `{ mode, key, anchor }` deterministically
