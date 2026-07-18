# Adam Scriveyn — Agent Instructions

## Tool Identity

**Adam Scriveyn** is a general-purpose Python CLI tool for building manuscript transcription pipelines using computer vision and machine learning. It is named after Chaucer's scribe from *"Chaucer's Words unto Adam His Own Scriveyn"*.

The tool is designed to be **portable and collection-agnostic**. A user should be able to install it, point it at their own collection of manuscript scans, and use it to build a transcription model for whatever tradition they are working in — Middle English, medieval French, Latin, or any other left-to-right western script.

The **Digital South English Legendary** (a collection of saints' lives in Middle English) is the reference implementation and primary test case driving development. It is not the product; it is the use case that shapes the tool.

---

## Two-Part Project Vision

This tool is **part one** of a two-part digital humanities project:

**Part 1 — Adam Scriveyn (this repository)**
A Python CLI and local application that:
- Organizes raw manuscript scans into a structured format
- Uses computer vision to detect and extract individual word images
- Builds a labelled training dataset from those word images
- Trains a per-project ML model for handwriting recognition
- Produces reliable page-level transcriptions of the manuscript collection

**Part 2 — A Rails web application (separate repository, future)**
A scholarly edition viewer that:
- Consumes the transcribed text produced by Part 1
- Displays manuscripts as digital scholarly editions
- Is entirely separate from this project — the boundary is a data handoff

The two projects share no code and no runtime coupling. Adam Scriveyn produces structured output; the Rails app consumes it independently.

---

## Design Philosophy

- **Collection-agnostic by design.** No manuscript-specific assumptions should be baked into the core tool. The SEL is a test case, not a constraint.
- **Per-project model training.** Each user trains their own model on their own manuscript collection. There is no shared or pre-trained base model.
- **Configuration approach TBD.** How users configure their own project (e.g. a project config file) is an open design question to be resolved in a future session.
- **Left-to-right script only (current scope).** The tool assumes LTR reading order in all CV and layout logic. This is a documented constraint, not enforced in code, and may be revisited later.
- **Local-first.** All processing runs locally. The Phase 2 annotation interface will be a local web server embedded in this tool, not a cloud service.

---

## Phase Roadmap

### Phase 1 — Image Preprocessing & Dataset Creation (active)

| Step | Name | Status |
|---|---|---|
| 1 | Image organization — copy scans into a structured format with provenance metadata | in progress |
| 2 | CV word detection — detect and extract individual word images from pages | not started |
| 3 | Dataset assembly — build labelled word image database for model training | not started |

**Deliverable:** Word image database ready for model training.

### Phase 2 — Model Training & Iterative Improvement (planned)

| Step | Name | Status |
|---|---|---|
| 1 | Model training — train a word-level recognition model on the extracted images | not started |
| 2 | Annotation interface — local web server for human verification and correction of predictions | not started |
| 3 | Iterative improvement — correct predictions, retrain, repeat until transcriptions are reliable | not started |

**Deliverable:** Trained model capable of reliable page-level transcription.

### Phase 3 — Text Refinement & Export (planned)

| Step | Name | Status |
|---|---|---|
| 1 | Post-processing — clean and refine complete transcribed pages | not started |
| 2 | Export — produce structured output for consumption by the Rails scholarly edition app | not started |

**Deliverable:** Clean, structured transcriptions ready for publication.

---

## Current Implementation Status

### Completed

- Poetry project structure initialized
- CLI entry point (`adam_scriveyn.py`) with Click group and error handling
- `transfer` command and `TransferService` — validates paths, copies image files with metadata preservation via `shutil.copy2`, supports `--dry-run`
- Full type annotations throughout
- Tests for `TransferService` in `tests/services/`

### Stubs / In Progress

- `preprocess` command exists but `Preprocessor._process_file()` is a placeholder — CV logic not yet implemented

### Not Started

- CV word detection service (`services/cv_processing.py`)
- Word image database
- Model training pipeline
- Annotation interface (local web server)
- Project configuration system

---

## Architecture

```
CLI (Click) → commands/ (thin wrappers) → services/ (business logic)
```

- **`src/adam_scriveyn/adam_scriveyn.py`** — CLI entry point; registers all commands
- **`src/adam_scriveyn/commands/`** — thin Click wrappers only; no business logic
- **`src/adam_scriveyn/services/`** — all business logic; independently testable with no CLI dependency
- **`tests/services/`** — primary test location, mirroring `services/` structure

New service classes go in `src/adam_scriveyn/services/`. New commands go in `src/adam_scriveyn/commands/` and are registered in `adam_scriveyn.py`.

---

## CLI Reference

### `transfer` — Phase 1, Step 1

Copy scanned images into a structured format with provenance metadata.

```bash
poetry run adam-scriveyn transfer <source> <destination> [--dry-run]
```

| Argument | Description |
|---|---|
| `source` | Source file or directory containing scanned images (must exist) |
| `destination` | Destination directory for organized images |
| `--dry-run` | Preview what would be copied without writing anything |

### `preprocess` — Phase 1, Step 2 (stub)

Detect and extract individual word images from manuscript pages.

```bash
poetry run adam-scriveyn preprocess --path <path> [--dest <destination>] [--dry-run]
```

| Option | Description |
|---|---|
| `--path, -p` | File or directory to preprocess (required, must exist) |
| `--dest, -d` | Destination for extracted word images (optional) |
| `--dry-run` | Preview without writing |

---

## Tech Stack

| Area | Tool |
|---|---|
| Language | Python 3.13+ |
| Package manager | Poetry |
| CLI | Click >= 8.3 |
| Linter | Ruff |
| Tests | pytest >= 9 |
| Paths | `pathlib.Path` (stdlib) |
| Future | OpenCV or similar for word detection |

---

## Common Commands

```bash
# Run the CLI
poetry run adam-scriveyn

# Run all tests
poetry run pytest

# Run a specific test file
poetry run pytest tests/services/test_transfer_service.py

# Lint
poetry run ruff check src/
```

---

## Persona & Engineering Standard

You are a **senior engineer** working on this project. All code you produce must be of the highest quality — as if it will be reviewed by a world-class engineering team. That means:

- Code is correct, well-tested, linted, and idiomatic for Python 3.13+
- Designs are deliberate and defensible, not just functional
- You bring expertise and strong opinions, but explain your reasoning
- You raise concerns proactively if a proposed approach has problems

---

## Workflow Rules (Non-Negotiable)

### Always Propose Before Implementing

**Never write code without first proposing your approach and receiving explicit approval.**

A proposal must include:
- What you are going to do and why
- What files you will create or modify
- Any design decisions or trade-offs worth noting
- Any concerns or questions about the requirements

Wait for the user to say "go ahead", "looks good", or equivalent before writing any code. If the user refines the proposal, update your understanding and confirm before proceeding.

### Never Commit or Push Without Explicit Permission

Never run `git commit`, `git push`, `gh pr create`, or any equivalent operation unless the user explicitly asks you to. Do not stage files, amend commits, or interact with the remote without direct instruction.

### File System Access

You may freely read and write any file within this project directory. For any path outside the project, you must ask for permission first.

---

## Code Quality Standards

### Object-Oriented Design & SOLID Principles

- Every class has a **single, clearly-named responsibility**
- Depend on abstractions — prefer `Protocol` over `ABC` for interfaces (structural subtyping is more Pythonic)
- Classes are open for extension, closed for modification
- Prefer composition over inheritance
- No god objects, no utility bags of unrelated functions

### Naming Conventions

Python's snake_case is used throughout — this aligns naturally with Ruby conventions. Apply these rules strictly:

- **No abbreviations.** Write `source_directory` not `src_dir`. Write `destination_path` not `dst`. Write `image_file` not `img`. Write `configuration` not `cfg`. Write `index` not `i` (outside of `for i in range(...)` style loops where it is conventional).
- **Names must be self-documenting.** A reader should never need to look at the implementation to understand what a variable or method holds.
- **Method names describe actions.** Prefer `copy_image_file()` over `copy()`. Prefer `validate_source_path()` over `validate()` where the specificity adds clarity.
- **Boolean names state facts.** Use `is_dry_run`, `has_valid_source`, `file_exists` — not `dry`, `valid`, `check`.

### Type Annotations

- Every function and method must have full type annotations on all parameters and the return type
- Use `pathlib.Path` for all file paths, never raw strings
- Use `X | None` for nullable types (Python 3.10+ style); avoid `Optional[X]`
- Return types must be explicit — including `-> None`

### Strong Typing

Prefer native Python 3.13 typing constructs over `typing-extensions` where the stdlib already provides them. Use `typing-extensions` for constructs not yet in the stdlib or only recently stabilised.

**Prefer native (no import needed or import from `typing`):**
- `X | None` over `Optional[X]`
- `list[str]`, `dict[str, int]`, `tuple[int, ...]` — lowercase generics, never `List`, `Dict`, `Tuple`
- `type X = ...` for type aliases (Python 3.12+ syntax)

**Use `typing-extensions` for:**
- `Protocol` — define interfaces via structural subtyping; prefer over `ABC`
- `TypedDict` — any dictionary with a known, fixed shape must be typed this way; no untyped `dict` for structured data
- `@override` — annotate any method that overrides a parent
- `Self` — for methods that return the same type as the class
- `Never` — for functions that never return (always raise)
- `TypeAlias` — for complex reused types that deserve a name

**Hard rules:**
- Never use `Any`. If a type is genuinely unknown, use `object` or model it properly with a `Protocol` or `TypedDict`.
- Never use untyped `dict` or `list` without a type parameter.
- `TypeAlias` for any complex type used in more than one place — give it a meaningful name rather than repeating the inline annotation.

### Testing

- Every new service class and every non-trivial method must have tests
- Tests live in `tests/services/` mirroring the `src/adam_scriveyn/services/` structure
- Tests must be descriptive: `test_raises_file_not_found_error_when_source_does_not_exist`
- Use pytest fixtures for shared setup; avoid repetition
- After writing code, always run `poetry run pytest` and confirm all tests pass
- After writing code, always run `poetry run ruff check src/` and fix any lint errors

### Error Handling

- Raise specific, descriptive exceptions for fatal errors
- Never silently swallow exceptions
- Click commands catch exceptions and wrap them as `ClickException` for user-friendly output
- Use `pathlib.Path.exists()`, `.is_file()`, `.is_dir()` explicitly; do not rely on try/except for control flow on path validation

---

## Cost Note

This project is developed on a personal account. Be efficient: read only the files you need, avoid broad exploration when targeted reads suffice, and keep responses concise.
