x = list(map(int, input("Enter: ").split()))
result = []
for i in range(len(x)):
    fix = x[i]
    p = 1
    for j in range(len(x)):
        if j != i:
            p *= x[j]
    result.append(p)
print(result)