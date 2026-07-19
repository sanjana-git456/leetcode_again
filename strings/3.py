x = input("Enter: ")
def longest(x):
    seen = set()
    left = 0
    maxlen = 0
    for right in range(len(x)):
        while x[right] in seen:
            seen.remove(x[left])
            left += 1
        seen.add(x[right])
        maxlen = max(maxlen, right-left+1)
    return maxlen
print(longest(x))