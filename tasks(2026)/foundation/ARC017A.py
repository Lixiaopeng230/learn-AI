import math
n=int(input())
if n <17:
   print("UNKNOW")
else:   
 is_prime = True
 for i in range(2,int(math.sqrt(n))+1):
     if n %i==0:
      is_prime = False
     break
 if is_prime:
     print("YES") 
 else:
     print("NO")   