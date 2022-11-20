# apply 메서드 사용하기 - 기초
import pandas as pd

df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]})

def my_sq(x):
    return x ** 2

# apply 메서드를 통해 함수를 전달
sq = df['a'].apply(my_sq)
print(sq)

# 2개의 인자를 받아야하는 경우
def my_exp(x, n):
    return x ** n

# apply 메서드의 첫 번째 인자에는 함수이름, 두 번째인자에는 함수의 두 번째 인자 전달
ex = df['a'].apply(my_exp, n=2)
print(ex)

# 데이터 프레임에 apply 메서드 사용방법
def print_me(x):
    print(x)

# axis=0 열방향 적용, axis=1 행방향적용
print(df.apply(print_me, axis=0))

# 3개 인자를 받는 함수 사용
def avg_3(x, y, z):
    return (x + y + z) / 3
'''
print(df.apply(avg_3))의 경우, 1개의 인자만 전달받았다는 오류 발생,
avg_3에 열 단위 데이터가 전달되었지만 1개의 인자로 인식하는 오류임.
따라서 다음과 같이 함수 변경
'''
def avg_3_apply(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x + y + z) / 3
print(df.apply(avg_3_apply))

# 행방향 데이터 처리
def avg_2_apply(row):
    sum = 0
    for item in row:
        sum += item
    return sum / df.shape[1]

print(df.apply(avg_2_apply, axis=1))