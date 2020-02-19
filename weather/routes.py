from flask import render_template, request
from weather import app, db
from weather.models import check
from weather.database import Names

@app.route('/', methods=['GET', 'POST'])
def home():
    reports = []
    deg = 0



# -----------------------POST METHOD-----------------------------------
    if request.method == 'POST':

        q = request.form.get('query')
        deg = int(request.form.get('deg'))

        # adding query to database
        city = Names(city=q)
        db.session.add(city)
        db.session.commit()

        names = Names.query.order_by(Names.id.desc()).limit(3).all()
        for name in names:
            report = check(name.city)
            reports.append(report)
        text = 'Your Search results here'

        return render_template('home.html',text=text, deg=deg, reports=reports)
# ----------------------- END POST METHOD-----------------------------------
    # getting data from API with existing names in db
    names = Names.query.order_by(Names.id.desc()).limit(3).all()
    for name in names:
        report = check(name.city)
        reports.append(report)

    return render_template('home.html', deg=deg, reports=reports)
