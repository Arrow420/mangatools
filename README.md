# MangaTools

MangaTools is a cli tool that helps you organize your digital manga

<img float="left" src=".github/readme-images/logo.png" alt="" width="80"/>


## Features

* Search manga details and covers
* Organize pages from volumes into chapters
* Archive chapters to .cbz files

## Installation

```sh
pip install mangatools
```
or

```sh
git clone https://github.com/arrow420/mangatools.git
cd mangatools
pip install .
mangatools [command]
```

## Usage
Below is a list of all the currently available commands that you can run.

* [`mangatools search <TITLE>`](#search) - Search details about manga from Mangadex
* [`mangatools extract`](#extract)       - Extract pages from volumes and organize them into chapters
* [`mangatools archive`](#archive)       - Archive chapters into .cbz files


### Search
The `search` command uses Mangadex to fetch details and creates a details.json file for Tachiyomi.


```commandline
Usage: mangatools search [OPTIONS] TITLE

Options:
  --doujin                      Shows only doujins
  -c, --cover [first|last|all]  Downloads cover art
  -d, --details                 Creates a details.json file
  --help                        Show this message and exit.
```


### Extract
The `extract` command extracts and organizes pages from volumes into chapters.

Examples of supported file naming schemes:
* Title - c001 (v01) - p001
* Title - c001 (v01) - p001-p002
* Title - c001x5 (v01) - p001
* Title - c001.5 (v01) - p001
* Title - c001 (v01) - p001 [Digital] [Chapter Name] [Source] [Group]
* Title - c001 (v01) - p001 [Cover] [Dig] [Chapter Name] [Source] [Group]
* Title - c001 (v01) - p001 [ToC] [digital-hd] [Chapter Name] [Source] [Group]


```commandline
Usage: mangatools extract [OPTIONS]

Options:
  --no-volume / --volume  Include the volume number in the folder name
  -n, --name              Include the name of the chapter in the folder name
  --delete, --del         Delete the original files after extracting
  -y, --yes               Assume yes on all queries
  --help                  Show this message and exit.
```


### Archive
The `archive` command archives chapters into .cbz files using 7-Zip. (make sure you have 7-Zip installed)


```commandline
Usage: mangatools archive [OPTIONS]

Options:
  -e, --extension [CBZ|ZIP]       Archive file extension  [default: CBZ]
  -mx, --compression [0|1|3|5|7|9]
                                  Archive compression level  [default: 5]
  --delete, --del                 Delete the original files after archiving
  -y, --yes                       Assume yes on all queries
  --help                          Show this message and exit.
```


## Contact
If you want to contact me you can reach me at <arrowsoftwaresolutions@gmail.com>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [MIT](<https://choosealicense.com/licenses/mit/>).

```
Copyright (c) 2021 Arrow

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```