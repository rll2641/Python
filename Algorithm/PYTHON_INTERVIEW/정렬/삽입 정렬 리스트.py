class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

# 삽입 정렬
def insertionSortList(head: Node):
    cur = parent = Node(None) # cur 정렬 끝난 대상, parent는 항상 루트를 가르킴
    
    while head: # head 정렬 해야 할 대상
        while cur.link and cur.link.data < head.data:
            cur = cur.link
    
        cur.link, head.link, head = head, cur.link, head.link
        cur = parent
    
    return cur.link # 루트(첫번 째, 요소 주소) 주소 반환

# 삽입 정렬 최적화 (비교 조건 개선)

def insertionSortList2(head: Node):
    cur = parent = Node(0)
    
    while head:
        while cur.link and cur.link.data < head.data:
            cur = cur.link
    
        cur.link, head.link, head = head, cur.link, head.link
        
        if head and cur.data > head.data: # 만약 다음번 head도 cur보다 큰 상태라면 돌아가지 않는다.(시간단축)
            cur = parent
    
    return cur.link
    
