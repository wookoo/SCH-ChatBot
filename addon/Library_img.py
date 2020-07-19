import requests
import json
from PIL import Image
from PIL import ImageColor
from PIL import ImageFont,ImageDraw

SQUARE_SIZE = 40

def GetLibrary(Index):
    url = "https://eseat.sch.ac.kr/EZ5500/SEAT/RoomDisplay.aspx/WEB_PROC_EZ5500_SEAT_ROOM_POLLINGDATA" #요청을 보낼 주소
    header = {'Content-Type': 'application/json; charset=euc-kr'} #서버에 보낼 헤더들
    result = requests.post(url,headers=header, params=None) #앞서 설정한 헤더로 리퀘스트를 날린다
    contents = result.content #리스폰스 값을 contents 에 저장

    NeedJSON = contents.decode("euc-kr") #바이너리 형태이므로 euc-kr 로 디코딩
    NeedJSON  = json.loads(NeedJSON)
    NeedJSON = json.loads(NeedJSON['d'])
    first = []
    for i in NeedJSON["1"]:
        if (i["ROOM_NO"] == 1):
            first.append(i)
    first = sorted(first,key = lambda x: x["X_POS"])
    X_MAX = max([i["X_POS"] for i in first])
    Y_MAX = max([i["Y_POS"] for i in first])
    img = Image.new("RGB",(X_MAX*SQUARE_SIZE,Y_MAX*SQUARE_SIZE),(255,255,255))
    im = img.load()

    fnt = ImageFont.truetype("arial.ttf",15)

    img.save("test.jpg")
    d = ImageDraw.Draw(img)
    for i in first:
        #print(i)
        NUMBER = i["NUMBER"]
        X_POS = i["X_POS"]-1
        Y_POS = i["Y_POS"]-1
        RGB = i["SEAT_COLOR"]
        im3 = Image.new("RGB",(SQUARE_SIZE,SQUARE_SIZE),ImageColor.getrgb(RGB))
        pos = (X_POS*SQUARE_SIZE,Y_POS*SQUARE_SIZE)
        img.paste(im3,pos)
        d.text((X_POS*SQUARE_SIZE+5,Y_POS*SQUARE_SIZE+10),str(NUMBER),fill=(255,255,255),font=fnt)
        img.save("test.jpg")

    return
    results = json.loads(NeedJSON) #디코딩 된 것을 Json 으로 형 변환
    Split = ((results["d"][5:]).split("}")) #값을 적절하게 split 을 한다.
    Info = []
    for line in range(0,6):
        Info.append((Split[line][1:]+"}"))
    ReturnInfo = json.loads(Info[Index]) #index 에 따라 열람실 1 2 3 등을 파싱한다.
    return (ReturnInfo)
    return ("""• %s
• 잔여좌석 : %d석
• 사용 좌석 : %s석
• 총좌석 : %s석
• 개방상태 : %s"""%(ReturnInfo["NAME"],int(ReturnInfo["TOTAL_NUM"])-int(ReturnInfo["USED"]),ReturnInfo["USED"],ReturnInfo["TOTAL_NUM"],ReturnInfo["ROOM_STATUS"]))

print(GetLibrary(0))
