x = list(map(int, input("Enter: ").split()))
m = len(x)
l = []
for i in range(1,m+1):
    if i not in x:
        l.append(i)
print(l)