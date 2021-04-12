class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
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
            lastnode.next =  newNode
    
    def insert_head(self,newnode):
        if self.head is None:
            self.head = newnode
        temp = self.head
        self.head = newnode
        self.head.next = temp
    
    def insert_At(self,position,newnode):
        currentNode = self.head
        currentIndex = 0
        while True:
            if currentIndex == position:
                previousNode.next = newnode
                newnode.next = currentNode
                break
            else:
                previousNode = currentNode
                currentNode = currentNode.next
                currentIndex += 1  
    
    def delete_head(self):
        temp = self.head
        self.head = self.head.next
        del temp

    def deleteAt(self,position):
        currentNode = self.head
        pos = 0
        while True:
            if position == pos:
                temp = currentNode
                previousNode.next = currentNode.next
                del temp
                break
            else:
                previousNode = currentNode
                currentNode = currentNode.next
                pos += 1

    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            

        

#n = int(input("Enter the number of inputs: "))
#i = 0
#data = []
#while i<n:
#    s = input("Enter a String: ")
#    data.append(s)
#    i += 1
#linkedlist = LinkedList()
#for j in data:
#    linked = Node(j)
#    linkedlist.insert(linked)
#ans = input("Enter a string: ")
#pos = int(input("Enter the index: "))
#result = Node(ans)
#linkedlist.insert_At(pos,result) 
#linkedlist.deleteAt(pos)
#linkedlist.printlist()
