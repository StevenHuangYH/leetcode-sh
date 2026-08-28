# 01: Audit and Tracking Harness

**What to build:** An automated test harness and inspection utility that scans the repository across `top-100/`, `daily-practice/`, and `luffy/` directories, detects all missing problem rows in `README.md`, and computes authoritative statistics counts to prevent tracking desynchronization.

**Blocked by:** None (can start immediately)

**Status:** done

- [x] Scan all `.py` and `.md` problem pairs across `top-100/`, `daily-practice/`, and `luffy/`
- [x] Implement an automated verification test in `tests/test_tracking_integrity.py` asserting that every problem on disk has a corresponding row in `README.md`
- [x] Assert that all markdown links in `README.md` point to existing files
- [x] Report accurate problem counts per track and overall total
