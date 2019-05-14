import time #시간을 가져오기 위한 time 모듈 import
import sqlite3 #db 접근을 위한 sqlite3 모듈 import


def hak(food_name):
    change_eng{'• 향설 1 관':'hyang1','• 향설 2 관':'hyang2','• 향설 3 관':'hyang3','• 학생회관':'student','• 교직원 식당':'teacher'}
    #if 문 대신 dictionary 로 가독성 좋게 수정
    now = time.localtime() #현재 시간을 가져온다.
    week = ("월요일","화요일","수요일","목요일","금요일","토요일","일요일") #요일을 한글로 바꾸기 위해 배열
    today = week[now.tm_wday] #tm_wday 는 월~일을 숫자로 표기한것이므로 week 의 tm_wday 의 값을 오늘 요일로 설정
    query = "select * from " + change_eng[food_name] + ' where day ="'+today+'"' #change_eng의 food_name토큰의 테이블의 오늘 식단을 쿼리로 만든다
    conn = sqlite3.connect('/SCH_CHAT_BOT/DATABASE/meals.db') #meals.db 를 열고
    cursor = conn.cursor()
    cursor.execute(query) #query 를 요청한다
    row = cursor.fetchone()
    return row[2] #그 후 값을 반환한다.
