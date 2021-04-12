class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)


    def preorder(self,start,traversal):
        if start:
            traversal += str(start.data)+"-"
            traversal = self.preorder(start.left,traversal)
            traversal = self.preorder(start.right,traversal)
        return traversal
   
    def inorder(self,start,traversal):
        if start:
            traversal = self.inorder(start.left,traversal)
            traversal += str(start.data)+"-"
            traversal = self.inorder(start.right,traversal)
        return traversal

    def postorder(self,start,traversal):
        if start:
            traversal =self.postorder(start.left,traversal)
            traversal =self.postorder(start.right,traversal)
            traversal += str(start.data)+"-"
        return traversal
    
    def left_view(self,start,traversal):
        if start:
            traversal = self.left_view(start.left,traversal)
            traversal += str(start.data)+"-"
        return traversal
"""
       1
      / \
     2   5
    / \ / \
   3  4 6  7
  / \
 8   9
"""
tree = Tree(1)
tree.root.left = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)

print(tree.postorder(tree.root,""))
