# 여러 열을 하나로 정리하기
import pandas as pd

weather = pd.read_csv('../CSV/data/weather.csv')
weather_melt = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'],
                       var_name='day', value_name='temp')
print(weather_melt.head())
'''
pivot_table 메서드는 행과 열의 위치를 다시 바꿔 정리해준다. 
index 인자에는 위치를 그대로 유지할 열 이름을 지정하고, columns 인자에는 피벗할 열 이름을 지정
values에는 새로운 열의 데이터가 될 열 이름을 저장하면 된다.
'''
weather_tidy = weather_melt.pivot_table(index=['id', 'year', 'month', 'day'],
                                        columns='element',
                                        values='temp',
                                        dropna=False)
print(weather_tidy.reset_index())