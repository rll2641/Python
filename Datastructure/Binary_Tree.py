class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
n7 = Node(15)
n6 = Node(10)
n5 = Node(6)
n4 = Node(4)
n3 = Node(3, n6, n7)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

def preorder(root):
    if root != None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
        
preorder(n1)
print("")
inorder(n1)
print("")
postorder(n1)