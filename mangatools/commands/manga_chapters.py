import click
import json
import requests
from natsort import natsorted


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=1)
    print(text)


def searchManga(idmanga):

    response = requests.get(f"https://api.mangadex.org/manga/{idmanga}/feed?translatedLanguage[]=en&offset=0&limit=100&order[chapter]=asc").json()
    

    if response["total"] != 0:
        click.echo("Swag")
    else:
        click.secho("\nCouldn't find any results", fg='red', reset=True)
        exit(404)
    
    return response

def getInfo(response):
    data = response['data']
    chapters = []
    for i in data:
        if i['type'] == "chapter":
            chapter = str(i['attributes']['title'])
            chapter_num = str(i['attributes']['chapter'])
            ch_tuple = (str(chapter_num), str(chapter))
            if not any(ch[0] == str(chapter_num) for ch in chapters):
                chapters.append(ch_tuple)
    
    click.echo("\n\nChapters:\n")

    for i in natsorted(chapters):
        print(f"Ch.{i[0]}: {i[1]}")

if __name__ == '__main__':
    getInfo(searchManga("a77742b1-befd-49a4-bff5-1ad4e6b0ef7b"))