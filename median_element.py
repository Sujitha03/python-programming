n=int(input())
if(n>=1 and n<=1000):
 m=list(map(int,input().split()))
 s=sorted(m)
 l=len(s)
 v=l//2
 print(s[v])
