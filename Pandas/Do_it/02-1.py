import pandas as pd

df = pd.read_csv('../CSV/data/gapminder.tsv', sep='\t')

# head 메서드 - 데이터프레임에서 가장 앞에 있는 5개 행 출력
print(df.head())

# tail 메서드 - 데이터프레임에서 가장 뒤에 있는 5개의 행 출력
print(df.tail())
# shape 속성값 - 데이터의 행과 열의 크기에 대한 정보
print(df.shape)

# columns 속성값 - 데이터 프레임의 열 이름을 확인할 수 있다.
print(df.columns) 

# dtypes 속성값이나 info 메서드로 갑의 자료형을 확인할 수 있다
print(df.dtypes)
print(df.info())

# 판다스는 문자열 자료형을 object라는 이름으로 인식한다.