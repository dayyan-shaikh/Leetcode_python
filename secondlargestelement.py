#SECOND LARGEST ELEMENT IN ARRRAY

l=[2,6,4,4,9,5,1,7]
# s=set(l)
# m=list(s)
# print(m[-2])
# li=list(s)
x=list(set(l))
print(x)
if len(x)>1:
    x.sort()
    print(x[-2])
else:
    print(-1)
    