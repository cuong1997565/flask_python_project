from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(140), index=True, unique=True)
    phone = db.Column(db.Integer)
    email = db.Column(db.String(120), index=True, unique=True)
    address = db.Column(db.String(140), index=True)
    contract = db.relationship('Contract', backref='author', lazy='dynamic')
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def __repr__(self):
        return '<Employee %r>' % (self.name)


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), index=True)
    type = db.Column(db.Integer, index=True)
    status = db.Column(db.Integer, index=True)
    date_sign = db.Column(db.DateTime, index=True)
    date_effective = db.Column(db.DateTime, index=True)
    date_expiration = db.Column(db.DateTime, index=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

    def __init__(self, title, type, status, date_sign, date_effective, date_expiration, employee_id):
        self.title = title
        self.type = type
        self.status = status
        self.date_sign = date_sign
        self.date_effective = date_effective
        self.date_expiration = date_expiration
        self.employee_id = employee_id
    def __repr__(self):
        return '<Contract %r>' % (self.title)
