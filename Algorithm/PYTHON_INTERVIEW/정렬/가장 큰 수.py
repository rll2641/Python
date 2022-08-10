# 항목들을 조합하여 만들 수 있는 가장 큰 수를 출력

nums = [30, 3, 9]
# 3, 30, 9 / 3, 9, 30 / 9, 3, 30

def to_swap(n1: int, n2: int):
    return str(n1) + str(n2) < str(n2) + str(n1)

def largestNumber(nums: list[int]):
    i = 1
    
    while i < len(nums):
        j = i
        while j > 0 and to_swap(nums[j-1], nums[j]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        i += 1
    
    return str(int(''.join(map(str, nums))))

print(largestNumber(nums))