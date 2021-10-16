import click
from mangatools.commands import archive_all, extract_all, search, ascii
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
@click.option('--doujin', is_flag=True, default=False, help="Shows only manga with the doujin tag")
@click.option('--covers/--no-covers', default=True, help="Downloads manga coverart")
@click.option('--details/--no-details', default=True, help="Creates a details.json file")
def search(title, doujin, covers, details):
    ascii.text_logo()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    getInfo(searchManga(title, doujin), covers, details)

@click.command()
@click.option('--no-volume', is_flag=True, default=False, help="Excludes the volume number from the folder name")
def extract(no_volume):
    ascii.text_logo()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    extract_all.extract(no_volume)

@click.command()
def archive():
    ascii.text_logo()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    archive_all.archive()

mangatools.add_command(search)
mangatools.add_command(extract)
mangatools.add_command(archive)

if __name__ == '__main__':
    mangatools()
