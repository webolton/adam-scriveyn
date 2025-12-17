# Digital South English Legendary - Project Context

## Project Overview

**Project Name:** The Digital South English Legendary
**Tool Name:** Adam Scriveyn (a reference to Chaucer's scribe)
**Purpose:** A system for processing scanned manuscripts and using machine learning to transcribe Middle English texts

### Domain

- **Subject Matter:** South English Legendary - a collection of saints' lives in Middle English
- **Source Material:** Scanned images of hand-written Middle English manuscripts in cursive script
- **Transcription Challenge:** Custom word-level recognition required (OCR won't work with hand-written cursive)

---

## Project Vision & Phases

### Phase 1: Image Preprocessing & Dataset Creation
**Current Focus**

1. **Image Organization**
   - Copy scanned images into a structured format that preserves manuscript page metadata
   - Maintain provenance information for each page

2. **Computer Vision Processing**
   - Use CV to detect and locate words on pages
   - Extract individual word images into a database
   - Create training dataset for ML model

3. **Deliverable**
   - Word image database ready for model training

### Phase 2: Model Training & Iterative Improvement

1. **Model Development**
   - Train model on word-level images to recognize Middle English cursive
   - Create web-based annotation interface

2. **Human-in-the-Loop Verification**
   - Display word image + model's predicted transcription
   - User corrects/verifies predictions
   - Iteratively improve model until page-level transcriptions are reliable

### Phase 3: Text Refinement & Publication

1. **Post-OCR Editing**
   - Clean and refine complete transcribed pages
   - Iterate with model to improve quality

2. **Scholarly Edition Publishing**
   - Export clean texts to database
   - Build multi-version web application for scholarly edition

---

## Technical Architecture

### Technology Stack

- **Language:** Python 3.13+
- **Package Manager:** Poetry
- **CLI Framework:** Click (for command-line interface)
- **Development Tools:** Ruff (linter)

### Design Principles

- **Object-Oriented Design:** Follow SOLID principles
- **Separation of Concerns:** Each class/module has single responsibility
- **CLI-First Architecture:** Command-line tool for all operations

### Project Structure

```
adam-scriveyn/
├── README.md
├── LICENSE
├── pyproject.toml
├── context/
│   ├── PROJECT_CONTEXT.md (human-readable)
│   └── PROJECT_CONTEXT.json (AI-consumable)
├── src/
│   └── adam_scriveyn/
│       ├── __init__.py
│       ├── adam_scriveyn.py (main entry point & Click CLI)
│       ├── commands/
       │   ├── __init__.py
       │   ├── transfer.py (Transfer class for organizing scanned images)
       │   └── preprocess.py (Preprocessor class for image preprocessing)
│       └── services/
│           ├── __init__.py
│           └── [future: image_io.py, cv_processing.py, etc.]
└── tests/
    └── __init__.py
```

---

## Current Implementation Status

### Completed

- **Project structure** initialized with Poetry
- **CLI entry point** set up with Click with improved error handling
- **Type hints** added throughout for better code quality
- **Preprocessor class** created with single responsibility:
  - `__init__`: Takes source path, optional destination, dry-run flag
  - `validate()`: Validates source existence
  - `run()`: Main processing method that handles files/directories
  - `_process_file()`: Placeholder for individual file processing
  - Supports recursive search for image files (.jpg, .jpeg, .png, .tif, .tiff)
- **Transfer class** created for Phase 1 Step 1 (image organization):
  - `__init__`: Takes source, required destination, dry-run flag
  - `validate()`: Validates source and destination paths
  - `run()`: Main transfer operation with structured file organization
  - `_copy_file()`: Handles individual file copying with metadata preservation
  - Supports recursive search for image files (.jpg, .jpeg, .png, .tif, .tiff)

### In Progress

- Image preprocessing logic implementation
- Computer Vision integration

### Planned

- Image I/O services (image_io.py)
- Computer Vision services (cv_processing.py)
- Database models for word images
- Model training pipeline
- Annotation interface
- Export/publishing tools

---

## Command-Line Interface

### Current Commands

#### `transfer`
Copy scanned images to a structured format with manuscript metadata (Phase 1, Step 1)

**Usage:**
```bash
poetry run adam-scriveyn transfer --source <path> --dest <directory> [--dry-run]
```

**Options:**
- `--source, -s`: Source file or directory with scanned images (required, must exist)
- `--dest, -d`: Destination directory for organized images (required)
- `--dry-run`: Preview changes without writing (optional flag)

**Example:**
```bash
poetry run adam-scriveyn copy-over -s ./scans --dest ./organized_scans
poetry run adam-scriveyn copy-over -s ./scans --dest ./organized_scans --dry-run
```

#### `preprocess`
Preprocess images to extract individual words (Phase 1, Step 2)

**Usage:**
```bash
poetry run adam-scriveyn preprocess --path <path> [--dest <destination>] [--dry-run]
```

**Options:**
- `--path, -p`: File or directory to preprocess (required, must exist)
- `--dest, -d`: Destination directory for processed word images (optional)
- `--dry-run`: Preview changes without writing (optional flag)
Command Classes Design**
   - Single Responsibility: Transfer handles image organization, Preprocessor handles word extraction
   - Both return count of processed files
   - Raise exceptions on fatal errors (validation, file not found, etc.)
   - I/O separated from business logic (placeholders for services modules)
   - Consistent interface: `validate()`, `run()`, and `_process_file()` methods

2. **Type Hints and Code Quality**
   - Full type annotations on all function parameters and return types
   - Type hints for better IDE support and error catching
   - Explicit `-> None` return type on functions that don't return values

3. **CLI Design**
   - Using Click for robust command structure with error handling
   - Consistent option naming across commands (--source/--path, --dest, --dry-run)
   - ClickException wrapping for user-friendly error messages
   - Extensible group-based command structure for future features

4. **Future Architecture**
   - Services directory for business logic (cv_processing.py for word detection, etc.)
   - Separation of concerns: each service handles specific domain
   - Each command corresponds to a specific phase/step in the workflow
- **click** (>=8.3.0, <9.0.0): CLI framework
- **path** (>=17.1.1, <18.0.0): Path manipulation utilities
- **typing-extensions** (dev): Enhanced type hints

### Key Design Decisions

1. **Preprocessor Class Design**
   - Single Responsibility: Only handles image preprocessing
   - Returns count of processed files
   - Raises exceptions on fatal errors (not exceptions for recoverable issues)
   - I/O separated from business logic (placeholder for services/image_io.py)

2. **CLI Design**
   - Using Click for robust command structure
   - Extensible group-based command structure for future features

3. **Future Architecture**
   - Services directory for business logic (image processing, CV, etc.)
   - Separation of concerns: each service handles specific domain

---

## Update Instructions

**At the end of each working session, update these context files:**

### Markdown Context (PROJECT_CONTEXT.md)
- Update "Current Implementation Status" section with progress
- Add any new design decisions or architectural changes
- Update the CLI section if new commands are added
- Modify the project structure diagram if directories/files are added
- Update the "Planned" section if priorities change

### JSON Context (PROJECT_CONTEXT.json)
- Update the `status` field for each completed/in-progress item
- Add new entries to `implementation` array for new features
- Update `cliCommands` if new commands are added
- Update `projectStructure` if directories change
- Modify `architectureNotes` as design evolves

**Command to help with updates:**
```bash
# Review what's been changed since last context update
git diff HEAD~1
# or
git status
```

---

## References

- [Chaucer's Words unto Adam His Own Scriveyn](https://faculty.goucher.edu/eng330/chaucers_wordes_unto_adam_his_own_scriveyn.htm)
- [South English Legendary](https://en.wikipedia.org/wiki/South_English_Legendary)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
