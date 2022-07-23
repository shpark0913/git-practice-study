import json


def dec_movies(movies):
    pass 
    dic_sb = {}
    for movie in movies:
        i = movie['title']
        j = movie['id']
        specific = open(f'data/movies/{j}.json', encoding = 'utf-8')
        uu = json.load(specific)
        k = uu['release_date']
        dic_sb[f'{i}'] = k

        dic_gg = {}

        for gg, hh in dic_sb.items():
            if hh[5:7] == '12':
                dic_gg[f'{gg}'] = hh
    
    
    return(list(dic_gg.keys()))



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
