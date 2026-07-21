x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def twosum(x,t):
    left = 0
    right = len(x) - 1
    for i in range(len(x)):
        if x[left] + x[right] == t:
            return left,right
        elif x[left] + x[right] < t:
            left += 1
        else:
            right -= 1
    return False
print(twosum(x,t))