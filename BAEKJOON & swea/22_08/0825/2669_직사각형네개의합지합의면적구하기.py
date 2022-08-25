import sys
sys.stdin = open("2669_직사각형네개의합집합의면적구하기.txt")

# 직사각형 : [좌측 하단 x좌표, y좌표,  우측 상단 x좌표, y좌표] 를 원소로 가지는 이중 배열
arr = [list(map(int,input().split())) for _ in range(4)]

area = 0

