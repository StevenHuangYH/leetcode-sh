# 03: Eliminate Residual Dead Extension Swapping

**What to build:**
In `templates/src/scripts/app.js`:
- In `resolveEntityReference(rawHref)`:
  - Remove step 2 check:
    ```javascript
    if (cleanPath.endsWith(".py")) {
      const mdKey = cleanPath.replace(/\.py$/, ".md");
      if (items[mdKey]) return { key: mdKey, anchor };
    }
    ```
    Problem entities are indexed strictly by `.py` paths in `items`, making `.md` entity queries unreachable dead code.
  - In step 4 (stem matching):
    Remove check attempting to swap candidate `.py` path to `.md`:
    ```javascript
    if (cleanPath.endsWith(".py")) {
      const mdKey = candidateKey.replace(/\.py$/, ".md");
      if (items[mdKey]) return { key: mdKey, anchor };
    }
    ```
  - Preserve unidirectional `.md` $\rightarrow$ `.py` conversion for companion note cross-references.

**Blocked by:** None (Frontier)

**Status:** done

- [x] Remove dead `.py` -> `.md` lookup branch in step 2 of `resolveEntityReference`
- [x] Remove dead `.py` -> `.md` lookup branch in stem matching (step 4)
- [x] Verify unidirectional `.md` -> `.py` conversion remains intact
- [x] Verify static `.md` documentation retains exact key matching
