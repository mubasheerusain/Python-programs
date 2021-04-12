class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def is_identical(self,start1,start2):
        if start1 and start2 is None:
            return True
        a = []
        b = []
        a.insert(0,start1)
        b.insert(0,start2)
        while a and b is not None:
            node1 = a.pop()
            node2 = b.pop()
            if node1.data != node2.data:
                break
            if node1.left and node2.left:
                self.is_identical(node1.left,node2.left)
            if node1.right and node2.right:
                self.is_identical(node1.right,node2.right)
        return False
        


           
tree = Tree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)


tree1 = Tree(4)
tree1.root.left = Node(2)
tree1.root.right = Node(6)
tree1.root.left.left = Node(1)
tree1.root.left.right = Node(9)
tree1.root.right.left = Node(5)
tree1.root.right.right = Node(7)

print(tree.is_identical(tree.root,tree1.root))

