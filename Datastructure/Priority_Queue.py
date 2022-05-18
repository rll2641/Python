from queue import PriorityQueue
import heapq as heap

q = PriorityQueue()
# maxsize를 활용하여 크기 제한
q1 = PriorityQueue(maxsize=3)

# 우선순위큐의 put(), get() 함수들은 O(log n)의 시간복잡도를 가짐
# 우선순위 넣기
q.put(3)
q.put(4)
q.put(1)

#(우선순위, 값)의 형태로 저장 가능
q1.put((1, 'apple'))
q1.put((2, 'banana'))
q1.put((3, 'melon'))

# 큐 사이즈 반환
print("return que_size")
print(q.qsize())
print('-'*50)

# 큐가 비어있으면 true, 비어있지 않으면 false
print(q.empty())
print('-'*50)

# 큐가 가득차있으면 true, 아니면 false
print(q.full())
print('-'*50)

# 원소 삭제 및 반환
while not q.empty():
    print(q.get())
print('-'*50)

# --------------------------------------------------------- 

# 최소 힙
min_heap = []
prio = [10, 5, 4, 1]
for i in prio:
    heap.heappush(min_heap, i)

while min_heap:
    print(heap.heappop(min_heap))
print('-'*50) 

# 최대 힙
max_heap = []
prio = [10, 5, 4, 1]
for i in prio:
    # 마이너스와 인덱스를 이용하여 최대 힙 완성
    heap.heappush(max_heap, (-i, i))

while max_heap:
    print(heap.heappop(max_heap)[1])