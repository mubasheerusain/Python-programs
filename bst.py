class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            currentNode = self.root
            self._insert(data,currentNode)

    def _insert(self,data,currentNode):
        if data < currentNode.data:
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self._insert(data,currentNode.left)
        elif data > currentNode.data:
            if currentNode.right is None:
                currentNode.right = Node(data)
            else:
                self._insert(data,currentNode.right)
        else:
            print("The number you have entered is already present.")

    def find(self,data):
        if self.root is None:
            print("tree is empty.")
        else:
            if self._find(data,self.root):
                return "Found"
            return "Not Found"

    def _find(self,data,currentNode):
        if data < currentNode.data and currentNode.left:
            if currentNode.left.data == data:
                return True
            else:
                return self._find(data,currentNode.left)
        elif data > currentNode.data and currentNode.right:
            if currentNode.right.data == data:
                return True
            else:
                return self._find(data,currentNode.right)
        
    def print_tree(self,start,traversal):
        if start:
            traversal += str(start.data)+"-"
            traversal = self.print_tree(start.left,traversal)
            traversal = self.print_tree(start.right,traversal)
        return traversal
        



n = int(input("Enter the number of input: "))
i = 0
tree = BST()
while i < n:
    s = int(input("Enter the number :"))
    tree.insert(s)
    i += 1
print(tree.print_tree(tree.root,""))
a = int(input("Enter a number: "))
result = tree.find(a)
print(result)
      
