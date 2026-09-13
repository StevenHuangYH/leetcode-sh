# 05: Workspace Rebuild, Linting, and End-to-End Quality Gate

**What to build:**
- Recompile `index.html` via `python3 update_index.py`.
- Run complete test suite via `python3 -m unittest discover tests`.
- Run note validator or linter if available.
- Ensure all Core Rules in `AGENTS.md` are strictly met.
- Ensure workspace working tree is clean.

**Blocked by:** 04-high-seam-compiler-tests-expansion-and-dry.md

**Status:** done

- [x] Rebuild `index.html` via `python3 update_index.py`
- [x] Run full test suite (`python3 -m unittest discover tests`)
- [x] Verify clean git diff and Core Rules compliance
