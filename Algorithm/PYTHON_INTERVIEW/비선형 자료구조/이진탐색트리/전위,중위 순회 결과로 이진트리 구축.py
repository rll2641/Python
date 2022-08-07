preorder_result = [3, 9, 20, 15, 7]
inorder_reuslt = [9, 3, 15, 20, 7]

class Node:
    def __init_(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        
        node = Node(inorder[index]) # 루트노드
        node.left = buildTree(preorder, inorder[:index])
        node.right = buildTree(preorder, inorder[index+1:])
        
    return node