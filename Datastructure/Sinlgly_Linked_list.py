class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class Singly_list:
    def __init__(self):
        self.head = self.tail = None
        self.node_count = 0
    
    def list_size(self):
        return self.node_count
    
    def insert_first(self, data):
        new_node = Node(data)
        new_node.data = data
        new_node.link = self.head
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.head = new_node
        self.node_count += 1
    
    def insert_last(self, data):
        new_node = Node(data)
        new_node.data = data
        new_node.link = None
        self.tail.link = new_node
        self.tail = new_node
        self.node_count += 1
    
    def insert(self, pos, data):
        new_node = Node(data)
        new_node.data = data
        new_node.link = pos.link
        pos.link = new_node
        self.node_count += 1
    
    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.link
        return False

    def delete_node(self, data):
        pos = self.search(data)
        removed = pos.link
        pos.link = removed.link
        self.node_count -= 1
        return removed.data
    
    def print_list(self):
        cur = self.head
        
        while cur:
            print(cur.data, end=" ")
            cur = cur.link