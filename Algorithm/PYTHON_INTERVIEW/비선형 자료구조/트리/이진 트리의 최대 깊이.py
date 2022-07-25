from collections import deque

trees = [3, 9, 20, None, None, 15, 7]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

def maxDepth(root):
    que = deque([root])
    depth = 0
    
    while que:
        depth += 1
        
        for _ in range(len(que)):
            cur_root = que.popleft()
            if cur_root.left:
                que.append(cur_root.left)
            if cur_root.right:
                que.append(cur_root.right)

print(maxDepth(root))