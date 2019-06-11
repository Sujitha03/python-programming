n=int(input())
m=list(map(int,input().split()))
sum=0
for num in m:
    sum=sum+num
avg=sum//n
print(avg)
