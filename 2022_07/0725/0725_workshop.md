1. def get_dict_avg(A) :
   
       lst = list(A.values())
   
       a = sum(lst)
   
       b = len(lst)
   
       return a/b

2. def count_blood(lst) :
   
       num_A = lst.count('A')
   
       num_B = lst.count('B')
   
       num_O = lst.count('O')
   
       num_AB = lst.count('AB')
   
       return {'A': num_A,'B': num_B,'O': num_O,'AB': num_AB}
