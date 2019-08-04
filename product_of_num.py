n=int(input())
p=1
while(n!=0):
   t=n%10
   p=t*p
   n=n//10
print(p) 
