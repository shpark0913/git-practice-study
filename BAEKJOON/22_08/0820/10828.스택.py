N = int(input())

lst = [list(input().split()) for _ in range(N)]
stack = []
for elt in lst:
    if elt[0] == 'push':
        stack.append(elt[1])
    elif elt[0] == 'pop':
        if len(stack):
            a = stack.pop()
            print(a)
        else:
            print(-1)

    elif elt[0] == 'size':
        print(len(stack))

    elif elt[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif elt[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)