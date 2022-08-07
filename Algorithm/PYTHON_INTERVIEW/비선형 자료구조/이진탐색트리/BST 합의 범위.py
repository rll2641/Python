root = [10, 5, 15, 3, 7, None, 18]
L, R = 7, 15
# BST가 주어졌을 때 L이상 R이하의 값을 지닌 노드의 합을 구하라

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

# 재귀 구조로 DFS 브루트 포스 탐색
def rangeToBST(root, L, R):
    if not root:
        return 0
    
    return (root.data if L <= root.data <= R else 0) + \
        rangeToBST(root.left, L, R) + \
            rangeToBST(root.right, L, R)

# dfs 가지치기로 필요한 노드 탐색 \ 위 방법보다 낫다
def rangeSumBST(root):
    def dfs(node):
        if not node:
            return 0
    
        if node.data < L:
            return dfs(node.right)
        elif node.data > R:
            return dfs(node.left)
        return node.data + dfs(node.left) + dfs(node.right)
    return dfs(root)

# 반복 dfs
def rangeSumBst(root, L, R):
    stack, sum = [root], 0
    
    while stack:
        node = stack.pop()
        
        if node:
            if node.data > L:
                stack.append(node.left)
            if node.data < R:
                stack.append(node.right)
            if L <= node.data <= R:
                sum += node.data
    
    return sum