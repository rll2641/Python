height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# 투 포인터
left, right, water = 0, len(height) - 1, 0
left_max, right_max = height[left], height[right]

while left < right:
    left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
    
    if left_max <= right_max:
        water += left_max - height[left]
        left += 1
    else:
        water += right_max - height[right]
        right -= 1

print(water)

# 스택
stack,water = [], 0

for i in range(len(height)):
     
    while stack and height[i] > height[stack[-1]]:
        top = stack.pop()
         
        if not len(stack):
            break
         
        distance = i - stack[-1] - 1
        waters = min(height[i], height[stack[-1]]) - height[top]
        water += distance * waters
        
    stack.append(i)
print(water)