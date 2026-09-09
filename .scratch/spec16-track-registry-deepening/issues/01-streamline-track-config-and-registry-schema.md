# 01: Streamline TrackConfig and TrackRegistry Schema

**What to build:**
In `scripts/compiler/track_definitions.py`:
- Remove the optional `legacy_prefix` attribute from `TrackConfig` and its serialization method `to_client_descriptor()`.
- Ensure `TrackConfig` strictly encapsulates `id`, `dir_path`, `display_label`, and `category_name`.
- In `tests/test_update_index.py`, update `test_track_registry_domain_model` to verify the streamlined schema.

**Blocked by:** None (Frontier)

**Status:** todo

- [ ] Remove `legacy_prefix` from `TrackConfig`
- [ ] Remove `legacy_prefix` from `TrackConfig.to_client_descriptor()`
- [ ] Update `test_track_registry_domain_model` in `tests/test_update_index.py`
- [ ] Run `python3 -m unittest tests/test_update_index.py` to confirm
