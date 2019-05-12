#import korean
import pyowm

def weather_parshing(API_KEY):
    City_ID = 1839726
    owm = pyowm.OWM(API_KEY)
    obs = owm.weather_at_id(City_ID)
    w = obs.get_weather()
    temperature = w.get_temperature(unit='celsius')
    temperature_F = w.get_temperature(unit='fahrenheit')
    humidity = w.get_humidity()  #습도
    humidity = '현재 습도 : ' + str(humidity) + ' %' #습도 퍼센트
    cloud = w.get_clouds()
    cloud = '구름 퍼센트 : ' + str(cloud) + ' %' #구름 퍼센트
    high_temp ='Max Temperature : ' + str( temperature['temp_max'] ) + ' ℃ ('+str( temperature_F['temp_max']) +'℉)' #최고기온
    low_temp ='Min Temperature : ' + str( temperature['temp_min'] ) + ' ℃('+str( temperature_F['temp_min']) +'℉)'#최저기온
    now_temp = 'Now Temperature : ' + str( temperature['temp'] ) + ' ℃('+str( temperature_F['temp']) +'℉)' #현재 기온
    now_sky = w.get_status()
    now_sky = 'Current Weather : ' + now_sky
    air = air_status()
    result = '■ SCH Univ. Weather ■\n\n• '+now_sky + '\n• ' + now_temp  + '\n• ' + high_temp + '\n• ' + low_temp
    result = result + air
    return result

def weather():
    try :
        KEY1 = "" #openWeatherAPI 의 키값
        return weather_parshing(KEY1)

    except:
        KEY2 = ""#openWeatherAPI 의 키
        return weather_parshing(KEY2)

def air_status():
    import urllib.request
    from bs4 import BeautifulSoup
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey='
    KEY = "" #openapi 의 대기오염도 API 의 키값.
    url += KEY +"&ver=1.3"
    page = urllib.request.urlopen(url)
    text = page.read().decode('utf8')
    soup = BeautifulSoup(text, 'html.parser')
    error_checker = text.find('도고면')
    if error_checker != -1:
        items = soup.find_all('item')
        items = list(items)
        index = 0
        for s in items:
            s = str(s)
            if s.find('도고면') != -1:
                index = index
                break
            else:
                index = index + 1

        if len(items) != index:
            need_parsing = str(items[index])
            start_so2value = need_parsing.find('<so2value>')
            end_so2value = need_parsing.find('</so2value>')
            so2value = need_parsing[start_so2value + len('<so2value>') : end_so2value]
            start_covalue = need_parsing.find('<covalue>')
            end_covalue = need_parsing.find('</covalue>')
            covalue = need_parsing[start_covalue + len('<covalue>') : end_covalue]
            start_o3value = need_parsing.find('<o3value>')
            end_o3value = need_parsing.find('</o3value>')
            o3value = need_parsing[start_o3value + len('<o3value>') : end_o3value]
            start_no2value = need_parsing.find('<no2value>')
            end_no2value = need_parsing.find('</no2value>')
            no2value = need_parsing[start_no2value + len('<no2value>') : end_no2value]
            start_pm10value = need_parsing.find('<pm10value>')
            end_pm10value = need_parsing.find('</pm10value>')
            pm10value = need_parsing[start_pm10value + len('<pm10value>') : end_pm10value]
            start_pm25value = need_parsing.find('<pm25value>')
            end_pm25value = need_parsing.find('</pm25value>')
            pm25value = need_parsing[start_pm25value + len('<pm25value>') : end_pm25value]
            #print(so2value) #아황산가스
            #print(covalue) #일산화탄소 농도
            #print(o3value) #오존농도
            #print(no2value) #이산화질소
            #print(pm10value) #미세먼지
            #print(pm25value) #초 미세먼지
            so2valu = float(so2value)
            covalu = float(covalue)
            o3valu = float(o3value)
            no2valu = float(no2value)
            pm10valu = float(pm10value)
            pm25valu = float(pm25value)
            so2 = ''
            co = ''
            o3 = ''
            pm10 = ''
            pm25 = ''
            if so2valu > 0.15 :
                so2 = 'Unhealthy'
            elif so2valu > 0.05:
                so2 = '나쁨'
            elif so2valu > 0.02:
                so2 = 'Moderate'
            else :
                so2 = 'Good'

            if covalu > 15 :
                co = 'Very Bad'
            elif covalu > 9:
                co = 'Bad'
            elif covalu > 2:
                co = 'Moderate'
            else :
                co = 'Good'

            if o3valu > 0.15 :
                o3 = 'Very Bad'
            elif o3valu > 0.09:
                o3 = 'Bad'
            elif o3valu > 0.03:
                o3 = 'Moderate'
            else :
                o3 = 'Good'

            if no2valu > 0.2 :
                no2 = 'Very Bad'
            elif no2valu > 0.06:
                no2 = 'Bad'
            elif no2valu > 0.03:
                no2 = 'Moderate'
            else :
                no2 = 'Good'

            if pm10valu > 150 :
                pm10 = 'Very Bad'
            elif pm10valu > 80:
                pm10 = 'Bad'
            elif pm10valu > 30:
                pm10 = 'Moderate'
            else :
                pm10 = 'Good'

            if pm25valu > 75 :
                pm25 = 'Very Bad'
            elif pm25valu > 35:
                pm25 = 'Bad'
            elif pm25valu > 15:
                pm25 = 'Moderate'
            else :
                pm25 = 'Good'

            return ('\n• O₃: ' + o3 +'\n• Fine Dust : ' + pm10 + '\n• Ultra Fine Dust : ' + pm25 + '\n• SO₂: ' + so2 +'\n• CO : ' + co +  '\n• NO₂: ' + no2 )
print(weather())
