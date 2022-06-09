import sys
h, w = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

water = 0
left, right = 0, len(height) - 1
height_max_left, height_max_right = height[left], height[right]

while left < right:
    height_max_left = max(height[left], height_max_left)
    height_max_right = max(height[right], height_max_right)
    
    if height_max_left <= height_max_right:
        water += height_max_left - height[left]
        left += 1
    else:
        water += height_max_right - height[right]
        right -= 1
    
print(water)