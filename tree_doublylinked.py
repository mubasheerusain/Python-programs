class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class doubly:
    def __init__(self):
        self.head = None
   
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while True:
                if currentNode.right is None:
                    break
                currentNode = currentNode.right
            currentNode.right = newNode
            newNode.left = currentNode

    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                return
            print(currentNode.data)
            currentNode = currentNode.right

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def doubly_linked(self,start,traversal):
        if start:
            traversal.append(start.data)
            self.doubly_linked(start.left,traversal)
            self.doubly_linked(start.right,traversal)
        return traversal


tree = Tree(4)
tree.root.left = Node(2) 
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left =  Node(5)
tree.root.right.right = Node(7)
result = tree.doubly_linked(tree.root,[])
print(result)
linked = doubly()
for i in result:
    ans = Node(i)
    linked.insert(ans)
linked.printlist()





        
