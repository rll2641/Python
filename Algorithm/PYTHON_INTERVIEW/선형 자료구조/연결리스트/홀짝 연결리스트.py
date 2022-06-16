class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link
    
class Linked_List:
    def __init__(self):
        self.head = self.tail = None
    
    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.link = self.tail = new_node
            
list1 = Linked_List()
for i in range(1, 6):
    list1.insert_last(i)

def oddEvenList(head):
    odd = head
    even = head.link
    even_head = head.link
    
    while even and even.link:
        #  2칸 앞에 있는 노드의 주소 저장 ex) 1->3 2->4
        odd.link, even.link = odd.link.link, even.link.link
        
        odd, even = odd.link, even.link
    
    odd.link = even_head
    return head

list1.head = oddEvenList(list1.head)
q = list1.head
while q:
    print(q.data, end=" ")
    q = q.link