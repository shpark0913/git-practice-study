## homework

1. range(), abs(), set(), map(), len()

2. odds = list(range(1, 51))
   
   a = odds[0:50:2]
   
   print(a)

3. n = int(input())
   
   m = int(input())
   
   for i in range(m):
   
       print('*'*n)

4. temp = 36.5
   
   print('입실 불가') if temp >= 37.5 else print('입실 가능')

5. get_middle_char = input('문자를 입력하시오 : ')
   
   a = len(get_middle_char)
   
   if a % 2 :
   
       print(get_middle_char[a//2])
   
   else :
   
       print(get_middle_char[a//2 -1]+get_middle_char[a//2])
