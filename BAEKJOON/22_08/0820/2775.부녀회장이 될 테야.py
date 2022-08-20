T = int(input())

for t in range(T):
    apart = [[0]*14 for _ in range(15)] # 모든 집에 0명 배치
    k = int(input())
    n = int(input())
    for h in range(14):
        apart[14][h] = h+1
    for i in range(13,-1,-1):
        for j in range(14):
            apart[i][j] = sum(apart[i+1][:(j+1)])
    print(apart[14-k][n-1])