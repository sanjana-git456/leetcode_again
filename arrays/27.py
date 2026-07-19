x = list(map(int, input("Enter: ").split()))
v = int(input("Enter value: "))
l = []
for i in x:
    if i != v:
        l.append(i)
print(l)