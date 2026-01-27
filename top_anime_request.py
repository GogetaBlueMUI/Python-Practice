from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.jikan.moe/v4"
ALL_JSON = "/top/anime"
printer = PrettyPrinter()

data = get(BASE_URL + ALL_JSON).json()
anime = data['data']

def get_anime_titles(anime):
    all_anime_titles=[]
    for a in anime:
        all_anime_titles.append(a['title'])
    return all_anime_titles

def get_score(anime):
    all_anime_score=[]
    for a in anime:
        all_anime_score.append(a['score'])
    return all_anime_score
def get_studios(anime):
    all_anime_studios_names=[]
    for a in anime:
        for s in a['studios']:
            all_anime_studios_names.append(s['name'])
    return all_anime_studios_names
def get_myanimelist_url(anime):
    all_anime_myanimelist_url=[]
    for a in anime:
        all_anime_myanimelist_url.append(a['url'])
    return all_anime_myanimelist_url
def get_genres(anime):
    all_anime_genres=[]
    for a in anime:
        genre_list=[]
        for g in a['genres']:
            genre_list.append(g['name'])
        all_anime_genres.append(genre_list)
    return all_anime_genres
def print_all_anime(title,score,studio_name,url,genres):
    for i in range(len(title)):
        print(f"{i+1} Anime")
        print(title[i])
        print(score[i])
        print(studio_name[i])
        print(genres[i])
        print(url[i])
        print()
title = get_anime_titles(anime)
score = get_score(anime)
studio_name = get_studios(anime)
url = get_myanimelist_url(anime)
genre = get_genres(anime)


print_all_anime(title, score, studio_name, url, genre)






