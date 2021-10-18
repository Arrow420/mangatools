import click
from mangatools.commands import manga_search, manga_extract, manga_archive, manga_ascii

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
@click.option('--covers', '-c', type=click.Choice(['first', 'last', 'all'], case_sensitive=False), help="Downloads manga cover art")
@click.option('--details', '-d', is_flag=True, default=False, help="Creates a details.json file")
def search(title, doujin, covers, details):
    manga_ascii.text_logo()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    manga_search.getInfo(manga_search.searchManga(title, doujin), covers, details)

@click.command()
@click.option('--no-volume', is_flag=True, default=False, show_default=True, help="Excludes the volume from the name  ")
@click.option('--delete-original', is_flag=True, default=False, show_default=True, help="Deletes the original volume folders")
def extract(no_volume, delete_original):
    manga_ascii.text_logo()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    manga_extract.extract(no_volume, delete_original)

@click.command()
@click.option('--extension', '-e', type=click.Choice(['CBZ', 'ZIP'], case_sensitive=False), default="CBZ", show_default=True, help="Archive file extension     ")
def archive(extension):
    manga_ascii.text_logo()
    click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    manga_archive.archive(extension)

mangatools.add_command(search)
mangatools.add_command(extract)
mangatools.add_command(archive)

if __name__ == '__main__':
    mangatools()
