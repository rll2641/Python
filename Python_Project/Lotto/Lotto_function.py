# 로또번호를 구하는 간단한 프로젝트
# 조건 1 : 지난 회차의 값이 중복되면 안됀다
# 조건 2 : 로또 값이 연속된 숫자면 안됀다 ex (2,3)

import random


class Lotto:

    def __init__(self):
        self.L_result = 0  # 지난 당첨회차번호 저장
        self.P_result = 0  # 난수값 저장

    def Last_Lotto_Num(self):
        self.L_result = list(input("지난 당첨회차 로또번호 입력: "))
        while " " in self.L_result:  # 리스트 안에 공백삭제
            self.L_result.remove(" ")
        self.L_result = list(map(int, self.L_result))  # 리스트안의 문자열을 정수로 바꿈

    def Random_value(self):
        save_num = []  # 로또값 저장을 위한 리스트
        while len(save_num) != 6:
            self.P_result = random.randint(1, 45)
            if self.P_result in self.L_result:  # 지난회차의 수와 중복될시 값을 다시 받음
                continue
            elif self.P_result - 1 in save_num or self.P_result + 1 in save_num:  # 연속된수 불가
                continue
            elif self.P_result in save_num:  # 로또번호가 중복이 안돼게 하기
                continue
            else:
                save_num.append(self.P_result)
        save_num.sort()
        return save_num
