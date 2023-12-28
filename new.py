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
digits = [1,2,3]
a=(''.join(str(x) for x in digits))
a=int(a)
b=(a+1)
b=[b]
c=list(map(int, str(b[0])))
print(c)