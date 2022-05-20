class Queue:
    def __init__(self, que_size):
        self.queue = [0 for _ in range(que_size)]
        self.que_size = que_size
        self.front = self.rear = 0
        
    def is_empty(self):
        return (self.front == self.rear)
    
    def is_full(self):
        return (self.front == (self.rear + 1) % self.que_size)
    
    def current_que_size(self):
        return len(self.queue)
    
    def enqueue(self, num):
        if self.is_full():
            print("queue is full")
            return
        else:
            self.rear = (self.rear + 1) % self.que_size
            self.queue[self.rear] = num
    
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        else:
            self.front = (self.front + 1) % self.que_size
            return self.queue[self.front]
        