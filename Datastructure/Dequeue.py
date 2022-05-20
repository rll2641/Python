from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque([])
        
    def deque_size(self):
        return len(self.deque)
    
    def is_empty(self):
        return (self.deque_size() == 0)
    
    def push_front(self, num):
        self.deque.appendleft(num)
        
    def push_rear(self, num):
        self.deque.append(num)
        
    def pop_front(self):
        return self.deque.popleft()
    
    def pop_rear(self):
        return self.deque.pop()
    
    def front(self):
        return self.deque[0]
    
    def rear(self):
        return self.deque[self.deque_size() - 1]
    
class DEQUE:
    def __init__(self, deq_size):
        self.deque = [0 for _ in range(deq_size)]
        self.deque_size = deq_size
        self.front = self.rear = 0
    
    def is_empty(self):
        return (self.front == self.rear)
    
    def is_full(self):
        return self.front == ((self.rear + 1) % self.deque_size)
    
    def deque_size(self):
        return len(self.deque)
    
    def push_front(self, num):
        if self.is_full():
            print("deque is full")
            return
        else:
            self.deque[self.front] = num
            self.front = (self.front - 1 + self.deque_size) % self.deque_size
    
    def push_rear(self, num):
        if self.is_full():
            print("deque is full")
            return
        else:
            self.rear = (self.rear + 1) % self.deque_size
            self.deque[self.rear] = num
            
    def pop_front(self):
        if self.is_empty():
            print("deque is empty")
            return
        else:
            self.front = (self.front + 1) % self.deque_size
            return self.deque[self.front]
    
    def pop_rear(self):
        if self.is_empty():
            print("deque is empty")
            return
        else:
            data = self.deque[self.rear]
            self.rear = (self.rear - 1 + self.deque_size) % self.deque_size
            return data
    
    
    