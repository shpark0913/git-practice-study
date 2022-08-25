import sys
sys.stdin = open("2605_줄세우기.txt")

N = int(input())
arr = list(map(int,input().split()))
lst = [1]

for i in range(1, N):   # i+1을 lst에 대입해야 함! index가 1인 학생은 2번째 학생이므로.
    lst.insert(-1*arr[i], i+1)
print(*lst)