# 02: README Catalog Sync and Metrics Alignment

**What to build:** Synchronize the primary tracking tables in `README.md` to include all missing problem entries from `top-100/` and `daily-practice/`, align all header badges and summary metric tables with exact disk counts, and ensure zero untracked problems remain.

**Blocked by:** 01: Audit and Tracking Harness

**Status:** done

- [x] Populate all missing problem rows into `README.md` Section 3 (Top 100 Liked Track) and Section 4 (Daily Practice Track)
- [x] Align the top `Problems Solved` badge with exact total count
- [x] Align the Section 2 summary metric table (Easy/Medium/Hard breakdown and track totals)
- [x] Verify `tests/test_tracking_integrity.py` passes completely
