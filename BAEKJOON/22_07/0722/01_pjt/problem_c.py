import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    data_c = []
    for movie in movies :
        data = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
        }
        genre_names = {}
        for i in genres:
            genre_names[i['id']] = i['name']

        change_name = []
        for j in data['genre_ids'] : 
            change_name.append(genre_names[j])

        data['genre_ids'] = change_name

        data_c.append(data)
    print(data_c)
    return data_c

    



        




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
