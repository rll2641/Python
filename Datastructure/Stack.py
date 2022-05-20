class Stack:
    def __init__(self):
        self.stack = []
        
    def stack_size(self):
        return len(self.stack)
    
    def is_empty(self):
        return (self.stack_size() == 0)
    
    def push(self, num):
        self.stack.append(num)
        
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return self.stack.pop()
        
    