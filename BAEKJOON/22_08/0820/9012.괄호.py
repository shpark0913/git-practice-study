def VPS():
    stack = []
    lst = list(input())
    for i in range(len(lst)):
        if lst[i] == '(' and i < len(lst)-1:
            stack.append(lst[i])
        elif lst[i] == ')' and i > 0:
            if len(stack):
                if stack[-1] == '(':
                    stack.pop()
            else:
                return 'NO'
        elif lst[0] == ')' or lst[-1] == '(':
            return 'NO'

    if len(stack):
        return 'NO'
    else:
        return 'YES'

T = int(input())
for t in range(1, T+1):
    print(VPS())