nums1=[1,2]
nums2=[3,4]

nums=nums1 + nums2 

nums.sort()

if len(nums)%2 != 0:
    centerindex=len(nums)//2
    print(nums[centerindex])
else:
    mid1=nums[len(nums)//2-1]
    print(mid1)
    mid2=nums[len(nums)//2]
    print(mid2)
    print(float(mid1+mid2)/2)