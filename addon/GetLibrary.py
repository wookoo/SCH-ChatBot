import requests
import json


def GetLibrary(Index):
    url = "https://eseat.sch.ac.kr/EZ5500/SEAT/RoomDisplay.aspx/WEB_PROC_EZ5500_SEAT_ROOM_POLLINGDATA" #요청을 보낼 주소
    header = {'Content-Type': 'application/json; charset=euc-kr'} #서버에 보낼 헤더들
    result = requests.post(url,headers=header, params=None) #앞서 설정한 헤더로 리퀘스트를 날린다
    contents = result.content #리스폰스 값을 contents 에 저장
    NeedJSON = contents.decode("euc-kr") #바이너리 형태이므로 euc-kr 로 디코딩
    results = json.loads(NeedJSON) #디코딩 된 것을 Json 으로 형 변환
    Split = ((results["d"][5:]).split("}")) #값을 적절하게 split 을 한다.
    Info = []
    for line in range(0,6):
        Info.append((Split[line][1:]+"}"))
    ReturnInfo = json.loads(Info[Index]) #index 에 따라 열람실 1 2 3 등을 파싱한다.
    return ("""• %s
• 잔여좌석 : %d석
• 사용 좌석 : %s석
• 총좌석 : %s석
• 개방상태 : %s"""%(ReturnInfo["NAME"],int(ReturnInfo["TOTAL_NUM"])-int(ReturnInfo["USED"]),ReturnInfo["USED"],ReturnInfo["TOTAL_NUM"],ReturnInfo["ROOM_STATUS"])) #스트링을 알맞게 반환



def GetLibraryENG(Index): #영어로 도서관 정보 반환
    url = "https://eseat.sch.ac.kr/EZ5500/SEAT/RoomDisplay.aspx/WEB_PROC_EZ5500_SEAT_ROOM_POLLINGDATA"#요청을 보낼 주소
    header = {'Content-Type': 'application/json; charset=euc-kr'} #서버에 보낼 헤더들
    result = requests.post(url,headers=header, params=None)#앞서 설정한 헤더로 리퀘스트를 날린다
    contents = result.content #리스폰스 값을 contents 에 저장
    NeedJSON = contents.decode("euc-kr") #바이너리 형태이므로 euc-kr 로 디코딩
    results = json.loads(NeedJSON) #디코딩 된 것을 Json 으로 형 변환
    Split = ((results["d"][5:]).split("}")) #값을 적절하게 split 을 한다.
    Info = []
    for line in range(0,6):
        Info.append((Split[line][1:]+"}"))
    ReturnInfo = json.loads(Info[Index]) #index 에 따라 열람실 1 2 3 등을 파싱한다.
    return ("""• %s
• Left Seat : %d
• Used Seat : %s
• Total Seat : %s
• Open Status : %s"""%(ReturnInfo["NAME"],int(ReturnInfo["TOTAL_NUM"])-int(ReturnInfo["USED"]),ReturnInfo["USED"],ReturnInfo["TOTAL_NUM"],ReturnInfo["ROOM_STATUS"]))#스트링을 알맞게 반환
