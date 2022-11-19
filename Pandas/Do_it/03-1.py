import pandas as pd

# 시리즈 만들기
s = pd.Series(['banana', 42])
print(s)

# 인덱스 지정명 바꾸기
s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

# 데이터프레임을 만들기 위해서는 딕셔너리를 DataFrame에 전달해야 한다.
# columns는 데이터프레임의 열 순서를 지정할 수 있다.
scientists = pd.DataFrame(
    data={'Name':['Rosaline Fraklin', 'William Gosset'],
        'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1958-04-16', '1937-10-16'],
        'Age': [37, 61]},
    index= ['Rosaline Franklin', 'William Gosset'],
    columns= ['Occupation', 'Born', 'Age', 'Died'])
print(scientists)

# 순서가 보장된 딕셔너리 pd.DataFrame(OrderedDict([('Name', ['Rosaline Franklin', 'Cho'])])) 