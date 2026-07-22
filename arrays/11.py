x = list(map(int, input("Enter: ").split()))
left = 0
right = len(x) - 1
area = 0
while left < right:
    current = min(x[left], x[right]) * (right - left)
    area = max(area, current)
    if x[left] < x[right]:
        left += 1
    else:
        right -= 1
print(area)