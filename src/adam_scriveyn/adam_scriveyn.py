import click
from .commands.preprocess import Preprocessor
from .commands.transfer import Transfer


@click.group()
def main() -> None:
    """Adam Scriveyn CLI - Image transcription processing tool"""
    pass


@main.command()
@click.option(
    "--source",
    "-s",
    type=click.Path(exists=True),
    required=True,
    help="Source file or directory with scanned images",
)
@click.option(
    "--dest",
    "-d",
    type=click.Path(),
    required=True,
    help="Destination directory for organized images",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Preview changes without writing",
)
def transfer(source: str, dest: str, dry_run: bool) -> None:
    """Transfer scanned images to a structured format with manuscript metadata."""
    try:
        transferer = Transfer(source, dest, dry_run=dry_run)
        count = transferer.run()
        click.echo(f"Transferred {count} file(s)")
    except (FileNotFoundError, NotADirectoryError) as e:
        raise click.ClickException(str(e))


@main.command()
@click.option(
    "--path",
    "-p",
    type=click.Path(exists=True),
    required=True,
    help="File or directory to preprocess",
)
@click.option(
    "--dest",
    "-d",
    type=click.Path(),
    default=None,
    help="Destination directory (optional)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Preview changes without writing",
)
def preprocess(path: str, dest: str | None, dry_run: bool) -> None:
    """Preprocess images to extract individual words."""
    try:
        processor = Preprocessor(path, dest, dry_run=dry_run)
        count = processor.run()
        click.echo(f"Processed {count} file(s)")
    except FileNotFoundError as e:
        raise click.ClickException(str(e))
