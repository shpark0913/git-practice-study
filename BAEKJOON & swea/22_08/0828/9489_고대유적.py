import sys
sys.stdin = open("9489_고대유적.txt")

T = int(input())   # 사진 데이터의 개수

for t in range(1, T+1):
    N, M = map(int,input().split())

    arr = [[0] * (M+2)]
    arr += [[0] + list(map(int,input().split())) + [0] for _ in range(N)]
    arr += [[0] * (M+2)]
    max_cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            cnt = 0
            if arr[i][j] == 1:
                while arr[i][j] == 1:
                    cnt += 1
                    j += 1
            if max_cnt < cnt:
                max_cnt = cnt
    for j in range(1, M+1):
        for i in range(1, N+1):
            cnt = 0
            if arr[i][j] == 1:
                while arr[i][j] == 1:
                    cnt += 1
                    i += 1
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{t} {max_cnt}')