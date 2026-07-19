x = list(map(int, input("Enter: ").split()))
l1 = []
l2 = []
for i in x:
    if i != 0:
        l1.append(i)
    else:
        l2.append(i)
print(l1+l2)