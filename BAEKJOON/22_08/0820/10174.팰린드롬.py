n = int(input())  # 테스트 케이스 개수

for i in range(1, n+1):
    A = input()
    A = A.lower()
    B = A[::-1]
    if A == B:
        print('Yes')
    else:
        print('No')