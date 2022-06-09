nums = [2, 4, 7, 11, 15, 5] 
target = 9

# 브루트 포스
idx_i = 0
idx_j = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            idx_i = i
            idx_j = j

print(f'[{idx_i}, {idx_j}]')

# in
for i, n in enumerate(nums):
    complement = target - n
    
    if complement in nums[i+1:]:
        result = [nums.index(n), nums.index(complement)]
        
print(result)

# 딕셔너리 이용해 조회, num -> key, index -> value
def twoSum(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [i, nums_map[target - num]]
        nums_map[num] = i

print(twoSum(nums, target))