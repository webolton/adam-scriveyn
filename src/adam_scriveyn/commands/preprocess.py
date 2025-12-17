from pathlib import Path
from typing import Optional


class Preprocessor:
    """
    Responsible only for preprocessing images to extract individual words.
    Uses Computer Vision to detect and extract word images.

    Inputs: source path (file or dir), optional output path, config options.
    Output: returns number of files processed or raises on fatal errors.
    """

    def __init__(
        self,
        source: str | Path,
        dest: str | Path | None = None,
        *,
        dry_run: bool = False,
    ) -> None:
        self.source = Path(source)
        self.dest = Path(dest) if dest else None
        self.dry_run = bool(dry_run)

    def validate(self) -> None:
        """Validate source path exists."""
        if not self.source.exists():
            raise FileNotFoundError(f"source not found: {self.source}")

    def run(self) -> int:
        """Perform preprocessing. Return count of processed files."""
        self.validate()
        processed = 0
        if self.source.is_file():
            processed += self._process_file(self.source)
        else:
            for p in self.source.rglob("*"):
                if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}:
                    processed += self._process_file(p)
        return processed

    def _process_file(self, file_path: Path) -> int:
        """
        Process a single image file to extract word images.
        
        TODO: Implement Computer Vision to detect and extract words.
              Keep I/O separated — call helpers in services/cv_processing.py
        """
        if self.dry_run:
            return 1
        # ... actual processing ...
        return 1
