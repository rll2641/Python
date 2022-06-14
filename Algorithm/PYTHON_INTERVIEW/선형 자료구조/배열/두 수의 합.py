nums, target = [2, 7, 11, 15], 9

# 반복문
for i in range(len(nums) - 1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f'[{i}, {j}]')

# in
for i in range(len(nums)):
    num = target - nums[i] 
    if num in nums[i+1:]:
        print(f'[{i}, {nums.index(num)}]')

# 딕셔너리
nums_dic = {}
for i, num in enumerate(nums):
    if target - num in nums_dic:
        print(f'[{nums_dic[target-num]}, {i}]')
    nums_dic[num] = i