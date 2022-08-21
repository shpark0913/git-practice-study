N = int(input())

lst = list(map(int, input().split()))
ANS = []                               # stack 중 idx가 가장 큰 원소와 작은 원소의 차이
stack = [lst[0]]                       # idx 조절 위해 0번째 항 먼저 넣기

for i in range(1, N):
    if lst[i] > lst[i - 1]:
        stack.append(lst[i])             # 특정 항이 이전보다 크다면 stack에 추가
        ANS.append(stack[-1] - stack[0]) # ANS에 (stack에 추가된 원소 - 첫 항) 추가

    elif lst[i] <= lst[i - 1]:
        #ANS.append(stack[-1] - stack[0])
        stack = [lst[i]]                  # stack 초기화

print(max(ANS))