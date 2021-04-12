def isunique(s):
    flag =0
    for i in range(0,len(s)):
        if i<len(s)-1:
            if s[i] == s[i+1]:
                flag = 1
    l = len(s)
    if s[l-1] == s[l-2]:
        flag = 1    
    return flag




s = input("Enter a string: ")
if isunique(s):
    print("all characters are not unique")
else:
    print("all characters are unique")

