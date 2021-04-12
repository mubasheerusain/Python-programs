



s = input("Enter a string: ")
result = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i] == s[j]:    
            result += 1
print(result)
