class QueuesList():
    def __init__(self):
        self.L=[]

    def enqueue(self,value):
        self.L.append(value)

    def dequeu(self):
        if self.L==None
            return None
        else:
            return self.L.pop(0)

    def peek(self):
        if self.isEmpty():
            raise ValueError("Queue Empty")
        return self.L[0]

    def isEmpty(self):
        return len(self.L)==0
