def has(s):
    l = len(s)-1
    if "g"==s[l] and "n"==s[l-1] and "i"==s[l-2]:
        return True
    else:
        return False


s  = input("Enter a string: ")
l = len(s)
if l<3:
    print(s)
else:
    if has(s):
        s += "ly"
        print(s)
    else:
        s += "ing"
        print(s)
