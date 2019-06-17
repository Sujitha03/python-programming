r,s=map(int,input().split())
r=list(map(int,input().split()))
z=sorted(r)
print(*(z[s-1:s]))
