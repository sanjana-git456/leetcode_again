x = list(map(int, input("Enter first array: ").split()))
y = list(map(int, input("Enter second array: ").split()))
result = []
i = 0
j = 0
while i < len(x) and j < len(y):
    if x[i] > y[j]:
        result.append(y[j])
        j += 1
    else:
        result.append(x[i])
        i += 1
if i < len(x):
    result.extend(x[i:])
if j < len(y):
    result.extend(y[j:])
print(result)