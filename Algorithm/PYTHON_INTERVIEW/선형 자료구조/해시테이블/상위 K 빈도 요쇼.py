nums, k = [1, 1, 2, 2, 3], 2

# Counter이용
from collections import Counter
freqs, result = Counter(nums), list()
set_freqs = set(freqs)
for i in set_freqs:
    if freqs[i] >= 2:
        result.append(i)
print(result)