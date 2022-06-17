import pandas as pd
dataurl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
df = pd.read_csv(dataurl)

# 데이터 상위 5개 행 출력
# print(df.head())

# 데이터 행과 열의 갯수 파악
# print(df.shape,'\n','행:',df.shape[0],'\n','열:',df.shape[1])

# 전체 컬럼을 출력
# print(df.columns)

# 6번재 컬럼 출력
# print(df.columns[5])

# 6번재 컬럼의 데이터 타입 확인
# Ans = df.iloc[:,5].dtpye
# print(Ans)

# 데이터셋의 인덱스 구성
# print(df.index)
 
# 데이터 마지막 3개행 출력
# print(df.tail(3))

# 수치형 변수를 가진 컬럼을 출력 (정수,실수,,,)
# Ans = df.select_dtypes(exclude=object).columns
# print(Ans)

# 범주형 변수를 가진 컬럼 출력 (문자열, 날짜형)
# Ans = df.select_dtypes(include=object).columns
# print(Ans)

# 각 수치형 변수의 분포(사분위,평균,표준편차,최대,최소)확인
# print(df.describe())

# 특정 컬럼의 값 출력
# print(df['특정'])

# 모든 행의 데이터에 대해 특정 컬럼 열을 추출 하는 방법
# df.loc[:,['특정', '특정']]
# df[df['특정', '특정']]

# 특정 컬럼의 유일값(중복x) 갯수 출력
# print(df['특정'].nunique())

# 특정 컬럼의 유일값을 출력(갯수x)
# print(df['특정'].unique())