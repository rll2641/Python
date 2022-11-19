import pandas as pd

scientists = pd.read_csv('../CSV/data/scientists.csv')

# 열의 자료형 바꾸기
# object(string) -> datetime, format 속성 %Y-%m-%d 지정
# 아래는 scientists의 dtype이 바뀌지 않음
born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
# 저장을 다시 해주어야 dtype이 바뀜
# scientists['Born'] = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')

# 새로운 열 추가
scientists['Born_dt'] = born_datetime
scientists['Died_dt'] = died_datetime

# datetime자료형 연산
scientists['Age_days_dt'] = scientists['Died_dt'] - scientists['Born_dt']
print(scientists)

# 데이터프레임 열 삭제하기
# drop 메서드를 통해 axis=1 전달시 삭제됌
scientists_dropped = scientists.drop(['Age'], axis= 1)
print(scientists_dropped)