# 정렬되지 않은 배열에서 K번째 큰 요소를 출력
nums, k = [3,2,3,1,2,4,5,5,6], 4

# heapq모듈 이용
import heapq as hq

def findKLargest(nums, k):
    heap = list()
    
    for n in nums:
        hq.heappush(heap, -n)
        
    for _ in range(1, k):
        hq.heappop(heap)
        
    return -hq.heappop(heap)

# heapq 모듈의 heapify 이용
def findKLargest2(nums, k):
    hq.heapify(nums)
    
    for _ in range(len(nums) - k):
        hq.heappop(nums)
    
    return hq.heappop(nums)

# heapq 모듈의 nlargest 이용 -> n 번째 큰 값을 추출 하는 기능
def findKLargest3(nums, k):
    return hq.nlargest(k, nums)

print(findKLargest3(nums, k))
