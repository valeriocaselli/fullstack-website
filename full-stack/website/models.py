from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    reviews = db.relationship('Review', backref='author', lazy=True)

    def __init__(self, first_name, last_name, email, password, confirmed):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirmed = confirmed

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, value, description, user_id):
        self.value = value
        self.description = description
        self.user_id = user_id

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    tax_id_code = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False) # Description for each staff's element which is showed in the homepage

