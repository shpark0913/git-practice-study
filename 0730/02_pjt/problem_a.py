import requests
 
 
def popular_count():
    pass 
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=3e6bef93583f44f23148ae1a83169eb1&language=en-US&page=1'
    response = requests.get(URL).json()
    a = response['results']
    b = len(a)
    return b


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
