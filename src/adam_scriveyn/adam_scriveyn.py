import click
from .commands.preprocess import Preprocessor

@click.group()
def main():
    """Adam Scriveyn CLI"""
    pass

@main.command()
@click.option("--path", "-p", type=click.Path(exists=True), required=True, help="File or directory to preprocess")
@click.option("--dest", "-d", type=click.Path(), default=None, help="Destination directory (optional)")
@click.option("--dry-run", is_flag=True, default=False, help="Don't write changes")
def preprocess(path, dest, dry_run):
    """Preprocess images in PATH"""
    p = Preprocessor(path, dest, dry_run=dry_run)
    count = p.run()
    click.echo(f"Processed {count} file(s)")
