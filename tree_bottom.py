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
            self._insert(data,self.root)

    def _insert(self,data,start):
         if data < start.data:
             if start.left is None:
                 start.left = Node(data)
             else:
                 self._insert(data,start.left)
         elif data > start.data:
             if start.right is None:
                 start.right = Node(data)
             else:
                 self._insert(data,start.right)

    def bottom(self,start,traversal):
        if start is None:
            return
        a = []
        a.insert(0,start)
        while len(a) > 0:
            node = a.pop()
            if node.left:
                a.insert(0,node.left)
            else:
                if node.data not in traversal:
                    traversal.append(node.data)
            if node.right:
                a.insert(0,node.right) 
            else:
                if node.data not in traversal:
                    traversal.append(node.data)
        return traversal
         



tree = Tree(20)
tree.root.left = Node(8)
tree.root.right = Node(22)
tree.root.left.left = Node(5)
tree.root.left.right = Node(3)
tree.root.left.right.left = Node(10)
tree.root.right.left = Node(4)
tree.root.right.right = Node(25)
tree.root.left.right.right = Node(14)
"""
n = int(input("Enter the number of inputs: "))
tree = Tree()
i = 0
while i < n:
    s = int(input("Enter number: "))
    tree.insert(s)
    i += 1
"""
print(tree.bottom(tree.root,[]))

