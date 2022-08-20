N = int(input())        # 배열의 크기
lst = []                # 연속한 자연수들의 개수를 elt로 갖는 리스트
                          # ex) 배열이 1, 2, 3, 5 -> lst = [3, 1]
s = set()               # 배열에 있는 원소들로 만들 집합

for n in range(N):
    elt = int(input())
    s.add(elt)          # 배열에 있는 원소들로 만든 집합

for i in s:
    sub_s = {i, i+1, i+2, i+3, i+4}
    if sub_s.issubset(s):
        lst.append(5)
    for j in range(1, 5):
        if len(s & sub_s) == j:
            lst.append(j)

for i in range(5, 0, -1):
    if i in lst:
        print(5-i)
        break           # break 안 걸면 for문이기 때문에 계속 print됨