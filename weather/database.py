from weather import db

class Names(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String, nullable = False)
    report = db.relationship('Reports', backref = 'name' )

class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather = db.Column(db.String, nullable=False)
    name_id = db.Column(db.Integer, db.ForeignKey('names.id'))
