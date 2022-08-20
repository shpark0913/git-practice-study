## 0806_codeproblem

- 개요 : 우리나라 화폐 '원'은 금액이 높은 돈을 우선적으로 계산할 때 돈의 개수가 가장 최소가 된다. 어떤 마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위해 각 종류의 돈이 몇 개씩 필요한지 계산하는 프로그램을 작성하라.

- 제약 : 
  
  - N은 10 이상 1,000,000 이하의 정수
  
  - N의 일의 자리 숫자는 항상 0 (ex : 32850)

- 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
  
  ex)
  
  2   
  32850  
  160

- 출력 : 각 줄은 '#t'로 시작하고, 다음줄에 각 돈의 종류마다 필요한 개수를 빈칸을 사이에 두고 출력한다.  
  
  (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
  
  ex)
  
  #1  
  0 3 0 2 1 3 1 0  
  #2  
  0 0 0 0 0 1 1 1