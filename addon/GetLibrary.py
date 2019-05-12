import requests
import json
#request = urllib.request('https://eseat.sch.ac.kr/EZ5500/SEAT/RoomDisplay.aspx/WEB_PROC_EZ5500_SEAT_ROOM_POLLINGDATA', None, {'Content-Type': 'application/json; charset=euc-kr'})

def GetLibrary(Index):
    url = "https://eseat.sch.ac.kr/EZ5500/SEAT/RoomDisplay.aspx/WEB_PROC_EZ5500_SEAT_ROOM_POLLINGDATA"
    header = {'Content-Type': 'application/json; charset=euc-kr'}
    result = requests.post(url,headers=header, params=None)
    contents = result.content
    NeedJSON = contents.decode("euc-kr")
    results = json.loads(NeedJSON)
    Split = ((results["d"][5:]).split("}"))
    Info = []
    for line in range(0,6):
        Info.append((Split[line][1:]+"}"))
    ReturnInfo = json.loads(Info[Index])
    return ("""• %s
• 잔여좌석 : %d석
• 사용 좌석 : %s석
• 총좌석 : %s석
• 개방상태 : %s"""%(ReturnInfo["NAME"],int(ReturnInfo["TOTAL_NUM"])-int(ReturnInfo["USED"]),ReturnInfo["USED"],ReturnInfo["TOTAL_NUM"],ReturnInfo["ROOM_STATUS"]))



def GetLibraryENG(Index):
    url = "https://eseat.sch.ac.kr/EZ5500/SEAT/RoomDisplay.aspx/WEB_PROC_EZ5500_SEAT_ROOM_POLLINGDATA"
    header = {'Content-Type': 'application/json; charset=euc-kr'}
    result = requests.post(url,headers=header, params=None)
    contents = result.content
    NeedJSON = contents.decode("euc-kr")
    results = json.loads(NeedJSON)
    Split = ((results["d"][5:]).split("}"))
    Info = []
    for line in range(0,6):
        Info.append((Split[line][1:]+"}"))
    ReturnInfo = json.loads(Info[Index])
    return ("""• %s
• Left Seat : %d
• Used Seat : %s
• Total Seat : %s
• Open Status : %s"""%(ReturnInfo["NAME"],int(ReturnInfo["TOTAL_NUM"])-int(ReturnInfo["USED"]),ReturnInfo["USED"],ReturnInfo["TOTAL_NUM"],ReturnInfo["ROOM_STATUS"]))
