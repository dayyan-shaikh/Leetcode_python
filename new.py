# prices = [98,54,6,34,66,63,52,39]
# # prices=[1,2,2]
# money = 62
# for i in range(len(prices)):
#     for j in range(i+1,(len(prices)-1)):
#         if prices[i]+prices[j]==money:
#             print("0")
#         else:
#             print(money)


x="abc"
y="ahjgbdsghc"
z=0

for i in range(len(x)-1):
    for j in range(i+1,len(y)):
        if x[i]==y[j]:
            z=i+1
            
            print(True)

