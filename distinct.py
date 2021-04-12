


s = input("Enter a string: ")
n = int(input("Enter k: "))
ans = []
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        sub = ""
        for k in range(i,j):
            sub += s[k]
        ans.append(sub)
a = []
for i in ans:
    if len(i) >= n:
        a.append(i)

result =0
temp = 0
for i in a:
    for j in range(0,len(i)-1):
        if i[j] == i[j+1]:
            temp = 1
    if temp == 0:    
        result += 1
    
print(result)

   
