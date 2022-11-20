# 데이터 필터링
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
# size 열의 데이터 수 확인
print(tips['size'].value_counts())
# size 열의 1, 5, 6 데이터가 적어 제외
tips_filtered = tips.groupby('size').filter(lambda x: x['size'].count() >= 30)
print(tips_filtered)