g,q=map(int,input().split())
for n in range(g,q):
 m=n
 remainder=0
 order=len(str(n))
 while(n!=0):
  num=n%10
  remainder=remainder+num**order
  n=n//10
 if(m==remainder):
  print(remainder,end=" ")
