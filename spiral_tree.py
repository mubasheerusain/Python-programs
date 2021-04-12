class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def spiral_print(self,start):
        s1 = []
        s2 = []
        s1.append(start)
        while not len(s1) == 0 or not len(s2) == 0:
            while not len(s1) == 0:
                node = s1.pop()
                print(node.data)
                if node.right:
                    s2.append(node.right)
                if node.left:
                    s2.append(node.left)
            while not len(s2) == 0:
                node = s2.pop()
                print(node.data)
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)



tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(7)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(4)
tree.spiral_print(tree.root)
        
