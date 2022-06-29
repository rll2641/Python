jew, stone = 'aA', 'aAAbbbb'

# 해시 테이블을 이용한 풀이
total, counts = {}, 0

for i in stone:
    if i not in total:
        total[i] = 1
    else:
        total[i] += 1

for i in jew:
    if i in total:
        counts += total[i]
print(counts)

# defaultdict을 이용한 풀이
from collections import defaultdict

total, counts = defaultdict(int), 0

for i in stone:
    total[i] += 1

for j in jew:
    counts += total[j]
print(counts)

# Counter을 이용한 풀이
from collections import Counter
total, counts = Counter(stone), 0

for i in jew:
    counts += total[i]

print(counts)

# 파이썬 다운 방식
print(sum(s in jew for s in stone))