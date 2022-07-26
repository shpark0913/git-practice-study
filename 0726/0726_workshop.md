1. def duplicated_letters(A) :
   
       lst = []
   
       for i in A :
   
           num_i = A.count(i)
   
           if num_i > 1 :
   
               lst.append(i)
   
       lst = set(lst)
   
       lst = list(lst)
   
       return lst

2. def low_and_up(A) :
   
       CB = ''
   
       for i in range(len(A)):
   
           if i%2 ==0:
   
               B = A[i].lower()
   
               CB += B
   
           elif i%2 :
   
               B = A[i].upper()
   
               CB += B
   
       return(CB)

3. def lonely(A) :
   
       B = [A[0]]
   
       for i in range(1,len(A)) :
   
           if A[i] != A[i-1] :
   
               B.append(A[i])
   
       return B
