import requests
url =  'http://api.openweathermap.org/data/2.5/weather?appid=41e49a44177d59caffa315f4fc69de5f&q='

def check(name):
    try:
        check_url = url+name
        r = requests.get(check_url).json()
        weather_main = r
        return weather_main
    except:
        return 'City not found, try another one.'
