import pandas as pd

# 시리즈 만들기
# s = pd.Series(['banana', 42])
# print(s)

# 인덱스에 이름 부여
# s= pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
# print(s)

# 데이터프레임 만들기
'''
df = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Age', 'Died'])
'''
# ex = df.loc['William Gosset']

# values 값 출력
# print(ex.values)

# *
# 요약 통계량 계산
# ex = df['Age'].describe()

df = pd.read_csv('./data/scientists.csv')
ages = df['Age']
# print(ages.max(), ages.mean())

# *
# 평균나이보다 나이가 많은사람 불린추출 
# 리스트안에 불린으로 시리즈에 전달하면 참인 인덱스만 추출할 수 있다.
# print(ages[ages > ages.mean()])

# sort_index 값 정렬, ascending은 차순, 디폴트는 오름차순
# print(ages.sort_index())

# age열에서 age평균보다 높은 행출력
# print(df[df['Age'] > df['Age'].mean()])

# *
# 데이터 타입 변경, object -> datetime
born_datetime = pd.to_datetime(df['Born'], format='%Y-%m-%d')
# print(born_datetime)

died_datetime = pd.to_datetime(df['Died'], format='%Y-%m-%d')
# print(died_datetime)

# astype Age열의 데이터 타입 int 64 -> float로
df = df.astype({'Age':'float'})

# *
# 새로운 열 추가
df['Born_dt'], df['Died_dt'] = (born_datetime, died_datetime)

# died_dt에서 born_dt 빼고 새로운 열에 저장 (일수로 저장됨)
df['Age_days_dt'] = (df['Died_dt'] - df['Born_dt'])

# 데이터 프레임에서 열 삭제
age_drop = df.drop(['Age'], axis=1)
# print(age_drop.columns) # 삭제 됌
# print(df) # 삭제안됌