import os
import subprocess
import shutil
import click

def archive(extension, delete):
    cwd = os.getcwd()
    chapters = []
    print(f"\nFOLDER:\n{os.path.basename(cwd)} [{cwd}]\n")

    for path in sorted(os.listdir(cwd)):
        full_path = os.path.join(cwd, path)
        if os.path.isdir(full_path):
            chapters.append(full_path)
    
    if os.path.join(cwd, "mangadex_covers") in chapters:
        chapters.remove(os.path.join(cwd, "mangadex_covers"))

    print("\nCHAPTERS:")
    for chapter in chapters:
        print(f"Archive: {os.path.basename(chapter)}.{extension.lower()}")
        subprocess.call(f'7z a -tzip -bso0 -bsp0 "{chapter}.{extension.lower()}" "{chapter}\\" -y')
    
    # Delete original directories
    if delete:
        click.confirm(f"\nDo you want to continue? {len(chapters)} folders will be deleted from {os.path.basename(cwd)}.", abort=True)
        for i in chapters:
            click.echo(f"Delete: {i.split(cwd, 1)[1][1:]}")
            shutil.rmtree(i)