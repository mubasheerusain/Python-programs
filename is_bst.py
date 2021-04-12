class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def is_bst(self,start):
        if start == None:
            return
        if start.left:
            if start.data > start.left.data:
                self.is_bst(start.left)
            else:
                return "Not a Bst"
        if start.right:
            if start.data < start.right.data:
                self.is_bst(start.right)
            else:
                return "Not a Bst"
        return "It is a Bst"
        

    




tree = Tree(4)
tree.root.left = Node(2)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)
print(tree.is_bst(tree.root))


