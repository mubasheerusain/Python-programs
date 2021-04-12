def insertion(a):
    for i in range(1,len(a)):
        value = a[i]
        j = i-1
        while j>=0:
            if a[j] > value:
                a[j+1] = a[j]
                a[j] = value
                j = j-1
            else:
                break

s = int(input("Enter the size of an array: "))
a = []
i = 0
while i<s:
     b = int(input("Enter a number: "))
     a.append(b)
     i =i+1
insertion(a)
print(a)
