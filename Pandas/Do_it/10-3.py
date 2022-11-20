# apply 메서드 사용하기 - 고급
import seaborn as sns
import pandas as pd
import numpy as np

titanic = sns.load_dataset('titanic')
print(titanic.info())

# df의 누락값을 처리한 다음 apply 메서드 사용
# isnull 메서드에 df를 전달하면 true,false를 적용한 df가 만들어지고
# 이 값을 numpy의 sum 메서드에 전달하면 누락값의 개수를 구할 수 있다.
def count_missing(vec):
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count

cmis_col = titanic.apply(count_missing)
print(cmis_col)

# 누락값의 비율 계산
def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num / dem

pmis_col = titanic.apply(prop_missing)
print(pmis_col)

# df의 누락값 처리 행방향, axis=1
cmis_row = titanic.apply(count_missing, axis=1)
pmis_row = titanic.apply(prop_missing, axis=1)
print(cmis_row.head())