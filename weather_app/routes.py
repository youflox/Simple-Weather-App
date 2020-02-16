from flask import render_template, request
from weather_app import app
from weather_app.models import check

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city_name')
        report = check(city)
        return render_template('home.html', report = report)

    return render_template('home.html')