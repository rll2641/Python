# 겹치는 구간을 병합하라 x좌표 1~3, 2~6은 겹친다.

nlist = [[1,3], [2,6], [8, 10], [15, 18]]

def merge(intervals: list):
    merged = []
    
    for i in sorted(nlist, key=lambda x: x[0]):
        if merged and i[0] <= merged[-1][1]: # [[1,3], [2,6]]에서 i[0] = 2와 merged[-1][1] = 3을 비교(겹치는지 확인)
            merged[-1][1] = max(merged[-1][1], i[1]) # 겹치면 [2,6]에서 2번째 요소로 스왑
        else:
            merged += i,
    return merged

print(merge(nlist))