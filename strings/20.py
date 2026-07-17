x = input("Enter: ")
d = {')' : '(' , ']' : '[' , '}' : '{'}
l = []
def par(x):
    for i in x:
        if i not in d:
            l.append(i)
        elif l != [] and l[-1] == d[i]:
            l.pop()
        else:
            return False
    return l == []
print(par(x))