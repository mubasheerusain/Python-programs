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
            
    def intersect(self,list1,list2):
        currentNode1 = list1
        position = 0
        intersection = None
        while currentNode1 is not None:    
            currentNode2 = list2
            while currentNode2 is not None:
                if currentNode1.data == currentNode2.data:
                    intersection = currentNode1.data
                    return dict({"point":intersection,"position":position})
                else:
                    currentNode2 = currentNode2.next
            currentNode1 = currentNode1.next
            position += 1

    def loop(self):
        currentNode = self.head
        temp = []
        flag = False
        while currentNode:
            if currentNode.data in temp:
                flag = True
                break
            temp.append(currentNode.data)
            currentNode = currentNode.next  
        return flag

    def remove_loop(self):
        currentNode = self.head
        temp = []
        while currentNode:
            if currentNode.data in temp:
                print(previousNode.data)
                previousNode.next = None
                break
            temp.append(currentNode.data)
            previousNode = currentNode
            currentNode = currentNode.next  
        
            



n = int(input("Enter the size: "))
linked = Linkedlist()
#linked1 = Linkedlist()
i = 0
while i < n:
    a = int(input("Enter Number for list 1: "))
    ans = Node(a)
    linked.insert(ans)
    i += 1
linked.printlist()
linked.head.next.next = linked.head
linked.remove_loop()
if linked.loop():
    print("it has loop")
else:
    print("it does not have a loop")
#j = 0
#x = int(input("Enter the size: "))
#while j < x:
#    b = int(input("Enter Number for list 2: "))
#    an = Node(b)
#    linked1.insert(an)
#    j += 1
#linked1.printlist()
#result = linked.intersect(linked.head,linked1.head)
#print(result)



            
