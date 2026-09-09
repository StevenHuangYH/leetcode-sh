# 02: Eliminate Client Speculative Fallbacks and Redundant Logic

**What to build:**
In `templates/src/scripts/app.js`:
- Remove dead hardcoded fallback arrays for tracks in `treeStructure` and `resolveEntityReference`.
- Directly map `dynamicTrackFolders` from `configuredTracks`.
- Derive legacy prefix dynamically (`${t.id}/`) without relying on `t.legacy_prefix`.
- Clean up redundant predicate checks in folder filters.

**Blocked by:** 01: Streamline TrackConfig and TrackRegistry Schema

**Status:** done

- [x] Remove hardcoded fallback arrays in `treeStructure`
- [x] Remove hardcoded fallback arrays in `resolveEntityReference`
- [x] Derive legacy prefix dynamically from `${t.id}/`
- [x] Verify client script syntax
