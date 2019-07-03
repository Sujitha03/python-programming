s=input().lower()
words=s.split()
r=[]
for word in words:
    c=word[0].upper()+word[1:]
    r.append(c)
result=' '.join(r)
print(*r)
