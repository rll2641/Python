import re

strs = re.sub('[^\w]', '', input().lower())

def expend(left, right):
    while left >= 0 and right < len(strs) and strs[left] == strs[right]:
        left -= 1
        right += 1
    return strs[left+1:right]

if len(strs) < 2 or strs == strs[::-1]:
    print('yes')
result = ''

for i in range(len(strs) - 1):
    result = max(result,
                 expend(i, i+1),
                 expend(i, i+2),
                 key=len)

print(result)