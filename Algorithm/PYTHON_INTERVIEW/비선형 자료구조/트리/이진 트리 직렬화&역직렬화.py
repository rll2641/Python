from collections import deque

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

# 직렬화
def serialize(root):
    que = deque([root])
    result = list()
    
    while que:
        node = que.popleft()
        
        if node:
            que.append(node.left)
            que.append(node.right)
            
            result.append(str(node.data))
        else:
            result.append('#')
    
    return result

print(serialize(root))

# 역직렬화
def deserialize(data):
    
    if data == '# #':
        return None
    
    nodes = data.split() # str형태인 data를 split으로 나눠 리스트 형태로 저장
    
    root = Node(int(nodes[1])) # 루트노드 삽입
    que = deque([root])
    index = 2
    
    while que:
        node = que.popleft()
        
        # left 처리
        if nodes[index] is not '#':
            node.left = Node(int(nodes[index]))
            que.append(node.left)
        
        index += 1
        
        # index + 1 해준 뒤, right 처리 총 2번
        if nodes[index] is not '#':
            node.right = Node(int(nodes[index]))
            que.append(node.right)
            
        index += 1
        
    return root

