candies = [2,3,5,1,3]
# candies=[4,2,1,1,2]
extraCandies = 1

final = []

maxNum = max(candies)
for i in range(len(candies)):
    if candies[i] + extraCandies >= maxNum:
        final.append(True)
    else:
        final.append(False)
print(final)

# l=[]
# m=[]
# for i in range(0,len(candies)):
#     l.append(candies[i]+extraCandies)
# for j in range(len(l)):
#     if (l[j]>j+1):
#         m.append("true")
#     else:
#         m.append("false")
# print(m)   


