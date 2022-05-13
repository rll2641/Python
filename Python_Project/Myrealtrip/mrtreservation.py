from mrtlogin import *
from mrtsearch import *
from selenium.webdriver.common.by import By

class myrealtripreservation(myrealtripsearch):

    def __init__(self):
        super().__init__()
        # 항공권 css_selector
        self.airList = '#OWList > li'
        self.airList2 = '#RTList > li'
        self.button = "//*[@id='div_dom_totalPrice']/div[2]/table/tfoot/tr/td[3]/button"

    # 예약 보여주기
    def show_reservation(self, aplist):
        name = self.driver.find_elements(By.CSS_SELECTOR, aplist)
        num = int(input("불러올 리스트 개수: "))
        # 리스트 갯수 설정 
        lname = name[:num]
        # 반복문와 split(인자값을 구분으로 나눈다)함수로 리스트로 출력
        for n in lname:
            for i in range(1):
                show = n.text.split('\n')
                print(show)

    # 예약선택
    def select_num(self):
        self.b = input("항공편입력ex(TW_9961): ")
        self.c = input("가격입력: ")

    # 예약클릭
    def select_reservation(self):
        self.show_reservation(self.airList)
        self.select_num()
        self.driver.find_element(By.XPATH, "//*[@id='OW_{0}_{1}']".format(self.b, self.c)).click()
        self.driver.implicitly_wait(10)
        self.show_reservation(self.airList2)
        self.select_num()
        self.driver.find_element(By.XPATH, "//*[@id='RT_{0}_{1}']".format(self.b, self.c)).click()
        self.driver.find_element(By.XPATH, self.button).click()
        self.driver.implicitly_wait(10)
        # mrtsearch.py에 있는 frame이동
        self.move_to_iframe(self.iframeSelect2)
        self.driver.find_element(By.XPATH, "//*[@id='k1_pop_wrap']/div[2]/div[2]/div/label/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='k1_pop_wrap']/div[2]/div[2]/a").click()
        self.driver.switch_to.default_content()