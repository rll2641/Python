class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
class DLinked_list:
    def __init__(self):
        self.head = Node(None)
        self.head.left = self.head.right = self.head
        self.node_size = 0
    
    def dlist_size(self):
        return self.node_size
    
    def insert_node(self, pre, data):
        new_node = Node(data)
        new_node.left = pre
        new_node.right = pre.right
        new_node.left.right = new_node
        new_node.right.left = new_node
    
    def search(self, data):
        cur = self.head.right
        while cur != self.head:
            if cur.data == data:
                return cur
            cur = cur.right
        return None
    
    def delete_node(self, removed):
        if(removed == self.head):
            return
        removed.left.right = removed.right
        removed.right.left = removed.left
    
    def print_dlist(self):
        cur = self.head.right
        while cur != self.head:
            print(cur.data, end=" ")
            cur = cur.right
        
dl = DLinked_list()
dl.insert_node(dl.head, 5)
dl.insert_node(dl.head, 4)
dl.insert_node(dl.head, 3)
dl.insert_node(dl.head, 2)  
dl.insert_node(dl.head, 1)
dl.delete_node(dl.search(3))
dl.print_dlist()