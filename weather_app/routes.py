from flask import render_template, request
from weather_app import app
from weather_app.models import check

@app.route('/', methods = ['GET','POST'])
def home():
    cities = []
    if request.method == 'POST':
        cities.append(request.form.get('city_name'))
        type1 = int(request.form.get("temp_select"))

        if cities:
            for city in cities:
                report= check(city)
                print(cities)
                return render_template('home.html', report = report, type1 = type1)
        else:
            text = 'Enter a city name'
            return  render_template('home.html', text = text)

    return render_template('home.html')