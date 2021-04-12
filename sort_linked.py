class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next =  newNode

    def merge(self,left,right):
        result = None
        if left == None:
            return right
        if right == None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next,right)
        else:
            result = right
            result.next = self.merge(left,right.next)
        return result
        

    def merge_sort(self,n):
        head = n
        if head is None or head.next is None:
            return head
        middle = self.get_middle(head)
        temp = middle.next
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(temp)
        lis = self.merge(left,right)
        return lis


    def get_middle(self,head):
        if head == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow


    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next



n = int(input("Enter the size: "))
i = 0
linked = Linkedlist()
while i<n:
    s = int(input("Enter the number: "))
    ans = Node(s)
    linked.insert(ans)
    i += 1
linked.printlist()
linked.head = linked.merge_sort(linked.head)
linked.printlist()
