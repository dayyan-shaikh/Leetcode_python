s="A man, a plan, a canal: Panama"
r=''
for i in s:
    if(i.isalnum()):
        r += i
r=r.lower()
print(r)
if(r==r[::-1]):
    print(True)
else:
    print(False)