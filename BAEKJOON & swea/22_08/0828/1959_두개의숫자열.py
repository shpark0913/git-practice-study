import sys
sys.stdin = open("1959_두개의숫자열.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())   # N : A의 길이  /  M : B의 길이
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    max_constant = 0
    if N == M:
        constant = 0
        for i in range(N):
            constant += A[i]*B[i]
        if constant > max_constant:
            max_constant = constant
    elif N > M:
        for i in range(N-M+1):
            constant = 0
            for j in range(M):
                constant += A[i+j]*B[j]
            if constant > max_constant:
                max_constant = constant
    elif N < M:
        for i in range(M-N+1):
            constant = 0
            for j in range(N):
                constant += A[j]*B[i+j]
            if constant > max_constant:
                max_constant = constant
    print(f'#{t} {max_constant}')