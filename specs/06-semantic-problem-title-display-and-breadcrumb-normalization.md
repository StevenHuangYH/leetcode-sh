# Spec 06: Semantic Problem Title Display and Breadcrumb Normalization

## Problem Statement

Users navigating problems in the LeetCode Study Station frequently encounter raw filesystem artifacts (e.g. `lc-0153-find-minimum-in-rotated-sorted-array.py`, `01-lc-2235-add-two-integers`, `topic-01-arrays-sliding-window`) in prominent UI surfaces such as the top breadcrumb bar and navigation components. Displaying disk filenames instead of cleanly formatted, bilingual problem titles creates cognitive friction, obscures problem identities, and distracts learners from algorithmic problem solving.

Furthermore, batch curriculum problems with numeric prefixes (such as `luffy/01-lc-2235-add-two-integers.py` or `10-oop-pre-main-practice.py`) fail to strip file-ordering prefixes during metadata aggregation, resulting in mangled titles like `01 Lc 2235 Add Two Integers` rather than standard LeetCode identifiers (`LC 2235 · Add Two Integers`).

## Solution

1. **ProblemTitleFormatter Domain Engine**: Implement a dedicated `ProblemTitleFormatter` class returning structured `FormattedTitle` dataclasses in the compiler pipeline. It symmetrically strips disk ordering prefixes (such as `^\d{2}-lc-\d{4}-`, `^lc-\d{4}-`, `^\d{2}-`), preserves Roman numerals (`II`, `IX`) and computer science acronyms (`OOP`, `BST`, `DFS`, `BFS`, `DP`, `LRU`), and formats standard bilingual titles (`LC {num} · {English Title} ({Chinese Title})`).
2. **Semantic Breadcrumb Hierarchy**: Upgrade the top navigation breadcrumb across workspace and topology roadmap modes to render clean, human-readable folder categories (`Daily Practice`, `Top 100 Liked`, `Luffy Curriculum`, `Curriculum`, `Overview`) and problem titles with native HTML `title` tooltip attributes.
3. **Graceful Overflow & Responsive Protection**: Enforce CSS ellipsis truncation (`max-width: 100%; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;`) on the breadcrumb container to maintain a rigid, compact toolbar height (46px) across all desktop and mobile viewports.
4. **Fallback & Tutorial Title Synthesis**: Ensure non-LC scripts (e.g. `10-oop-pre-main-practice.py`) and edge-case problems without notes synthesize clean, title-cased fallback names (e.g. `OOP Pre Main Practice`).
5. **Deep Module Export Architecture**: Expose `ProblemTitleFormatter` and `FormattedTitle` as part of the compiler's top-level public interface in `scripts/compiler/__init__.py`.

## User Stories

1. As a learner viewing a problem note, I want the top breadcrumb to display the clean bilingual title (e.g. `Daily Practice / LC 153 · Find Minimum in Rotated Sorted Array (寻找旋转排序数组中的最小值)`), so that I immediately understand the problem context without deciphering a disk filename.
2. As a user studying curriculum problems in the `luffy/` track, I want batch numbers like `01-lc-2235-` cleaned into standard `LC 2235 · Add Two Integers`, so that the curriculum track looks unified with standard problem tracks.
3. As a user inspecting non-LC tutorial scripts (such as OOP practices or prefix sum examples), I want the title to be neatly formatted (e.g. `OOP Pre Main Practice`), so that non-LC exercises are readable and professional.
4. As a student studying problems with Roman numerals (e.g. `LC 59 Spiral Matrix II Alt` or `LC 167 Two Sum II`), I want Roman numerals and acronyms capitalized accurately rather than formatted in generic title case (`Ii` or `Oop`).
5. As a user on a laptop or split screen with limited horizontal space, I want long bilingual titles in the breadcrumb to truncate cleanly with an ellipsis rather than wrapping and breaking the top toolbar height.
6. As a learner using a desktop browser, I want to hover over any breadcrumb (in both problem workspace and topology roadmap views) to view the full English and Chinese title in a native tooltip.
7. As a student browsing curriculum index topics, I want the breadcrumb to show `Curriculum / 1. Arrays, Strings & Sliding Window` rather than `Problem Index / topic-01-arrays-sliding-window`.
8. As a learner opening the project overview, I want the breadcrumb to read `Overview / LeetCode Self-Practices Overview` rather than `Overview / README.md`.
9. As an AI assistant or human developer, I want `ProblemTitleFormatter` and `FormattedTitle` to be exported directly from `scripts.compiler`, maintaining high architectural depth without reaching into internal submodule files.
10. As a continuous integration system, I want automated unit and generator tests in `tests/test_update_index.py` and `tests/test_preview_and_generator.py` to verify title extraction contracts and compiled HTML breadcrumb rendering.
11. As a contributor, I want original `.py` filenames on disk to remain strictly immutable while the UI displays clean semantic titles.

## Implementation Decisions

### 1. Title Parsing & Normalization Engine (`ProblemTitleFormatter`)
* Define `@dataclass class FormattedTitle` in `scripts/compiler/entities.py`:
  * Fields: `lc_num: str`, `en_title: str`, `cn_title: str`, `full_title: str`.
  * Implements `__iter__` to allow convenient 4-tuple unpacking.
* Define `class ProblemTitleFormatter`:
  * `KNOWN_ACRONYMS = frozenset({"oop", "bst", "dfs", "bfs", "dp", "lca", "lru", "lfu"})`
  * `ROMAN_NUMERALS = frozenset({"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"})`
  * Prefix extraction rules:
    * Symmetric prefix match: `match_lc = re.search(r'^(?:\d{2}-)?(?:lc-)?(\d{4})(?:-|$)', stem)`
    * Stripped raw slug: `raw_slug = re.sub(r'^(?:\d{2}-)?(?:lc-)?\d{4}-?', '', stem)`
    * Range match fallback: `match_range = re.search(r'^(\d{2}-\d{2})-(.+)$', stem)`
    * Non-LC numeric strip: `raw_slug = re.sub(r'^\d{2}-', '', stem)`
  * Extract Chinese title from Markdown H1 header (`# LC ... | {Chinese Title}`).
  * Full title assembly:
    * `LC {num} · {English Title} ({Chinese Title})` if both exist.
    * `LC {num} · {English Title}` if only English exists.
    * `LC {num} · {Chinese Title}` if only Chinese exists.
    * `{lc_num} · {clean_fallback}` if neither exists and `lc_num` is present.
    * `{clean_fallback}` for non-LC scripts.

### 2. Seam Export & Duplication Removal
* Export `ProblemTitleFormatter` and `FormattedTitle` in `scripts/compiler/__init__.py`.
* Remove duplicate `read_file` function definitions in `scripts/compiler/entities.py`.

### 3. Breadcrumb Styling & Category Cleaning
* Breadcrumb container styles:
  * `.breadcrumb`: `display: flex; align-items: center; gap: 8px; font-size: 13.5px; color: var(--text-main); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0; max-width: 100%;`
  * `.breadcrumb-folder`, `.breadcrumb-sep`, `.diff-badge`: `flex-shrink: 0;`
  * `.breadcrumb-file`: `font-weight: 600; color: var(--text-bright); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; min-width: 0;`
* Category label normalization in JavaScript:
  * Strip trailing `" Track"` (e.g. `"Daily Practice Track"` $\rightarrow$ `"Daily Practice"`).
  * Strip trailing curriculum batch ranges (e.g. `"Luffy Curriculum (01-42)"` $\rightarrow$ `"Luffy Curriculum"`).
  * Ensure topology roadmap breadcrumb includes `title="Interactive Topology Graph"`.

## Testing Decisions

### Good Test Principles
* Test domain formatter contracts and output artifact HTML representations rather than private variables.
* Test diverse filename patterns across all tracks (`top-100/`, `daily-practice/`, `luffy/`, `problem-index/`).

### Modules Tested
* `scripts.compiler.ProblemTitleFormatter` & `FormattedTitle` (`tests/test_update_index.py`)
* `StudyStationCompiler` compiled HTML breadcrumb contracts (`tests/test_preview_and_generator.py`)
* Curriculum topic parser (`scripts/compiler/parser.py`)

### Prior Art
* Existing test suites in `tests/test_update_index.py` and `tests/test_preview_and_generator.py`.

## Out of Scope

* Renaming `.py` or `.md` source files on the local filesystem (strictly immutable per Core Rule 1).
* Changing problem difficulty rating schemas or tags.
* Modifying algorithm topology graph node connectivity.

## Further Notes

* Codified in `CONTEXT.md` under `ProblemTitleFormatter` and Principle 6 (*Semantic Breadcrumb & Bilingual Title Normalization*).
