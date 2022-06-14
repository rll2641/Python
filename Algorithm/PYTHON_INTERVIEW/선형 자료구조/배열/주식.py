import sys

nums = [7,1,4,3,6,4]
max_price = 0

# 브루트 포스
for index, price in enumerate(nums):
    for j in range(index, len(nums)):
        max_price = max(max_price, nums[j] - price)
        
print(max_price)

# 저점과현재값
min_price, profit = sys.maxsize, 0
for i in nums:
    min_price = min(min_price, i)
    profit = max(profit, i - min_price)
print(profit)