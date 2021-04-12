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
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode


    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
      
    def reverse(self):
        currentNode = self.head
        previousNode = None
        while True:
            if currentNode is None:
                break
            next = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = next
        self.head = previousNode

    def rotate(self,pos):
        currentNode = self.head
        position = 0
        while True:
            if position == pos:
                lastNode = currentNode
                while True:
                    if currentNode.next is None:
                        break
                    currentNode = currentNode.next
                currentNode.next = self.head
                self.head = lastNode.next
                lastNode.next = None
                break
            currentNode = currentNode.next
            position += 1
              

    def reverseBy(self,head,k):
        currentNode = head
        previousNode = None
        next = None
        position = 0
        while currentNode is not None and position < k:
            next = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = next
            position += 1
        if next is not None:
            head.next = self.reverseBy(next,k)
        return previousNode
            
        


n = int(input("Enter the size: "))
i = 1
linked = Linkedlist()
while i <= n:
    a = int(input("Enter a number: "))
    ans = Node(a)
    linked.insert(ans)
    i += 1
linked.printlist()
b = int(input("Enter a position: "))
linked.head = linked.reverseBy(linked.head,b)
linked.printlist()
             
