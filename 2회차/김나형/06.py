import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.
    # id키를 이용하여 value값 불러오기
    # id == movies'genre_ids'면 movie name에 name 값을 불러오기

    
    for m in movies:
        for movie_id in m['genre_ids']:
            movie_list = []
            
            for genre in genres:
                if genre['id'] in movie_id:
                    movie_list.append(genre['name'])
            result = {
            'genre_ids': movie_list,
            'id': m.get('id'),
            'overview': m.get('overview'),
            'title': m.get('title'),
            'vote_average': m.get('vote_average')
            }
    return result
               

    # movie_info_list = []

    # for m in movies: # movies에 있는 딕셔너리를 하나씩 m에 삽입
    #     genre_ids = m['genre_ids'] # m  genre_ids에 1개의 딕셔너리의 'genre_ids' value 값 저장
    #     genre_names = [] # genre_names 리스트 변수

    #     for genre in genres: # genres에 genre
    #         if genre['id'] in genre_ids:
    #             genre_names.append(genre['name'])



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))