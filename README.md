# MangaTools <img style="float: left;" src="logo.png" width="120"/>


MangaTools is a cli tool to help you manage your digital manga.

## Features

* Search manga details and covers
* Organize volume pages to chapters
* Archive chapters to .cbz files.

## Installation


```sh
1. git clone https://github.com/Arrow420/manga-tools.git
2. cd eve
3. pip install .
4. mangatools [command]
```

## Usage
Below is a list of the currently support API command you can run.

* [`mangatools search <TITLE>`](#search) - Search details about manga from Mangadex.
* [`mangatools extract`](#extract)       - Extract pages from volumes and organize them to chapters.
* [`mangatools archive`](#archive)       - Archive chapters into .cbz files.


### Search
The search command uses mangadex to fetch details about manga and creates a details.json file for Tachiyomi.


```commandline
Usage: mangatools search [OPTIONS] TITLE

Options:
  --doujin      Shows manga with the doujin tag
  --no-covers   Doesn't download manga volume coverart
  --no-details  Doesn't create a details.json file
  --help        Show this message and exit.
```


### Extract
Blalawdwodjawdj owadojwalkndw kwdknkwajdkwajdjwalk  djlkwa manga ojdwjod ojwdojwdojwojowdwdwkndadanwdnawkdnwakn dkwakndwank wefeefe.


```commandline
Usage: mangatools extract [OPTIONS]

Options:
  --help  Show this message and exit.
```


### Archive
The archive command uses 7-zip to archive chapter folders into .cbz archives.


```commandline
Usage: mangatools archive [OPTIONS]

Options:
  --help  Show this message and exit.
```


## Contact

If you want to contact me you can reach me at <arrowsoftwaresolutions@gmail.com>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [MIT](<link>).
