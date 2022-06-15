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

linked_list1,linked_list2 = Linked_List(), Linked_List()
for i in range(3):
    n1, n2 = map(int, input().split())
    linked_list1.insert_last(n1)
    linked_list2.insert_last(n2)

# 연결리스트 요소를 덱에 저장 후, appendleft를 이용하여 역순 저장
from collections import deque
list1, list2 = deque([]), deque([])

q, p = linked_list1.head, linked_list2.head
while q:
    list1.appendleft(q.data)
    list2.appendleft(p.data)
    q, p = q.link, p.link

list1 = int("".join(map(str, list1)))
list2 = int("".join(map(str, list2)))
result = list(map(int, str(list1+list2)))

linked_list3 = Linked_List()
for i in result[::-1]:
    linked_list3.insert_last(i)

q = linked_list3.head
while q:
    print(q.data, end="->")
    q = q.link
    
# 연결리스트 뒤집어서 역순 저장
node, pre = linked_list1.head, None
while node:
    next, node.link = node.link, pre
    pre, node = node, next
linked_list1.head = pre
# 연결리스트를 리스트로 변환
q = linked_list1.head
list1 = []
while q:
    list1.append(q.data)
    q = q.link

# 리스트를 연결리스트로 변환
linked_list3 = Linked_List()
for i in list1:
    linked_list3.insert_last(i)

