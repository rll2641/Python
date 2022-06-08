logs = ["digi1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
digits, letters = [], []

for i in logs:
    # isdigit 문자열이 숫자로만 이루어져 있는지 확인 함수 모든 문자가 숫자면 true 아니면 false
    if i.split()[1].isdigit():
        digits.append(i)
    else:
        letters.append(i)
        
# sorted(반복가능 자료형, key=파라미터, reverse=파라미터)
# letters의 split한 인덱스1(ex:art can, own kit dig)을 먼저 정렬한 후, 인덱스0(ex: let1, let2, let3)을 기준으로 정렬하겠다.
letters_ = sorted(letters, key=lambda x: (x.split()[1:], x.split()[0]))
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(letters + digits)
print(letters_ + digits)