# 02: Eliminate Client Speculative Fallbacks and Redundant Logic

**What to build:**
In `templates/src/scripts/app.js`:
- Remove dead hardcoded fallback arrays for tracks in `treeStructure` and `resolveEntityReference`.
- Directly map `dynamicTrackFolders` from `configuredTracks`.
- Derive legacy prefix dynamically (`${t.id}/`) without relying on `t.legacy_prefix`.
- Clean up redundant predicate checks in folder filters.

**Blocked by:** 01: Streamline TrackConfig and TrackRegistry Schema

**Status:** todo

- [ ] Remove hardcoded fallback arrays in `treeStructure`
- [ ] Remove hardcoded fallback arrays in `resolveEntityReference`
- [ ] Derive legacy prefix dynamically from `${t.id}/`
- [ ] Verify client script syntax
