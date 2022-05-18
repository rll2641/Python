class Node:
    def __init__(self, data, llink = None, rlink = None):
        self.data = data
        self.llink = llink
        self.rlink = rlink
        
class Linked_list:
    def __init__(self):
        self.head = Node(None)
        self.head.llink = self.head.rlink = self.head
        
    def list_size(self):
        return self.node_count
    
    # pre주소값 뒤에 삽입
    def insert(self, pre, data):
        new_node = Node(data)
        new_node.llink = pre
        new_node.rlink = pre.rlink
        new_node.llink.rlink = new_node
        new_node.rlink.llink = new_node
    
    def print_list(self):
        cur = self.head.rlink
        while cur != self.head:
            print(cur.data, end=" ")
            cur = cur.rlink
    
dl = Linked_list()

dl.insert(dl.head, 5)
dl.insert(dl.head, 3)
dl.insert(dl.head, 2)
dl.insert(dl.head, 1)

dl.print_list()