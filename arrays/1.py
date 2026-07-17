x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def twosum(x,t):
    d = {}
    for i in range(len(x)):
        a = t-x[i]
        if a in d:
            return (d[a],i)
        d[x[i]] = i
    return False
print(twosum(x,t))