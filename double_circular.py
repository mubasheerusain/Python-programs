class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.head.prev = self.head
        else:
            lastNode = self.head
            while True:
                if lastNode.next is self.head:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode
            newNode.prev =  lastNode
            newNode.next = self.head

    def printlist(self):
        currentNode = self.head    
        while True:
            print(currentNode.data)
            currentNode = currentNode.next
            if currentNode is self.head:
                break

    def insert_head(self,newNode):
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.head.prev = self.head
        else:
            currentNode = self.head
            while True:
                currentNode = currentNode.next
                if currentNode.next is self.head:
                    break
            currentNode.next = newNode
            newNode .prev = currentNode
            newNode.next = self.head
            self.head = newNode


    def size(self):
        size = 0
        currentNode = self.head
        while True:
            if currentNode.next is self.head:
                break
            currentNode = currentNode.next
            size += 1
        return size


    def insertAt(self,pos,newNode):
        if pos == self.size:
            self.insert(newNode)
        currentNode = self.head
        position = 0
        while True:
            if position == pos:
                break
            previousNode = currentNode
            currentNode = currentNode.next
            position += 1
        previousNode.next = newNode
        newNode.prev = previousNode
        newNode.next = currentNode
        currentNode.prev = newNode
        

n = int(input("Enter the number of inputs: "))
i = 0
linkedlist = Linkedlist()
while i<n:
    s = input("Enter a String: ")
    linked = Node(s)
    linkedlist.insert(linked)
    i += 1
linkedlist.printlist()
a = input("Enter a String: ")
pos = int(input("Enter the position: "))
link = Node(a)
linkedlist.insertAt(pos,link)
linkedlist.printlist()

      
                    
