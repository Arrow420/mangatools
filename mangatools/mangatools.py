import click
from mangatools.commands import archive, ascii, extract, search
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
@click.option('--no-logo', is_flag=True, default=False, help="Disables the ascii logo")
def search(title, doujin, covers, details, no_logo):
    if not no_logo:
        ascii.text_logo()
        click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    getInfo(searchManga(title, doujin), covers, details)

@click.command()
@click.option('--volume/--no-volume', default=True, help="Includes the volume number in the folder name")
@click.option('--no-logo', is_flag=True, default=False, help="Disables the ascii logo")
def extract(no_volume, no_logo):
    if not no_logo:
        ascii.text_logo()
        click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    extract.extract(no_volume)

@click.command()
@click.option('--no-logo', is_flag=True, default=False, help="Disables the ascii logo")
def archive(no_logo):
    if not no_logo:
        ascii.text_logo()
        click.secho(f'Manga Tools v{get_version()}\n', fg='white', bold=True)
    archive.archive()

mangatools.add_command(search)
mangatools.add_command(extract)
mangatools.add_command(archive)

if __name__ == '__main__':
    mangatools()
