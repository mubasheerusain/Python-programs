class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        

    def push(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        temp = self.head
        self.head = temp.next
        del temp
        
    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
 
        

n = int(input("Enter the number of inputs: "))
stack = stack()
i = 0
while i < n:
    a = int(input("Enter a number: "))
    ans = Node(a)
    stack.push(ans)
    i += 1
stack.printlist()
stack.pop()
print("After poping")
stack.printlist()
