import shutil
from pathlib import Path


class TransferService:
    """
    Service layer for transferring and copying scanned images with manuscript metadata.

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
        """
        Initialize TransferService.

        Args:
            source: Source file or directory path containing images to transfer.
            dest: Destination directory path where images will be copied.
            dry_run: If True, simulate operation without actual file copying.
        """
        self.source = Path(source)
        self.dest = Path(dest)
        self.dry_run = bool(dry_run)

    def validate(self) -> None:
        """Validate source exists and destination parent directory exists."""
        if not self.source.exists():
            raise FileNotFoundError(f"source not found: {self.source}")
        if not self.source.is_file():
            raise IsADirectoryError(f"source must be a file: {self.source}")
        if not self.dest.parent.exists():
            raise FileNotFoundError(f"destination parent directory not found: {self.dest.parent}")
        if self.dest.exists():
            raise FileExistsError(f"destination already exists: {self.dest}")

    def run(self) -> int:
        """
        Perform copy operation. Return count of files copied.

        Returns:
            Number of files successfully copied.
        """
        self.validate()
        return self.copy_file(self.source)

    def copy_file(self, file_path: Path) -> int:
        """
        Copy a single file to the destination with the new name.

        Args:
            file_path: Path to the file to copy.

        Returns:
            1 if file was copied, 0 otherwise.
        """
        if self.dry_run:
            self.validate()
            print(self.dest)
        else:
            shutil.copy2(str(file_path), str(self.dest))
        return 1
