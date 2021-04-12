class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def find_path(self,start,path,k):
        if start is None:
            return 
        path.append(start)
        if start.data == k:
            return True
        if start.left is not None and self.find_path(start.left,path,k) or start.right is not None and self.find_path(start.right,path,k):
            return True
        path.pop()
        return False

    def lowest(self,start,n1,n2):
        if start is None :
            return
        path1 = []
        path2 = []
        if not self.find_path(start,path1,n1) or not self.find_path(start,path2,n2):
             return -1
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1].data

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
print(tree.lowest(tree.root,n1,n2))
        
