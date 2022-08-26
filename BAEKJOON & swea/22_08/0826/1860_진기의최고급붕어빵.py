import sys
sys.stdin = open("1860_진기의최고급붕어빵.txt")

'''
T = int(input())
 
for t in range(1, T+1):
    N, M, K = map(int,input().split())
    p = list(map(int,input().split()))
    result = 'Possible'
    p.sort()
 
    for i in range(N):
        if p[i] // M * K - i > 0:
            result
        else:
            result = 'Impossible'
            break
 
    print(f'#{t} {result}')
'''