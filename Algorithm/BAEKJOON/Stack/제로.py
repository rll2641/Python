import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.stack_size = 0
    
    def is_empty(self):
        return (self.stack_size == 0)

    def push(self, data):
        self.stack.append(data)
        self.stack_size += 1
    
    def pop(self):
        if self.is_empty():
            return False
        else:
            self.stack_size -= 1
            self.stack.pop()

stack = Stack()
k = int(sys.stdin.readline())
for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.push(num)

print(sum(stack.stack))