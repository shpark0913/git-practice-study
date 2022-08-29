import sys
sys.stdin = open("input2.txt")

N = int(input())                                        # 스위치 개수

arr1 = list(map(int,input().split()))                   # 스위치 현재 상태

N_student = int(input())                                # 학생의 수

for _ in range(N_student):
    s, n = map(int,input().split())
    if s == 1:
        for i in range(n - 1, N, n):
            arr1[i] = 0 if arr1[i] else 1
    elif s == 2:
        n -= 1
        arr1[n] = abs(arr1[n] - 1)
        start = n - 1
        end = n + 1
        while start > -1 and end < N:
            if arr1[start] == arr1[end]:
                arr1[start] = abs(arr1[start] - 1)
                arr1[end] = abs(arr1[end] - 1)
                start -= 1
                end += 1
            else:
                break


for i in range(0, N, 20):
    print(*arr1[i:i+10])