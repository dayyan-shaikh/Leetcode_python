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

nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
numSet = set(nums)
longest = 0

for n in numSet:
    # check if its the start of a sequence
    if (n - 1) not in numSet:
        length = 1
    while (n + length) in numSet:
        length += 1
    longest = max(length, longest)
print(longest)
        