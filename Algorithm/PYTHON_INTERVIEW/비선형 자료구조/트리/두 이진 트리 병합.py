class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def mergeTwoTree(t1, t2):
    if t1 and t2:
        node = Node(t1.data + t2.data)
        node.left = mergeTwoTree(t1.left, t2.left)
        node.right = mergeTwoTree(t1.right, t2.right)
        
        return node
    else:
        return t1 or t2
