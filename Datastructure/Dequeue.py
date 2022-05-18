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