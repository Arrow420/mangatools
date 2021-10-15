import requests
import json
import os


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=1)
    print(text)

def searchManga(title, doujin):
    
    if doujin:
        excluded_tags = []
        included_tags = ["b13b2a48-c720-44a9-9c77-39c9979373fb"] # include doujins
    else: 
        excluded_tags = ["b13b2a48-c720-44a9-9c77-39c9979373fb", "320831a8-4026-470b-94f6-8353740e6f04"] # exclude both colored and doujins
        included_tags = []

    params = {
        "title": title,
        "order[relevance]": "desc",
        "excludedTags[]": excluded_tags,
        "includedTags[]": included_tags
    }
    response = requests.get("https://api.mangadex.org/manga", params=params).json()
    print(response['data'][0]['attributes']['title']['en'])
    return response


def getInfo(response, covers, details):
    data = response['data'][0]
    manga_id = data['id']
    title = data['attributes']['title']['en']
    author = getAuthor(data['relationships'][0]['id'].strip('"'))
    artist = getArtist(data['relationships'][1]['id'].strip('"'))
    description = str(data['attributes']['description']['en']).split("[", 1)[0].rstrip().split("\\", 1)[0].rstrip().split("---", 1)[0].rstrip()
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

    print("\nDETAILS:\n")
    print("Title: " + title +"\nAuthor: " + author +"\nArtist: " + artist + "\nDescription: " + description + "\n\nGenres: \n" + str(tags) + "\n\nStatus: " + status.title())
    print("\n\nId: " + manga_id + "\n")
    
    if covers:
        getCover(manga_id)

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


def getCover(id):
    params = {
        "manga[]": id,
        "order[volume]": "asc",
        "limit": 100,
    }
    response = requests.get("https://api.mangadex.org/cover", params=params).json()
    cwd = os.getcwd()
    cover_folder = os.path.join(cwd, "mangadex-covers")
    if os.path.isdir(cover_folder) == False:
        os.mkdir(cover_folder)
    
    for i in response['data']:
        cover_filename = i['attributes']['fileName']
        volume = i['attributes']['volume']
        if volume != None:
            print("Volume " + volume + ": " + cover_filename)
            saveCover(volume, cover_filename, id, cover_folder)


def saveCover(volume, filename, id, folder):
    url = "https://uploads.mangadex.org/covers/" + id + "/" + filename
    response = requests.get(url=url)
    cover = os.path.join(folder, "cover" + volume) + ".jpg"
    file = open(cover, "wb")
    file.write(response.content)
    file.close()
    
def saveDetails(title, author, artist, description, tags, status):
    if os.path.isfile("details.json") == False:
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
            json.dump(details_dict, json_file, indent=1, ensure_ascii=False)
    
    else: print("\n'details.json' already exists")


if __name__ == "__main__":
    print("Welcome to Manga Tools\n")
    title = input("Enter a Mangadex title: ")
    getInfo(searchManga(title, False, True, True))

