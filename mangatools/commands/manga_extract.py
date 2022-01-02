import os
import re
import shutil
import click


def extract(no_volume, chapter_name, delete, yes):
    cwd = os.getcwd()
    volumes = []
    chapters = []

    pg_syntax = "(p\d\d\d(?:[^\s]+)?)"
    ch_syntax = "(c\d\d\d(?:[^\s]+)?)"
    v_syntax = "(v\d\d)"
    name_syntax = "(?:\[dig\]|\[digital\]|\[digital-hd\]) \[(.+?)\] \[.+?\] \[.+?\]"
    num = 0

    click.echo("\nVOLUMES:")
    
    for path in os.listdir(cwd):
        full_path = os.path.join(cwd, path)
        if os.path.isdir(full_path):
            click.echo(path)
            volumes.append(full_path)

    for volume in volumes:
        num += 1
        click.echo(f"\nVOLUME {num}:")
        for page in os.listdir(volume):
            if os.path.isdir(page) == False:
                if re.search(pg_syntax, page):
                    pg = str(re.search(pg_syntax, page).group(1))
                else:
                    click.secho("\nCouldn't find the page number", fg='red', reset=True)
                    exit(404)

                if re.search(ch_syntax, page):
                    ch = str(re.search(ch_syntax, page).group(1))
                else:
                    click.secho("\nCouldn't find the chapter number", fg='red', reset=True)
                    exit(404)

                if chapter_name:
                    if re.search(name_syntax, page, re.IGNORECASE): 
                        ch_name = str(re.search(name_syntax, page, re.IGNORECASE).group(1))
                    else:
                        click.secho("\nCouldn't find the chapter name", fg='red', reset=True)
                        exit(404)
                
                if not no_volume:
                    if re.search(v_syntax, page):
                        v = str(re.search(v_syntax, page).group(1))

                        if str(ch[1:].lstrip('0')) != '': # Vol.1 Ch.1
                            chapter = f"Vol.{v[1:].lstrip('0')} Ch.{ch[1:].lstrip('0')}"
                        else:
                            chapter = f"Vol.{v[1:].lstrip('0')} Ch.{ch[1:].lstrip('0') + 0}"
                    else:
                        click.secho("\nCouldn't find the volume number", fg='red', reset=True)
                        exit(404)
                else:
                    if str(ch[1:].lstrip('0')) != '': # Ch.1
                        chapter = f"Ch.{ch[1:].lstrip('0')}"
                    else:
                        chapter = f"Ch.{ch[1:].lstrip('0') + 0}"

                if chapter_name and ch_name:
                    chapter = f"{chapter} - {ch_name}"

                chapter_dir = os.path.join(volume, chapter)
                chapters.append(chapter_dir)
                if os.path.isdir(chapter_dir) == False:
                    os.mkdir(chapter_dir)
                shutil.copy2(os.path.join(volume, page), chapter_dir)
                
                if pg != None:
                    click.echo(f"{chapter} [{pg}]")
                else: 
                    click.echo(chapter)

    # Move chapter folders out of the volume folders
    for i in list(dict.fromkeys(chapters)):
        shutil.move(i, cwd)

    # Delete original directories
    if delete:
        if not yes:
            click.confirm(f"\nDo you want to continue? {len(volumes)} folders will be deleted from {os.path.basename(cwd)}.", abort=True)
        for i in volumes:
            click.echo(f"Delete: {i.split(cwd, 1)[1][1:]}")
            shutil.rmtree(i)
