# method 1
v="This is a string"
# v_1=v.split()
# print(len(v_1))

# method 2
count=1
for i in v:
    if i == " ":
        count += 1
print(count)