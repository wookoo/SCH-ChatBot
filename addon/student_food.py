import time
import codecs
import sqlite3
def hak(food_name):
    if food_name == '• 향설 1 관':
        food_name = 'hyang1'
    elif food_name =='• 향설 2 관':
        food_name = 'hyang2'
    elif food_name =='• 향설 3 관':
        food_name = 'hyang3'
    elif food_name == '• 학생회관':
        food_name = 'student'
    elif food_name == '• 교직원 식당':
        food_name = 'teacher'
    now = time.localtime()
    week = ("월요일","화요일","수요일","목요일","금요일","토요일","일요일")
    today = week[now.tm_wday]
    query = "select * from " + food_name + ' where day ="'+today+'"'
    conn = sqlite3.connect('/SCH_CHAT_BOT/DATABASE/meals.db')
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    return row[2]
