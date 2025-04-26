class Queues:
    def __init__(self,k):
        self.queue=None*k
        self.front=-1
        self.rear=-1
        self.size=0
        self.capacity=k

    def enqueue(self,value):
        if self.isFull():
            print("Full")
            return False
        self.queue[self.rear]=value
        self.rear=(self.rear+1)%self.capacity
        self.size+=1
        return True
    def dequeu(self):
        if self.isEmpty():
            print("Empty Queue")
            return False
        removed = self.queue[self.front]
        self.queue[self.front]=None
        self.front=(self.front+1)%self.capacity
        self.size -= 1
        return removed
    def peek(self):
        if self.isEmpty():
            print("Queueu empty")
            return None
        return self.queue[self.front]

    def isFull(self):
        return self.size == self.capacity
    def isEmpty(self):
        return self.size==0
    