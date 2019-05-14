import urllib.request #웹에서 크롤링을 하기 위한 request 라이브러리를 가져옴
import urllib.parse

def result_book(book_name):
    book_name = str(book_name) #매개변수로 받아온 book_name 을 str 형으로 형변환
    book_name = urllib.parse.quote_plus(book_name) #책의 이름을 인코딩 한다.
    target = urllib.request.urlopen('https://library.sch.ac.kr/search/caz/result?st=KWRD&si=TOTAL&q='+book_name+'&folder_id=null') #url 에 책이름 등을 포함한 get request 를 날린다.
    page = target.read().decode('utf8') #받아온 결과값을 읽은후 디코딩 한다.
    result = '총 <strong>' #파싱을 위한 result 2 3 생성
    result2 = '</strong>건 중 <strong>'
    result3 = '</strong>건 출력'
    where = page.find(result)
    where2 = page.find(result2)
    where3 = page.find(result3)
    firt_book = page[where+len(result):where2] #스트링을 슬라이싱 한다
    last_book = page[where2+len(result2):where3] #스트링을 슬라이싱 한다
    return '총 ' +firt_book+ '건 중' + last_book +'건의 검색 결과가 존재합니다.\n• 자세한 사항은 아래 url 을 확인해주세요.' #슬라이싱 결과를 반환한다.
