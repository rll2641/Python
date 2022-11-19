import pandas as pd

scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1958-04-16', '1937-10-16'],
        'Age': [37, 61]},
    index= ['Rosaline Franklin', 'William Gosset'],
    columns= ['Occupation', 'Born', 'Age', 'Died'])
print(scientists)

# 데이터프레임에서 시리즈 선택하기
first_row = scientists.loc['William Gosset']
print(first_row)

# index 속성 - index를 Series로 반환
print(first_row.index, type(first_row))

# values 속성 - 시리즈의 데이터(values값)가 저장
print(first_row.values)

# keys 메서드 - index속성과 같은 역할
print(first_row.keys())

# 기초 통계 메서드
# mean 메서드 - 평균 값, min 메서드 - 제일 작은 값, max 메서드 - 제일 큰 값, std 메서드 - 표준편차
# 많은 메서드가 존재한다. 
ages = scientists['Age']
print(ages.mean(), ages.min(), ages.max(), ages.std())