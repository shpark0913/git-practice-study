import sys
sys.stdin = open("2669_직사각형네개의합집합의면적구하기.txt")

canvas = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if canvas[i][j] == 1:
                continue
            canvas[i][j] = 1
            cnt += 1
print(cnt)