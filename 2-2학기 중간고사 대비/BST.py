class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    # 반복문
    def search_node(self, data):
        node = self.root
        while True:
            if node is None:
                return -1
            elif data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right
    
    def insert_node(self, data):
        node = self.root
        
        while True:
            if node is None:
                self.root = Node(data)
                break
            if data < node.data:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = Node(data)
                    break
            elif data > node.data:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = Node(data)
                    break
                
    # 재귀
    def search_node_(self, root, data):
        if root is None:
            return None
        if data == root.data:
            return root
        elif data < root.data:
            return self.search_node_(root.left, data)
        else:
            return self.search_node_(root.right, data)
        
    def insert_node_(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert_node_(root.left, data)
        else:
            root.right = self.insert_node_(root.right, data)
        
        return root
    
    # 삭제
    def get_min(self, node):
        min_val = node.data
        
        while node.left:
            min_val = node.left.data
            node = node.left
        return min_val
    
    def delete_node(self, node, data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self.delete_node(node.left, data)
        elif data > node.data:
            node.right = self.delete_node(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            node.data = self.get_min(node.right)
            node.right = self.delete_node(node.right, node.data)
        return node

# 순회       
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
        
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# 예시

roop_bst = BST()
recursion_bst = BST()

tree = [10, 5, 15, 19, 3, 6, 14]

for i in tree:
    roop_bst.insert_node(i)
    recursion_bst.root = recursion_bst.insert_node_(recursion_bst.root, i)

roop_bst.delete_node(roop_bst.root, 5)

preorder(roop_bst.root)
print("")
preorder(recursion_bst.root)