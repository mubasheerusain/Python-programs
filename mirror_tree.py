class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def is_mirror(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        if node1 and node2 is not None:
            if node1.data == node2.data:
                return self.is_mirror(node1.left,node2.right) and self.is_mirror(node1.right,node2.left)
        return False

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.right.left = Node(8)
tree.root.right.right = Node(3)
print(tree.is_mirror(tree.root,tree.root))
