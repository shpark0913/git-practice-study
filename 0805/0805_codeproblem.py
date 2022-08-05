n = int(input())

for i in range(1, n+1):
    P, Q, R, S, W = map(int,input().split())
    print(f'#{i} ', end='')
    a = P * W
    if R >= W:
        if a >= Q:
            print(Q)
        else:
            print(a)
    elif R < W:
        b = Q + S*(W-R)
        if a >= b:
            print(b)
        else:
            print(a)