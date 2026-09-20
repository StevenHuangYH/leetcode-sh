# Spec 15: Canonical Track Registry Centralization and Fixture Normalization

**Triage Label**: `ready-for-agent`

---

## Problem Statement

Following the consolidation of problem tracks under the unified `problems/` parent directory, two architectural weaknesses and maintenance liabilities remain in the codebase:

1. **Primitive Obsession and Duplicated Track Definitions**:
   - Track directory paths (`problems/top-100`, `problems/daily-practice`, `problems/luffy`), track display names, and client-side category filters are duplicated as loose string literals across compiler scripts, build watch routines, document audit tools, and client-side JavaScript routers.
   - When a track is modified or a new track is introduced, changes must be scattered across multiple compiler files and client template scripts (shotgun surgery risk).

2. **Legacy Track Paths in Test Fixtures**:
   - Unit test suites (specifically graph builder tests) continue to construct mock problem entities using deprecated un-prefixed path keys (e.g. `top-100/...`), creating a divergence between production entity keys and test fixtures.

---

## Solution

1. **Establish a Single Source of Truth for Track Configurations**:
   - Define a centralized Track Registry in the compiler architecture that encapsulates track identifiers, directory paths, human-readable labels, and sidebar ordering.
   - Ensure all backend scripts (document collection, markdown linting, file watching, and documentation synchronization) consume this centralized registry.

2. **Dynamic Client Template Track Injection**:
   - Inject the compiled track metadata directly into the client application bundle during compilation, allowing client-side navigation, category tabs, and entity resolvers to derive track filters dynamically rather than relying on duplicated hardcoded string lists.

3. **Normalize All Test Fixtures to Canonical Path Keys**:
   - Update all mock entities across unit test suites to use the canonical `problems/` hierarchy, ensuring test fixtures 100% reflect runtime compiler behavior.

---

## User Stories

1. As a developer maintaining the study station compiler, I want a single centralized track configuration module, so that I can add or adjust tracks in one place without touching multiple scripts.
2. As a frontend user browsing the web application, I want track tabs and category filters to be driven dynamically by compiler-bundled metadata, so that the UI always mirrors the exact track configuration of the repository.
3. As a student navigating problem notes, I want the client-side router and entity reference resolver to resolve track paths deterministically, so that cross-note links never break regardless of navigation path.
4. As a test engineer running test suites, I want all mock document entities in tests to use canonical `problems/` path keys, so that tests accurately reflect production entity structures.
5. As an author running watch mode during note writing, I want the watch listener to derive its monitored directory list from the centralized track registry, so that new files in any configured track automatically trigger recompilation.
6. As a CI pipeline operator running pre-commit linters, I want the markdown audit tool to iterate through tracks defined by the registry, ensuring no tracks are omitted from lint checks.
7. As a code reviewer inspecting new pull requests, I want track string literals eliminated in favor of registry lookups, so that code smell baselines remain clean and maintainable.
8. As a documentation sync maintainer, I want the README generator to source track directory locations directly from the registry, so that generated tracking tables always point to valid relative paths.
9. As a developer extending the SPA viewer, I want the client JavaScript to receive structured track descriptors at build time, so that adding new problem categories requires zero manual client code duplication.
10. As an AI assistant generating new solutions, I want explicit contracts and schemas for track keys, so that generated files adhere to the canonical track taxonomy without ambiguity.

---

## Implementation Decisions

### 1. Centralized Track Registry in Compiler Architecture
- Introduce a dedicated Track Registry in the compiler domain model.
- Each track configuration encapsulates:
  - `id`: A normalized slug identifier (e.g. `top-100`, `daily-practice`, `luffy`).
  - `dir_path`: The relative directory path from repository root (e.g. `problems/top-100`).
  - `display_label`: The primary display name for sidebar navigation and breadcrumbs.
  - `category_name`: The canonical track category name for entity grouping.
- The Problem Collector, Note Validator, Watch Listener, and Readme Synchronizer will import and consume this registry directly.

### 2. Client-Side Track Metadata Injection
- Update the Study Station Compiler bundling pipeline to serialize track configuration metadata into JSON.
- Inject the serialized track descriptor into the template bundle during HTML compilation.
- Refactor client-side sidebar category definitions and entity resolution fallbacks to consume injected track definitions dynamically, while preserving backward compatibility for legacy URLs.

### 3. Test Fixture Path Normalization
- Refactor all test suites that instantiate mock problem entities to use canonical `problems/` directory paths for entity keys and file references.
- Verify that graph builder assertions, keyword matchers, and category filters operate seamlessly against normalized fixtures.

---

## Testing Decisions

### Good Test Principles
- Tests must verify external behavior and system invariants rather than internal implementation minutiae.
- Tests must assert that the compiler discovers and pairs all problem files across all registered tracks.
- Tests must verify that the compiled application bundle contains valid track metadata and that document entity keys conform to the canonical hierarchy.

### Target Test Suites
- **Track Registry & Collector Tests**: Assert that the collector correctly discovers documents across all registered tracks and that registry definitions are well-formed.
- **Compiler Bundling & Template Tests**: Assert that compiled HTML output includes the injected track metadata and that client-side category filters function as expected.
- **Graph Builder & Normalization Tests**: Assert that all mock document fixtures with canonical `problems/` keys pass topological keyword matching and node aggregation.
- **Lint & Validation Integrity Tests**: Assert that all repository notes across configured tracks pass strict 7-section and topology macro anchor validation.

### Prior Art
- Existing test suites under `tests/test_update_index.py`, `tests/test_graph_builder.py`, `tests/test_tracking_integrity.py`, and `tests/test_note_structure.py`.

---

## Out of Scope

- Introducing new problem tracks or restructuring existing track contents.
- Altering the 38-Node Compound Algorithmic Topology Graph taxonomy or edge definitions.
- Modifying original Python solution code (`.py` files remain strictly immutable).
- Redesigning visual themes, color schemes, or layout orientations of the web viewer.

---

## Further Notes

- This specification completes the architectural consolidation initiated by the unified `problems/` parent directory migration.
- All implementations must continue to honor the Mandatory 4-Step Push & Walkthrough Protocol and strict pre-commit quality gates mandated by `AGENTS.md`.
