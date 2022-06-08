import re
import collections

pragraph = "Bob hit :a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

# 문자열에서 영어대문자 - > 소문자, 소문자 외 특수문자 삭제
words = [word for word in re.sub('[^\w]', ' ', pragraph).lower().split() if word not in banned]
# counts == Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
counts = collections.Counter(words)
# 인덱스로 불러오기
print(counts.most_common()[0][0])
