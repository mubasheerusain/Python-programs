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
                currentNode =currentNode.next
            currentNode.next = newNode

    def printlist(self):
        currentNode = self.head
        while True:
            print(currentNode.data)
            currentNode = currentNode.next
            if currentNode is None:
                break

    def ispalindrome(self):
        currentNode = self.head
        s = ""
        while True:
            if currentNode is None:
                break
            s += str(currentNode.data)
            currentNode = currentNode.next
        temp = s[::-1]
        if s == temp:
            print("it is a palindrome.")
        else:
            print("it is not a palindrome.")



n = int(input("Enter the size: "))
i = 0
linked = Linkedlist()
while i<n:
    a = input("Enter a number: ")
    ans = Node(a)
    linked.insert(ans)
    i += 1
linked.printlist()
linked.ispalindrome()
        
