# 자료형 변환하기
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')

# 여러가지 자료형을 문자열로 변환하기
# astype으로 자료형 변환
tips['sex_str'] = tips['sex'].astype(str)
print(tips.dtypes)

# 카테고리 자료형
# sex열의 데이터는 남자 또는 여자로만 구성되어 있다. 따라서 카테고리 자료형으로 저장되어있다.
# 이와 같이 반복되는 문자열은 카테고리를 사용하는것이 용량 문제에서 더 효율적이다.
tips['sex'] = tips['sex'].astype('category')
print(tips.info())