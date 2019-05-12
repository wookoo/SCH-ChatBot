from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.request
from addon import student_food
from addon import train
from addon import find_book
from addon import weather_edit
from addon import asanbus
from addon import calander
from addon import GetLibrary
from addon import GetDB
from module.buttons import *
from module import process
from module.message import *
from module.message_eng import *
from module.buttons_eng import *
from addon import weather_edit_eng

import time

def keyboard(request):


    return JsonResponse({'type': 'buttons',
                        'buttons' : basic_button
        },json_dumps_params = {'ensure_ascii':False})



@csrf_exempt
def message(request):


    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']
    GetDB.GetDB(content_name)
    type_name = received_json['type']

#===================도서관 좌석보기 ================================
    if content_name == '• 도서관':
        msg = '• 도서관에 관한 정보를 확인하실 수 있습니다.\n• 원하는 버튼을 눌러주세요.'
        return process.JsonReturn(msg,library_button)

    elif content_name == '• 도서관 이용 정보':
        return process.JsonReturn(library_info_msg,library_button)

    elif content_name == '• 열람실 좌석 확인':
        msg = content_name+' 항목을 선택 하셨습니다.'
        return process.JsonReturn(msg,reading_zone)

    elif content_name == '• 제 1 열람실':
        msg = GetLibrary.GetLibrary(0)
        return process.JsonReturn(msg,reading_zone)
        #return process.JsonLibraryReturn(first_reading_msg ,'first',1060,502,reading_zone)

    elif content_name == '• 제 2 열람실':
        msg = GetLibrary.GetLibrary(1)
        return process.JsonReturn(msg,reading_zone)

    elif content_name == '• 제 3 열람실':
        msg = GetLibrary.GetLibrary(2)
        return process.JsonReturn(msg,reading_zone)

    elif content_name == '• 멀티존':
        msg = GetLibrary.GetLibrary(3)
        return process.JsonReturn(msg,reading_zone)

    elif content_name == '• 인터넷존':
        msg = GetLibrary.GetLibrary(4)
        return process.JsonReturn(msg,reading_zone)

    elif content_name == '• 프리미어존':
        msg = GetLibrary.GetLibrary(5)
        return process.JsonReturn(msg,reading_zone)

    elif content_name == '• 처음으로' or content_name == '처음으로' :
        msg = '• 처음으로 돌아갑니다.'
        return process.JsonReturn(msg,basic_button)
    elif content_name == '• 문의사항':
        msg = "• 문의하기는 상담원 채팅으로 이용해주세요."
        return process.JsonReturn(msg,basic_button)
#==================날씨코드==================
    elif content_name == '• 날씨':
        msg = weather_edit.weather()
        return process.JsonReturn(msg,basic_button)

#=======================학식 구현 코드===========
    elif content_name == '• 학식':
        msg ='• 학식에 관한 정보를 확인 하실수 있습니다.\n• 원하는 식당을 선택하세요.'
        return process.JsonReturn(msg,food)

    elif content_name == '• 향설 1 관':
        msg = student_food.hak(content_name)
        msg = calander.calander() + '\n■ 향설 1 관 학식 정보 ■\n\n' +msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 향설 2 관':
        msg = student_food.hak(content_name)
        msg = calander.calander() + '\n■ 향설 2 관 학식 정보 ■\n\n' +msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 향설 3 관':
        msg = student_food.hak(content_name)
        msg = calander.calander() +'\n■ 향설 3 관 학식 정보 ■\n\n' +msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 학생회관':
        msg = student_food.hak(content_name)
        msg = calander.calander() + '\n■ 학생회관 학식 정보 ■\n\n' + msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 교직원 식당':
        msg = student_food.hak(content_name)
        msg = calander.calander() + '\n■ 교직원 식당 학식 정보 ■\n\n' + msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 학식 이용 시간':
        return process.JsonReturn(student_food_info_msg,food)


#교통정보 구현 =====================================
    elif content_name == '• 교통':
        msg = '학교에서 탑승하실수 있는 교통수단 정보입니다.'
        return process.JsonReturn(msg,ride)

    elif content_name == '학내순환 버스':

        nows = time.localtime()
        times = (int(nows.tm_hour)*60)+int(nows.tm_min)
        today_da = weeks[nows.tm_wday]

        if (times < 500 or times > 1080 or today_da =='sun' or today_da =='sat'):
            msg = '현재 학내 순환 버스가 운행중이지 않습니다.\n학내순환 버스는 평일 8:00 ~ 18:00 까지 운행합니다.'
            return process.JsonReturn(msg,ride)

        else:
            msg = '파란 핀은 정류소, 빨간 핀은 버스 위치입니다.\n현재 시범운행 진행중이기 때문에 버스 위치가 승강장에서 멈춰 있을수 있습니다. 그러나 운행은 정상적으로 되고 있는거에요.\n새로고침을 하시면 새 정보를 확인 가능합니다.\n http://bit.ly/2s41M7x'
            return process.JsonReturn(msg,ride)


    elif content_name == '• 순천향 대학교 → 신창역':
        nows = time.localtime()
        times = (int(nows.tm_hour)*60)+int(nows.tm_min)
        today_da = weeks[nows.tm_wday]
        if (times < 655 or times >  1349 or today_da == 'sat') and (today_da != 'sun'):
            return process.JsonReturn(bus_to_sin_error_msg,ride)

        elif (times < 890 or times >  1360) and (today_da == 'sun'):
            return process.JsonReturn(bus_to_sin_error_msg,ride)

        else:
            msg = train.bus_time()
            msg = msg
            return process.JsonReturn(msg,ride)

    elif content_name == '• 신창역 지하철 출발시간':
        minute = train.train_time()
        msg = '■ 신창역 지하철 출발 시간 ■\n\n• 이번 지하철은 ' + str(minute[0]) +'분 후 출발 예정입니다. (' + minute[1] + '행)\n• 다음 지하철은 '+str(minute[2])+  '분 후 출발 예정입니다. (' + minute[3] + '행)\n\n• 지하철 시간표 데이터로 정보를 제공합니다.\n• 참고용으로만 사용해주세요.'
        return process.JsonReturn(msg,ride)

    elif content_name == '• 신창 시외버스 터미널':
        msg = '■ 신창 시외버스 터미널 ■\n\n• 사진을 크게 보실려면 아래 링크로 접속하세요.\n• http://bit.ly/2KXYBa3'
        return JsonResponse(
            {
                'message': {
                    'text': msg,
                    'photo':{
                        'url': 'http://wookoo.ze.am/photo/bus.jpg',
                        'width': 1280,
                        'height':1162

                }},
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ride
                }
            }
        )
    elif content_name == '• 학교 주변 시내버스':
        msg = '• 학교 주변에서 탑승하실수 있는 버스 정보 입니다.'
        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 순천향대학교 후문 (신창초 방향)':
        xml = asanbus.get_xml(288001690)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start(402,'ASB288000044',xml)
        bus_403 = asanbus.start(403,'ASB288000045',xml)
        bus_404 = asanbus.start(404,'ASB288000209',xml)
        msg = '■ 순천향대학교 후문 (신창초) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 순천향대학교 후문 (경희학성 방향)':
        xml = asanbus.get_xml(288001691)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start(402,'ASB288000244',xml)
        bus_403 = asanbus.start(403,'ASB288000245',xml)
        bus_404 = asanbus.start(404,'ASB288000246',xml)
        msg = '■ 순천향대학교 후문 (경희학성) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 경희학성아파트 (순천향대 후문 방향)':
        xml = asanbus.get_xml(288000362)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start(402,'ASB288000044',xml)
        bus_403 = asanbus.start(403,'ASB288000045',xml)
        bus_404 = asanbus.start(404,'ASB288000209',xml)
        msg = '■ 경희학성 (순천향대후문) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 경희학성아파트 (창암1리 방향)':
        xml = asanbus.get_xml(288001578)
        xml = asanbus.xml_checker(xml)
        bus_350 = asanbus.start(350,'ASB288000240',xml)
        bus_352 = asanbus.start(352,'ASB288000041',xml)
        bus_402 = asanbus.start(402,'ASB288000044',xml)
        bus_403 = asanbus.start(403,'ASB288000245',xml)
        bus_404 = asanbus.start(404,'ASB288000246',xml)
        msg = '■ 경희학성 (창암1리) ■\n\n'
        msg = msg + bus_350 + '\n\n'+ bus_352 + '\n\n'+ bus_402+ '\n\n'+ bus_403+ '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 순천향대학교 (와신1리 방향)':
        xml = asanbus.get_xml(288010276)
        xml = asanbus.xml_checker(xml)
        bus_430 = asanbus.start(430,'ASB288000048',xml)
        bus_450 = asanbus.start(450,'ASB288000050',xml)
        bus_451 = asanbus.start(451,'ASB288000051',xml)
        msg = '■ 순천향대학교 (외산1리) ■\n\n'
        msg = msg + bus_430 + '\n\n'+ bus_450 + '\n\n'+ bus_451

        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 순천향대학교':
        xml = asanbus.get_xml(288000377)
        xml = asanbus.xml_checker(xml)
        bus_400 = asanbus.start(400,'ASB288000243',xml)
        bus_404 = asanbus.start(404,'ASB288000246',xml)
        bus_450 = asanbus.start(450,'ASB288000248',xml)
        bus_451 = asanbus.start(451,'ASB288000249',xml)
        msg = '■ 순천향대학교 ■\n\n'
        msg = msg + bus_400 + '\n\n'+ bus_404 + '\n\n'+ bus_450+ '\n\n'+ bus_451

        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 신창역 (행목 1리 방향)':

        xml = asanbus.get_xml(288001943)
        xml = asanbus.xml_checker(xml)
        bus_32 = asanbus.start(32,'ASB288000189',xml)
        bus_41 = asanbus.start(41,'ASB288000246',xml)
        bus_41_1 = asanbus.start('41-1','ASB288000300',xml)
        bus_402 = asanbus.start(402,'ASB288000244',xml)
        bus_403 = asanbus.start(403,'ASB288000245',xml)
        bus_404 = asanbus.start(404,'ASB288000246',xml)
        msg = '■ 신창역 (행목 1리) ■\n\n'
        msg = msg + bus_32 + '\n\n'+ bus_41 + '\n\n'+ bus_41_1 + '\n\n'+ bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404

        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 신창역 (행목리 방향)':
        xml = asanbus.get_xml(288001942)
        xml = asanbus.xml_checker(xml)
        bus_32 = asanbus.start(32,'ASB288000297',xml)
        bus_41 = asanbus.start(41,'ASB288000191',xml)
        bus_41_1 = asanbus.start('41-1','ASB288000192',xml)
        bus_402 = asanbus.start(402,'ASB288000044',xml)
        bus_403 = asanbus.start(403,'ASB288000045',xml)
        bus_404 = asanbus.start(404,'ASB288000209',xml)
        msg = '■ 신창역 (행목리) ■\n\n'
        msg = msg + '\n'+ bus_32 + '\n\n'+ bus_41 + '\n\n'+ bus_41_1 + '\n\n'+ bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)
#건물 정보 파트 ===============================================
    elif content_name == '• 순천향 건물':
        msg = '• 학교 건물 정보를 확인하실수 있습니다.'
        return process.JsonReturn(msg,building)

    elif content_name == '• 편의시설':
        return process.JsonMapReturn(building_comfortable_msg,'편의시설.jpg',1216,1294)

    elif content_name == '• 학교 지도':
        return process.JsonMapReturn(school_map_msg,'지도.jpg',1280,719)

    elif content_name == '• 학교 건물 번호':
        return process.JsonMapReturn(building_number_msg,'강의실넘버.png',1280,1280)

#도서검색 파트 =================================================

    elif content_name == '• 도서 검색':
        return process.JsonErrorReturn(search_book_msg)

#보건실 이용시간 정보=========================================
    elif content_name == '• 보건실':
        return process.JsonReturn(health_room_msg,basic_button)

    elif content_name == '• WI-FI':
        return process.JsonReturn(wifi_msg,basic_button)
#택시 정보====================================
    elif content_name == '• 신창 택시 연락처 정보':
        return process.JsonReturn(taxi_msg,ride)


# 영어 부분 ====================================================================
    elif content_name == '• Library':
        msg = '• You can get information about library.\n• Choose buttons and press.'
        return process.JsonReturn(msg,library_button_eng)

    elif content_name == '• Reading Room Status':
        msg = '• Content : Reading Room Status.'

        return process.JsonReturn(msg,reading_zone_eng)

    elif content_name == '• First Reading room':
        msg = GetLibrary.GetLibraryENG(0)
        return process.JsonReturn(msg,reading_zone_eng)

    elif content_name == '• Second Reading room':
        msg = GetLibrary.GetLibraryENG(1)
        return process.JsonReturn(msg,reading_zone_eng)

    elif content_name == '• Third Reading Room':
        msg = GetLibrary.GetLibraryENG(2)
        return process.JsonReturn(msg,reading_zone_eng)

    elif content_name == '• Multi Zone':
        rmsg = GetLibrary.GetLibraryENG(3)
        return process.JsonReturn(msg,reading_zone_eng)

    elif content_name == '• Internet Zone':
        msg = GetLibrary.GetLibraryENG(4)
        return process.JsonReturn(msg,reading_zone_eng)

    elif content_name == '• Premier Zone':
        msg = GetLibrary.GetLibraryENG(5)
        return process.JsonReturn(msg,reading_zone_eng)

    elif content_name == '• Go First Page' or content_name == 'Go First Page' :
        msg = '• Return To First Page.'
        return process.JsonReturn(msg,basic_button_eng)

    elif content_name == '• Contact Us':
        return process.JsonReturn(developer_question_msg_eng,basic_button_eng)
#==================날씨영어==================
    elif content_name == '• Weather':
        msg = weather_edit_eng.weather()
        return process.JsonReturn(msg,basic_button_eng)

#=======================학식 구현 영어===========
    elif content_name == '• Cafeteria':
        msg ='• You can get information about cafeteria.\n• Choose buttons and press.\n• We don`t support english menu T.T'
        return process.JsonReturn(msg,food_eng)

    elif content_name == '• Hyangsul 1 Hall':
        msg = student_food.hak('• 향설 1 관')
        msg = '■ Hyangsul 1 Menu ■\n\n' + msg
        return process.JsonReturn(msg,food_eng)

    elif content_name == '• Hyangsul 2 Hall':
        msg = student_food.hak('• 향설 2 관')
        msg = '■ Hyangsul 2 Menu ■\n\n' + msg
        return process.JsonReturn(msg,food_eng)

    elif content_name == '• Hyangsul 3 Hall':
        msg = student_food.hak('• 향설 3 관')
        msg = '■ Hyangsul 3 Menu ■\n\n' + msg
        return process.JsonReturn(msg,food_eng)

    elif content_name == "• Student's Hall":
        msg = student_food.hak('• 학생회관')
        msg = "■  Student's Hall Menu ■\n\n" + msg
        return process.JsonReturn(msg,food_eng)

    elif content_name == '• Teaching Staff Cafeteria':
        msg = student_food.hak('• 교직원 식당')
        msg = '■ Teaching Staff Cafeteria Menu ■\n\n' + msg
        return process.JsonReturn(msg,food_eng)

    elif content_name == '• Cafeteria hours of operation':
        return process.JsonReturn(student_food_info_msg_eng,food_eng)


#교통정보 영어=====================================
    elif content_name == '• Transportation':
        msg = '• This is the information about the transportation system you can get on at school.'
        return process.JsonReturn(msg,ride_eng)

    elif content_name == '• SCH Univ. → Sinchang Station':
        nows = time.localtime()
        times = (int(nows.tm_hour)*60)+int(nows.tm_min)
        today_da = weeks[nows.tm_wday]
        if (times < 655 or times >  1349 or today_da == 'sat') and (today_da != 'sun'):
            return process.JsonReturn(bus_to_sin_error_msg_eng,ride_eng)

        elif (times < 890 or times >  1360) and (today_da == 'sun'):
            return process.JsonReturn(bus_to_sin_error_msg_eng,ride_eng)

        else:
            msg = train.bus_time_eng()
            msg = msg
            return process.JsonReturn(msg,ride_eng)

    elif content_name == '• Sinchang Station Subway Departure time':
        minute = train.train_time()
        msg = '■ Sinchang Sta. Subway Departure time ■\n\n• This subway departing after ' + str(minute[0]) +'min. (Destination : ' + minute[1] + ')\n• Next subway departing after '+str(minute[2])+  'min. (Destination : ' + minute[3] + ')\n\n• Information is provided by subway timetable data.\n•  Use for reference only..'
        return process.JsonReturn(msg,ride_eng)

    elif content_name == '• SCH Univ. Back gate (1690)':
        xml = asanbus.get_xml(288001690)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start_eng(402,'ASB288000044',xml)
        bus_403 = asanbus.start_eng(403,'ASB288000045',xml)
        bus_404 = asanbus.start_eng(404,'ASB288000209',xml)
        msg = '■ SCH Univ. Back gate (1690) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop_eng)

    elif content_name == '• SCH Univ. Back gate (1691)':
        xml = asanbus.get_xml(288001691)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start_eng(402,'ASB288000244',xml)
        bus_403 = asanbus.start_eng(403,'ASB288000245',xml)
        bus_404 = asanbus.start_eng(404,'ASB288000246',xml)
        msg = '■ SCH Univ. Back gate (1691) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop_eng)

    elif content_name == '• 경희학성 APT. (362)':
        xml = asanbus.get_xml(288000362)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start_eng(402,'ASB288000044',xml)
        bus_403 = asanbus.start_eng(403,'ASB288000045',xml)
        bus_404 = asanbus.start_eng(404,'ASB288000209',xml)
        msg = '■ 경희학성 APT. (362) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop_eng)

    elif content_name == '• 경희학성 APT. (1578)':
        xml = asanbus.get_xml(288001578)
        xml = asanbus.xml_checker(xml)
        bus_350 = asanbus.start_eng(350,'ASB288000240',xml)
        bus_352 = asanbus.start_eng(352,'ASB288000041',xml)
        bus_402 = asanbus.start_eng(402,'ASB288000044',xml)
        bus_403 = asanbus.start_eng(403,'ASB288000245',xml)
        bus_404 = asanbus.start_eng(404,'ASB288000246',xml)
        msg = '■ 경희학성 APT. (1578) ■\n\n'
        msg = msg + bus_350 + '\n\n'+ bus_352 + '\n\n'+ bus_402+ '\n\n'+ bus_403+ '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop_eng)

    elif content_name == '• SCH Univ. (10276)':
        xml = asanbus.get_xml(288010276)
        xml = asanbus.xml_checker(xml)
        bus_430 = asanbus.start_eng(430,'ASB288000048',xml)
        bus_450 = asanbus.start_eng(450,'ASB288000050',xml)
        bus_451 = asanbus.start_eng(451,'ASB288000051',xml)
        msg = '■ SCH Univ. (10276) ■\n\n'
        msg = msg + bus_430 + '\n\n'+ bus_450 + '\n\n'+ bus_451

        return process.JsonReturn(msg,bus_stop_eng)

    elif content_name == '• SCH Univ. (377)':
        xml = asanbus.get_xml(288000377)
        xml = asanbus.xml_checker(xml)
        bus_400 = asanbus.start_eng(400,'ASB288000243',xml)
        bus_404 = asanbus.start_eng(404,'ASB288000246',xml)
        bus_450 = asanbus.start_eng(450,'ASB288000248',xml)
        bus_451 = asanbus.start_eng(451,'ASB288000249',xml)
        msg = '■ SCH Univ. (377) ■\n\n'
        msg = msg + bus_400 + '\n\n'+ bus_404 + '\n\n'+ bus_450+ '\n\n'+ bus_451

        return process.JsonReturn(msg,bus_stop_eng)

    elif content_name == '• Sinchang Station (1943)':

        xml = asanbus.get_xml(288001943)
        xml = asanbus.xml_checker(xml)
        bus_32 = asanbus.start_eng(32,'ASB288000189',xml)
        bus_41 = asanbus.start_eng(41,'ASB288000246',xml)
        bus_41_1 = asanbus.start_eng('41-1','ASB288000300',xml)
        bus_402 = asanbus.start_eng(402,'ASB288000244',xml)
        bus_403 = asanbus.start_eng(403,'ASB288000245',xml)
        bus_404 = asanbus.start_eng(404,'ASB288000246',xml)
        msg = '■ Sinchang Sta. (1943) ■\n\n'
        msg = msg + bus_32 + '\n\n'+ bus_41 + '\n\n'+ bus_41_1 + '\n\n'+ bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404

        return process.JsonReturn(msg,bus_stop_eng)

    elif content_name == '• Sinchang Sta. (1942)':
        xml = asanbus.get_xml(288001942)
        xml = asanbus.xml_checker(xml)
        bus_32 = asanbus.start_eng(32,'ASB288000297',xml)
        bus_41 = asanbus.start_eng(41,'ASB288000191',xml)
        bus_41_1 = asanbus.start_eng('41-1','ASB288000192',xml)
        bus_402 = asanbus.start_eng(402,'ASB288000044',xml)
        bus_403 = asanbus.start_eng(403,'ASB288000045',xml)
        bus_404 = asanbus.start_eng(404,'ASB288000209',xml)
        msg = '■ Sinchang Sta. (1942) ■\n\n'
        msg = msg + '\n'+ bus_32 + '\n\n'+ bus_41 + '\n\n'+ bus_41_1 + '\n\n'+ bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop_eng)

    elif content_name == '• Near SCH Univ. City Bus':
        msg = '• You can get information about city bus schedule.\n• Information provides real bus time.\n• Buttons : Bus stop (Bus stop ID)\n• Choose buttons and press'
        return process.JsonReturn(msg,bus_stop_eng)
#도서검색 파트 =================================================

    elif content_name == '• 도서 검색':
        return process.JsonErrorReturn(search_book_msg)

#보건실 이용시간 정보=========================================
    elif content_name == '• Health Room':
        return process.JsonReturn(health_room_msg_eng,basic_button_eng)

    elif content_name == '• WI-FI Info':
        return process.JsonReturn(wifi_msg_eng,basic_button_eng)
#택시 정보====================================
    elif content_name == '• Sinchang Taxi Telephone Number':
        return process.JsonReturn(taxi_msg_eng,ride_eng)

    elif content_name == '• Language / 언어':
        msg = '• 언어를 선택하실수 있습니다.' + '\n• You Can Chage Language.'
        return process.JsonReturn(msg,language_button)

    elif content_name == '• 한국어':
        msg = '• 한국어를 선택하셨습니다.'
        return process.JsonReturn(msg,basic_button)

    elif content_name == '• English':
        msg = '• Language Changed.'
        return process.JsonReturn(msg,basic_button_eng)

#디버깅===================================================
    else:
        if type_name == 'photo':
            msg = '• 사진이 아닌 도서 제목을 입력하세요.'
            return process.JsonErrorReturn(msg)

        elif type_name == 'video':
            msg = '• 영상이 아닌 도서 제목을 입력하세요.'
            return process.JsonErrorReturn(msg)

        elif type_name == 'audio':
            msg = '• 음성 파일이 아닌 도서 제목을 입력하세요.'
            return process.JsonErrorReturn(msg)

        elif type_name == 'text':
            content_name2 = content_name.replace(" ","+")
            msge = find_book.result_book(content_name)
            research = "■ 도서관 도서 검색 ■\n\n• '"+ content_name + ' 에 대한 도서 검색 결과 입니다.\n• '+str(msge)
            search_url = 'https://library.sch.ac.kr/search/caz/result?st=KWRD&si=TOTAL&q='+content_name2+'&folder_id=null'
            msg = research + '\n• ' + search_url
            return process.JsonReturn(msg,library_button)



# Create your views here.
