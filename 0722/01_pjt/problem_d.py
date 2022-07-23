import json


def max_revenue(movies):
    dic_sb = {}
    for movie in movies:
        i = movie['title']
        j = movie['id']
        specific = open(f'data/movies/{j}.json', encoding = 'utf-8')
        uu = json.load(specific)
        k = uu['revenue']
        dic_sb[f'{i}'] = k
    maximum = max(dic_sb, key=dic_sb.get)
    return maximum

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
