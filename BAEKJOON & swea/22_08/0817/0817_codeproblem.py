T = int(input())  # 테스트 케이스 개수


for t in range(1, T+1):
    N = int(input())  # 몇 줄 짜리 파스칼의 삼각형을 만들 것인가
    print(f'#{t}')
    lst = [list([0]*N) for _ in range(N)]
    for n in range(N):
        lst[n][0] = 1
        if n >= 1:
            lst[n][n] = 1
        if n >= 2:
            for j in range(1, N-1):
                lst[n][j] = lst[n-1][j-1] + lst[n-1][j]
    for i in lst:
        for j in i:
            if j != 0:
                print(j, end = ' ')
        print()