nums=[1,3,4,5,8]
target=8
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])