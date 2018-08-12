import click

from workers import WorkerMangaReader


@click.group()
def cli():
    pass


@cli.command()
def get_manga_list():
    worker = WorkerMangaReader()
    worker.get_manga_list()


if __name__ == '__main__':
    cli()