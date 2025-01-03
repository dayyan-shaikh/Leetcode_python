nums = [0,1,1,0]

dic = {}
l = []

for i in nums:
    if i not in dic:
        dic[i] = 1
    elif i in dic:
        dic[i] += 1

for i in dic:
    if dic[i] > 1:
        l.append(i)
print(l)
