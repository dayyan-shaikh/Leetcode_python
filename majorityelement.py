# a=[1,2,2,2,6,5,6]

# b={}

# for i in a:
#     if i not in b:
#         b[i] = 1
#     else:
#         b[i] += 1 

# maxkey=max(b,key=b.get)
# print(maxkey)   

nums = [1,2,3,1]
k = 3

counts={}
for num in nums:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] +=1
keymax=max(zip(counts.values()))
print(keymax)
if k==keymax:
    print(True)
else:
    print(False)   