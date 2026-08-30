# Spec 05: Notes-First Layout, Dual Split Reorientation, and Declarative View Architecture

## Problem Statement

Users studying algorithmic solutions often suffered from "spoiler bias" when opening problem entries in the LeetCode Study Station. Because the previous workspace defaulted to a dual-split view or prioritized code visibility on the left, users would immediately see the Python solution code before having the opportunity to actively recall algorithm patterns, mental models, and complexity bounds from the companion notes.

Additionally, the dual-split view placed Python source code in the left pane and companion Markdown walkthrough notes in the right pane, running counter to the reading intuition where problem documentation precedes implementation. Furthermore, the viewer runtime mutated inline DOM styles (`style.display`, `style.width`, `style.flex`) imperatively in JavaScript across desktop and mobile viewports, introducing maintenance overhead and layout drift.

## Solution

1. **Notes-First Default Viewing Mode**: When opening any problem in the Study Station workspace, the viewer defaults strictly to Notes-Only mode (`viewMode = "notes"`), rendering the companion active recall Markdown notes in full-width without displaying the solution code.
2. **Reoriented Dual-Split Layout**: When split view is activated, the Notes viewer occupies the left pane (`#left-pane`) and the Python solution code occupies the right pane (`#right-pane`) with dynamic draggable split resizing.
3. **Declarative CSS View State Management**: Eliminate imperative inline style mutations by transitioning to parent container CSS class toggles (`.mode-notes`, `.mode-code`, `.mode-dual` on desktop, `.tab-notes`, `.tab-code` on mobile), maintaining pure declarative control over pane visibility.
4. **Synchronized Architecture Rules**: Update `AGENTS.md` (Core Rule 5) and `CONTEXT.md` to codify the layout orientation and state architecture across all automated agents and human contributors.

## User Stories

1. As a learner practicing active recall, I want the Study Station workspace to default to showing only the Markdown notes, so that I can think through the algorithm pattern before viewing the Python solution.
2. As a user reviewing code alongside notes, I want the split view to display notes on the left and code on the right, so that reading flows naturally from problem explanation to code implementation.
3. As a user inspecting a problem with verified code but no companion note, I want to see an informative placeholder message in the notes pane with a single-click button to expand code view.
4. As a user resizing split panes on desktop, I want to drag the vertical splitter between notes and code and double-click to reset to a balanced 50/50 ratio.
5. As a mobile learner on a phone screen, I want the bottom navigation bar to seamlessly toggle between the full-width Problem Notes tab and Python Code tab without broken split sizing.
6. As an AI assistant or developer building features, I want view modes to be governed by declarative CSS classes rather than inline style mutations, so that UI behavior is predictable and maintainable.
7. As a continuous integration system, I want automated unit tests to verify that `index.html` strictly defaults to `viewMode = "notes"`, preventing regression to code-first or dual-split defaults.

## Implementation Decisions

### 1. View Mode & State Machine
* The application state `viewMode` initializes to `"notes"`.
* Segmented control buttons in the top toolbar reflect the active view mode (`#btnNotes` marked `active` by default).
* The workspace container `#workspace` defaults with classes `mode-notes tab-notes`.

### 2. DOM Pane Reorientation
* `#left-pane` serves exclusively as the companion documentation reading surface (`#notesViewer`) styled with the primary background color.
* `#right-pane` serves exclusively as the syntax-highlighted Python solution viewer (`#codeViewer`) styled with the IDE sidebar background color and dedicated header controls (`Copy Python`).
* `#workspace-resizer` sits between `#left-pane` and `#right-pane`.

### 3. Declarative CSS Architecture
* Desktop layout:
  * `#workspace.mode-notes`: Left pane displays full width (`flex: 1; width: 100%`); right pane and resizer are hidden (`display: none !important`).
  * `#workspace.mode-code`: Right pane displays full width (`flex: 1; width: 100%`); left pane and resizer are hidden (`display: none !important`).
  * `#workspace.mode-dual`: Both panes display side-by-side with draggable resizer enabled (`display: block`).
* Mobile layout ($\le 768\text{px}$):
  * `#workspace.tab-notes`: Left pane displays full width; right pane and resizer are hidden.
  * `#workspace.tab-code`: Right pane displays full width; left pane and resizer are hidden.
* Inline style clearing: When switching out of dual split mode, inline `width` and `flex` properties applied during dragging are reset to empty strings, allowing declarative CSS rules to take full precedence.

### 4. Compiler & Template Decoupling
* Modular sources in `templates/src/layout.html`, `templates/src/styles/base.css`, `templates/src/styles/mobile.css`, and `templates/src/scripts/app.js` are inlined by `TemplateBundler`.
* `StudyStationCompiler` compiles and outputs the production `index.html` artifact with zero external runtime dependencies.

## Testing Decisions

### Good Test Principles
* Tests verify external system behavior and output artifact contracts rather than internal variable naming.
* Verify default view mode regex contract directly against compiled `index.html`.
* Ensure curriculum topic parsing and note active-recall structures adhere to standards.

### Modules Tested
* `StudyStationCompiler` & `TemplateBundler` (`tests/test_preview_and_generator.py`)
* Curriculum Parser & Markdown Collector (`tests/test_update_index.py`)
* Note Structure Validator (`scripts/validator/note_validator.py`)

### Prior Art
* Existing test suite in `tests/test_preview_and_generator.py` asserting LaTeX formula protections, template decoupling, and compact payload constraints.

## Out of Scope

* Modifying or refactoring original LeetCode solution `.py` files (strictly immutable per Core Rule 1).
* Introducing third-party client CSS frameworks or external JavaScript libraries.
* Changing the Cytoscape Dagre algorithm topology graph logic or HUD layout.

## Further Notes

* All architectural conventions, core rules, and layout invariants are codified in `AGENTS.md` (Core Rule 5) and `CONTEXT.md` (Principle 5).
