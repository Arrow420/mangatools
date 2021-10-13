import os
import re
import shutil


def extract():
    
    cwd = os.getcwd()

    volumes = []
    chapters = []

    pg_syntax = "(p\d\d\d(?:[^\s]+)?)"
    ch_syntax = "(c\d\d\d(?:[^\s]+)?)"
    v_syntax = "(v\d\d)"

    num = 0

    print("\nVOLUMES:")

    for path in os.listdir(cwd):
        full_path = os.path.join(cwd, path)
        if os.path.isdir(full_path):
            print(path)
            volumes.append(full_path)

    for volume in volumes:
        num += 1
        print("\nVOLUME " + str(num) + ":")
        for page in os.listdir(volume):
            if os.path.isdir(page) == False:
                pg = str(re.findall(pg_syntax, page)[0])
                ch = str(re.findall(ch_syntax, page)[0])
                v = str(re.findall(v_syntax, page)[0])
                if str(ch[1:].lstrip('0')) != '':
                    chapter = "Vol." + str(v[1:].lstrip('0')) + " " + "Ch." + str(ch[1:].lstrip('0'))
                else:
                    chapter = "Vol." + str(v[1:].lstrip('0')) + " " + "Ch." + str(ch[1:].lstrip('0')) + "0"
                chapter_dir = os.path.join(volume, chapter)
                chapters.append(chapter_dir)
                if os.path.isdir(chapter_dir) == False:
                    os.mkdir(chapter_dir)
                shutil.copy2(os.path.join(volume, page), chapter_dir)
                print(chapter + " [" + pg + "]")
        
    # Move chapter folders out of the volume folders
    for i in list(dict.fromkeys(chapters)):
        shutil.move(i, cwd)
