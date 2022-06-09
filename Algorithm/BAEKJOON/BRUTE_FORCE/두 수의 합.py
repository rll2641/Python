n = int(input())
num_dic = {}
count = 0

num_list = list(map(int, input().split()))
result = int(input())

for i,j in enumerate(num_list):
    if result - j in num_dic:
        count += 1
    num_dic[j] = i
print(count)