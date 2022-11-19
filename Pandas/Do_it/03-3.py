import pandas as pd

scientists = pd.read_csv('../CSV/data/scientists.csv')

# 시리즈와 불린 추출
ages = scientists['Age']

# 평균보다 나이가 많은 사람의 데이터 추출
print(ages[ages > ages.mean()])

# ages > ages.mean()의 결과 값 -> 조건식을 만족하는 값(True)만 출력
'''
0    False
1     True
2     True
3     True
4    False
5    False
6    False
7     True
'''
# 리스트 형태로 참, 거짓을 담아 참인 인덱스의 데이터 추출을 불린 추출이라고 한다.
# 시리즈나 데이터프레임에 있는 모든 데이터에 대해 한 번에 연산을 하는 것을 브로드캐스팅이라고 한다.
# 시리즈처럼 여러 개의 값을 가진 데이터를 벡터라 하고, 단순 크기를 나타내는 데이터를 스칼라라고 한다.

# 벡터와 스칼라로 브로드캐스팅 수행
# 벡터와 벡터의 연산은 일치하는 index의 값끼리 수행한다.
print(ages + ages)
print(ages * ages)
# 벡터에 스칼라를 연산
print(ages + 100)

# 서로 다른 벡터 계산
print(ages + pd.Series([1, 100])) # 인덱스 수의 차이가 있으므로 NaN값 발생

# sort_index 메서드 - index 정렬
print(ages.sort_index(ascending=False))

