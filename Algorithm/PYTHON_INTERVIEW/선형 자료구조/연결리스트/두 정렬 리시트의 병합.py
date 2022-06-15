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
            new_node.link = new_node
        else:
            self.tail = self.tail.link = new_node

lst1 = Linked_List()
lst2 = Linked_List()

for i in range(3):
    n1, n2 = map(int, input().split())
    lst1.insert_last(n1)
    lst2.insert_last(n2)
    
# 재귀 lst1, lst2 두 포인터가 전부 널을 가르킬 때 까지 재귀반복
# lst1의 데이터가 lst2의 데이터보다 더 크거나 현재lst1이 가르키는 것이 none이면(다른 리스트에는 값이 있을 수 잇으니) 둘이 스왑 후, lst1의 link를 변경
def mergeTwoLists(lst1, lst2):
    # 조건 list1이 비어있거나 (list2가 비어 있지 않으며, list1의 데이터가 list2의 데이터보다 클 때) 실행
    if not lst1 or (lst2 and lst1.data > lst2.data):
        lst1, lst2 = lst2, lst1
    # list1이 비어있지 않을 때
    if lst1:
        lst1.link = mergeTwoLists(lst1.link, lst2)
    return lst1