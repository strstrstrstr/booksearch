from pybo import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    age = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(100))
    region = db.Column(db.String(100))
    subject = db.Column(db.String(100))

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref=db.backref('user_set'))
    bookname = db.Column(db.String)
    bookrate = db.Column(db.String)
    class_nm = db.Column(db.String)
    isbn13 = db.Column(db.String)
