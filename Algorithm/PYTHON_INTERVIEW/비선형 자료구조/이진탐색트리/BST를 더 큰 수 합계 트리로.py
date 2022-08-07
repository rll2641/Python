# BST의 각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라

nums = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
class Solution:
    val = 0
    
    def bstToGST(self, root):
        if root:
            self.bstToGST(root.right)
            self.val += root.data
            root.data = self.val
            self.bstToGST(root.left)
        
        return root