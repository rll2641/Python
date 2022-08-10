# 연결리스트를 O(nlogn)에 정렬하라

nums = [-1, 5, 3, 4, 0]

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.link = new_node
            self.tail = new_node

# 연결리스트 생성 후 삽입
nlist = Linked_List()
for n in nums:
    nlist.insert(n)


# 두 정렬 리스트 병합
def mergeTwoList(l1: Node, l2: Node):
    if l1 and l2:
        if l1.data > l2.data:
            l1, l2 = l2, l1
        l1.link = mergeTwoList(l1.link, l2)
        
    return l1 or l2

def sortList(head: Node):
    if not (head and head.link):
        return head

# 런너 기법으로 연결리스트의 중간 지점 찾음 -> -1, 5 / 3, 4, 0
half, slow, fast = None, nlist.head, nlist.head
while fast and fast.link:
    half, slow, fast = slow, slow.link, fast.link.link
half.link = None

l1 = sortList(nlist.head)
l2 = sortList(slow)

# 내장 함수 풀이

def sortList2(head: Node):
    p = head
    lst = []
    
    while p:
        lst.append(p.data)
        p = p.link
    
    lst.sort()
    
# 병합 정렬 풀이 2

def merge_sort(arr: list):
    def sort(low, high): # low -> index 0 , high -> index len(arr)
        if high - low < 2:
            return
        mid = low + high // 2 # 리스트의 중간지점
        sort(low, mid) # list1의 중간 나누기
        sort(mid, high) # list2의 중간 나누기
        merge(low, mid, high)
    
    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        
        while l < mid and h < high:
            if arr[1] < arr[h]:
                temp.append(arr[1])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
                
        while l < mid:
            temp.append(arr[1])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        
        for i in range(low, high):
            arr[i] = temp[i - low]
    
    return sort(0, len(arr))