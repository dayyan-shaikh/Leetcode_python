nums = [1,2,3,1]
k = 3

indices={}

for ind,key in enumerate(nums):
    if(key in indices and ind-indices[key]<=k):
        indices[key]=ind
        print(True)
print(False)