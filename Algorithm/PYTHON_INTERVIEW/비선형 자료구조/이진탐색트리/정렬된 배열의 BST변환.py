nums = [-10, -7, -3, 0, 5, 7, 9] # 정렬된 배열을 높이 균형 이진 탐색 트리로 변환
# -> [0,-7, 7, -10, -3, 5, 9]

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    
    node = Node(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid+1:])
    
    return node