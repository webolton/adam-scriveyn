from pathlib import Path
from typing import Optional


class Transfer:
    """
    Responsible for copying scanned images with a file name format that contains metadata about the
    image.

    Inputs: source path (file or dir), destination path, config options.
    Output: returns number of files copied or raises on fatal errors.
    """

    def __init__(
        self,
        source: str | Path,
        dest: str | Path,
        *,
        dry_run: bool = False,
    ) -> None:
        self.source = Path(source)
        self.dest = Path(dest)
        self.dry_run = bool(dry_run)

    def validate(self) -> None:
        """Validate source exists and destination is writable."""
        if not self.source.exists():
            raise FileNotFoundError(f"source not found: {self.source}")
        if not self.dest.exists():
            raise FileNotFoundError(f"destination not found: {self.dest}")
        if not self.dest.is_dir():
            raise NotADirectoryError(f"destination must be a directory: {self.dest}")

    def run(self) -> int:
        """Perform copy operation. Return count of files copied."""
        self.validate()
        copied = 0
        if self.source.is_file():
            copied += self._copy_file(self.source)
        else:
            for p in self.source.rglob("*"):
                if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}:
                    copied += self._copy_file(p)
        return copied

    def _copy_file(self, file_path: Path) -> int:
        """
        Copy a single file to the destination, preserving manuscript structure.
        
        TODO: Implement structured naming/organization that preserves page metadata.
        """
        if self.dry_run:
            return 1
        # ... actual copy and organization logic ...
        return 1
