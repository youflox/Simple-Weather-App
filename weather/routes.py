from flask import render_template, request, redirect, url_for
from weather import app, db
from weather.models import check
from weather.database import Names, Reports

@app.route('/', methods=['GET', 'POST'])
def home():
    reports = []

    # getting data from API with existing names in db
    names = Names.query.order_by(Names.id.desc()).limit(5).all()
    for name in names:
        report = check(name.city)
        reports.append(report)

# -----------------------POST METHOD-----------------------------------
        if request.method == 'POST':
            global deg
            q = request.form.get('query')
            deg = request.form.get('deg')

           # adding query to database
            city = Names(city=q)
            db.session.add(city)
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('home.html',deg=deg, reports=reports)
