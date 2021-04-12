class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)
        

    def max_path(self,start):
        self.maximum = float('-inf')
  
        def dfs(start):
            if start is None:
                return 0
            l = max(0,self.max_path(start.left))
            r = max(0,self.max_path(start.right))
            self.maximum = max(self.maximum, l+r+start.data)
            return max(l,r)+start.data
        dfs(start)
        return self.maximum

tree = Tree(10)
tree.root.left = Node(2)
tree.root.right = Node(10)
tree.root.left.left = Node(20)
tree.root.left.right = Node(1)
tree.root.right.right = Node(-25)
tree.root.right.right.left = Node(3)
tree.root.right.right.right = Node(4)
print(tree.max_path(tree.root))
