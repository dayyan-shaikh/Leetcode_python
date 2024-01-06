nums = [1,2,3,4,5,6,7]
k = 3
# nums = [-1,-100,3,99]
# k = 2
# res=nums[-k:]
# res1=nums[:k+1]
# r=res+res1
# print(r)
for i in range(k):
    print(i)
    a=nums.pop()
    nums.insert(0,a)