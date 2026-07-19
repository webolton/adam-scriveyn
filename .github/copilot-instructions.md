# Adam Scriveyn — Copilot Instructions

## Tool Identity

**Adam Scriveyn** is a general-purpose Python CLI tool for building manuscript transcription pipelines using computer vision and machine learning.

It is **collection-agnostic by design**. A user should be able to install it, point it at their own manuscript scans, and build a transcription model for any left-to-right western script tradition — Middle English, medieval French, Latin, etc.

The **Digital South English Legendary** is the reference implementation and primary test case. It is not the product; it is the use case that shapes the tool.

---

## Two-Part Project Vision

**Part 1 — Adam Scriveyn (this repository)**
- Organizes raw manuscript scans into a structured format
- Uses computer vision to detect and extract individual word images
- Builds a labelled training dataset
- Trains a per-project ML model for handwriting recognition
- Produces reliable page-level transcriptions

**Part 2 — Rails web application (separate repository, future)**
- Displays transcribed manuscripts as digital scholarly editions
- Consumes structured output from Part 1 — no shared code or runtime coupling

---

## Design Philosophy

- **Collection-agnostic.** No manuscript-specific assumptions in core code.
- **Per-project model training.** Each user trains their own model on their own data.
- **LTR only (current scope).** Left-to-right reading order assumed throughout. Documented constraint, not enforced in code.
- **Local-first.** All processing runs locally. Phase 2 annotation interface is a local web server embedded in this tool.
- **Configuration approach TBD.**

---

## Phase Roadmap

| Phase | Name | Status |
|---|---|---|
| 1 | Image Preprocessing & Dataset Creation | active |
| 2 | Model Training & Iterative Improvement | planned |
| 3 | Text Refinement & Export | planned |

**Phase 1 steps:** image organization (in progress) → CV word detection (not started) → dataset assembly (not started)

**Phase 2 steps:** model training → annotation interface (local web server) → iterative improvement

**Phase 3 steps:** post-processing → export for Rails app

---

## Current Implementation Status

**Done:** Poetry structure, CLI entry point, `transfer` command + `TransferService` (copies images, dry-run support), full type annotations, tests for `TransferService`.

**Stub:** `preprocess` command exists; `Preprocessor._process_file()` is a placeholder.

**Not started:** CV word detection, word image database, model training, annotation interface, project configuration system.

---

## Workflow Rules (Non-Negotiable)

- **Never write code without proposing first and receiving explicit approval.** A proposal must state: what, why, which files, trade-offs, concerns.
- **Never commit, push, or interact with git/GitHub without explicit instruction.**
- **File access:** freely read/write within this project. Ask before accessing anything outside it.

---

## Code Quality Standards

### OOP & SOLID

- Single responsibility per class
- Depend on abstractions — prefer `Protocol` over `ABC` for interfaces (structural subtyping is more Pythonic)
- Prefer composition over inheritance
- No god objects

### Naming

Python snake_case throughout. Strictly:

- **No abbreviations.** `source_directory` not `src_dir`. `destination_path` not `dst`. `image_file` not `img`. `configuration` not `cfg`.
- Names must be self-documenting.
- Method names describe actions: `copy_image_file()` not `copy()`.
- Booleans state facts: `is_dry_run`, `has_valid_source`, `file_exists`.
- Single-letter variables only acceptable as loop counters in `for i in range(...)`.

### Type Annotations

- Full annotations on every parameter and return type
- `pathlib.Path` for all file paths — never raw strings
- `X | None` not `Optional[X]`
- `-> None` explicit on void functions

### Strong Typing

Prefer native Python 3.13 typing over `typing-extensions` where the stdlib provides it. Use `typing-extensions` for constructs not yet native.

**Prefer native:**
- `X | None` over `Optional[X]`
- `list[str]`, `dict[str, int]`, `tuple[int, ...]` — lowercase generics always; never `List`, `Dict`, `Tuple`
- `type X = ...` for type aliases (Python 3.12+)

**Use `typing-extensions` for:**
- `Protocol` — interfaces via structural subtyping; prefer over `ABC`
- `TypedDict` — any dict with a known shape must use this; no untyped `dict` for structured data
- `@override` — on any method that overrides a parent
- `Self` — methods returning the same type as the class
- `Never` — functions that always raise
- `TypeAlias` — complex types used in more than one place

**Hard rules:**
- Never use `Any`. Use `object` or model the type properly with `Protocol` or `TypedDict`.
- Never use untyped `dict` or `list` without a type parameter.

### Testing

- Every service class and every non-trivial method must have tests
- Tests in `tests/services/` mirroring `src/adam_scriveyn/services/`
- Descriptive test names: `test_raises_file_not_found_error_when_source_does_not_exist`
- After writing code: run `poetry run pytest` and `poetry run ruff check src/`; fix all failures

### Error Handling

- Raise specific, descriptive exceptions for fatal errors; never swallow exceptions
- Click commands wrap exceptions as `ClickException`
- Use `pathlib.Path.exists()` / `.is_file()` / `.is_dir()` for path checks — not try/except

---

## Architecture

```
CLI (Click) → commands/ (thin wrappers) → services/ (business logic)
```

- `src/adam_scriveyn/adam_scriveyn.py` — CLI entry point
- `src/adam_scriveyn/commands/` — thin Click wrappers; no business logic
- `src/adam_scriveyn/services/` — all business logic; independently testable
- `tests/services/` — primary test location

New services → `src/adam_scriveyn/services/`
New commands → `src/adam_scriveyn/commands/` + registered in `adam_scriveyn.py`

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
| Future | OpenCV for word detection |

---

## Common Commands

```bash
poetry run adam-scriveyn                    # run the CLI
poetry run pytest                           # run all tests
poetry run ruff check src/                  # lint
poetry run adam-scriveyn transfer <src> <dest> [--dry-run]
```
