class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

longest = 0

def diameterOfBinaryTree(root):
    def dfs(node):
        if not node:
            return -1
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        longest = max(longest, left + right + 2)
        return max(left, right) + 1
    
    dfs(root)
    return longest

print(diameterOfBinaryTree(root))