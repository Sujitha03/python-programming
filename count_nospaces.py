name=input()
k=0
for line in name:
    words=line.split()
    for i in words:
        for letter in i:
            if(letter!=' '):
                k=k+1
print(k)
