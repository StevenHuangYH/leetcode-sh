# 02: SPA Dual View and Fallback

**What to build:** Fix the SPA viewer initialization so that both code and notes appear side-by-side by default in dual view mode, and implement smart fallback so that problems without companion notes automatically maximize their code viewer rather than presenting a blank screen.

**Blocked by:** 01: Preview and Generator Test Harness

**Status:** done

- [x] Change default `viewMode` in the client script to `"dual"`
- [x] Implement adaptive fallback in `switchItem` to expand the code viewer when markdown notes are empty
- [x] Ensure navigation from roadmap cards immediately focuses and opens the workspace view
