import sys
sys.stdin = open("14696_딱지놀이.txt")

# 별 : 4        /  동그라미 : 3     /  네모 : 2     /  세모 : 1
# A  : A가 승리  /  B : B가 승리    / D : 무승부

N = int(input())            # N 라운드 진행

for _ in range(N):
    about_A = list(map(int,input().split()))  # 1st elt : 모양의 수  /  그 이후 : 모양의 분포
    about_B = list(map(int,input().split()))  # 1st elt : 모양의 수  /  그 이후 : 모양의 분포
    about_A.pop(0) # 카드의 모양을 보기 위해
    about_B.pop(0) # 카드의 모양을 보기 위해
    status_A = [about_A.count(4), about_A.count(3), about_A.count(2), about_A.count(1)]
    status_B = [about_B.count(4), about_B.count(3), about_B.count(2), about_B.count(1)]

    if status_A[0] > status_B[0]:
        print('A')
    elif status_A[0] < status_B[0]:
        print('B')
    else:
        if status_A[1] > status_B[1]:
            print('A')
        elif status_A[1] < status_B[1]:
            print('B')
        else:
            if status_A[2] > status_B[2]:
                print('A')
            elif status_A[2] < status_B[2]:
                print('B')
            else:
                if status_A[3] > status_B[3]:
                    print('A')
                elif status_A[3] < status_B[3]:
                    print('B')
                else:
                    print('D')
