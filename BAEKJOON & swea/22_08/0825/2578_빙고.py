import sys
sys.stdin = open("2578_빙고.txt")

bingo = [list(map(int,input().split())) for _ in range(5)]  # 빙고
nums = [list(map(int,input().split())) for _ in range(5)]   # 사회자가 부르는 숫자

numsnums = []  # 12개

for elt in bingo:
    numsnums.append(elt)

for j in range(len(bingo)):
    lsttt = []
    for i in range(len(bingo)):
        lsttt.append(bingo[i][j])
    numsnums.append(lsttt)

ans_set = set()                                                          # 사회자가 현재까지 부른 숫자들의 집합

lst_left_diagonal = []
lst_right_diagonal = []
for i in range(len(bingo)):
    lst_left_diagonal.append(bingo[i][i])

for i in range(len(bingo)):
    lst_right_diagonal.append(bingo[i][len(bingo) - i - 1])

numsnums.append(lst_left_diagonal)
numsnums.append(lst_right_diagonal)

lstt = []
for i in range(5):
    for j in range(5):
        cnt = 0
        num = nums[i][j]
        ans_set.add(num)                                    # 사회자가 현재까지 부른 숫자들을 집합으로.
        for elt in numsnums:
            if ans_set.issuperset(set(elt)):
                cnt += 1
                if cnt == 3:
                    lstt.append(len(ans_set))
print(lstt[0])