height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# 투 포인터
water = 0
left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right] # 최대높이 갱신

while left < right:
    left_max = max(height[left], left_max) # 최대높이 갱신
    right_max = max(height[right], right_max)
    
    if left_max <= right_max:
        water += left_max - height[left] 
        left += 1
    else:
        water += right_max - height[right]
        right -= 1

print(water)

# 스택 (아직이해안감)
def trap(): 
    stack = []
    water = 0
    
    for i in range(len(height)):
        # 변곡점을 만나는 반복문 실행
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
        
            if not len(stack):
                break
                
            # 이전과의 차이만큼 물 높이 처리
            distance = i - 1 - stack[-1]
            waters = min(height[i], height[stack[-1]]) - height[top]
            water += distance * waters
        
        stack.append(i)
    print(water)
    
trap()