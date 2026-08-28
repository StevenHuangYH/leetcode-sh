# 05: Generator Deduplication and E2E Build

**What to build:** Refactor `update_index.py` to ingest topic hierarchies and problem groupings dynamically from markdown documentation without duplicate hardcoded data dictionaries, rebuild `index.html`, and execute the full test suite for end-to-end verification.

**Blocked by:** 02: README Catalog Sync and Metrics Alignment, 04: Luffy Notes Upgrade Part 2 (Topics 21-42)

**Status:** ready-for-agent

- [ ] Remove hardcoded duplicate roadmap and topic dictionaries from `update_index.py`
- [ ] Bundle loose document item arguments into structured data objects
- [ ] Rebuild `index.html` via `python3 update_index.py` with zero errors
- [ ] Run full automated test suite (`unittest discover tests`) ensuring 100% pass rate
- [ ] Verify clean UI rendering across all tracks in `index.html`
