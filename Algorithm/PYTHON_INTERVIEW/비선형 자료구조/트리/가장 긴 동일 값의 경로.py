class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(1)
root.right.right = Node(5)

result = 0

def longestValue(root):
    def dfs(node):
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0 
        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0
            
        result = max(result, left + right)
        return max(left, right)
    
    dfs(root)
    return result

print(longestValue(root))