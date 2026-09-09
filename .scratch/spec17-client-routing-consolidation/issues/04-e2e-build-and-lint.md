# 04: End-to-End Build Verification & Workspace Integrity

**What to build:**
- Recompile `index.html` via `python3 update_index.py`.
- Run pre-commit note audit via `python3 update_index.py --lint` to ensure all 96 companion notes adhere to the 7-section format.
- Run complete test suite via `python3 -m unittest discover tests` and verify all tests pass.
- Verify `git status` clean and index updated.

**Blocked by:** 03-high-seam-compiler-tests.md

**Status:** done

- [x] Rebuild `index.html` via `python3 update_index.py`
- [x] Run `python3 update_index.py --lint` (pass all notes)
- [x] Run `python3 -m unittest discover tests` (all pass)
- [x] Verify clean build artifact
