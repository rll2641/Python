import pandas as pd
dataurl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
df = pd.read_csv(dataurl)

# * quantity 컬럼 값이 3인 데이터를 추출하여 첫 5행 출력
# print(df.loc[df['quantity'] == 3].head())
# print(df[df['quantity'] == 3].head())

# * quantity 컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬후 첫5행출력
# Ans = df[df['quantity'] == 3].head().reset_index(drop=True)
# print(Ans)

# * quantity, item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임 정의
# print(df[['quantity', 'item_price']])

# * item_price 컬럼의 달러문자를 제거하고 float으로 new_price에 저장
df['new_price'] = df['item_price'].str[1:].astype('float')
# Ans = df['new_price']
# print(Ans.head())

# * new_price 컬럼이 5이하의 값을 가지는 데이터프레임을 추출하고 전체 갯수 구하기
# Ans = len(df[df['new_price'] <= 5])
# print(Ans)

# item_name명이 Chicken Salad Bowl인 데이터 프레임을 추출하고 index값 초기화
# Ans = df[df['item_name'] == 'Chicken Salad Bowl'].reset_index(drop=True)
# print(Ans.head(3))

# new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라
# Ans = df.loc[(df['item_name'] == 'Chicken Salad Bowl') & (df['new_price'] <= 9)]
# print(Ans.head())

# df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 index를 초기화 하여라
# Ans = df.sort_values('new_price').reset_index(drop=True)
# rint(Ans.head(4))

# df의 item_name 컬럼 값중 Chips 포함하는 경우의 데이터를 출력하라
# Ans = df.loc[df['item_name'].str.contains('Chips')]
# print(Ans.head(5))

# df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라
# ans = df.loc[:,::2]
# print(ans.head(5))

# df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라
# ans = df.sort_values('new_price', ascending=False).reset_index(drop=True)
# print(ans.head(4))

# df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라
# ans = df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')]
# print(ans)

# df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라
# ans = df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')]
# ans.drop_duplicates('item_name')
# print(ans)

# df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라
# ans = df.loc[(df['new_price'] >= df['new_price'].mean())]
# print(ans.head(5))

# df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라
# df.loc[df['item_name'] == 'Izze', 'item_name'] = 'Fizzy Lizzy'
# print(df.head(3))

# df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라
# ans = df['choice_description'].isnull().sum()
# print(ans)

# df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용)
# df.loc[df['choice_description'] == NaN, 'choice_description'] = 'NoData'
# print(df.head())

# df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라
# Ans = df[df.choice_description.str.contains('Black')]
# print(Ans.head())

# df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라
# ans = df[~df['choice_description'].str.contains('Vegetables')]
# print(ans)

# df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라
# ans = df[df['item_name'].str.startswith('N')]
# print(ans.head(3))

# df의 데이터 중 item_name 값의 단어갯수가 15개 이상인 데이터를 인덱싱하라
# ans = df[df['item_name'].str.len() >= 15]
# print(ans.head(3))

# df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라
# lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
# ans = df.loc[df['new_price'].isin(lst)]
# print(ans.head())