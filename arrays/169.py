x = list(map(int, input("Enter: ").split()))
def counting(x):
    n = len(x) // 2
    d = {}
    for i in range(len(x)):
        if x[i] not in d:
            d[x[i]] = 1
        else:
            d[x[i]] += 1
    for i in range(len(x)):
        if d[x[i]] > n:
            return x[i]
print(counting(x))