x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def twosum(x,t):
    left = 0
    right = len(x) - 1
    while left < right:
        if x[left] + x[right] == t:
            return left+1,right+1
        elif x[left] + x[right] < t:
            left += 1
        else:
            right -= 1
    return False
print(twosum(x,t))