n=int(input())
m=n
if(n<=100000):
 remainder=0
 while(n!=0):
  num=n%10
  remainder=remainder+num*num*num
  n=n//10
 if(m==remainder):
  print("yes")
 else:
  print("no")
