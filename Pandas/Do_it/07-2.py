# 열 이름 관리하기 ex) Cases_Guinea같은 이름 분리 -> Cases, Guniea
import pandas as pd

ebola = pd.read_csv('../CSV/data/country_timeseries.csv')

# ebola의 0,1,2,3,10,11열의 5개 데이터만 확인
print(ebola.iloc[:5, [0, 1, 2, 3, 10, 11]])
# Date와 Day를 고정하고 나머지를 행으로 피벗
ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])

# Cases_Guinea같이 2개 이상의 의미를 가지고 있는 열이름은 밑줄을 
# 기준으로 Cases, Guniea로 나눌수 있다.
# split메서드로 열 이름 분리하기
variable_split = ebola_long['variable'].str.split('_')
print(variable_split)

status_values = variable_split.str.get(0)
country_values = variable_split.str.get(1)

ebola_long['status'] = status_values
ebola_long['country'] = country_values
print(ebola_long.head())