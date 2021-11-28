import click
import natsort
from mangatools.commands import manga_search, manga_extract, manga_archive, manga_ascii

def get_version():
    version_number = "0.2.0"
    version_name = ""
    info = f"{version_number} ('{version_name}')"
    return info

@click.group(name='mangatools')
@click.version_option(version=get_version(), prog_name="Mangatools", message="%(prog)s v%(version)s")
def mangatools():
    pass

@click.command()
@click.argument('title')
@click.option('--doujin', is_flag=True, default=False, help="Shows only doujins")
@click.option('--cover', '-c', type=click.Choice(['first', 'last', 'all'], case_sensitive=False), help="Downloads cover art")
@click.option('--details', '-d', is_flag=True, default=False, help="Creates a details.json file")
def search(title, doujin, cover, details):
    manga_ascii.text_logo()
    click.secho(f'MangaTools v{get_version()}\n', fg='white', bold=True)
    manga_search.getInfo(manga_search.searchManga(title, doujin), cover, details)

@click.command()
@click.option('--no-volume / --volume', is_flag=True, default=False, help="Include the volume number in the folder name")
@click.option('--delete', '--del', is_flag=True, default=False, help="Delete the original files after extracting")
def extract(no_volume, delete):
    manga_ascii.text_logo()
    click.secho(f'MangaTools v{get_version()}\n', fg='white', bold=True)
    manga_extract.extract(no_volume, delete)

@click.command()
@click.option('--extension', '-e', type=click.Choice(['CBZ', 'ZIP'], case_sensitive=False), default="CBZ", show_default=True, help="Archive file extension")
@click.option('--delete', '--del', is_flag=True, default=False, help="Delete the original files after archiving")
def archive(extension, delete):
    manga_ascii.text_logo()
    click.secho(f'MangaTools v{get_version()}\n', fg='white', bold=True)
    manga_archive.archive(extension, delete)

mangatools.add_command(search)
mangatools.add_command(extract)
mangatools.add_command(archive)

if __name__ == '__main__':
    mangatools()
