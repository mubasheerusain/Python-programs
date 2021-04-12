def sub(s):
    l = len(s)
    print(l)
    if l==1:
        return "Empty String"
    elif l>1 and l<3:
        a =[]
        result = ""
        for i in s:
            a.append(i)
        for i in s:
            a.append(i)
        for i in a:
            result += i
        return result
    else:
        start = 0
        end = len(s)-1
        a = []
        result = ""
        for i in range(0,len(s)):
            if i==start or i==start+1 or i==end or i==end-1:
                a.append(s[i])
        for i in a:
            result += i
        return result














s = input("Enter a string: ")
ans = sub(s)
print(ans)


