import sys
sys.stdin = open("2635_수이어가기.txt")

N = int(input())

memo = [N]
max_cnt = 0
max_case = []

for i in range(N//2, N+1):
    if i == 1:
        max_cnt = 4
        max_case = [1, 1, 0, 1]
    elif i != 1:
        memo.append(i)
        while 1:
            alpha = memo[-2] - memo[-1]
            if alpha >= 0:
                memo.append(alpha)
            else:
                break
        if len(memo) >= max_cnt:
            max_cnt = len(memo)
            max_case = memo
        memo = [N]
print(max_cnt)
print(*max_case)