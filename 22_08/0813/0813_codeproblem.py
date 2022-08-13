def bi(N, key):
    page = [i+1 for i in range(N)]
    s = 1
    e = N
    n = 0
    while s <= e:
        n += 1
        m = int((s + e)/2)
        if page[m-1] == key:
            return n
        elif page[m-1] > key:
            e = m
        else:
            s = m

T = int(input())

for t in range(1, T+1):
    P, Pa, Pb = map(int,input().split())
    A_page = bi(P, Pa)
    B_page = bi(P, Pb)

    if A_page < B_page:
        print(f'#{t} A')
    elif A_page > B_page:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')