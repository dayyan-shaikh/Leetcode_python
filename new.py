# nums = [2,3,1,1,4]
# nums=[3,4,5,2]

# for i in range(len(nums)):
#     if nums[i]>nums[i]+1:
#         i+=1
#         print(True)
#     else:
#         print(False)
nums1 = [1,3]
nums2 = [2]

merged = nums1 + nums2
print(merged)

# Sort the merged array.

merged.sort()

# Calculate the total number of elements in the merged array.
total = len(merged)
print(total)

if total % 2 == 1:
            # If the total number of elements is odd, return the middle element as the median.
    print(float(merged[total // 2]))
else:
            # If the total number of elements is even, calculate the average of the two middle elements as the median.
    middle1 = merged[total // 2 - 1]
    print(middle1)
    middle2 = merged[total // 2]
    print(middle2)
    print((float(middle1) + float(middle2)) / 2.0)
    

