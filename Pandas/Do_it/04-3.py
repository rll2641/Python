import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

ax = plt.subplots()
# distplot 메서드 - 히스토그램과 밀집도 그래프를 같이 그려준다.
ax = sns.distplot(tips['total_bill'])
ax.set_title('Total Bill')
plt.show()

# regplot 메서드 - 산점도 그래프와 회귀선을 같이 그려준다.
bx = plt.subplots()
bx = sns.regplot(x='total_bill', y='tip', data=tips)
plt.show()

# 육각그래프 - jointplot kind="hex"
# 2차원 밀집도 - kdeplot (shade=True, 음영효과)
# 산점도 그래프의 점을 다른 기호로 표현 lmplot markers= ['o', 'x']