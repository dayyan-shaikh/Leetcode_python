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
        