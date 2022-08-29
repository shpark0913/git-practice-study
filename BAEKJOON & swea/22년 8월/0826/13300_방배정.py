import sys
sys.stdin = open("13300_방배정.txt")

N, K = map(int,input().split())       # N : 총 학생 수  /  K : 한 방의 최대 인원 수

boys = []
girls = []
boys_dic = {}
girls_dic = {}
for _ in range(N):
    S, Y = map(int,input().split())   # S : 성별 (0 : 여, 1 : 남)  /  Y : 학년
    if S == 0:                        # 여기부터
        girls.append(Y)
    else:
        boys.append(Y)                #삽

for i in range(1, 7):
    nums = 0
    for elt in girls:                 #질
        if elt == i:
            nums += 1
    girls_dic[i] = nums

for i in range(1, 7):                 #중 (좀 돌아서 풀음. 수정은 귀찮!)
    nums = 0
    for elt in boys:
        if elt == i:
            nums += 1
    boys_dic[i] = nums                # 여기까지 성별과 학년에 따른 딕셔너리 만들었!

room_num = 0
for elt in girls_dic.values():        # 여학생 기준 최대 방 배정 인원수에 따라 필요 방 개수 계산
    if 0 < elt <= K:
        room_num += 1
    else:
        room_num += ((elt//2) + (elt%2))

for elt in boys_dic.values():         # 남학생 기준 최대 방 배정 인원수에 따라 필요 방 개수 계산
    if 0 < elt <= K:
        room_num += 1
    else:
        room_num += ((elt//2) + (elt%2))

print(room_num)