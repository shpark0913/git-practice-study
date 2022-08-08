T = int(input())   # T는 테스트 케이스의 개수

for i in range(1, T + 1):
    m, n = map(str,input().split())  # 띄어쓰기로 구분된 두 단어를 각각 m, n으로 할당
    m1 = sorted(m) # m1은 m이 정렬된 리스트
    n1 = sorted(n) # n1은 n이 정렬된 리스트
    if m1 == n1: # m1과 n1이 같다면, 애너그램
        print(f'{m} & {n} are anagrams.')
    else :
        print(f'{m} & {n} are NOT anagrams.')