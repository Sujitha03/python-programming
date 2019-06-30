n=int(input())
count=0
for i in range(1,n):
    if(2**i==n):
       count=count+1
if(count>=1):
    print('yes')
elif(n==1):
    print('yes')
else:
    print('no')
