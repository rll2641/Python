# 데이터 변환
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('../CSV/data/gapminder.tsv', sep='\t')

# 표준점수 계산하기
def my_zscore(x):
    return (x - x.mean()) / x.std()

transform_z = df.groupby('year')['lifeExp'].transform(my_zscore)
print(transform_z)

# 누락값을 평균값으로 처리하기
np.random.seed(42)
# 데이터집합에서 10개의 행데이터만 가져오고 total_bill열의 데이터 4개를 임의로 선택하여
# 누락값으로 바꾼것
tips_10 = sns.load_dataset('tips').sample(10)
tips_10.loc[np.random.permutation(tips_10.index)[:4], 'total_bill'] = np.nan
print(tips_10)

def fill_na_mean(x):
    avg = x.mean()
    return x.fillna(avg)

total_bill_group_mean = tips_10.groupby('sex')['total_bill'].transform(fill_na_mean)
tips_10['fill_total_bill'] = total_bill_group_mean
print(tips_10)