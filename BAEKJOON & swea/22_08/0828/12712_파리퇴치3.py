import sys
sys.stdin = open("12712_파리퇴치3.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [[0] * (2*M+N-2) for _ in range(M-1)]
    arr += [[0]*(M-1) + list(map(int,input().split())) + [0]*(M-1) for _ in range(N)]
    arr += [[0] * (2*M+N-2) for _ in range(M-1)]

    max_constant = 0
    for i in range(M-1,M+N-1):                         # 십자가
        for j in range(M-1,M+N-1):                     # 파리채 중앙이 될 수 있는 인덱스가 M-1 부터 N-M 이다!
            constant = -arr[i][j]                      # 십자가 모양 카운트할 때 중앙은 중복되므로 하나 제외
            for alpha in range(-M+1, M):               # 중앙 기준으로 상하좌우 친구들 더해줌
                constant += arr[i+alpha][j]
                constant += arr[i][j+alpha]
            if constant > max_constant:                # max_constant보다 constant가 크면 최신화
                max_constant = constant
    for i in range(M-1,M+N-1):                         # 크로스
        for j in range(M-1,M+N-1):
            constant = -arr[i][j]
            for alpha in range(-M+1, M):
                constant += arr[i+alpha][j+alpha]
                constant += arr[i+alpha][j-alpha]
            if constant > max_constant:
                max_constant = constant

    print(f'#{t} {max_constant}')