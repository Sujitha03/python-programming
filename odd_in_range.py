N,Q=list(map(int,input().split()))
if(N<=100000 and Q<=100000):
 for num in range(N+1,Q):
  if(num%2!=0):
   print(num,end=" ")
  num=num+1
else:
 print("Out of range")
