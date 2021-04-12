class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.nextright = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def connect(self,start):
        queue = []
        queue.append(start)
        queue.append(None)
        while queue:
            node = queue.pop(0)
            if node:
                node.nextright = queue[0]
                #print(str(node)+"->"+str(node.nextright))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            elif queue:
                queue.append(None)


tree = Tree(10)
tree.root.left = Node(8)
tree.root.right = Node(2)
tree.root.left.left = Node(3)
tree.root.right.right = Node(90)
tree.connect(tree.root)
if tree.root.nextright != None:
    print("nextright of %d is %d\n" %(tree.root.data,tree.root.nextright.data))
else:
    print("nextright of %d is %d\n" %(tree.root.data,-1))
if tree.root.left.nextright != None:
    print("nextright of %d is %d\n" %(tree.root.left.data,tree.root.left.nextright.data))
else:
    print("nextright of %d is %d\n" %(tree.root.left.data,-1))
if tree.root.right.nextright != None:
    print("nextright of %d is %d\n" %(tree.root.right.data,tree.root.right.nextright.data))
else:
    print("nextright of %d is %d\n" %(tree.root.right.data,-1))
if tree.root.left.left.nextright != None:
    print("nextright of %d is %d\n" %(tree.root.left.left.data,tree.root.left.left.nextright.data))
else:
    print("nextright of %d is %d\n" %(tree.root.left.left.data,-1))
if tree.root.right.right.nextright != None:
    print("nextright of %d is %d\n" %(tree.root.right.right.data,tree.root.right.right.nextright))
else:
    print("nextright of %d is %d\n" %(tree.root.right.right.data,-1))

