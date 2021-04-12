




s = input("Enter a string: ")
a = s.split()
print(a)
large = ""
small = ""
temp = 0 
ans = 0
for i in range(0,len(a)):
    if len(a[temp]) < len(a[i]):
        temp = i
    elif len(a[ans]) > len(a[i]):
         ans = i
large += a[temp]
small += a[ans]
print("large :",large)
print("small :",small) 
        
