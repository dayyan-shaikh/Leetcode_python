# prices = [98,54,6,34,66,63,52,39]
# # prices=[1,2,2]
# money = 62
# for i in range(len(prices)):
#     for j in range(i+1,(len(prices)-1)):
#         if prices[i]+prices[j]==money:
#             print("0")
#         else:
#             print(money)



# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# s="(]"
# p=["{}","[]","()"]
# for i in range(len(p)):
#     if s==p[i]:
#         print((True))
# print(False)


# nums = [5,4,2,3]
# nums.sort()
# res=[]
# for i in range(0,len(nums),2):
#     print(i)
#     res.append(i+1)
#     res.append(i)
# print(res)

# list1 = [1,2,4]
# list2 = [1,3,4]
# list3=[]
# for i in list1:
#     list3.append(i)
# for j in list2:
#     list3.append(j)
# list3.sort()
# print(list3)

test_list = [3, 6, 7, 8, 9, 2, 1, 5]
 
res = test_list[::2] 

print(res)
sum=0
for i in range(len(res)):
    sum=sum+res[i]
print(sum)

# a=[1,4,5,7,8]
# b=[2,3,6]
# c=[]
# for i in a:
#     for j in b:
#         c.append(i)
#         c.append(j)
# c=list(set(c))
# print(c)
            
