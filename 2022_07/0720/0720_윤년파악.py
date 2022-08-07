Year = int(input('연도를 입력하시오 : '))

if Year % 4 ==0 and Year % 100 != 0:
    print(f'{Year}은 윤년입니다.')
elif Year % 400 ==0:
    print(f'{Year}은 윤년입니다.')
else : 
    print(f'{Year}은 윤년이 아닙니다.')