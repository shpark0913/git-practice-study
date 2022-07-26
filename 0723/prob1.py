def max_score(scores):
    c = 0
    for score in scores:
        if score >= c:
            c = score
    return(c)



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
