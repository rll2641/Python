from selenium import webdriver
from selenium.webdriver.common.by import By

class myrealtripLogin:

    def __init__(self):
        # myrealtrip의 아이디,패스워드,로그인 입력창의 xpath주소 저장.
        self.idXpath = "//*[@id='userEmail']"
        self.pwXpath = "//*[@id='userPasswordCurrent']"
        self.loginCss = ".Button-module__button--1H779.Button-module__primary--3KITS.Button-module__large--xFJf5.Button-module__block--2gnY_"
        self.airXpath = "//*[@id='flights-link']/span"
        self.advXpath = "/html/body/div[10]/div/button[1]"

    # 로그인
    def login(self):
        self.yourId = input("아이디 입력: ")
        self.yourPw = input("비밀번호 입력: ")
    
    # 브라우저 열기
    def call_brower(self):
        try:
            # 변수에 객체저장
            self.driver = webdriver.Chrome(executable_path='C:/Users/jh/OneDrive/바탕 화면/study/Pythonvs/selenium\chromedriver.exe')
            # 변수를 이용해 브라우저 불러오기
            self.driver.get("https://www.myrealtrip.com/users/email_sign_in")
            # 웹사이트가 로딩되는 동안 초(인자값) 기다림
            self.driver.implicitly_wait(5)
            # 전체창
            self.driver.maximize_window()
        except:
            print("브라우저 열기 실패!")
        else:
            print("브라우저 열기 성공!")

    # 브라우저에 아이디,비밀번호 입력 후 로그인창 클릭
    def login_web(self):
        try:
            try:
                # find_element로 html의 특정 요소에 대한 주소,아이디,클래스네임,css_selector찾기
                elemId = self.driver.find_element(By.XPATH, self.idXpath)
                # 찾은 변수를 통해 click하기 = 마우스클릭
                self.driver.execute_script("arguments[0].click();", elemId) # = elemId.click()
                # send keys는 키보드로 입력하는 것과 같음
                elemId.send_keys(self.yourId)
            except:
                print("아이디입력 실패!")
            try:
                elemPw = self.driver.find_element(By.XPATH, self.pwXpath)
                elemPw.click()
                elemPw.send_keys(self.yourPw)
            except:
                print("비밀번호 입력 실패")
            # 해쉬알고리즘 때문에 xpath값이 항상 달라져서 css_selector로 함
            self.driver.find_element(By.CSS_SELECTOR, self.loginCss).click()
            self.driver.find_element(By.XPATH, self.advXpath).click()
            self.driver.find_element(By.XPATH, self.airXpath).click()
            self.driver.implicitly_wait(10)
        except:
            print("로그인 실패!")
        else:
            print("로그인 성공!")