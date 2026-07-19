x = list(map(int, input("Enter: ").split()))
x = list(map(str, x))
j = ''.join(x)
j = int(j)
y = j+1
res = list(map(int, str(y)))
print(res)