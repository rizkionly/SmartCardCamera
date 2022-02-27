from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nama = db.Column(db.String(10000))
    Kode_RFID = db.Column(db.String(10000))
    Nama_Wajah = db.Column(db.String(10000))
    Waktu = db.Column(db.String(10000))