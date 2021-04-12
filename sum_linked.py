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
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = newNode

    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
 

    def sum(self,list1,list2):
        currentNode1 = list1.head
        currentNode2 = list2.head
        carry = 0
        while True:
            if currentNode1 is None and currentNode2 is None:
                break
            if currentNode1 is None:
                a = 0
            else:
                a = int(currentNode1.data)
            if currentNode2 is None:
                b = 0
            else:
                b = int(currentNode2.data)
            res = carry + a + b
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            result = Node(res)
            self.insert(result)
            if currentNode1 is not None:
                currentNode1 = currentNode1.next
            if currentNode2 is not None:
                currentNode2 = currentNode2.next
             



n = int(input("Enter the number of inputs: "))
linked = Linkedlist()
i = 0
while i < n:
    a = int(input("Enter a number: "))
    ans = Node(a)
    linked.insert(ans)
    i += 1
n = int(input("Enter the number of inputs: "))
linked1 = Linkedlist()
i = 0
while i < n:
    a = int(input("Enter a number: "))
    ans = Node(a)
    linked1.insert(ans)
    i += 1
linked2 = Linkedlist()
linked.printlist()
linked1.printlist()
linked2.sum(linked,linked1)
linked2.printlist()

