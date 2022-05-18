class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
class BST:
    def __init__(self):
        self.root = None
    
    # 반복문으로 탐색
    def search_node(self, value):
        node = self.root
        while True:
            if node is None:
                return -1
            elif value == node.value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
    
    # 재귀문으로 탐색
    def search_node_(self, root, value):
        if root is None:
            return None
        if root.value == value:
            return root
        elif value < root.value:
            return self.search_node_(root.left, value)
        else:
            return self.search_node_(root.right, value)
    
    # 반복문 노드 삽입
    def insert_node(self, root, value):
        current_node = root
        
        while True:
            if current_node is None:
                self.root = Node(value)
                break
            if value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    break
            elif value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    break
    
    # 재귀문으로 삽입    
    def insert_node_(self, root, value):
        current_node = root
        
        if current_node is None: return Node(value)
        if value < current_node.value:
            current_node.left = self.insert_node_(current_node.left, value)
        else:
            current_node.right = self.insert_node_(current_node.right, value)
        
        return current_node
            
def preorder(root):
    if root is not None:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

bst = BST()
bst_ = BST()

tree = [10, 5, 15, 19, 3, 6, 14]
for i in tree:
    bst.insert_node(bst.root, i)

for i in tree:
    bst_.root = bst_.insert_node_(bst_.root, i)
    
preorder(bst.root)
print("")
preorder(bst_.root)