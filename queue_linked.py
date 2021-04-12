class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def enqueue(self,newNode):
        if self.is_empty():
            self.head = self.tail = newNode
            self.size += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def dequeue(self):
        temp = self.head
        self.head = temp.next
        del temp
        self.size -= 1
        

    def printlist(self):
        currentNode = self.head
        i = 0
        while True:
            if i >= self.size:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            i += 1


n = int(input("Enter the number of inputs: "))
queue = Queue()
i = 0
while i < n:
    a = int(input("Enter a number: "))
    ans = Node(a)
    queue.enqueue(ans)
    i += 1
queue.printlist()
queue.dequeue()
queue.printlist()
