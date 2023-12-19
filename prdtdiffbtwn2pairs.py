nums=[5,6,2,7,4]
#return max 2 numbers product and min 2 product numbers difference

nums.sort()
print(nums)

print((nums[-1]*nums[-2])-(nums[0]*nums[1]))