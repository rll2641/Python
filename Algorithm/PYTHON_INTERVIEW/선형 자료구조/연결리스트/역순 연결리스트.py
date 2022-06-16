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

# m~n(인덱스)까지 역순
m, n = map(int, input().split())

# m~n의 역순은 m-1의 주소f를 알아야한다.
root = start = Node(None) 
root.link = list1.head
for _ in range(m - 1):
    start = start.link
end = start.link

for _ in range(n - m):
    tmp, start.link, end.link = start.link, end.link, end.link.link
    start.link.link = tmp

list1.head = root.link
q = list1.head
while q:
    print(q.data, end=" ")
    q = q.link