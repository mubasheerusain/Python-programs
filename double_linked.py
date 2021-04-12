class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            newNode.next = None
            newNode.previous = lastnode
            lastnode.next =  newNode
    
    def insert_head(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
            temp.previous = self.head 
            

    def insertAt(self,pos,newNode):
        lastNode = self.head
        position = 0    
        while True:
            if pos == position:
                previousNode.next = newNode
                newNode.previous = previousNode
                newNode.next = lastNode
                lastNode.previous = newNode
                break
            previousNode = lastNode
            lastNode = lastNode.next
            position += 1

 
    def printlist(self):
        lastNode = self.head
        while True:
            if lastNode is None:
                break
            print(lastNode.data)
            lastNode = lastNode.next




n = int(input("Enter the number of inputs: "))
i = 0
linkedlist = Linkedlist()
while i<n:
    s = input("Enter a String: ")
    linked = Node(s)
    linkedlist.insert(linked)
    i += 1
linkedlist.printlist()
pos = int(input("Enter the position: "))
b  = input("Enter a String: ")
ans = Node(b)
linkedlist.insertAt(pos,ans)
#linkedlist.insert_head(ans)
linkedlist.printlist()




























