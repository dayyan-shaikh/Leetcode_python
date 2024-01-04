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

n = 3
a=[]
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        a.append("FizzBuzz")
    elif i%3==0:
        a.append("Fizz")
    elif i%5==0:
        a.append("Buzz")
    else:
        a.append(i)
print(a)

