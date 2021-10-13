import click
from mangatools.commands import search, extract, archive, ascii
from mangatools.commands.search import getInfo, searchManga

def get_version():
    version_number = "0.1.0"
    version_name = "Net Terminal Gene"
    info = f"{version_number} ('{version_name}')"
    return info

@click.group(name='mangatools')
def mangatools():
    pass

@click.command()
@click.argument('title')
@click.option('--doujin', is_flag=True, default=False, help='Shows manga with the doujin tag')
@click.option('--no-covers', is_flag=True, default=False, help="Doesn't download manga volume coverart")
@click.option('--no-details', is_flag=True, default=False, help="Doesn't create a details.json file")
def search(title, doujin, no_covers, no_details):
    ascii.small_ascii()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    getInfo(searchManga(title, doujin), no_covers, no_details)

@click.command()
def extract():
    ascii.small_ascii()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    extract.extract()

@click.command()
def archive():
    ascii.small_ascii()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    archive.archive()


mangatools.add_command(search)
mangatools.add_command(extract)
mangatools.add_command(archive)

if __name__ == '__main__':
    mangatools()