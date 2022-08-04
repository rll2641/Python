class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

# 파이썬다운 방식
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root
    return None

# bfs
from collections import deque
def invertTreeBfs(root):
    que = deque([root])
    
    while que:
        node = que.popleft()
        
        if node:
            node.left, node.right = node.right, node.left
            
            que.append(node.left)
            que.append(node.right)
    
    return root

# 반복구조로 dfs
def invertTree(root):
    stack = deque([root])
    
    while stack:
        node = stack.pop()
        
        if node:
            node.left, node.right = node.right, node.left
            
            stack.append(node.left)
            stack.append(node.right)
            
    return root