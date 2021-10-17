import os
import subprocess


def archive(extension):
    cwd = os.getcwd()
    chapters = []
    print(f"\nFOLDER:\n{os.path.basename(cwd)} [{cwd}]\n")

    for path in os.listdir(cwd):
        full_path = os.path.join(cwd, path)
        if os.path.isdir(full_path):
            chapters.append(full_path)

    print("\nCHAPTERS:")
    for chapter in chapters:
        print(f"{os.path.basename(chapter)}")
        subprocess.call(f'"C:\\Program Files\\7-Zip\\7z.exe" a -tzip "{chapter}.{extension}" "{chapter}\\"')
                