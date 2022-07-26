1. def count_vowels(A):
   
       lst_A = list(A)
   
       a = lst_A.count('a')
   
       e = lst_A.count('e')
   
       i = lst_A.count('i')
   
       o = lst_A.count('o')
   
       u = lst_A.count('u')
   
       B = a + e + i + o + u
   
       return B

2.  (4)번.
   
   특정 문자열 지정하지 않으면 공백을 제거할 뿐, 오류가 생기지 않는다.

3. def only_square_area(A, B) :
   
       lst = []
   
       for i in A :
   
           if i in B :
   
               lst.append(i**2)
   
       return lst
