


s = input("Enter a string: ")
l = s.split()
for i in range(0,len(l)):
    if l[i] == "poor" or l[i] == "not":
        l[i] = "good"
result = " ".join(l)
print(result)
