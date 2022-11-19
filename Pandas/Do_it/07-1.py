import pandas as pd

'''
melt 메서드는 지정한 열의 데이터를 모두 행으로 정리해줍니다.
인자 -> id_vars 위치를 그대로 유지할 열의 이름을 저장
value_vars 행으로 위치를 변경할 열의 이름을 저장
var_name value_vars로 위치를 변경한 열의 이름을 저장
value_name var_name으로 위치를 변경한 열의 데이터를 저장한 열의 이름을 저장
'''

pew = pd.read_csv('../CSV/data/pew.csv')
# 6개의 열 출력
print(pew.iloc[:,:6])

pew_long = pd.melt(pew, id_vars='religion')
'''
id_vars로 지정한 열(religion)을 제외한 나머지 소득 정보 열(10k, 10~20k...)이 variable 열로
정리되고 소득 정보 열의 행 데이터도 value 열로 정리되었다. 이 과정을 religion열을 고정하여 피벗했다.
'''
print(pew_long.head())
# variable, value열의 이름 바꾸기
pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')

# 2개 이상의 열을 고정하고 나머지 열을 행으로 바꾸기
billboard = pd.read_csv('../CSV/data/billboard.csv')
print(billboard.iloc[:5, :16])

billboard_long = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week', value_name='rating')
print(billboard_long.head())