import sys
sys.stdin = open("2605_줄세우기.txt")

N = int(input())
arr = list(map(int,input().split()))
lst = [1]               # 1번 학생은 처음에 그냥 혼자 줄 서니깐 초기 list를 [1]로 설정

for i in range(1, N):   # i+1을 lst에 대입해야 함! index가 1인 학생은 2번째 학생이므로.
    if arr[i] != 0:     # 0을 제외한 번호를 뽑은 학생들을 list의 알맞은 위치에 서게 한다.
        lst.insert(-1*(arr[i]), i+1)
    elif arr[i] == 0:   # 0을 뽑은 학생은 list 맨 뒤에 서게 한다.
        lst += [i+1]
print(*lst)             # * 만든 사람은 진짜 똑똑한 듯 하다!