# 에볼라 최초 발병일 계산
import pandas as pd

ebola = pd.read_csv('../CSV/data/country_timeseries.csv')
ebola['data_dt'] = pd.to_datetime(ebola['Date'])

# 에볼라 발생하기 시작한 날
# ebola['data_dt'].min()
# 발병일 계산
ebola['outbreak_d'] = ebola['data_dt'] - ebola['data_dt'].min()
print(ebola['outbreak_d'])

# 은행 파산일 계산
banks = pd.read_csv('../CSV/data/banklist.csv', parse_dates=[5, 6])
# 분기별, 연도별 열 따로 저장
banks['closing_quater'], banks['closing_year'] = (banks['Closing Date'].dt.quarter,
                                                  banks['Closing Date'].dt.year)
# groupby 메서드로 연도별 파산한 은행 개수
closing_year = banks.groupby('closing_year').size()
print(closing_year)

# 연도별, 분기별 파산한 은행
closing_year_q = banks.groupby(['closing_year', 'closing_quater']).size()
print(closing_year_q)

# 그래프
import matplotlib.pyplot as plt

fig = plt.subplot()
ax = closing_year.plot()
plt.show()

fig = plt.subplot()
ax = closing_year_q.plot()
plt.show()