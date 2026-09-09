# 05: High-Seam Compiler Tests and E2E Build

**What to build:**
- In `tests/test_update_index.py`:
  - Add test asserting compiled `index.html` contains zero hardcoded track fallback lists (`"problems/top-100"` inside fallback branches).
  - Add test asserting that client-side category folder predicates correctly match canonical paths and legacy prefixes.
- Rebuild `index.html` via `python3 update_index.py`.
- Run all test suites across the repository (`test_update_index.py`, `test_tracking_integrity.py`, `test_graph_builder.py`, `test_note_structure.py`).

**Blocked by:** 02: Eliminate Client Speculative Fallbacks, 03: Complete Validator and Tracking Integrity Registry Adoption, 04: Harden Documentation Synchronizer

**Status:** todo

- [ ] Add high-seam tests in `tests/test_update_index.py`
- [ ] Run `python3 update_index.py` to regenerate `index.html`
- [ ] Run full test suite
- [ ] Verify index.html contains updated client scripts
