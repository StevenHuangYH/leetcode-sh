# 04: Harden Documentation Synchronizer

**What to build:**
In `scripts/sync_readme.py`:
- Remove inline string literal fallback (`"problems/top-100"`) when looking up `"top-100"`.
- Query `TrackRegistry.get_track_by_id("top-100")` and raise an explicit `RuntimeError` if missing rather than silently falling back to a raw string.

**Blocked by:** 01: Streamline TrackConfig and TrackRegistry Schema

**Status:** todo

- [ ] Remove raw string fallback in `generate_top_100_table` in `scripts/sync_readme.py`
- [ ] Verify README generation via `python3 scripts/sync_readme.py` or unit tests
