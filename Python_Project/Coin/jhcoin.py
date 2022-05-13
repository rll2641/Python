import pyupbit
import datetime
import time

# 업비트의 각자 코드 입력
access = "bvKAlsmKfCxd6r3BCv1WheCXKHlh4GCaRB8BSrak"         
secret = "nENom0nvzCJAybD31mBaKXHPP9KbNPcwPixeFZz4"         

# 시작시간을 위한 함수
def get_start_time(ticker):
    # get_ohlcv의 2번째 매개변수로 day라는 문자열을 주게 되면 그날의 시작시간이 나오는데 그게 9시로 설정되어있다.(그냥 ticker로 넘겨주게되면 krw-btc의 값이 넘어간다)
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    # df의 값 중 첫번째 즉 인덱스[column]의 첫번째 index[0]의 값이 시간인데 이걸 받아와서 start_time에 저장.
    start_time = df.index[0] + datetime.timedelta(hours=6)
    return start_time

# 매수 목표가를 위한 함수
def get_target_price(ticker, k):
    # 하루치의 정보를 df(데이터프레임)에 저장.
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    # df.iloc[0][3]은 .iloc의 위치 인덱싱을 사용해 count=1(하루치의 시가,저가,종가등등)중에 저가를 뽑아준다.
    low_price = df.iloc[0,2]
    # 목표매수가 설정. 저가*1.02(1.02는 저가의 +2퍼센트를 매수하기 위해 1.02를 곱해준 값을 target_price에 저장)
    target_price = low_price * k
    return target_price

# 현재가 조회를 위한 함수
def get_current_price(ticker):
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 잔고 조회
def get_balance(ticker):
    # pyupbit에서 제공하는 get_balances 메서드는 보유중인 모든 암호화폐의 잔고 및 단가 정보를 딕셔너리로 조회한다.
    balance = upbit.get_balances()
    for b in balance:
        # b 딕셔너리중 key의 값이 currency이고 value의 값이 ticker가 맞고
        if b['currency'] == ticker:
            # key의 값이 balance가 거짓이 아니면 float형태의 b['balance']의 값을 return한다.
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("auto trading start!")

# 본격 매매시작
while True:
    try:
        # 현재시간 datetime모듈의 now함수는 현재시간을 반환한다.
        now = datetime.datetime.now()
        # 시작시간
        start_time = get_start_time("KRW-BTC")
        # 끝나는 시간 = 시작시간(15:00) + 17시간 = 8:00
        end_time = start_time + datetime.timedelta(hours=17)
        
        # 시간이 15:00 ~ 현재 ~ 8:00시가 되면 자동매매를 한다.
        if start_time < now < end_time:
            target_price = get_target_price("KRW-BTC", 1.02)
            current_price = get_current_price("KRW-BTC")
            # 목표 매수가가 현재가보다 낮을 때 매수
            if target_price < current_price:
                my_krw = get_balance("KRW")
                # 내 원화가 5000원(최소거래금액) 이상이면 비트코인 매수 시작
                if my_krw > 5000:
                    # 0.9995를 곱해주는 이유는 업비트의 수수료가 0.05퍼센트이기 때문             
                    upbit.buy_market_order("KRW-BTC", my_krw*0.9995)
            if (target_price*1.02) < current_price:
                # 내 비트코인 잔고 저장
                btc = get_balance("BTC")
                # 현재 내 비트코인 잔고가 최소금액인 5000원(0.00011btc)를 넘으면 전량매도
                if btc > 0.00011:
                    upbit.sell_market_order("KRW-BTC", btc*0.9995)
        # 나머지 시간 휴식
        else:
            time.sleep(21600)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
