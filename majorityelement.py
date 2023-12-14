a=[1,2,2,2,6,5,6]

b={}

for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1 

maxkey=max(b,key=b.get)
print(maxkey)   