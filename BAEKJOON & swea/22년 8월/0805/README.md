## 0805_codeproblem

- 개요 : 집의 위치가 두 수도 회사 A, B 중간에 위치하기에 원하는 수도 회사를 선택해 수도 요금을 낼 수 있다. 두 회사 중 더 적게 수도 요금을 부담해도 되는 회사를 고르는 프로그램을 작성하라.
  
  - A사 : 1리터 당 P원의 요금
  
  - B사 : 기본 요금이 Q원
    
    - 월간 사용량이 R리터 이하 : 기본 요금만 청구
    
    - 월간 사용량이 R리터 초과 : 초과량에 대해 1리터 당 S원 추가 청구
  
  - 종민의 집에서 한 달간 사용하는 수도의 양 : W리터

- 입력 : 
  
  첫 번째 줄에 테스트 케이스의 수 T가 주어진다.  
  
  각 테스트 케이스마다 첫 번째 줄에 위 본문에서 설명한 대로 P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수)가 순서대로 공백 하나로 구분되어 주어진다.
  
  ex )
  
  2  
  9 100 20 3 10  
  8 300 100 10 250

- 출력 : 
  
  ex)
  
  #1 90  
  #2 1800

## 0805_codeproblem2

- 개요 : N명의 수강생을 몇 개의 조로 나누려고 한다. 조의 수의 최댓값이 얼마인지를 구하는 프로그램을 작성하라.

- 제약 : 한 조의 학생을 2명 이하로 구성하지 않는다.

- 입력 : 첫 번째 줄에 테스트 케이스의 수 T가 주어진다. 각 테스트는 하나의 줄로 이루어진다.
  
  ex) 
  
  3  
  1  
  10  
  100

- 출력 : 각 테스트 케이스마다 N명의 학생들을 조로 적당히 나누었을 때, 3명 이상의 학생으로 구성된 조의 수의 최댓값을 출력한다.
  
  ex)
  
  #1 0  
  #2 3  
  #3 33
