nums=[3,4,5,2]
# method1
# nums=[1,5,4,5]

# frstmax=max(nums)
# nums.remove(frstmax)

# scndmax=max(nums)
# print((frstmax-1)*(scndmax-1))

# method2
nums.sort()
n=nums[-1]
m=nums[-2]

l=(n-1)*(m-1)
print(l)