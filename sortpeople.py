
names = ["Alice","Bob","Bob"]
heights = [155,185,150]
# res={}

# for key in names:
#     for value in heights:
#        res[key]=value
#        heights.remove(value)
#        break
# print(res)
# l=[]
# for w in sorted(res, key=res.get, reverse=True):
#     l.append(w)
# print(l)
heights_dict = zip(heights, names)
sorted_dict = sorted(heights_dict, reverse=True)
print([names for heights, names in sorted_dict])