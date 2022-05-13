from mrtlogin import *
from mrtsearch import *
from mrtreservation import *

class myrealtripmain(myrealtripreservation):

    def __init__(self):
        super().__init__()

    # 로그인 및 선택
    def Login_select(self):
        self.login()
        self.select_city()
        self.select_day()
    
    # 웹 불러오기 및 로그인
    def Call_web(self):
        self.call_brower()
        self.login_web()
    
    # 도착,출발,가는날,오는날 선택
    def select_where_when(self):
        self.select_depart()
        self.select_arrive()
        self.select_when()
    
    # 예약하기
    def reservation_airplane(self):
        self.select_reservation()

if __name__=="__main__":
    a = myrealtripmain()
    a.Login_select()
    a.Call_web()
    a.select_where_when()