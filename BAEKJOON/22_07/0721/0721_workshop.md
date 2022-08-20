## workshop

1. N = int(input('정수를 입력하세요 : '))
   
   lst = []
   
   for i in range(1, N + 1):
   
       if N % i == 0 :
   
           print(i,'', end='')

2. def list_sum(A):
   
       j = 0
   
       for i in A:
   
           j += i
   
       return j
   
   #B = [1, 2, 3]
   
   #print(list_sum(B))
   
   #이런 식으로 작동이 된다!

3. a = {'name' : 'kim', 'age' : 12}
   
   b = {'name' : 'lee', 'age' : 4}
   
   A = [a, b]
   
   def dict_list_sum(A):
   
       n = 0
   
       for i in A:
   
           j = i['age']
   
           n += j
   
       return n
   
   print(dict_list_sum(A))

4. A = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
   
   def all_list_sum(A):
   
       a = 0
   
       for i in A:
   
           b=0
   
           for j in i:
   
               b += j
   
           a += b
   
       return a
   
   print(all_list_sum(A))
