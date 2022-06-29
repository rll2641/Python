from collections import defaultdict

class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.link = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hash_map = defaultdict(Node)
        
    def put(self, key, value):
        index = key % self.size
        if self.hash_map[index].value is None:
            self.hash_map[index] = Node(key, value)
            return
        
        # 충돌이 발생하는 경우
        p = self.hash_map[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.link is None:
                break
        p.link = Node(key, value)

    def get(self, key):
        index = key % self.size
        if self.hash_map[index].value is None:
            return -1
        
        # 노드가 존재할 때
        p = self.hash_map[index]
        while p:
            if p.key == key:
                return p.value
            p = p.link
        return -1
    
    def remove(self, key):
        index = key % self.size
        if self.hash_map[index].value is None:
            return
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.hash_map[index]
        if p.key == key:
            # p.link is None 유일한 노드일 경우 빈노드를 할당(defaultdict이기 때문)
            self.hash_map[index] = Node() if p.link is None else p.link
        
        # 연결리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.link = p.link
                return
        prev, p = p, p.link
        
    