import pandas as pd

df = pd.read_csv('../CSV/data/gapminder.tsv', sep='\t')

# 열 단위 데이터 추출하기
country_df = df['country'] # 시리즈
print(country_df.head())

# 리스트에 열(세로) 이름을 전달하면 여러개의 열을 한 번에 추출할 수 있다.
subset = df[['country', 'continent', 'year']] # 데이터프레임
print(subset.head())

# 행 단위 데이터 추출하기
# loc - 인덱스를 기준으로 행 데이터 추출
# iloc - 행 번호를 기준으로 행 데이터 추출

# loc 속성으로 행(가로) 데이터 추출하기
print(df.loc[0]) 

# 마지막 행 뽑기, df.loc[-1] -> 에러, shape 이용
print(df.loc[df.shape[0] - 1])

# 행 데이터 한 번에 출력
print(df.loc[[0, 99, 999]])

# iloc 속성으로 행 데이터 출력
print(df.iloc[1])

# iloc 속성은 음수사용으로 데이터 추출이 가능하다.
print(df.iloc[-1])

# 슬라이싱으로 모든 행 데이터 추출하기
subset = df.loc[:, ['year' ,'pop']]
print(subset.head())

# iloc 속성의 열 지정값에 문자열 리스트를 전달하면 오류 발생
subset = df.iloc[:, [2 ,4, -1]]
print(subset.head())

# range 메서드로 데이터 추출하기
subset = df.iloc[:, list(range(5))]
print(subset.head())

# 슬라이싱과 range 비교
# subset = df.iloc[:, list(range(5))] 아래와 동일
subset = df.iloc[:, :3]
print(subset.head())