x = input("Enter: ")
def pal(x):
    left = 0
    right = len(x) - 1
    while left < right:
        while left < right and x[left].isalnum() == False:
            left += 1
        while left < right and x[right].isalnum() == False:
            right -= 1
        if x[left].lower() != x[right].lower():
            return False
        left += 1
        right -= 1
    return True
print(pal(x))