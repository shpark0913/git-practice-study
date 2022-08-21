N = int(input())

for n in range(N):
    s = list(input().split())           # 공백 기준 문자열 자르고 리스트로
    s = s[::-1]                         # 거꾸로
    print(f'Case #{n+1}: ', end='')     # 삽
    for i in range(len(s)):             # 투
        print(f'{s[i]} ', end = '')     # 더
    print()                             # 질