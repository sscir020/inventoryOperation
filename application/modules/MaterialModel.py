from start import *

class Materials(db.Model):
    __tablename__ = 'materials'
    material_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    material_name = db.Column(db.String(64), unique=True, index=True)
    count = db.Column(db.Integer,nullable=False)