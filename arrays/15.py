x = list(map(int, input("Enter: ").split()))
x.sort()
l = len(x)
def threesum(x):
    result = []
    for i in range(l):
        if i > 0 and x[i] == x[i-1]:
            continue
        left = i+1
        right = l-1
        n = -x[i]
        while left < right:
            if x[left] + x[right] == n:
                new = [x[i], x[left], x[right]]
                result.append(new)
                left += 1
                right -= 1
            elif x[left] + x[right] < n:
                left += 1
            else:
                right -= 1
    return result
print(threesum(x))