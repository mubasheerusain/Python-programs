def count(s):
    a = []
    for i in s:
        if i not in a:
            a.append(i)
    result = dict()
    for i in a :
        temp = 0
        for j in s:
            if i == j:
                temp += 1
                result.update({i:temp})
            result.update({i:temp})
    return result
                
                   














s = input("Enter a string: ")
ans = count(s)
print(ans)
