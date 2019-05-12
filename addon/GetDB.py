import time
import sqlite3
import datetime
def GetDB(Contents):
    nows = time.localtime()
    s = datetime.datetime.now()
    TodayDates = "A_%04d_%02d_%02d"%(nows.tm_year, nows.tm_mon, nows.tm_mday)
    conn = sqlite3.connect('/SCH_CHAT_BOT/DATABASE/kakaotalkLog.db')
    try:
        cursor = conn.cursor()
        cursor.execute("insert into "+str(TodayDates)+" (PressedName,Time) values(?,?)",(Contents,str(s)))
        conn.commit()
    except:
        cursor = conn.cursor()
        sql = 'create table %s (PressedName text,  Time text)'%(TodayDates)
        cursor.execute(sql)
        conn.commit()
        cursor.execute("insert into "+str(TodayDates)+" (PressedName,Time) values(?,?)",(Contents,str(s)))
        conn.commit()
    conn.close()
