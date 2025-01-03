nums = [3,6,9]
count = 0
for i in nums:
    if i%3 == 1:
        i - 1
        count+= 1
    elif i%3 == 2:
        i + 1
        count+= 1
print(count)