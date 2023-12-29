#we have to add 1 to -1 index return the value
digits = [1,2,3]
#output[1,2,4]
a=(''.join(str(x) for x in digits))
a=int(a)
b=(a+1)
b=[b]
c=list(map(int, str(b[0])))
print(c)