import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./data/gapminder.tsv', sep='\t')

# head 메서드는 가장 앞에 있는 5개의 행을 출력한다. tail은 가장 뒤
# print(df.head())

# shape 속성값은 행과 열의 개수를 출력한다.
# print(df.shape)

# columns 속성값은 프레임의 열 이름을 확인할 수 있다.
# print(df.columns)

# dtypes, info로 자료형 확인 가능
# print(df.dtypes)
# print(df.info())

# 열 추출 시리즈
# country_df = df['country']
# print(country_df.head(),country_df.tail())

# 리스트에 열 전달, 데이터프레임
# subset = df[['country','continent', 'year']]
# print(subset)

# 인덱스 단위 데이터 추출 
# loc(인덱스)
# print(df.loc[0])

# iloc(행 번호)
# print(df.iloc[0])
# print(df.iloc[-1])

# 슬라이싱 데이터 추출
# subset = df.loc[:, ['year', 'pop']] == df[['year', 'pop']]
# print(subset)

# range 메서드로 데이터 추출 [:, ~] ~는 column에 해당, 따라서 country,continent,year,lifeExp,pop 5개출력
# small_range = list(range(5))
# subset = df.iloc[:, small_range]
# print(subset)

# lifeExp 열을 연도별로 그룹화하여 평균 구하기
# print(df.groupby('year')['lifeExp'].mean())

# lifeExp,gdpPercap 열의 평균값을 연도,지역별로 그룹화하여 한 번에 계산하기
# ex01 = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
# print(ex01)

# continent를 기준으로 country열만 추출하여 빈도수 계산
# ex01 = df.groupby('continent')['country'].nunique()
# print(ex01)

# 그래프 그리기
# ex = df.groupby('year')['lifeExp'].mean()
# plt.plot(ex)
# plt.show()