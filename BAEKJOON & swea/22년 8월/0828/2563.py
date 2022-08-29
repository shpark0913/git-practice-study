import sys
sys.stdin = open("2563.txt")

N = int(input())

canvas = [[0] * 100 for _ in range(100)]

arr = [list(map(int,input().split())) for _ in range(N)]

for elt in arr:
    a, b = elt[0], elt[1]
    for i in range(10):
        for j in range(10):
            canvas[a+i][b+j] = 1
lst = []
for elt in canvas:
    for e in elt:
        lst.append(e)

print(lst.count(1))