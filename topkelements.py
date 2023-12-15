nums=[1,1,1,2,2,3]
k=2
counts = {}
for num in nums:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1
print(counts)

print(num)       

#arranging in decending order
counts_list = sorted(counts.items(),key=lambda x:x[1], reverse=True)
print(counts_list)

#slicing till k value
sorted_counts = dict(counts_list[:k])
print(sorted_counts)

#printing value in list        
print([num for num in sorted_counts])