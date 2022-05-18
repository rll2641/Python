# 노드 생성
class Node:
    # 주소의 초기값은 None
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    # 헤드와 테일, 사이즈 초기화
    def __init__(self):
        self.head = self.tail = None
        self.node_count = 0
    # 리스트 사이즈 반환
    def list_size(self):
        return self.node_count
    # 맨 앞에 삽입
    def insert_first(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = self.tail = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    # 맨 뒤에 삽입
    def insert_last(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = self.tail = new_node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
    # 연결리스트 중간 삽입
    def insert_next(self, pos, data):
        new_node = Node(data)
        new_node.next = pos.next
        pos.next = new_node
    # 삭제
    def delete_node(self, data):
        pre = self.search_list(data)
        removed = pre.next
        item = removed.data
        
        pre.next = removed.next
        return item
    # 연결리스트 탐색
    def search_list(self, data):
        search = self.head
        while search:
            if search.next.data == data:
                return search
            search = search.next
        return None
    # 연결리스트 출력
    def print_list(self):
        if self.head == None:
            print("list is empty")
        else:
            cur = self.head
            while cur:
                print(cur.data, end=" ")
                cur = cur.next
                
ll = LinkedList()
ll.insert_first(3)
ll.insert_first(2)
ll.insert_first(1)
ll.insert_last(5)

save = ll.search_list(5)
ll.insert_next(save, 4)
ll.delete_node(4)

ll.print_list()