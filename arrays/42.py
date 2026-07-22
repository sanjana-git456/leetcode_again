x = list(map(int, input("Enter: ").split()))
s = 0
left_max = [0] * len(x)
left_max[0] = x[0]
for i in range(1, len(x)):
    left_max[i] = max(left_max[i-1], x[i])
right_max = [0] * len(x)
right_max[-1] = x[-1]
for i in range(len(x)-2, -1, -1):
    right_max[i] = max(right_max[i+1], x[i])
for i in range(len(x)):
    final = min(left_max[i], right_max[i]) - x[i]
    if final > 0:
        s += final
print(s)