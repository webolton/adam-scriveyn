from pathlib import Path
from typing import Optional

class Preprocessor:
    """
    Responsible only for preprocessing images.
    Inputs: source path (file or dir), optional output path, config options.
    Output: returns number of files processed or raises on fatal errors.
    """

    def __init__(self, source: str | Path, dest: Optional[str | Path] = None, *, dry_run: bool = False):
        self.source = Path(source)
        self.dest = Path(dest) if dest else None
        self.dry_run = bool(dry_run)

    def validate(self) -> None:
        if not self.source.exists():
            raise FileNotFoundError(f"source not found: {self.source}")
        # more validation rules here

    def run(self) -> int:
        """Perform preprocessing. Return count of processed files."""
        self.validate()
        processed = 0
        if self.source.is_file():
            # process single file
            processed += self._process_file(self.source)
        else:
            for p in self.source.rglob("*"):
                if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}:
                    processed += self._process_file(p)
        return processed

    def _process_file(self, file_path: Path) -> int:
        # placeholder: open, resize, normalize, save
        # keep I/O separated — call helpers in services/image_io.py
        if self.dry_run:
            return 1
        # ... actual processing ...
        return 1
