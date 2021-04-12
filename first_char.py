def first_char(s):
    a = s[0]
    result = ""
    result += a
    for i in range(1,len(s)):
        if a == s[i]:
            result += "$"

        else:
            result += s[i]
    return result
             




s = input("Enter a string: ")
ans = first_char(s)
print(ans)
