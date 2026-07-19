s = input("Enter s: ")
t = input("Enter t: ")
d = {}
def iso(s,t):
    for i in range(len(s)):
        if s[i] not in d:
            if t[i] in d.values():
                return False
            d[s[i]] = t[i]
        else:
            if d[s[i]] != t[i]:
                return False
    return True
print(iso(s,t))