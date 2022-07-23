## homework

1. def ssafy(name, location='서울'):
   
       print(f'{name}의 지역은 {location}입니다.')
   
   ssafy('가흔')
   
   ssafy(location = '부울경', name = '승현')
   
   ssafy('지우', location = '서울')
   
   ssafy(name = '승호', '광주') ->  # 오류. key argument 다음에 positional argument 활용 불가능

2. def my_avg(*args):
   
       a = 0
   
       for i in args:
   
           a += i
   
       b = len(args)
   
       return a/b

3. result에 저장된 값은 None이다.
   
   print는 단순히 호출될 때마다 값을 출력할 뿐, c에 데이터 처리를 하지는 않는다. 

4. L : Local scope (지역 범위)
   
   E : Enclosed scope (지역 범위 한 단계 위 범위)
   
   G : Global scope (최상단에 위치한 범위)
   
   B : Built-in scope (모든 것을 담고 있는 범위)

5. (1) tuple 형식으로 가능하다.
