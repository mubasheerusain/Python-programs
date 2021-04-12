class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self,data):
        self.queue.insert(0,data)
        self.size += 1
  
    def is_empty(self):
        return self.size == 0

    def dequeue(self):
        if self.is_empty():
            return
        self.size -= 1
        return self.queue.pop()

    def peek(self):
        if self.is_empty():
            return
        return self.queue[-1].data

    def _len(self):
        return self.size


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def reverse_level_order(self,start):
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while queue._len() > 0:
            traversal += str(queue.peek())+"-"
            node = queue.dequeue()
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        return traversal[::-1]


tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.reverse_level_order(tree.root))
    
