# nums = [2,3,1,1,4]
# nums=[3,4,5,2]

# for i in range(len(nums)):
#     if nums[i]>nums[i]+1:
#         i+=1
#         print(True)
#     else:
#         print(False)


nums1 = [1, 2]
nums2 = [4,5]

nums = nums1 + nums2
nums.sort()

if len(nums) % 2 != 0:
    centerIndex = len(nums) // 2
    print(nums[centerIndex])
else:
    middle1 = nums[len(nums) // 2 - 1]
    print(middle1)
    middle2 = nums[len(nums) // 2]
    print((float(middle1) + float(middle2)) / 2.0)

    


