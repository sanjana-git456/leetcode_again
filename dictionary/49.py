x = input("Enter: ").split()
d = {}
for i in range(len(x)):
    a = ''.join(sorted(x[i]))
    if a not in d:
        d[a] = []
    d[a].append(''.join(x[i]))
print(d)