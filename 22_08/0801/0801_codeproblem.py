# 10 개의 수를 입력 받아, 그 중 홀수만 더한 값은?
# 첫 줄에는 테스트 케이스의 개수 입력!


T = int(input())  # 테스트 케이스의 개수 입력
for i in range(1, T + 1):
    A = map(int,input().split()) # 각 테스트 케이스를 입력
    B = []
    for j in A:
        if j % 2 :
            B.append(j) 
        else :
            pass
        C = sum(B)
    print(f'#{i} {C}')