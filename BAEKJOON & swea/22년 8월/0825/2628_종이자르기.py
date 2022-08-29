import sys
sys.stdin = open("2628_종이자르기.txt")

garo , sero = map(int,input().split())            # 전체 종이의 가로와 세로

num_slice = int(input())                          # 칼로 잘라야 하는 점선의 개수

for i in range(num_slice):
    garo_num, sero_num = map(int,input().split()) # 가로, 세로로 자르는 점선의 번호