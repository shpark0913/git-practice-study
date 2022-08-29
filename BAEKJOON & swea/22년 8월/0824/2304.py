import sys
sys.stdin = open("input2.txt")

N = int(input())

dic1 = dict((map(int,input().split())) for _ in range(N))       # 주어진 자료 dict으로 받고
dic2 = {}                                                       # key값 작은 순으로 나열
lst = []
for elt in dic1:
    lst.append(elt)
lst.sort()
for i in lst:
    dic2[i] = dic1[i]                                           # dic2는 key 값이 오름차순으로 정렬된 dictionary

lst_keys = []                                                   # dic2의 key만 모은 리스트
lst_values = []                                                 # dic2의 value만 모은 리스트
                                                                # 왜 이런 리스트 2개 만든 거냐면 딕셔너리 극혐이라서;;
for i in dic2.keys():
    lst_keys.append(i)
for i in dic2.values():
    lst_values.append(i)

area = 0                                                        # 영역 넓이를 area라는 변수에 할당
max_idx = lst_values.index(max(lst_values))                     # 높이가 가장 높은 지역의 idx(x좌표)
partial_idx = 0                                                 # max_idx 제외하고 계산과정동안의 최댓값(극댓값 느낌)
for idx in range(max_idx):
    if idx == 0:
        partial_idx = idx
        area += (lst_keys[max_idx] - lst_keys[partial_idx]) * (lst_values[partial_idx])
    elif lst_values[idx] > lst_values[partial_idx]:
        not_partial = partial_idx
        partial_idx = idx
        area += (lst_keys[max_idx] - lst_keys[partial_idx]) * (lst_values[partial_idx] - lst_values[not_partial])

partial_idx = len(lst_keys) - 1
for idx in range(len(lst_keys) - 1, max_idx - 1, -1):
    if idx == len(lst_keys) - 1:
        partial_idx = idx
        area += (lst_keys[partial_idx] - lst_keys[max_idx]) * (lst_values[partial_idx])
    elif lst_values[idx] > lst_values[partial_idx]:
        not_partial = partial_idx
        partial_idx = idx
        area += (lst_keys[partial_idx] - lst_keys[max_idx]) * (lst_values[partial_idx] - lst_values[not_partial])


'''
26 ~ 33은 높이가 가장 높은 영역 왼쪽의 넓이를 생각한 것
36 ~ 43은 높이가 가장 높은 영역 오른쪽 넓이를 생각한 것
51은 높이가 가장 높은 영역의 넓이를 생각한 것
'''
area += lst_values[max_idx]
print(area)
