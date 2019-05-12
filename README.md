# SCH CHAT BOT

## 소개

Python 의 Django 프레임 워크를 사용하여 제작한 카카오톡 챗봇입니다.

2018년 12월 이후 생성되는 카카오톡 챗봇은, 카카오톡 정책상 더이상 이 프로그램으로 운영 하실 수 없습니다.

친구추가는 [여기](https://pf.kakao.com/_lxmrmC) 에서 가능합니다.

[해당](https://github.com/plusfriend/auto_reply) 문서를 통해 구현하였고, 보다 상세하게 구현 방법을 확인 하실 수 있습니다.

사용된 라이브러리는 cmd 혹은 터미널에서 다음과 같은 명령어를 통해 설치 하실수 있습니다.
~~~
pip install 라이브러리명
~~~


## 개발 환경 및 기술 정보

### 개발 운영체제

- Windows 10

### 언어

- Python (3.x 이상)

### 프레임 워크

- Django (2.0 이상)

### 사용 라이브러리
- pywon
- BeautifulSoup4
- urllib3
- requests

### 서버
- Ubuntu 를 지원하는 모든 PC
- Ubuntu OR Windows

### 사용 API

- [버스위치정보조회서비스](https://www.data.go.kr/dataset/15000515/openapi.do)
- [(신)동네예보정보조회서비스](https://www.data.go.kr/dataset/15000099/openapi.do)
- [OpenWeatherMap](https://openweathermap.org/api)

### 파일 구조

각 파일에서 주석 업데이트 중입니다.

~~~
SCH_CHAT_BOT/
  ├─ addon/
  │  ├─ asanbus.py (버스 정보)
  │  ├─ find_book.py (도서 검색 정보)
  │  ├─ GetDB.py (챗봇 이용 횟수 업데이트)
  │  ├─ GetLibrary.py (열람실 좌석정보)
  │  ├─ train.py (지하철및 셔틀버스 정보)
  │  ├─ weather_edit.py (날씨 정보)
  │  └─ weather_edit_eng.py (영어 날씨 정보)
  │
  ├─ DATABASE/
  │  ├─ meals.db (학식 정보 저장)
  │  └─ kakaotalkLog.db (챗봇 이용 횟수 정보 저장)
  │
  └─ module/
     ├─ buttons.py (반환되는 버튼)
     ├─ buttons_eng.py (반환되는 영어 버튼)
     ├─ message.py (반환되는 메세지 ex: 와이파이 정보 등)
     ├─ message_eng.py (반환되는 영어 메세지)
     └─ process.py (Return 형식 분류)

~~~



## 사전작업

외부 API 키가 여러개 있습니다. 그렇기 때문에 사용하시기 전, `API 키`를 발급 받으신 후 입력해주셔야 합니다.

- addon/weather_edit.py
  - [(신)동네예보정보조회서비스](https://www.data.go.kr/dataset/15000099/openapi.do) 에서 발급받으신 KEY 값을 수정해줍니다.
  - [OpenWeatherMap](https://openweathermap.org/api)에서 발급받으신 KEY 값을 수정해줍니다.
- addon/weather_edit_eng.py
  - [(신)동네예보정보조회서비스](https://www.data.go.kr/dataset/15000099/openapi.do) 에서 발급받으신 KEY 값을 수정해줍니다.
  - [OpenWeatherMap](https://openweathermap.org/api)에서 발급받으신 KEY 값을 수정해줍니다.
- addon/asanbus.py
  - [버스위치정보조회서비스](https://www.data.go.kr/dataset/15000515/openapi.do) 에서 발급 받으신 KEY 값을 수정해줍니다.

### 실행방법

cmd 또는 터미널에서 다음과 같이 입력후 실행하시면 됩니다.

~~~
python manage.py runserver 0.0.0.0:포트번호
~~~


## 제공기능

### 학식

- 학교에 존재하는 `모든` 학생식당의 `당일` 학식 확인 가능
- 학교에 존재하는 `모든` 학생식당의 `유무` 확인 가능
- `일부` 학식의 금액 확인 가능
- 학교에 존재하는 `모든` 학생식당의 이용 시간 확인 가능
  - `일부` 학식의 제공 반찬 및 특징 표기

### 도서관

- 도서관에 존재하는 도서의 검색 가능
  - n개의 도서가 있음을 알려주며, 확인할 수 있는 링크 제공
- 도서관에 열람실 자리 `여석` 확인 가능
  - n번째 자리가 비었는지 확인 `불가`
- 도서관의 기타정보 표기
  - 열람 가능시간, 문헌팀 연락처 등

### 교통

- 학교 주변에 존재하는 `모든` 정류소의 버스 도착시간 확인 가능
- 학교 -> 신창역으로 가는 셔틀버스의 `대략적인` 출발시간 확인 가능
- 신창역 지하철의 `대략적인` 출발시간 확인 가능
- 신창 주변 `일부` 콜 택시회사의 연락처 확인 가능
- 신창 시외버스 터미널의 시간표 확인 가능

### 날씨

- 신창면의 날씨 확인 가능
  - 현재 날씨
  - 현재 기온
  - 최고 기온
  - 최저 기온
  - 오존 수치
  - 미세먼지 수치
  - 초미세먼지 수치
  - 아황산가스 수치
  - 일산화탄소 수치
  - 이산화질소 수치

### WI-FI

- 교내에서 제공하는 와이파이 연결 방법 등 확인 가능

### 순천향 건물

- 학교 지도 표기
- `모든` 학교 건물 번호 확인 가능
- `일부` 교내 편의 시설 확인 가능

### 보건실

- 보건실 위치확인 가능
- 이용시간 확인 가능
- 체성분 측정시간 확인 가능


## 기타

카카오톡 측에서 더이상 지원하지 않게될 API 이므로, 더이상의 업데이트는 없습니다.
