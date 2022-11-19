# 기초적인 통계 계산하기

import pandas as pd

df = pd.read_csv('../CSV/data/gapminder.tsv', sep='\t')

# lifeExp 열을 연도별로 그룹화하여 평균 계산하기
print(df.groupby('year')['lifeExp'].mean())

# lifeExp, gdpPercap 열의 평균값을 연도, 지역별로 그룹화하여 한 번에 계산하기
print(df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean())

# 그룹화한 데이터 개수 세기 - 같은 것 끼리 몇개씩 묶였는지
print(df.groupby('continent')['country'].nunique())

