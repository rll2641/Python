import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# 기초 그래프 그리기

# 히스토그램은 데이터프레임의 열 데이터 분포와 빈도를 살펴보는 용도로 자주 사용한다.
# 변수 하나만 사용해서 그린 그래프를 일변량 그래프라고 한다.

fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)

# x축의 간격을 bins 인자값으로 조정가능하다.
axes1.hist(tips['total_bill'], bins=10)
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')

# 산점도 그래프는 변수 2개를 사용해서 만드는 그래프이며 변수 2개이기 때문에 이변량 그래프라고 한다.
axes2 = fig.add_subplot(2, 2, 2)
axes2.scatter(tips['total_bill'], tips['tip'])
axes2.set_title('Scatterplot of Total Bill vs Tip')
axes2.set_xlabel('Total Bill')
axes2.set_ylabel('Tip')

# 변수 3개 이상을 사용하는 다변량 그래프
def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1

# 새로운 열 추가
tips['sex_color'] = tips['sex'].apply(recode_sex)

axes3 = fig.add_subplot(2, 2, 3)
# s 는 점의 크기, c 는 점의 색상을 의미한다. 
axes3.scatter(x = tips['total_bill'],
              y = tips['tip'],
              s = tips['size'] * 10,
              c = tips['sex_color'],
              alpha=0.5)

axes3.set_title('Total Bill vs Tip colored by')
axes3.set_xlabel('Total_Bill')
axes3.set_ylabel('Tip')

fig.tight_layout()
plt.show()