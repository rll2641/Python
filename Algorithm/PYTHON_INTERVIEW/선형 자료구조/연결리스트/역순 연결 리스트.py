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

list1 = Linked_List()
list2 = Linked_List()
for i in range(1, 6):
    list1.insert_last(i)
    list2.insert_last(i)

# 반복
node, pre = list1.head, None # node는 포인터 변경, pre는 이전 주소 저장
while node:
    pri, node.link = node.link, pre
    pre, node = node, pri

q = pre
while q:
    print(q.data, end=" ")
    q = q.link

# 재귀
def recursion_reverse(head):
    def reverse(node, pre = None):
        if not node:
            return pre
        pri, node.link = node.link, pre
        return reverse(pri, node)
    return reverse(list2.head)

list2.head = recursion_reverse(list2.head)
q = list2.head
while q:
    print(q.data, end=" ")
    q = q.link