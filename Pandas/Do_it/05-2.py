import pandas as pd

# 데이터 연결하기 
# concat 메서드로 데이터 연결
df1 = pd.read_csv('../CSV/data/concat_1.csv')
df2 = pd.read_csv('../CSV/data/concat_2.csv')
df3 = pd.read_csv('../CSV/data/concat_3.csv')

# concat 메서드에 연결하려는 데이터프레임을 리스트에 담아 전달하면
# 연결한 데이터프레임을 반환한다. 
# 데이터 삽입 방향 : 아래
row_concat = pd.concat([df1, df2, df3])
print(row_concat.iloc[3,])

# 데이터프레임에 시리즈 연결하기
# 행이 아닌 새로운 열로 추가된다.
new_row_concat = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(pd.concat([df1, new_row_concat]))

# 행이 1개라도 데이터프레임에 담아 연결해야 한다.
new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], columns=['A', 'B', 'C', 'D'])
print(pd.concat([df1, new_row_df]))

# concat메서드는 한 번에 2개 이상의 데이터프레임을 연결할 수 있는 메서드다.
# 만약 1개를 연결하고 싶으면 append 메서드를 사용해도 된다.

# append 메서드와 딕셔너리 사용
# ignore_index를 true로 설정하면 인덱스를 0부터 다시 지정
data_dict = {'A': 'n1', 'B': 'n2', 'C': 'n3', 'D': 'n4'}
print(df1.append(data_dict, ignore_index=True))

# 행 방향이 아닌 열 방향으로 데이터 연결 
# 데이터 삽입 방향 : 오른쪽
col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)

# 공통 열과 공통 인덱스만 연결하기 (열 방향 : 위에서 아래)
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

# 위 데이터프레임을 concat으로 연결 시, 열 이름이 정렬되면 연결된다.
# 없는 열 이름의 데이터(value)는 누락값으로 처리 된다.

# df1, df3의 공통 열(A, C)만 골라서 연결하기
# df1과 df3의 공통 열만 연결하려면 join의 inner(데이터베이스의조인같음)
common = pd.concat([df1, df3], ignore_index=True, join='inner') 
print(common)

# 행 방향 연결 (왼쪽에서 오른쪽)
df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]

col_concat = pd.concat([df1, df3], axis=1, join='inner')
print(col_concat)