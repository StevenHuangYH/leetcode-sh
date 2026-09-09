# 03: High-Seam Compiler Tests & Production Script Evaluation

**What to build:**
In `tests/test_update_index.py`:
- Remove duplicated synthetic `resolveInitialHash` function string from `test_client_track_fallback_elimination_and_folder_structure`.
- Extract the actual production routing and resolution functions from the compiled HTML output using regex.
- Execute the real extracted functions in the Node.js test harness:
  - Assert that legacy paths with standard prefixes (`top-100/lc-0001-two-sum.md`) map dynamically to configured canonical paths (`problems/top-100/lc-0001-two-sum.py`).
  - Assert that custom directory tracks (e.g. `{ id: "custom", dir_path: "external/custom" }`) dynamically map `${id}/` to `${dir_path}/` without prepending `'problems/'`.
  - Assert that compiled HTML contains zero `'problems/' + cleanPath` or `'problems/' + hashKey` string literals.
  - Assert that startup hash routing delegates to `resolveEntityReference`.

**Blocked by:** 02-centralize-startup-hash-routing.md

**Status:** done

- [x] Remove synthetic `resolveInitialHash` function from test string
- [x] Extract real compiled production routing/resolver routines from HTML
- [x] Add assertions verifying dynamic directory path substitution for standard and non-standard tracks
- [x] Assert zero `'problems/' + cleanPath` or `'problems/' + hashKey` literals in compiled HTML
