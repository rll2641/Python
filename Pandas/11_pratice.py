import numpy as np
import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

avg_life = df.groupby('year')['lifeExp'].mean()

# unique 중복없이 출력
years = df['year'].unique()

# 데이터 수 반환, count
print(df.groupby('year').count())

# agg 함수적용 lifeExp에 갯수, 평균값, 표준편차 적용
gdf = df.groupby('year')['lifeExp'].agg([np.count_nonzero, np.mean, np.std])
