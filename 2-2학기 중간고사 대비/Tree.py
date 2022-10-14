class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

n6 = Node(25)
n5 = Node(16)
n4 = Node(1)
n3 = Node(20, n5, n6)
n2 = Node(4, n4)
n1 = Node(15, n2, n3)

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
        
print(preorder(n1))

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print(inorder(n1))

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
        
print(postorder(n1))