



s = input("Enter a String: ")
a = ""
start = 0
mid = len(s)//2
for i in range(0,mid):
    if s[i] in a:
        start = i
        break
    if s[i] not in a:
        a += s[i]
b = ""
end = 0
for i in range(mid,len(s)):
    if s[i] in b:
        end = i-1
        break
    if s[i] not in b:
        b += s[i]
result = ""
if end == 0:
    end = len(s)
for i in range(start,end):
    result += s[i]
print(result)
