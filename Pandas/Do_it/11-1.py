# 데이터 집계
import pandas as pd
import numpy as np

df = pd.read_csv('../CSV/data/gapminder.tsv', sep='\t')

# year열을 기준으로 데이터를 그룹화 한 다음 lifeExp열의 평균 구하기
avg_life_exp_by_year = df.groupby('year')['lifeExp'].mean()
print(avg_life_exp_by_year)

# groupby 메서드 이해하기
# unique 메서드는 데이터를 중복없이 출력한다.
years = df['year'].unique()
print(years)

# 1952년도 데이터 추출
y1952 = df.loc[df['year'] == 1952, :]
# print(y1952)

# 1952년도 데이터 평균 구하기 -> 반복하는게 7번째 줄
y1952_mean = y1952['lifeExp'].mean()
# print(y1952_mean)

# 라이브러리에서 제공하는 집계 메서드로 원하는 값을 계산할 수 없는 경우
# 함수를 직접 만들어서 사용해야 한다.
# 입력받은 열의 평균값을 구하는 함수
def my_mean(values):
    n = len(values)
    sum = 0
    
    for value in values:
        sum += value
        
    return sum / n

agg_my_mean = df.groupby('year')['lifeExp'].agg(my_mean)
print(agg_my_mean)

# 인잣값 2개를 받아 처리하는 사용자 함수
def my_mean_diff(values, diff_value):
    n = len(values)
    sum = 0
    
    for value in values:
        sum += value
    mean = sum / n
    return mean - diff_value

# 연도별 평균 수명에서 전체 평균 수명을 뺀 값을 구한 것
gloabl_mean = df.lifeExp.mean()
print(gloabl_mean)
# 예제 굿
agg_mean_diff = df.groupby('year').lifeExp.agg(my_mean_diff, diff_value=gloabl_mean)
print(agg_mean_diff)

# 리스트담아 전달
gdf = df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std])
print(gdf)

# agg에 딕셔너리 key= 열이름 전달, value= 집계 메서드 전달
gdf_dict = df.groupby('year').lifeExp.agg({ 'lifeExp': 'mean', 'pop': 'median', 'gdpPer-cap': 'median'})
print(gdf_dict)