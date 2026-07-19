x = input("Enter: ").split()
def prefix(x):
    result = ""
    first = x[0]
    for i in range(len(first)):
        char = first[i]
        for word in x:
            if i >= len(word) or word[i] != char:
                return result
        result += char
    return result
print(prefix(x))