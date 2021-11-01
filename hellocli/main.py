"""Hello CLI."""
import click


@click.command()
@click.argument('phrase')
def cli(phrase):
    """Print phrase."""
    print(phrase)
