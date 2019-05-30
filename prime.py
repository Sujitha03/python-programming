n=int(input())
if(n<=1000):
 if(n>1):
  for i in range(2,n):
   if(n%i==0):
    print("No")
    break
  else:
   print("Yes")
 else:
  print("No")
else:
 print("Out of range")
  
