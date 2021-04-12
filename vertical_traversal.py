class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)
  
    def _insert(self,currentNode,data):
        if data < currentNode.data:
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self._insert(currentNode.left,data)
        elif data > currentNode.data:
            if currentNode.right is None:
                currentNode.right = Node(data)
            else:
                self._insert(currentNode.right,data)

    def find_min_max(self,start,minimum,maximum,hd):
        if start is None:
            return
        if hd < minimum[0]:
            minimum[0] = hd
        elif hd > maximum[0]:
            maximum[0] = hd
        self.find_min_max(start.left,minimum,maximum,hd-1)
        self.find_min_max(start.right,minimum,maximum,hd+1)

    def print_vertical(self,start,line_no,hd):
        result = ""
        if start is None:
            return
        if hd == line_no:
            print(str(start.data)+"->"+str(line_no))
        self.print_vertical(start.left,line_no,hd-1)
        self.print_vertical(start.right,line_no,hd+1)
        return result

    def vertical_traversal(self,start):
        maximum = [0]
        minimum = [0]
        self.find_min_max(start,minimum,maximum,0)
        for line_no in range(minimum[0],maximum[0]+1):
            self.print_vertical(start,line_no,0)
            

    def print_tree(self,start,traversal):
        if start:
            traversal += str(start.data)+"-"
            traversal = self.print_tree(start.left,traversal)
            traversal = self.print_tree(start.right,traversal)
        return traversal

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.left.right = Node(8)
tree.root.right.right.right = Node(9)
tree.vertical_traversal(tree.root)
"""
n = int(input("Enter size: "))
tree = Tree()
i = 0
while i<n:
    s = int(input("Enter number: "))
    tree.insert(s)
    i += 1
print(tree.print_tree(tree.root,""))
print("vertical Traversal: ")
tree.vertical_traversal(tree.root)
"""
