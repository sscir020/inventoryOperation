from start import *

class Oprs(db.Model):
    __tablename__ = 'oprs'
    opr_id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    diff=db.Column(db.Integer,nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.material_id'))