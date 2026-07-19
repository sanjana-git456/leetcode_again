s = input("Enter first word: ")
t = input("Enter second word: ")
def anagram(s,t):
    if len(s) != len(t):
        return False
    elif sorted(s) == sorted(t):
        return True
    else:
        return False
print(anagram(s,t))