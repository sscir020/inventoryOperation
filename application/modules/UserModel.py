from start import *
from .OprModel import Oprs
class Users(db.Model):
    __tablename__ = 'users'
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name=db.Column(db.String(64), unique=True, index=True)
    user_password=db.Column(db.String(64), nullable=False)
    materials = db.relationship('Materials',
                              secondary=Oprs,
                              backref=db.backref('Users', lazy='dynamic'),
                              lazy='dynamic')