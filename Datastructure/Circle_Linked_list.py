# 노드 생성
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Circle_list:
    def __init__(self):
        self.head = self.tail = None
        self.node_size = 0
    
    def list_size(self):
        return self.node_size
    
    def insert_first(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def insert_last(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
    
    def print_list(self):
        cur = self.head
        while cur != self.tail:
            print(cur.data)
            cur = cur.next
        print(cur.data)
        
c = Circle_list()
c.insert_first(3)
c.insert_first(2)
c.insert_first(1)
c.print_list()