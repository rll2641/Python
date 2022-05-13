from mrtlogin import *
from selenium.webdriver.common.by import By

class myrealtripsearch(myrealtripLogin):

    def __init__(self):
        super().__init__()
        # 프레임 id
        self.iframeSelect = "ifrSegSelect"
        self.iframeSelect2 = "_ifrm"
        # 출발지 도착지 버튼 xpath
        self.departXpath = "//*[@id='depCtyCodeSearch']"
        self.departXpath2 = "//*[@id='input_search']"
        self.arriveXpath = "//*[@id='txt_arrCtyCode']"
        self.selectCt = "//*[@id='btn_search']"
        # 가는날 오는날 xpath
        self.goXpath = "//*[@id='txt_depDt_view']"
        self.selectWh = "//*[@id='calendarPop']/div[2]/a"
        self.selectLa = "//*[@id='intfareSchForm']/div[3]/a"

    # 선택할 지역 불러오기
    def show_city(self):
        
        for i in range(1,4):
            for j in range(2, 6):
                elem = self.driver.find_element(By.CSS_SELECTOR, "#maincitylist > tbody > tr:nth-child({0}) > td:nth-child({1}) > a".format(i,j))
                print(elem.text, end=" ")

    # 지역 입력
    def select_city(self):
        self.city = input("출발 도시 입력: ")
        self.city2 = input("도착 도시 입력: ")

    # 날짜 선택
    def select_day(self):
        self.day = int(input("가는 요일 선택: "))
        self.day2 = int(input("오는 요일 선택: "))

    # 날짜 검색
    def show_day(self, day):
        if day>0 and day<=6:
            self.driver.find_element(By.XPATH, "//*[@id='datePicker']/div[1]/table/tbody/tr[1]/td[{0}]/a".format(day+1)).click()
        elif day>6 and day<=13:
            self.driver.find_element(By.XPATH, "//*[@id='datePicker']/div[1]/table/tbody/tr[2]/td[{0}]/a".format(day-6)).click()
        elif day>13 and day<=20:
            self.driver.find_element(By.XPATH, "//*[@id='datePicker']/div[1]/table/tbody/tr[3]/td[{0}]/a".format(day-13)).click()
        elif day>20 and day<=27:
            self.driver.find_element(By.XPATH, "//*[@id='datePicker']/div[1]/table/tbody/tr[4]/td[{0}]/a".format(day-20)).click()
        else:
            self.driver.find_element(By.XPATH, "//*[@id='datePicker']/div[1]/table/tbody/tr[5]/td[{0}]/a".format(day-27)).click()
        self.driver.switch_to.default_content()

    # html 특정 iframe으로 이동 (태그에 iframe이 존재하면 특정 요소를 찾을시 그 iframe에 이동 후 요소를 찾아야함)
    def move_to_iframe(self, framid):
        self.frame = self.driver.find_element(By.ID, framid)
        self.driver.switch_to.frame(self.frame)

    # 출발지역 선택 함수
    def select_depart(self):
        try:
            # 특정 프레임 이동
            self.move_to_iframe(self.iframeSelect)
            # 요소찾고 클릭
            self.driver.find_element(By.XPATH, self.departXpath).click()
            # 포인터 다시 맨처음
            self.driver.switch_to.default_content()
            # 특정 프레임 이동
            self.move_to_iframe(self.iframeSelect2)
            # 센드키로 요소에 매개변수 전달
            self.driver.find_element(By.XPATH, self.departXpath2).send_keys(self.city)
            self.driver.find_element(By.XPATH, self.selectCt).click()
            self.driver.switch_to.default_content()
        except:
            print("출발지역 열기 실패!")
    
    # 도착지역 선택 함수
    def select_arrive(self):
        try:
            self.move_to_iframe(self.iframeSelect)
            self.driver.find_element(By.XPATH, self.arriveXpath).click()
            self.driver.switch_to.default_content()
            self.move_to_iframe(self.iframeSelect2)
            self.driver.find_element(By.XPATH, self.departXpath2).send_keys(self.city2)
            self.driver.find_element(By.XPATH, self.selectCt).click()
            self.driver.switch_to.default_content()
        except:
            print("도착지역 열기 실패!")

    # 날짜 선택
    def select_when(self):
        self.move_to_iframe(self.iframeSelect)
        self.driver.find_element(By.XPATH, self.goXpath).click()
        self.driver.switch_to.default_content()
        self.show_day(self.day)
        self.show_day(self.day2)
        self.driver.find_element(By.XPATH, self.selectWh).click()
        self.move_to_iframe(self.iframeSelect)
        self.driver.find_element(By.XPATH, self.selectLa).click()
        self.driver.switch_to.default_content()
        self.driver.implicitly_wait(10)