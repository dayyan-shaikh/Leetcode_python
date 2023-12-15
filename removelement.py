nums=[1,2,3,4,3]
val=2
k=0
for i in range(len(nums)):
        # print([i],end=" ")
        if nums[i] != val:
                nums[k] = nums[i]
                k += 1
print(k)
        
         
    
    