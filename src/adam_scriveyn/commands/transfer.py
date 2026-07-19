"""Click CLI interface for the transfer command."""

import click

from adam_scriveyn.services.transfer import TransferService


@click.command()
@click.argument("source", type=click.Path(exists=True))
@click.argument("dest", type=click.Path(exists=True, file_okay=False))
@click.option("--dry-run", is_flag=True, help="Simulate operation without copying files.")
def transfer(source: str, dest: str, dry_run: bool) -> None:
    """
    Transfer and organize scanned manuscript images with metadata.

    SOURCE: Path to source file or directory containing images.
    DEST: Destination directory where images will be organized.
    """
    service = TransferService(source, dest, dry_run=dry_run)
    copied = service.run()
    click.echo(f"Transferred {copied} file(s).")
