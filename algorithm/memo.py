S = input()
T = ''
for i in range(len(S)):
    T += S[len(S) - 1 - i]

print(T)




############교수님#############
s = 'Reverse this strings'
ans =''
for char in s:
    ans = char + ans
    # 파이썬에서 ans += char 의 모양이 윗 줄 처럼 반영된다!
print(ans)




############교수님#############
== : 값
is : 메모리 주소




############교수님############# 교재 29쪽
atoi => 문자열을 숫자로
itoa => 숫자를 문자열로
(단, 자연수 => 정수)

print(chr(x + ord('0'))) : 숫자 x 를 str으로

def itoa(num):
    if num == 0:
        return 0

    is_positive = True
    if num<0:
        is_positive = False
        num = -num
    ans = ''
    while num:
        num, remainder = divmod(num, 10) # divmod : 몫과 나머지
        chr(remainder + ord('0'))  # 한글자짜리 숫자(문자열인)
        ans = chr(remainder + ord('0')) + ans
    if is_positive:
        return ans
    else:
        return '-'+ans




############교수님#############(패턴 매칭 다른 코드) 교재 p.37
t = 'this is book'
p = 'is'
# i : t의 idx / j : p의 idx
def func(t, p):
    for i in range(len(t) - len(p) + 1):
        for j in range(len(p)):
            if t[i + j] != p[j]:
                break
        else :
            return i
    return -1

# 충격적 사실 : pattern in text를 하면 된다!

pythonic하게!

def func(text, pattern):
    m = len(pattern)
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i+m] == pattern :
            break
        else :
            return i
    return -1




############교수님#############