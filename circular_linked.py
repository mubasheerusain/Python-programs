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
            self.head.next = self.head
        else:
            lastNode = self.head
            while True:
                if lastNode.next is self.head:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.next = self.head

    def insert_head(self,newNode):
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            currentNode = self.head
            while currentNode.next is not self.head:
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.next = self.head
            self.head = newNode
    
    def size(self):
        position = 0
        currentNode = self.head
        while True:
            if currentNode == self.head:
                break
            currentNode = currentNode.next
            position += 1
        return position

    def insertAt(self,pos,newNode):
        currentNode = self.head
        position = 0
        if pos == position:
            self.insert_head(newNode)
        while True:
            if position == pos:
                break
            previousNode = currentNode
            currentNode = currentNode.next
            position += 1
        if position == self.size:
            self.insert(newnode)
        previousNode.next = newNode
        newNode.next = currentNode
  
    def printlist(self):
        currentNode = self.head
        while True:
            print(currentNode.data)
            currentNode = currentNode.next
            if currentNode is self.head:
                break

s = int(input("Enter the size: "))
i = 0
linkedlist = Linkedlist()
while i < s:
    a = input("Enter a string: ")
    ans = Node(a)
    linkedlist.insert(ans)
    i += 1
linkedlist.printlist()
b = input("Enter a string: ")
n = int(input("Enter the position: "))
ns = Node(b)
linkedlist.insertAt(n,ns)
linkedlist.printlist()
