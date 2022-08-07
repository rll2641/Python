# 두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력
import sys
root = [4, 2, 6, 1, 3, None, None] # 1

# 재귀
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class Soultion:
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.data - self.prev)
        self.prev = root.data
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result

# 반복
def minDiffinBST(root):
    prev = -sys.maxsize
    result = sys.maxsize
    
    stack = []
    node = root
    
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
            
        node = stack.pop()
        
        result = min(result, node.data - prev)
        prev = node.data
        
        node = node.right
    
    return result