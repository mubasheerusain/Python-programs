class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def print_tree(self,start,traversal):
        if start:
            traversal = self.print_tree(start.left,traversal)
            traversal += str(start.data)+"-"
            traversal = self.print_tree(start.right,traversal)
        return traversal

    def height_tree(self,start):
        if start is None:
            return -1
        start.left = self.height_tree(start.left)
        start.right = self.height_tree(start.right)
        return 1 + max(start.left,start.right)
            
    def size_tree(self,start):
        a = []
        size = 0
        a.insert(0,start)
        while len(a) > 0:
            size += 1
            node = a.pop()
            if node.left:
                a.insert(0,node.left)
            if node.right:
                a.insert(0,node.right)
        return size
        
        




tree = Tree(1)
tree.root.left = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.left.left.left = Node(5)
tree.root.right = Node(6)
tree.root.right.left = Node(7)
tree.root.right.right = Node(8)
print("size is "+str(tree.size_tree(tree.root)))
print(tree.print_tree(tree.root,""))
print("The height of the tree is "+str(tree.height_tree(tree.root)))


