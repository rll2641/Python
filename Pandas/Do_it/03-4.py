import pandas as pd

scientists = pd.read_csv('../CSV/data/scientists.csv')

# 데이터프레임의 Age열에서 Age 열의 평균보다 높은 행 출력
print(scientists[scientists['Age'] > scientists['Age'].mean()])

# 참 거짓을 담은 리스트를 bool 벡터라고 부른다.
# 데이터프레임에 스칼라 연산 -> 문자열은 2배, 정수 2배
print(scientists*2)