# ---------------------deque-------------------- #
from collections import deque
# 리스트 내포(리스트 컴프리헨션)
# isalnum -> 문자열이 한글,영어,숫자면 참 아니면 거짓 리턴
strs = deque([i.lower() for i in input() if i.isalnum()])
while len(strs) > 1:
    if strs.popleft() != strs.pop():
        print('no')
        exit(0)
print('yes')

# ----------------------슬라이싱------------------ #
import re
# 정규 표현식, 패턴 대체: sub(정규표현식, 대상 문자열, 치환문자) -> 매치되는것을 대상 문자열로 바꾸겠다
strs = re.sub('[^a-z]', '', input().lower())
if strs == strs[::-1]: # ::-1 -> 리스트 뒤집기
    print('yes')
else:
    print('no')