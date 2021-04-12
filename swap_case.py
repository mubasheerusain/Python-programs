s = input("Enter a string: ")
result = ""
for i in range(0,len(s)):
    if s[i].isupper():
        result += s[i].lower()
    elif s[i].islower():
        result += s[i].upper()
    else:
        result += s[i]
print(result)
        

