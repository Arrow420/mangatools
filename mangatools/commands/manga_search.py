import requests
import json
import os
import click


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=1)
    print(text)

def getTitleLang(Titledict):
    langList = ["en", "ja", "ko", "zh"] # determine which langauge to use for title, prefers english, japanese, korean or chinese respectively
    
    if any([i in Titledict for i in langList]): # check if the title is available in aforementioned languages
        for lang in Titledict:
            if lang in langList:
                title = Titledict[lang]
                return title
    else:
        title = list(Titledict.values())[0]
        return title


def searchManga(title, doujin):
    
    if doujin:
        excluded_tags = []
        included_tags = ["b13b2a48-c720-44a9-9c77-39c9979373fb", "7b2ce280-79ef-4c09-9b58-12b7c23a9b78"] # include doujins and fan colored
    else: 
        excluded_tags = ["b13b2a48-c720-44a9-9c77-39c9979373fb", "7b2ce280-79ef-4c09-9b58-12b7c23a9b78"] # exclude both colored and doujins
        included_tags = []

    params = {
        "title": title,
        "order[relevance]": "desc",
        "excludedTags[]": excluded_tags,
        "includedTags[]": included_tags,
        "includedTagsMode": "OR"
    }
    response = requests.get("https://api.mangadex.org/manga", params=params).json()
    
    if response["total"] != 0:
        click.echo(getTitleLang(response['data'][0]['attributes']['title']))
    else:
        click.secho("\nCouldn't find any results", fg='red', reset=True)
        exit(404)
    
    return response


def getInfo(response, cover, details):
    data = response['data'][0]
    manga_id = data['id']
    title = getTitleLang(data['attributes']['title'])
    author = getAuthor(data['relationships'][0]['id'])
    artist = getArtist(data['relationships'][1]['id'])
    description = str(data['attributes']['description']['en']).split("[", 1)[0].rstrip().split("\\", 1)[0].rstrip().split("---", 1)[0].rstrip().split("**", 1)[0].rstrip()
    demographic = data['attributes']['publicationDemographic']
    country_of_origin = data['type']
    tags = []
    for i in data['attributes']['tags']:
        tag = str(i['attributes']['name']['en'])
        tags.append(tag)
    
    if demographic != None:
        tags.append(demographic.title())
    
    if country_of_origin != None:
        tags.append(country_of_origin.title())
    
    status = data['attributes']['status']

    click.echo("\nDETAILS:\n")
    click.echo(f"Title: {title} \nAuthor: {author} \nArtist: {artist} \nDescription: {description} \n\nGenres: \n{tags} \n\nStatus: {status.title()}")
    click.echo(f"\n\nId: {manga_id} \n")
    
    if cover:
        click.echo("\nCOVERS:\n")
        getCover(manga_id, cover)

    if details:
        saveDetails(title, author, artist, description, tags, status)
    
    return manga_id


def getAuthor(id):
    url = "https://api.mangadex.org/author/" + id
    response = requests.get(url=url).json()
    author = response['data']['attributes']['name']
    return author


def getArtist(id):
    url = "https://api.mangadex.org/author/" + id
    response = requests.get(url=url).json()
    artist = response['data']['attributes']['name']
    return artist


def getCover(id, cover):
    if cover == 'last':
        cover_order = 'desc'
    else: 
        cover_order = 'asc'
    
    params = {
        "manga[]": id,
        "order[volume]": cover_order,
        "limit": 100,
    }
    response = requests.get("https://api.mangadex.org/cover", params=params).json()
    cwd = os.getcwd()
    cover_folder = os.path.join(cwd, "volume_covers")
    if cover == 'all':
        if os.path.isdir(cover_folder) == False:
            os.mkdir(cover_folder)
    else:
        cover_folder = cwd
    
    for i in response['data']:
        cover_filename = i['attributes']['fileName']
        volume = i['attributes']['volume']
        if volume != None:
            click.echo(f"Volume {volume}: {cover_filename}")
            saveCover(volume, cover_filename, id, cover_folder)
            if cover == 'first' or cover == 'last':
                break


def saveCover(volume, filename, id, folder):
    url = "https://uploads.mangadex.org/covers/" + id + "/" + filename
    response = requests.get(url=url)
    cover = os.path.join(folder, "cover" + volume) + ".jpg"
    file = open(cover, "wb")
    file.write(response.content)
    file.close()
    
def saveDetails(title, author, artist, description, tags, status):
    status_dict = {
        "ongoing": 1,
        "completed": 2,
        "hiatus": 0,
        "cancelled": 0
    }

    details_dict = {
        "title": title,
        "author": author,
        "artist": artist,
        "description": description,
        "genre": tags,
        "status": int(status_dict[status]),
        "_status values": ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed"]
    }
    
    with open('details.json', 'w') as json_file:
        json.dump(details_dict, json_file, indent=2, ensure_ascii=False)
    