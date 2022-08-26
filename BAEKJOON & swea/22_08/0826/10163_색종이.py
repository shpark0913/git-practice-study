import sys
sys.stdin = open("10163_색종이.txt")

N = int(input())        # 색종이 몇 장일까? N 장이지~

canvas = [[0]*1001 for _ in range(1001)]
c = 1
for _ in range(N):
    x, y, delta_x, delta_y = map(int,input().split())
    for i in range(x, x + delta_x):
        for j in range(y, y + delta_y):
            canvas[i][j] = c
    c += 1

canvas2 = []
for i in range(1001):
    for j in range(1001):
        canvas2.append(canvas[i][j])

for i in range(1, N+1):
    print(canvas2.count(i))
# from pprint import pprint
# pprint(canvas)
