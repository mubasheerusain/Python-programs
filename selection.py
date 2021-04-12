def selection(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1,len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]



n = int(input("Enter the size: "))
i =0
a = []
while i<n:
    b = int(input("Enter the number: "))
    a.append(b)
    i +=1
selection(a)
print(a)
