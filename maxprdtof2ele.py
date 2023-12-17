# nums=[3,4,5,2]
nums=[1,5,4,5]

frstmax=max(nums)
nums.remove(frstmax)

scndmax=max(nums)
print((frstmax-1)*(scndmax-1))