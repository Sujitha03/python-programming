n=int(input())
m=list(map(int,input().split()))
s=0
for num in m:
    s=s+num
avg=s//n
print(avg)
