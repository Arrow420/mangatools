import os
import subprocess
import shutil
import click
from natsort.natsort import natsorted

def archive(extension, compression, delete, yes):
    if not shutil.which("7z"): # if 7-zip is not installed, abort
        click.secho("\n7-zip isn't installed or added to path", fg='red', reset=True)
        exit(404)
    
    cwd = os.getcwd()
    chapters = []
    click.echo(f"\nFOLDER:\n{os.path.basename(cwd)} [{cwd}]\n")

    for path in sorted(os.listdir(cwd)):
        full_path = os.path.join(cwd, path)
        if os.path.isdir(full_path):
            chapters.append(full_path)
    
    if os.path.join(cwd, "volume_covers") in chapters:
        chapters.remove(os.path.join(cwd, "volume_covers"))

    click.echo("\nCHAPTERS:")
    for chapter in natsorted(chapters):
        click.echo(f"Archive: {os.path.basename(chapter)}.{extension.lower()}")
        subprocess.call(f'7z a -tzip -bso0 -bsp0 -mx{compression} "{chapter}.{extension.lower()}" "{chapter}\\" -y')
    
    # Delete original directories
    if delete:
        if not yes:
            click.confirm(f"\nDo you want to continue? {len(chapters)} folders will be deleted from {os.path.basename(cwd)}.", abort=True)
        for i in natsorted(chapters):
            click.echo(f"Delete: {i.split(cwd, 1)[1][1:]}")
            shutil.rmtree(i)