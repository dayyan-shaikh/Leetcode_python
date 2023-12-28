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
nums = [-1,0,3,5,9,12]
target = 9
for i in range(len(nums)):
    if nums[i]!=target:
        i=i+1
    elif nums[i]==target:
        print(i)
else:
    print(-1)