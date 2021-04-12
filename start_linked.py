class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedlist:
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
    
    def insert_head(self,data):
        temp = self.head
        self.head = data
        self.head.next = temp

    def insertAt(self,position,data):
        pos = 0
        currentNode = self.head
        while True:
            if pos == position:
                previousNode.next = data
                data.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            pos += 1
       
        

    def printList(self):
        currentNode = self.head
        while True:
            print(currentNode.data)
            if currentNode.next is None:
                break
            currentNode = currentNode.next

firstNode = Node("Mubasheer")
linked = linkedlist()
linked.insert(firstNode)
secondNode = Node("Hussain")
linked.insert(secondNode)
thirdNode = Node("Mohamed")
linked.insert_head(thirdNode)
fourthNode = Node("Hello")
linked.insertAt(1,fourthNode)
linked.printList()
