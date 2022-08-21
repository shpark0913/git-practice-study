tall = []  # 난쟁이 키들의 리스트
strangers = []  # 가짜 난쟁이 키들의 리스트

for i in range(9):
    n = int(input())
    tall.append(n)
tall.sort()  # 모든 난쟁이들 키 순서대로 리스트

a = sum(tall) - 100  # 가짜 난쟁이 2명의 키의 합

for i in tall:  # 이 반복문에서 i, j의 키의 합이 a인 경우를 찾아 strangers에 넣음.
    for j in tall:  # 하지만 i + j == a 인 경우가 여러 경우일 수가 있다.
        if i + j == a:
            strangers.append(i)
            strangers.append(j)

tall.remove(strangers[0])  # 따라서 strangers 리스트의 1, 2번째 원소만
tall.remove(strangers[1])  # tall 리스트에서 제거

for i in range(len(tall)):
    print(tall[i])
