nums = [1,4,3,2]
nums.sort()
# 반복
result, total = [], 0
for i in nums:
    result.append(i)
    if len(result) == 2:
        total += min(result)
        result = []
print(total)

# 짝수번째 값
total = 0
for index, num in enumerate(nums):
    if index % 2 == 0:
        total += num
print(total)

# 파이썬다운 방식
print(sum(sorted(nums)[::2]))