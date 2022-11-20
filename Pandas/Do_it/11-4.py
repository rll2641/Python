# 그룹 오브젝트
import pandas as pd
import seaborn as sns

# 한번에 그룹 오브젝트 계산하기
tips_10 = sns.load_dataset('tips').sample(10, random_state=42)
grouped = tips_10.groupby('sex')
# male, female에 따른 인덱스 번호 출력
print(grouped.groups)

# 파이썬은 그룹 연산에 적합한 열을 알아서 골라준다.
avgs = grouped.mean()
print(avgs)

# 그룹오브젝트에서 특정 데이터 추출
# get_group 메서드는 인잣값으로 들어온 오브젝트를 포함한 데이터 반환
female = grouped.get_group('Female')
print(female)

# 여러 열을 사용하여 데이터를 그룹화
bill_sex_time = tips_10.groupby(['sex', 'time']).mean()
print(bill_sex_time)

# 현재 bill_sex_time의 인덱스는 MultiIndex인데, 이 경우 reset_index메서드를 통해
# 인덱스 새로부여 가능
bill_sex_time_re = bill_sex_time.reset_index()
print(bill_sex_time_re)

# reset_index 대신 as_index값으로 false를 넣어도 똑같다.
bill_sex_time = tips_10.groupby(['sex', 'time'], as_index=False).mean()
print(bill_sex_time)