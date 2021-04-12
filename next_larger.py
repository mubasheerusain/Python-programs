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

   
    def larger(self):
        currentNode = self.head
        a = []
        while True:
            if currentNode is None:
                break
            a.append(currentNode.data)
            currentNode = currentNode.next
        a.sort()
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            index = a.index(currentNode.data)
            if index < len(a)-1: 
                print(currentNode.data,"->",a[index+1])
            else:
                print(currentNode.data,"->",-1)
            currentNode = currentNode.next
            

    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


n = int(input("Enter the size: "))
i = 0
st = stack()
while i<n:
    s = int(input("Enter a number: "))
    ans = Node(s)
    st.push(ans)
    i += 1
st.printlist()
st.larger()
