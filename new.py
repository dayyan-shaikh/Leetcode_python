# nums=[0,0,1,1,1,2,2,3,4,4,3]
# l=list(set(nums))
# print(l)

a="A man, a plan, a canal: Panama"
b=a[::-1].replace(" ","").replace(":","").replace(",","").lower()
c=a.replace(" ","").replace(":","").replace(",","").lower()
print(b)
print(c)
if b==c:
    print(True)
else:
    print(False)
    
    