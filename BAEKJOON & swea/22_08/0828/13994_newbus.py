import sys
sys.stdin = open("13994_newbus.txt")

T = int(input())

for t in range(1, T+1):
    stations = [0] * 1001
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]  #elt : / 1일반 2급행 3광역급행  /  출발 정류장  /  종점 정류장 /

    for elt in arr:
        if elt[0] == 1:
            for i in range(elt[1], elt[2]+1):
                stations[i] += 1

        elif elt[0] == 2:
            if elt[1] % 2:   # 출발 정류장 홀수일 때
                for i in range(elt[1], elt[2]+1, 2):
                    stations[i] += 1
            else:            # 출발 정류장 짝수일 때
                for i in range(elt[1], elt[2]+1, 2):
                    stations[i] += 1

        elif elt[0] == 3:
            if elt[1] % 2:   # 출발 정류장 홀수일 때
                for i in range(elt[1], elt[2]+1):
                    if i % 3 == 0 and i % 10 != 0:
                        stations[i] += 1

            else:               # 출발 정류장 짝수일 때
                if elt[1] % 4:  # 4의 배수 아닐 때
                    for i in range(elt[1]+2, elt[2]+1, 4):
                        stations[i] += 1
                else:           # 4의 배수일 때
                    for i in range(elt[1], elt[2]+1, 4):
                        stations[i] += 1

        if stations[elt[2]] == 0:
            stations[elt[2]] = 1


    max_count = max(stations)

    print(f'#{t} {max_count}')