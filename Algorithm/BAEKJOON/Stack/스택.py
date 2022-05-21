import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.stack_size = 0
        
    def is_empty(self):
        if self.stack_size == 0:
            return 1
        else:
            return 0
    
    def stack_size_(self):
        return self.stack_size
    
    def push(self, data):
        self.stack.append(data)
        self.stack_size += 1
        
    def pop(self):
        if self.is_empty():
            return -1
        else:
            self.stack_size -= 1
            return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            return -1
        else:
            return self.stack[self.stack_size - 1]

stack = Stack()
n = int(sys.stdin.readline())
for i in range(n):
    option = sys.stdin.readline().split()
    if option[0] == "push":
        stack.push(option[1])
    elif option[0] == "pop":
        print(stack.pop())
    elif option[0] == "size":
        print(stack.stack_size_())
    elif option[0] == "empty":
        print(stack.is_empty())
    elif option[0] == "top":
        print(stack.top())
