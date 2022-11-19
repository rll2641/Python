import seaborn as sns
import matplotlib.pyplot as plt

# 앤스콥 데이터 집합 불러오기
# dataset 열이 데이터 그룹을 구분한다.
anscombe = sns.load_dataset("anscombe")
print(anscombe)

# I 그룹 데이터 추출
dataset_1 = anscombe[anscombe['dataset'] == 'I']
# I 그룹의 x 열, y열을 시각화(선)
plt.plot(dataset_1['x'], dataset_1['y'])
plt.show()
# 시각화(점)
plt.plot(dataset_1['x'], dataset_1['y'], 'o')
plt.show()

# 그래프 4개 그리기
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

# 그래프 격자가 위치할 기본 틀(fig)
fig = plt.figure()

# add_subplot 메서드로 그래프 격자를 그린다. 
# add_subplot(그래프 기본 틀의 행 크기, 그래프 기본 틀의 열 크기)
# 크기가 기본값 1(최대크기), 2(1의 크기를 2분의1)
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(dataset_1['x'], dataset_1['y'])
axes2.plot(dataset_2['x'], dataset_2['y'])
axes3.plot(dataset_3['x'], dataset_3['y'])
axes4.plot(dataset_4['x'], dataset_4['y'])

# 격자 제목 변경
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

# 기본 틀 제목 변경
fig.suptitle('Anscombe Data')

# tight_layout으로 레이아웃 조절
fig.tight_layout()

plt.show()