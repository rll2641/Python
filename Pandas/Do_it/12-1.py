# datetime 오브젝트
from datetime import datetime
import pandas as pd
import os

# now, today 메서드 사용시 현재시간 출력
now1 = datetime.now()
now2 = datetime.today()

print(now1)
print(now2)

# datetime 오브젝트 생성시 시간을 직접 입력
t1 = datetime.now()
t2 = datetime(1970, 1, 1) # 1970-01-01 00:00:00
t3 = datetime(1970, 12, 12, 13, 24, 34) # 1970-12-12 13:24:34

# datetime 오브젝트는 시간계산이 가능하다
diff1 = t1 - t2 # 계산은 day만큼 표시
print(diff1)

# 문자열을 datetime 오브젝트로 변환
ebola = pd.read_csv('../CSV/data/country_timeseries.csv')
# to_datetime 메서드를 이용해 문자열을 datetime으로 변환
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
# to_datetime에 시간 형식 지정자 format='%d/%m/%y'입력가능
test_df1 = pd.DataFrame({'order_day': ['01/01/15', '02/01/15', '03/01/15']})
test_df1['date_dt1'] = pd.to_datetime(test_df1['order_day'], format='%d/%m/%y')
print(test_df1)

# 시계열 데이터 구분 추출
now = datetime.now() # 2022-11-21 15:32:26.553599
nowDate = now.strftime('%Y-%m-%d')
print(nowDate) # 2022-11-21
nowTime = now.strftime('%H:%M:%S') # 15:33:25
print(nowTime)

# datetime 오브젝트로 변환하고자 하는 열 전달
# Date 열이 오브젝트에서 datetime으로 변환
ebola1 = pd.read_csv('../CSV/data/country_timeseries.csv', parse_dates=['Date'])

# datetime 오브젝트에서 날짜 정보 추출
date_series = pd.Series(['2018-05-16', '2018-05-17', '2018-05-18'])
d1 = pd.to_datetime(date_series)
print(d1[0].year) # 2018
print(d1[1].month) # 5
print(d1[2].day) # 16

# dt 접근자로 시계열 데이터 정리
ebola['year'] = ebola['date_dt'].dt.year
print(ebola['year'])