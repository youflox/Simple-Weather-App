from weather_app import db
from weather_app import app

import requests
url =  'http://api.openweathermap.org/data/2.5/weather?appid=41e49a44177d59caffa315f4fc69de5f&q='

def check(name):
    try:
        weather = []
        temp = []
        types = ['temp','feels_like', 'temp_min', 'temp_max']
        check_url = url+name
        r = requests.get(check_url).json()

        def cel(temp):
            return int(temp)-273.15

        def F(K):
            return ((float(K)-273.15)*1.8) + 32

        for type in types:
            temp.append((round(cel(r['main'][type]),2),'°C'))
            temp.append((round(F(r['main'][type]), 2), '°F'))



        wind = ['wind']
        weather.append(temp)
        w = r['wind']['speed']
        wind.append(w)
        wind.append(r['wind']['deg'])
        weather.append(wind)
        weather.append(r['weather'][0]['description'])

        sun = ['sun']
        sun.append(r['sys']['sunrise'])
        sun.append(r['sys']['sunset'])
        weather.append(sun)

        return weather
    except:
        return 'City not found, try another one.'

#-------------------------------   DATABASE ---------------------------------------------------------------------

class citynames(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    city = db.column(db.String, nullable = False)