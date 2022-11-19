import pandas as pd
import matplotlib.pyplot as plt

dataurl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv'
df = pd.read_csv(dataurl)

# 데이터의 각 host_name의 빈도수(종류의 개수)를 구하고 host_name으로 정렬하여 상위 5개를 출력하라
ans = df.groupby('host_name').size() # sort를 안해도 hostname기준으로 정렬됨
print(ans.head())

# 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. 빈도수 컬럼은 counts로 명명하라
ans = df.groupby('host_name').size()\
    .to_frame().rename(columns={0:'counts'}).sort_values('counts', ascending=False)
print(ans.head())

# neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라
ans = df.groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size()
print(ans.head())

# neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 neighbourhood_group그룹의 최댓값들을 출력하라
ans = df.groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size()\
    .groupby('neighbourhood_group', as_index = False).max()
print(ans.head())

# neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라
ans = df.groupby('neighbourhood_group')['price'].agg(['mean', 'var', 'max', 'min'])
print(ans)

# neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라
ans = df.groupby('neighbourhood_group')['reviews_per_month'].agg(['mean', 'var', 'max', 'min'])
print(ans)

# neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 구하라
ans = df.groupby(['neighbourhood', 'neighbourhood_group'])['price'].mean()
print(ans)

# 데이터중 neighbourhood_group 값이 Queens값을 가지는 데이터들 중 neighbourhood 그룹별로 price값의 평균, 분산, 최대, 최소값을 구하라
ans = df.loc[df['neighbourhood_group'] == 'Queens'].groupby('neighbourhood')['price'].agg(['mean', 'var', 'max', 'min'])
print(ans)