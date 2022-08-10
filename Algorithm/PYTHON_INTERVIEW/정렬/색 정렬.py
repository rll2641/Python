# 빨간색을 0, 흰색을 1, 파란색을 2라 할 때, 순서대로 인접하는 제자리 정렬을 수행하라

colors = [2, 0, 2, 1, 1, 0]

def sortColors(nums: list[int]):
    red, white, blue = 0, 0, len(nums)
    
    # 기존 퀵정렬의 두 부분 분할에 비해 개선방안 제시 (세 부분으로 분할)
    while white < blue:
        if nums[white] < 1: # 1은 colors의 중간값 mid = 1
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else:
            white += 1
    return nums

print(sortColors(colors))