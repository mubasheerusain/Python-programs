def check(s):
    b =[]
    for i in s:
        b.append(i)
    b.sort()     
    print(b)
    c =[]
    for i in range(0,len(b)):
        if i<len(b)-1:
            if b[i]!=b[i+1] and b[i]!=b[i-1] :
                c.append(b[i])
    l = len(s)
    if b[l-1] != b[l-2]:
            c.append(b[l-1])   
    print(c)
    c.pop(0)
    c.pop(0)
    a = []
    for i in s:
        if i not in c:
            a.append(i)
    u = ""
    for i in a:
        u += i
    return u
  







s=input("Enter a string: ")
ans = check(s)
print(ans)
