'''
 Aplicação queue:
    Tudo que se pareça com uma fila.

'''

class Queue:

    def __init__(self, cap):
        self.cap = cap
        self.front = self.size = 0
        self.back = cap - 1
        self.arr = [None] * cap

    def isFull(self):
        if self.size == self.cap:
            print("Queue Full")
            return True
        return False

    def isEmpty(self):
        if self.size == 0:
            print("is Empty")
            return True
        return False
    
    def enqueue(self, item):
        if self.isFull():
            return
        self.back = (self.back + 1) % (self.cap)
        self.arr[self.back] = item
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return
        self.front = (self.front + 1) % (self.cap)
        self.size -= 1
    
    def qfront(self):
        return self.arr[self.front]
    
    def qback(self):
        return self.arr[self.back]
    

q = Queue(5)

for i in range(0, 5):
    q.enqueue(i)

print(q.qfront())
q.dequeue()
print(q.qfront())
print(q.arr)