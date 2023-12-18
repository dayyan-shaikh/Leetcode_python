numbers = [2,7,11,15]
target = 9

# solution 1
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
        
# solution 2
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i]+numbers[j]==target:
#             print([i+1,j+1])