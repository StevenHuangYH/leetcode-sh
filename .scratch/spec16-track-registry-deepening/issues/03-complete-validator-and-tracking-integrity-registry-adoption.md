# 03: Complete Validator and Tracking Integrity Registry Adoption

**What to build:**
- In `scripts/validator/note_validator.py`: provide a workspace track audit helper (`audit_workspace_tracks`) or consume `TrackRegistry.get_all_tracks()` / `TrackRegistry.get_track_paths()`.
- In `tests/test_tracking_integrity.py`: remove loose string literals (`TRACKS = ["problems/top-100", ...]`) and derive track manifests and link regexes directly from `TrackRegistry.get_all_tracks()`.

**Blocked by:** 01: Streamline TrackConfig and TrackRegistry Schema

**Status:** done

- [x] Add `audit_workspace_tracks` / registry integration in `scripts/validator/note_validator.py`
- [x] Migrate `tests/test_tracking_integrity.py` to `TrackRegistry`
- [x] Run `python3 -m unittest tests/test_tracking_integrity.py` to confirm
