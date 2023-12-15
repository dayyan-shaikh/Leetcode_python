prices = [7,1,5,3,6,4]
# prices=[7,6,4,3,1]

minprice=float('inf')
maxprofit=0

for i in range(len(prices)):
    if(prices[i]<minprice):
        minprice=prices[i]
    elif(prices[i]-minprice>maxprofit):
        maxprofit=prices[i]-minprice
print(maxprofit)
