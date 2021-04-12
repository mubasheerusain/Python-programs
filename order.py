



s = input("Enter a string: ")
temp = 0
result = 1
for i in range(0,len(s)):
    if ord(s[i]) == temp+1:
        result += 1
        temp = ord(s[i])
    else:
        temp = ord(s[i])
print(result)
