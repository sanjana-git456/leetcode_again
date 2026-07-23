x = list(map(int, input("Enter: ").split()))
d = {}
total = 0
for i in range(len(x)):
    if x[i] not in d:
        d[x[i]] = 1
    else:
        total += d[x[i]]
        d[x[i]] += 1
print(total)