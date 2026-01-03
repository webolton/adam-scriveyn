"""Tests for the TransferService class."""

import pytest
from pathlib import Path
from adam_scriveyn.services.transfer import TransferService


class TestTransferService:
    """Test suite for TransferService."""

    def test_initialization(self):
        """Test TransferService initialization."""
        source = Path("/tmp/source")
        dest = Path("/tmp/dest")
        service = TransferService(source, dest, dry_run=True)

        assert service.source == source
        assert service.dest == dest
        assert service.dry_run is True

    def test_initialization_with_string_paths(self):
        """Test TransferService initialization with string paths."""
        source = "/tmp/source"
        dest = "/tmp/dest"
        service = TransferService(source, dest, dry_run=False)

        assert service.source == Path(source)
        assert service.dest == Path(dest)
        assert service.dry_run is False

    def test_validate_source_not_found(self, tmp_path):
        """Test validation when source does not exist."""
        service = TransferService(
            tmp_path / "nonexistent.jpg",
            tmp_path / "dest.jpg",
            dry_run=True
        )

        with pytest.raises(FileNotFoundError):
            service.validate()

    def test_validate_source_not_file(self, tmp_path):
        """Test validation when source is a directory, not a file."""
        source_dir = tmp_path / "source_dir"
        source_dir.mkdir()

        service = TransferService(
            source_dir,
            tmp_path / "dest.jpg",
            dry_run=True
        )

        with pytest.raises(IsADirectoryError):
            service.validate()

    def test_validate_dest_parent_not_found(self, tmp_path):
        """Test validation when destination parent directory does not exist."""
        source_file = tmp_path / "source.jpg"
        source_file.touch()

        service = TransferService(
            source_file,
            tmp_path / "nonexistent_dir" / "dest.jpg",
            dry_run=True
        )

        with pytest.raises(FileNotFoundError):
            service.validate()

    def test_validate_dest_already_exists(self, tmp_path):
        """Test validation when destination file already exists."""
        source_file = tmp_path / "source.jpg"
        source_file.touch()
        dest_file = tmp_path / "dest.jpg"
        dest_file.touch()

        service = TransferService(
            source_file,
            dest_file,
            dry_run=True
        )

        with pytest.raises(FileExistsError):
            service.validate()

    def test_copy_file_dry_run(self, tmp_path):
        """Test copy_file in dry-run mode."""
        source_file = tmp_path / "test.jpg"
        source_file.touch()
        dest_file = tmp_path / "renamed.jpg"

        service = TransferService(source_file, dest_file, dry_run=True)
        result = service.copy_file(source_file)

        assert result == 1
        # File should not actually be copied in dry-run mode
        assert not dest_file.exists()

    def test_copy_file_actual_copy(self, tmp_path):
        """Test copy_file actually copies the file."""
        source_file = tmp_path / "test.jpg"
        source_file.write_text("test content")
        dest_file = tmp_path / "renamed.jpg"

        service = TransferService(source_file, dest_file, dry_run=False)
        result = service.copy_file(source_file)

        assert result == 1
        # File should be copied
        assert dest_file.exists()
        assert dest_file.read_text() == "test content"
