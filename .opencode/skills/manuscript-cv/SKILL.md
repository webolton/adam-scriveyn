---
name: manuscript-cv
description: Use when working on computer vision, image preprocessing, or word extraction tasks for the adam-scriveyn medieval manuscript pipeline. Covers Phase 1 Step 2: CV word detection, image segmentation, and building the word image dataset.
---

# Manuscript CV Skill

## Domain Context

The project processes scanned images of the **South English Legendary** — hand-written Middle English manuscripts in cursive script. Standard OCR doesn't work; instead, the approach is:

1. Detect and extract individual **word images** from each manuscript page
2. Build a labelled word image dataset
3. Train a word-level handwriting recognition model

## Phase 1 Step 2: CV Word Extraction

The stub for this lives in `src/adam_scriveyn/commands/preprocess.py` — specifically the `Preprocessor._process_file()` method.

### Likely CV Approach

- **Line detection:** Detect horizontal text lines using projection profiles or Hough transforms
- **Word segmentation:** Find gaps between connected components within lines
- **Bounding boxes:** Extract each word as a cropped image
- **Output:** Save word images to a structured directory, indexed by manuscript/page/line/word position

### Recommended Libraries

- **OpenCV (`opencv-python`)** — primary CV library; already the planned dependency
- `numpy` — array operations on image matrices
- `Pillow` — image I/O if needed alongside OpenCV

### Architecture Pattern

New CV logic should follow the existing pattern:
- Business logic in `src/adam_scriveyn/services/` (e.g., `cv_processing.py`)
- `Preprocessor` in `commands/preprocess.py` delegates to a service
- Full type annotations, single responsibility

### Image File Formats Supported

`.jpg`, `.jpeg`, `.png`, `.tif`, `.tiff`

## Adding OpenCV

```bash
poetry add opencv-python numpy
```
