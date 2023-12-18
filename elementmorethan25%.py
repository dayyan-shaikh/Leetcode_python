arr = [1,2,2,6,6,6,6,7,10]
map={}

for char in arr:
    if char not in map:
        map[char]=1
    else:
        map[char]+=1
print(map)
print(max(map, key=map.get))