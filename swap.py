def swap(s,w):
    result = ""
    for i in range(0,2):
        result += w[i]
    for i in range(2,len(s)):
        result += s[i]
    result += " "
    for i in range(0,2):
        result += s[i]
    for i in range(2,len(w)):
        result += w[i]
    return result
        









s = input("Enter a string: ")
w = input("Enter a string: ")
ans = swap(s,w)
print(ans)
