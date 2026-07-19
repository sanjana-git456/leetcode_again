x = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))
d = {}
def dup(x):
    for i in range(len(x)):
        if x[i] in d:
            if i - d[x[i]] <= k:
                return True
        d[x[i]] = i
    return False
print(dup(x))