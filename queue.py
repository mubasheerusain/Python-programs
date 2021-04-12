class Arrayqueue:
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0
 
    def enqueue(self,data):
        self.data.append(data)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("It is empty")
        value = self.data[self.front]
        del self.data[self.front]
        #self.data[self.front] = None
        self.front += 1
        self.size -= 1
        return value


n = int(input("Enter the size: "))
i = 0
q = Arrayqueue()
while n > i:
    a = int(input("Enter a number: "))
    q.enqueue(a)
    i = i + 1
print(q.data)
q.dequeue()
print(q.data)
