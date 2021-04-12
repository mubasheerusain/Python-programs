from single_linked import LinkedList


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



def merge(list1,list2,list3):
    currentNode1 = list1.head
    currentNode2 = list2.head
    while True:
        if currentNode1 is None:
            list3.insert(currentNode2)
            break    
        if currentNode2 is None:
            list3.insert(currentNode1)
            break 
        if currentNode1.data < currentNode2.data:
            temp = currentNode1.next
            currentNode1.next = None
            list3.insert(currentNode1)
            currentNode1 = temp
        else:
            temp = currentNode2.next
            currentNode2.next = None
            list3.insert(currentNode2)
            currentNode2 = temp
        
      
            

list1 = LinkedList()
list2 = LinkedList()
list3 = LinkedList()
n = int(input("Enter the size: "))
i = 0
while i < n:
    a = int(input("Enter a number: "))
    ans = Node(a)
    list1.insert(ans)
    i += 1
list1.printlist()
j = 0
while j < n:
    a = int(input("Enter a number: "))
    ans = Node(a)
    list2.insert(ans)
    j += 1
list2.printlist()
merge(list1,list2,list3)
print("Result: ")
list3.printlist()

