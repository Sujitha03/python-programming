n=int(input())
s=0
r=1
for i in range(2,n+2):
    print(r,end=' ')
    c=s+r 
    s=r 
    r=c
