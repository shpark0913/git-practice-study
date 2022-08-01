import requests
from pprint import pprint

#https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=3e6bef93583f44f23148ae1a83169eb1&language=ko-KR
def credits(title):
 
    URL1 = f'https://api.themoviedb.org/3/search/movie?api_key=3e6bef93583f44f23148ae1a83169eb1&language=ko-KR&query={title}'
    response = requests.get(URL1).json()
    try:
        result1 = response.get('results')
        a = result1[0]
        movie_id =a.get('id')
    
        URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=3e6bef93583f44f23148ae1a83169eb1&language=ko-KR'
        recommendations =[]
        response2 = requests.get(URL2).json()

        result2 = response2.get('cast')
        a = []
        for i in result2:
            if i.get('cast_id') < 10 :
                a.append(i.get('name'))

        result3 = response2.get('crew')
        b = []
        for j in result3:
            if j.get('department') == 'Directing':
                b.append(j.get('name'))

        c = {}
        c['cast'] = a
        c['directing'] = b
        return c
                
    except:
        return None 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
