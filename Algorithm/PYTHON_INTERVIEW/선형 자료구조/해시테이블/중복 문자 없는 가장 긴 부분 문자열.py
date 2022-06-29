import re
strs = re.sub('[^\w]', '', input())
# abcabcbb

used = {}
max_len = start = 0

for i, ch in enumerate(strs):
    # 중복 문자일 경우
    if ch in used and start <= used[ch]:
        start = used[ch] + 1
    # 처음 보는 문자인 경우 갱신
    else:
        max_len = max(max_len, i - start + 1)
    used[ch] = i

print(max_len)