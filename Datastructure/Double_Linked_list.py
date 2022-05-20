class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
class Dlinked_list:
    def __init__(self):
        self.head = Node(None)
        self.head.left = self.head.right = self.head
        self.node_count = 0
    
    def list_size(self):
        return self.node_count
    
    def insert_node(self, pre, data):
        new_node = Node(data)
        new_node.left = pre
        new_node.right = pre.right
        new_node.left.right = new_node
        new_node.right.left = new_node
        self.node_count += 1
    
    def search_list(self, data):
        cur = self.head.right
        while cur is not self.head:
            if cur.data == data:
                return cur
            cur = cur.right
        return None
    
    def delete_node(self, data):
        removed = self.search_list(data)
        if removed is self.head: return
        removed.left.right = removed.right
        removed.right.left = removed.left
    
    def print_list(self):
        cur = self.head.right
        while cur is not self.head:
            print(cur.data, end=" ")
            cur = cur.right
            
    