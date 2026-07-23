x = list(map(int, input("Enter: ").split()))
sorted_x = sorted(x)
d = {}
for i in range(len(sorted_x)):
    if sorted_x[i] not in d:
        d[sorted_x[i]] = i
result = []
for num in x:
    result.append(d[num])
print(result)