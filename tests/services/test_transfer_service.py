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
            tmp_path / "nonexistent",
            tmp_path,
            dry_run=True
        )

        with pytest.raises(FileNotFoundError):
            service.validate()

    def test_validate_dest_not_found(self, tmp_path):
        """Test validation when destination does not exist."""
        source = tmp_path / "source"
        source.mkdir()

        service = TransferService(
            source,
            tmp_path / "nonexistent_dest",
            dry_run=True
        )

        with pytest.raises(FileNotFoundError):
            service.validate()

    def test_validate_dest_not_directory(self, tmp_path):
        """Test validation when destination is not a directory."""
        source = tmp_path / "source"
        source.mkdir()
        dest_file = tmp_path / "dest_file"
        dest_file.touch()

        service = TransferService(
            source,
            dest_file,
            dry_run=True
        )

        with pytest.raises(NotADirectoryError):
            service.validate()

    def test_copy_file_dry_run(self, tmp_path):
        """Test copy_file in dry-run mode."""
        source_file = tmp_path / "test.jpg"
        source_file.touch()

        service = TransferService(tmp_path, tmp_path, dry_run=True)
        result = service.copy_file(source_file)

        assert result == 1

    # TODO: Add more comprehensive tests as implementation is completed.
