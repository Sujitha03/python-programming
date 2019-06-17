n,k=map(int,input().split())
m=list(map(int,input().split()))
z=k-1
l=[]
for num in m:
    if(num%2!=0):
        l.append(num)
print(*(l[z:z+1]))
