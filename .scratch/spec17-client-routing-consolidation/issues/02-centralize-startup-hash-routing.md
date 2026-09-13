# 02: Centralize Startup Hash Routing to EntityReferenceResolver

**What to build:**
In `templates/src/scripts/app.js`:
- Extract a clean route helper function `resolveInitialRoute(rawHash)` (or consolidate within startup initialization) that delegates entity resolution directly to `resolveEntityReference(hashKey)`.
- If `hashKey === "roadmap"`, set `mainMode = "roadmap"`.
- For all entity paths, query `resolveEntityReference(hashKey)`.
  - If a valid entity key is returned and exists in `items`, set `currentKey = resolved.key`, set `mainMode = "workspace"`, and preserve `resolved.anchor` if present.
  - Fallback cleanly to default (`README.md`) if unresolved.
- Remove duplicate legacy prefix loop and duplicate `.md` $\leftrightarrow$ `.py` extension swapping logic in the startup routing block.
- Ensure the extracted routing helper is accessible for high-seam automated testing.

**Blocked by:** 01-dynamic-track-directory-mapping.md

**Status:** todo

- [x] Consolidate startup hash routing to delegate to `resolveEntityReference`
- [x] Remove duplicate legacy prefix iteration and hardcoded `'problems/'` literal in startup block
- [x] Remove duplicate extension swapping logic
- [x] Ensure `mainMode` and `currentKey` are correctly assigned
