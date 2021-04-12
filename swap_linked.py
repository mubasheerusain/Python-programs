class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = newNode

    def printlist(self):
        currentNode = self.head
        while True:
            print(currentNode.data)
            currentNode = currentNode.next
            if currentNode is None:
                break

    def pair_swap(self):
        a=[]
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            a.append(currentNode.data)
            currentNode = currentNode.next
        i = 0
        j = 1
        while j < len(a):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i += 2
            j += 2
        return a



n = int(input("Enter the size: "))
linked = Linkedlist()
i = 0
while i < n:
    a = int(input("Enter a number: "))
    ans = Node(a)
    linked.insert(ans)
    i += 1
linked.printlist()
result = linked.pair_swap()
linked1 = Linkedlist()
for i in result:
    b = Node(i)
    linked1.insert(b)
linked1.printlist()
