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
            return self.stack.pop()

    def top(self):
        if self.is_empty():
            return False
        else:
            return self.stack[self.stack_size - 1]
        
while True:
    stack = Stack()
    vps = input()
    is_vps = True
    if vps == '.':
        break
    else:
        vps = list(vps)
        
        for i in vps:
            if i == '(' or i == '[':
                stack.push(i)
            elif i == ')':
                if stack.is_empty() or stack.pop() != '(':
                    is_vps = False
                    break
            elif i == ']':
                if stack.is_empty() or stack.pop() != '[':
                    is_vps = False
                    break
        
        if is_vps and stack.is_empty():
            print('yes')
        else:
            print('no')