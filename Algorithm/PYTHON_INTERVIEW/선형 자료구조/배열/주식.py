import sys

num_list = [7, 1, 5, 3, 6, 4]

# 저점과 현재 값과의 차이계산
profit = 0
min_price = sys.maxsize

for price in num_list:
    # 리스트안에서 min값 확인
    min_price = min(min_price, price)
    # 현재 profit과 price - min의 값중 뭐가 최대인지 확인하면
    # O(n^2) 대신 O(n) 가능
    profit = max(profit, price - min_price)

print(profit)