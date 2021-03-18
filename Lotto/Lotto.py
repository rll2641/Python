import os
import Lotto_function


class Intro:

    def __init__(self):
        print("#" * 50)
        print("{0:^45}".format("로또번호 생성기"))
        print("#" * 50)
        print("\n")
        print("{0:^45}".format("[1.로또번호 생성 2.종료]"))

    # noinspection PyMethodMayBeStatic
    def input_num(self, num):
        if num == 1:
            os.system("cls")
        else:
            os.system(0)


i = Intro()
num1 = int(input("메뉴 번호를 입력해주세요: "))
i.input_num(num1)
lo = Lotto_function.Lotto()
lo.Last_Lotto_Num()
num2 = lo.Random_value()
print(num2)
