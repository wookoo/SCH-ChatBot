import time
import sqlite3 #db 접근을 위한 sqlite3 라이브러리 import
import datetime
def GetDB(Contents): #누른 버튼을 매개변수로 받는다.
    nows = time.localtime() #현재 시간 정보를 가져온다
    s = datetime.datetime.now()
    TodayDates = "A_%04d_%02d_%02d"%(nows.tm_year, nows.tm_mon, nows.tm_mday) #테이블을 생성하기 또는 검색하기 위한 쿼리 생성
    conn = sqlite3.connect('/SCH_CHAT_BOT/DATABASE/kakaotalkLog.db') #db 에 접속후
    cursor = conn.cursor() #커서 객체 생성
    try:

        cursor.execute("insert into "+str(TodayDates)+" (PressedName,Time) values(?,?)",(Contents,str(s))) #TodayDates 테이블에 값을 넣어본다
        conn.commit()
    except:#TodayDates 테이블에 값을  넣는게 실패하면
        sql = 'create table %s (PressedName text,  Time text)'%(TodayDates) #테이블을 생성하고
        cursor.execute(sql)
        conn.commit()
        cursor.execute("insert into "+str(TodayDates)+" (PressedName,Time) values(?,?)",(Contents,str(s))) #그 안에 값을 넣는다
        conn.commit()
    conn.close() #db 와 연결을 끊는다.
