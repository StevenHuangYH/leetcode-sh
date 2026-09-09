# 01: Dynamic Track Directory Mapping in EntityReferenceResolver

**What to build:**
In `templates/src/scripts/app.js` (`resolveEntityReference`):
- Eliminate hardcoded `'problems/'` string literals in step 3 (direct legacy track resolution).
- Dynamically substitute the matched track identifier prefix `${t.id}/` with the configured directory path `${t.dir_path}/`:
  `const canonicalCandidate = `${t.dir_path}/${cleanPath.slice(t.id.length + 1)}`;`
- Remove the dead code branch checking `items[canonicalCandidate.replace(/\.py$/, ".md")]` since problem entities are indexed exclusively by `.py` paths.
- Ensure step 4 (stem matching) derives search directories strictly from unique `t.dir_path` entries in `configuredTracks`.

**Blocked by:** None (Frontier)

**Status:** todo

- [ ] Replace `'problems/' + cleanPath` with dynamic `${t.dir_path}/` replacement
- [ ] Remove dead `.replace(/\.py$/, ".md")` lookup branch in step 3
- [ ] Verify stem search collects unique `t.dir_path`
- [ ] Confirm basic syntax integrity
