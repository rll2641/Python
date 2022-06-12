from collections import Counter
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['ball']
# re.sub 한다음 -> lower() -> split()
paragraph_list = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]

# 딕셔너리형태
counts = Counter(paragraph_list)
print(counts.most_common()[0][0])