import sys
sys.stdin = open("1934_최소공배수.txt")


T = int(input())

for t in range(T):
    A, B = map(int,input().split())
    C = max(A, B)
    D = min(A, B)
    E = max(A, B)
    while 1:
        if E % D == 0:
            print(E)
            break
        else:
            E += C



