import pandas as pd
from numpy import NaN
import numpy as np

# 누락값 확인 방법
print(pd.isnull(NaN), pd.notnull(NaN))

survey = pd.read_csv('../CSV/data/survey_survey.csv')
visited = pd.read_csv('../CSV/data/survey_visited.csv')

vs = visited.merge(survey, left_on='ident', right_on='taken')
print(vs)

# 누락값의 개수 구하기
ebola = pd.read_csv('../CSV/data/country_timeseries.csv')
# count 메서드로 누락값이 아닌 값의 개수 구하기
# shape를 이용해 각 열마다 누락값의 개수 구하기
num_rows = ebola.shape[0]
num_missing = num_rows - ebola.count()
print(num_missing)

# count_nonzero(numpy) 와 isnull 메서드를 조합
print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))

# 누락값 처리하기
# df에 포합된 fillna 메서드에 0을 대입하면 누락값을 0으로 변경할 수 있다.
# iloc[0:10, 0:5]의 의미 -> 10개의 행뽑기, 5개의 열까지 출력
print(ebola.fillna(0).iloc[0:10, 0:5])

# fillna 메서드의 method 인잣값을 ffill로 지정하면 누락값 이전의 값으로 변경됨
# ex 1번 인덱스의 열 값이 1이면 2번 인덱스 또한 1로 변경됌
# bfill로 지정 시, 누락값이 나타난 이후의 첫 번째 값으로 모두 변경됌
# interplot 메서드는 누락값 양쪽의 있는 값을 이용하여 중간값으로 변경함

# 누락값 삭제하기 
# 필요없을 경우 삭제가능
# dropna() 메서드 이용

# 누락값이 포함된 데이터 계산
# 누락값이 포함된 계산은 nan이 된다.
# 누락값 무시한채 계산은 skipna= 의 인자를 True로 설정
