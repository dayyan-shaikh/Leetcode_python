# # nums = [1,2,3,1,2,3]
# # k = 2
# nums=[1]
# k=1
# l=0

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if (len(nums)==1):
#             print(k)
#         else:
#             nums[i]==nums[j]
#             l=i-j
# print(l)
# if l<=k:
#     print(True)
# else:
#     print(False)

numbers = [2,7,11,15]
target = 9

left=0
right=len(numbers)-1
while(left<right):
    totalsum=numbers[left]+numbers[right]
    if(totalsum>target):
        right -= 1
    elif(totalsum<target):
        left += 1
    else:
        print([left+1,right+1]) 
        break
        