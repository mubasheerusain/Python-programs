def quick_sort(a):
    sort(a,0,len(a)-1)

def sort(a,low,hi):
    if low < hi:
        p = partition(a,low,hi)
        sort(a,low,p-1)
        sort(a,p+1,hi)

def get_pivot(a,low,hi):
    mid = (low+hi) //2
    pivot = hi
    if a[low] < a[mid]:
        if a[mid] < a[hi]:
            pivot = mid
    elif a[low] < a[hi]:
        pivot = low
    return pivot

def partition(a,low,hi):
    pivotIndex = get_pivot(a,low,hi)
    pivotValue = a[pivotIndex]
    a[pivotIndex],a[low] = a[low],a[pivotIndex]
    border = low
    for i in range(low,hi+1):
        if a[i] < pivotValue:
            border += 1
            a[i] ,a[border] = a[border],a[i]
    a[low],a[border] = a[border],a[low]
    return border

n = int(input("Enter a number: "))
i = 0
a = []
while i<n:
    b = int(input("Enter a number: "))
    a.append(b)
    i += 1
l= len(a)
quick_sort(a)
print(a)
