import sys
sys.stdin = open('input.txt')

lst = []
for i in range(8):
    n = int(input())
    lst.append(n)
lst.sort()
print(lst)

