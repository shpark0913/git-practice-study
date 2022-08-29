T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(input().split())

    if len(arr) % 2:
        arr1 = arr[:(len(arr)-1)//2 + 1]
        arr2 = arr[(len(arr)-1)//2 +1:]

        hello = []

        for i in range(len(arr2)):
            hello.append(arr1[i])
            hello.append(arr2[i])
        hello.append(arr1[-1])

    else:
        arr1 = arr[:(len(arr)+1)//2]
        arr2 = arr[(len(arr)+1)//2:]

        hello = []

        for i in range(len(arr1)):
            hello.append(arr1[i])
            hello.append(arr2[i])

    print(f'#{t}', *hello)