x = list(map(int, input("Enter: ").split()))
def minprice(x):
    price = x[0]
    maxprofit = 0
    for i in range(1, len(x)):
        profit = x[i] - price
        maxprofit = max(maxprofit, profit)
        price = min(price, x[i])
    return maxprofit
print(minprice(x))