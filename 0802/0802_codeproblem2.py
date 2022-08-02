# 1부터 n까지 369게임 규칙 적용
# 3, 9 같은 경우는 -   /   33 같은 경우는 -- 으로 표시

n = int(input())

for i in range(1, n+1):
    a = []
    I = str(i)
    for j in I:
        if j == '3':
            a.append(int(j))
        elif j == '6':
            a.append(int(j))
        elif j == '9':
            a.append(int(j))
    if len(a) == 0:
        print(f'{i} ', end = '')
    elif len(a) == 1:
        print('- ', end = '')
    elif len(a) == 2:
        print('-- ', end = '')
