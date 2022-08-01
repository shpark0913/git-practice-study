import requests
from pprint import pprint
 

def recommendation(title):

    URL1 = f'https://api.themoviedb.org/3/search/movie?api_key=3e6bef93583f44f23148ae1a83169eb1&language=ko-KR&query={title}'
    response = requests.get(URL1).json()
    try:
        result1 = response.get('results')
        a = result1[0]
        movie_id =a.get("id")
    
        URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=3e6bef93583f44f23148ae1a83169eb1&language=ko-KR'
        recommendations =[]
        response2 = requests.get(URL2).json()
        result2 = response2.get('results')
        a = []
        for i in result2:
            b = i.get('title')
            a.append(b)
        return a
    except:
        return None 




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
