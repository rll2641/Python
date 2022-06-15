class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link
        
class Linked_List:
    def __init__(self):
        self.head = self.tail =None
    
    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.link = self.tail = new_node
            
linked_list = Linked_List()
linked_list2 = Linked_List()
for i in range(1,9):
    linked_list.insert_last(i)
    linked_list2.insert_last(i)

# 값만 교환
'''
q = linked_list.head
while q and q.link:
    q.data, q.link.data = q.link.data, q.data
    q = q.link.link
'''
# 반복 
# b는 헤드앞에 pre는 헤드뒤에 존재하면서 스왑해준다.
root = pre = Node(None)
while linked_list.head and linked_list.head.link:
    b = linked_list.head.link
    linked_list.head.link = b.link
    b.link = linked_list.head
    
    pre.link = b
    
    linked_list.head = linked_list.head.link
    pre = pre.link.link
q = root.link
while q:
    print(q.data, end=" ")
    q = q.link

# 재귀
# 매개변수 head가 None이 나올때 까지 재귀호출. 
# p는 항상 head앞에 존재하면서 포인터를 head로 전환
def recursion_swap(head):
    if head and head.link:
        p = head.link
        head.link = recursion_swap(p.link)
        p.link = head
        return p
    return head

linked_list2.head = recursion_swap(linked_list2.head)
q = linked_list2.head
while q:
    print(q.data, end=" ")
    q = q.link