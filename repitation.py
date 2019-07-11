r,s=list(map(int,input().split()))
m=list(map(int,input().split()))
count=0
for n in m:
    if(n==s):
        count+=1
print(count)     
