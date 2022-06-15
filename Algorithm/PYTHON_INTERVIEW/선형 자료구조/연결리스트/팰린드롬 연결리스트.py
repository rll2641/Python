from collections import deque

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.link = next

class Linked_List:
    def __init__(self):
        self.head = self.tail = None
    
    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.link = new_node
        else:
            self.tail.link = self.tail = new_node

# 덱 이용
que, lst = deque([]), Linked_List()
nums = [1,2,2]
for i in nums:
    lst.insert_last(i)
q = lst.head
while q:
    que.append(q.data)
    q = q.link

while len(que) > 1:
    if que.popleft() != que.pop():
        print('no')
        exit(0)
print('yes')

# 런너
slow = fast = lst.head
rev = None
while fast and fast.link:
    fast = fast.link.link
    rev, rev.link, slow = slow, rev, slow.link

if fast:
    slow = slow.link

# slow와 rev의 이동으로 팰린드롬 확인
while rev and rev.data == slow.val:
    slow, rev = slow.link, rev.link