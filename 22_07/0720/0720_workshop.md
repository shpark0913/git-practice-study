## workshop

1. number = int(input('자연수를 입력하시오 : '))
   
   N=1
   
   while N <= number:
   
       print(N)
   
       N += 1

2. number = int(input('자연수를 입력하시오 : '))
   
   N=1
   
   while N <= number:
   
       print(N,'', end='')
   
       N += 1

3. number = int(input('자연수를 입력하시오 : '))
   
   a = list(range(1, number + 1))
   
   b = list(reversed(a))
   
   for i in b:
   
       print(i)

4. number = int(input('자연수를 입력하시오 : '))
   
   a = list(range(0, number + 1))
   
   b = list(reversed(a))
   
   for i in b:
   
       print(i, '', end = '')

5. num = int(input('자연수를 입력하시오 : '))
   
   a = range(1, num + 1)
   
   b = sum(a)
   
   print(b)

6. num = int(input('자연수를 입력하시오 : '))
   
   a = range(1, num + 1)
   
   for i in a:
   
       print('*' * i)

7. num = list(map(int, input().split()))
   
   N = len(num)
   
   num.sort()
   
   if N % 2 == 1 :
   
       print(num[N//2])
   
   elif N % 2 ==0 :
   
       b = (num[N//2] + num[N//2 - 1])/2
   
       print(b)
