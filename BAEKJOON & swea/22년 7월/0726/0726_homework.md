1. numbers = [4, 3, 2, 1]
   
   result = numbers.sort()
   
   print(numbers, result) 
   
   결과는 [1, 2, 3, 4] None
   
   원본이 변경된다.
   
   
   
   numbers = [4, 3, 2, 1]
   
   result = sorted(numbers)
   
   print(numbers, result)
   
   결과는 [4, 3, 2, 1] [1, 2, 3, 4]
   
   원본이 변경되지 않는다.

2. lst = ['a', 'b', 1, 2]
   
   lst.append(['cup'])
   
   print(lst)
   
   결과는 ['a', 'b', 1, 2, ['cup']]
   
   
   
   lst = ['a', 'b', 1, 2]
   
   lst.append('cup')
   
   print(lst)
   
   ['a', 'b', 1, 2, 'cup']
   
   -----------------------------------------
   
   lst = ['a', 'b', 1, 2]
   
   lst.extend(['cup'])
   
   print(lst)
   
   결과는 ['a', 'b', 1, 2, 'cup']
   
   
   
   lst = ['a', 'b', 1, 2]
   
   lst.extend('cup')
   
   print(lst)
   
   결과는 ['a', 'b', 1, 2, 'c', 'u', 'p']
   
   
   
   append는 원래 형태 그대로 삽입되지만
   
   extend는 항목을 추가한다.

3. a와 b에 담긴 list의 요소가 같다.
   
   대입 연산자를 통한 복사이기 때문이다.
