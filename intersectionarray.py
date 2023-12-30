# we have to return intersection between two arrays
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums3=[]
for i in nums1:
    for j in nums2:
        if i==j:
            nums3.append(i)    
print(list(set(nums3)))