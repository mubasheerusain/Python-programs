def bubble(a):
    for i in range(len(a)-1):
        for j in range(0,len(a)-i-1):
            if a[j+1] > a[j]:
                a[j],a[j+1] = a[j+1],a[j]


n = int(input("Enter the size: "))
i = 0
a = []
while i<n:
    b = int(input("Enter the number: "))
    a.append(b)
    i += 1
bubble(a)
print(a[::-1])
