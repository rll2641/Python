num_list = [1, 4, 3, 2]
# 오름차순
num_list.sort()
pair = list()
total = 0
for n in num_list:
    pair.append(n)
    if len(pair) == 2:
        total += min(pair)
        pair = list()
print(total)

# 짝수번째 값 계산
total = 0
for index, value in enumerate(num_list):
    if index % 2 == 0:
        total += value
print(total)

# 파이썬다운방식
print(sum(sorted(num_list)[::2]))