



s = input("Enter a string: ")
f = input("Enter a sub string to find: ")
index = dict()
for i in range(0,len(s)):
    if s[i] == f[0]:
        index.update({"start":i})
    elif s[i] == f[len(f)-1]:
        index.update({"end":i})
print(index)
        

