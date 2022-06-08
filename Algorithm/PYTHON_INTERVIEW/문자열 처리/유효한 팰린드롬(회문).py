s = list(input("입력: "))
strs = []
for i in s:
    # isalnum -> 문자열이 한글,영어,숫자면 참 아니면 거짓 리턴
    if i.isalnum():
        strs.append(i.lower())

# 팰린드롬 확인
while len(strs) > 1:
    if strs.pop(0) != strs.pop():
        print("false")
        exit(0)
print('true')

# ---------------------deque-------------------- #
from collections import deque
import re
# 리스트 내포(리스트 컴프리헨션)
strs_03 = deque([i.lower() for i in s if i.isalnum()])

while len(strs_03) > 1:
    if strs_03.popleft() != strs_03.pop():
        print('false')
        exit(0)
print('true')

# ----------------------슬라이싱------------------ #
strs_02 = ("".join(s)).lower()
# 정규 표현식, 패턴 대체: sub(정규표현식, 대상 문자열, 치환문자) ->매치되는것을 대상 문자열로 바꾸겠다
strs_02 = re.sub('[^a-z0-9]', '', strs_02)
# ::-1 -> 리스트 뒤집기
if strs_02 == strs_02[::-1]:
    print('true')
else:
    print('false')
    
