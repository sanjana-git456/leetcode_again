x = list(map(int, input("Enter: ").split()))
prefix = [1] * len(x)
suffix = [1] * len(x)
result = []
for i in range(1, len(x)):
    prefix[i] = prefix[i-1] * x[i-1]
for i in range(len(x)-2, -1, -1):
    suffix[i] = suffix[i+1] * x[i+1]
for i in range(len(x)):
    result.append(prefix[i] * suffix[i])
print(result)