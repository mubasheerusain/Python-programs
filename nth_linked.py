class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head is None:
            self.head = data
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = data

    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
    
    def size(self):
        currentNode = self.head
        size = 0
        while True:
            if currentNode is None:
                break
            currentNode = currentNode.next
            size += 1
        return size
 
    def node(self,pos):
        size = self.size()
        k = size - pos
        position = 0
        currentNode = self.head
        while True:
            if position == k:
                print(currentNode.data)
                break
            currentNode = currentNode.next
            position += 1



n = int(input("Enter the size: "))
linked = Linkedlist()
i = 0
while i < n:
    a = int(input("Enter Number: "))
    ans = Node(a)
    linked.insert(ans)
    i += 1
linked.printlist()
b = int(input("Enter Number: "))
linked.node(b)

