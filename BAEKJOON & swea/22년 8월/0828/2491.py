import sys
sys.stdin = open("input_2491.txt")

N = int(input())
arr = list(map(int,input().split()))

max_cnt = 0
for i in range(N-1):
    cnt = 0
    if arr[i] < arr[i+1]:
        while arr[i] <= arr[i+1]:
            if i < N-1:
                i += 1
                cnt += 1
            else:
                cnt += 1
                break
        if max_cnt < cnt:
            max_cnt = cnt
    elif arr[i] > arr[i+1]:
        while arr[i] >= arr[i+1]:
            if i < N-1:
                i += 1
                cnt += 1
            else:
                cnt += 1
                break
    elif arr[i] == arr[i+1]:
        while arr[i] == arr[i+1]:
            if i < N-1:
                i += 1
                cnt += 1
            else:
                cnt += 1
                break
        if arr[i] < arr[i+1]:
            while arr[i] <= arr[i+1]:
                if i < N - 1:
                    i += 1
                    cnt += 1
                else:
                    cnt += 1
                    break
            if max_cnt < cnt:
                max_cnt = cnt
        if arr[i] > arr[i+1]:
            while arr[i] >= arr[i+1]:
                if i < N - 1:
                    i += 1
                    cnt += 1
                else:
                    cnt += 1
                    break
            if max_cnt < cnt:
                max_cnt = cnt

print(max_cnt)




