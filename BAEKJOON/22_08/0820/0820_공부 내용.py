# 버블 정렬 (Bubble Sort)

# 정렬 과정
# 1st 원소부터 인접한 원소끼리 계속 자리를 교환하며 맨 마지막 자리까지 이동한다.
# 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
# 교환하며 자리를 이동하는 못브이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 한다.

# PseudoCode
BubbleSort(a, N)                # a : 정렬할 배열    //    N : 배열의 크기
    for i : N-1 -> 1            # 정렬될 구간의 끝
        for j : 0 -> i-1        # 비교할 원소 중 왼쪽 원소의 idx
            if a[j] > a[i]      # 왼쪽 원소가 더 크면
                a[j] <-> a[i]   # 오른쪽 원소와 교환

# Code
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]





# 카운팅 정렬 (Counting Sort)
#  : 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
# 제한 사항:
#    1. 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능. (각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스되는
#                                                       카운트들의 배열을 사용하기 때문이다.)
#    2. 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.

# [0, 4, 1, 3, 1, 2, 4, 1] 카운팅 정렬 가즈아-----!!!!!
# 1단계 : Data에서 각 항목들의 발생 횟수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장한다.
# counts = [0]*5    //    Data의 최소 원소 : 0, 최대 원소 : 4 이므로 총 5개의 숫자 존재
# counts = [1, 3, 1, 1, 2]   //  ex) counts[i]는 i가 Data에 몇 번 있었나 센 것.(i의 발생 횟수)
# counts = [1, 4, 5, 6, 8]   //  elt들을 누적으로 바꿈
# Temp = [0]*8    //    Data들을 재배열할 list.

# counts[1] 하나 감소시키고 Temp에 1을 삽입한다.
# Data = [0, 4, 1, 3, 1, 2, 4, 0]
#   -> counts = [1, 3, 5, 6, 8]
#   -> Temp = [0, 0, 0, 1, 0, 0, 0, 0]

# counts[4] 하나 감소시키고 Temp에 4를 삽입한다.
# Data = [0, 4, 1, 3, 1, 2, 0, 0]
#   -> counts = [1, 3, 5, 6, 7]
#   -> Temp = [0, 0, 0, 1, 0, 0, 0, 4]

# counts[2] 하나 감소시키고 Temp에 2를 삽입한다.
# Data = [0, 4, 1, 3, 1, 0, 0, 0]
#   -> counts = [1, 3, 4, 6, 7]
#   -> Temp = [0, 0, 0, 1, 2, 0, 0, 4]

# counts[1] 하나 감소시키고 Temp에 1을 삽입한다.
# Data = [0, 4, 1, 3, 0, 0, 0, 0]
#   -> counts = [1, 2, 4, 6, 7]
#   -> Temp = [0, 0, 1, 1, 2, 0, 0, 4]

# counts[3] 하나 감소시키고 Temp에 3을 삽입한다.
# Data = [0, 4, 1, 0, 0, 0, 0, 0]
#   -> counts = [1, 2, 4, 5, 7]
#   -> Temp = [0, 0, 1, 1, 2, 3, 0, 4]

# counts[1] 하나 감소시키고 Temp에 1을 삽입한다.
# Data = [0, 4, 0, 0, 0, 0, 0, 0]
#   -> counts = [1, 1, 4, 5, 7]
#   -> Temp = [0, 1, 1, 1, 2, 3, 0, 4]

# counts[4] 하나 감소시키고 Temp에 4를 삽입한다.
# Data = [0, 0, 0, 0, 0, 0, 0, 0]
#   -> counts = [1, 1, 4, 5, 6]
#   -> Temp = [0, 1, 1, 1, 2, 3, 4, 4]

# counts[0] 하나 감소시키고 Temp에 0을 삽입한다.
# Data = [0, 0, 0, 0, 0, 0, 0, 0]
#   -> counts = [0, 1, 4, 5, 6]
#   -> Temp = [0, 1, 1, 1, 2, 3, 4, 4]

# 카운팅 정렬 CODE
def Counting_Sort(A, B, K):
    # A : 입력 배열 (0~K)
    # B : 정렬된 배열
    # C : 카운트 배열
    C = [0]*(K+1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]] = A[i]





# 2차원 배열이란?
#       1차원 List를 묶어놓은 List
#       2차원 이상의 다차원 List는 차원에 따라 Index를 선언
#       2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
#       ex) arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
#                   0 1 2 3
#                   4 5 6 7

'''
# 배열 순회 : 행 우선 순회, 열 우선 순회, 지그재그 순회
# 행 우선 순회
for i in range(n):
    for j in range(m):
# 열 우선 순회
for j in range(m):
    for i in range(n)
# 짘쟄 순회
for i in range(n):
    for j in range(m):
        array[i][j + (i%2)*(m-1-2*j)]      # 미지수 설정 잘 하기(진짜 사람들 머리 좋군)
        
        
# 델타를 이용한 2차 배열 탐색
 - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

PseudoCode:
arr[0 ... N-1][0 ... N-1]                    # N by N matrix
di[] <- [0, 0, -1, -1]                       # 상하좌우
dj[] <- [-1, 1, 0, 0]

for i : 1 -> N - 1:
    for j : 1 -> N - 1:
        for k in range(4):
            ni <- i + di[k]
            nj <- j + dj[k]
            if 0 <= ni < N and 0 <= nj < N   # 유효한 idx
                test(arr[ni][nj])
'''

# 전치 행렬(Transpose)
'''
ex) 3 X 3 mat
for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
'''

# 비트 연산자
'''
& : 비트 단위로 AND 연산을 한다.
| : 비트 단위로 OR 연산을 한다.
<< : 피연산자의 비트 열을 왼쪽으로 이동시킨다.
>> : 피연산자의 비트 열을 오른쪽으로 이동시킨다.

<< 연산자 :
    1<<n  : 2**n , 원소가 n개일 경우 모든 부분집합의 수를 의미
    
& 연산자 : 
    i & (1<<j) : i의 j번째 비트가 1인지 아닌지를 검사한다.
    
# 보다 간단하게 부분집합을 생성하는 방법:
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)                 # 원소의 개수

for i in range(1<<n) :                # 1<<n : 부분집합의 개수
    for j in range(n):                # 원소의 수만큼 비트를 비교함
        if i & (1<<j):                # i의 j번 비트가 1인 경우
            print(arr[j], end=", ")   # j번 원소 출력
    print()
print()
'''

# 순차 검색(no정렬 ver.)
'''
def sequentialSearch(a, n, key):
    i <- 0
    while i<n and a[i] != key:
        i <- i + 1
    if i < n:
        return i
    else:
        return -1
'''

# 순차 검색(정렬 ver.)
'''
def sequentialSearch(a, n, key):
    i <- 0
    while i<n and a[i] < key:
        i <- i + 1
    if i < n and a[i] == key:
        return i
    else:
        return -1
'''

# 이진 검색
'''
def binarySearch(a, N, key):
    s = 0
    e = n-1
    while s <= e:
        m = (s + e)//2
        if a[m] == key:
            return True
        elif a[m] > key:
            e = m - 1
        else:
            s = m + 1
    return False
'''
        


# 선택 정렬
'''
PSEUDOCODE

def SelectionSort(a[], n):
    for i from 0 to n-2
        a[i], ... , a[n-1] 원소 중 최솟값 a[k] 찾음
        a[i] 와 a[k] 교환
        
CODE
def SelectionSort(a, N):        # a : 배열    //    N: 배열의 킈
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
'''
        
        
# Brute Force(고지식한 알고리즘)
'''
pattern = 'is'                  # 찾을 패턴
text = 'This is a book~!'       # 전체 텍스트
M = len(p)                      # 찾을 패턴의 길이
N = len(t)                      # 전체 텍스트의 길이

CODE

def BruteForce(pattern, text):
    i = 0           # text의 idx
    j = 0           # pattern의 idx
    while j < M and i < N:
        if text[i] != pattern[j]:
            i = i-j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M   # 성공
    else:
        return -1      # 실패


'''