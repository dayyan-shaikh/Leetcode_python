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


nums = [1,2,3,4,5,6,7]
k = 3
# nums = [-1,-100,3,99]
# k = 2
# res=nums[-k:]
# res1=nums[:k+1]
# r=res+res1
# print(r)
for i in range(k):
    print(i)
    a=nums.pop()
    # print(a)
    nums.insert(0,a)
    # print(nums)
# print(i)