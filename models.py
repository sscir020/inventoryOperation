from start import *

class Materials(db.Model):
    __tablename__ = 'materials'
    material_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    material_name=db.Column(db.String(64), unique=True, index=True)
    count=db.Column(db.Integer,nullable=False)

class Users(db.Model):
    __tablename__ = 'users'
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name=db.Column(db.String(64), unique=True, index=True)

class Oprs(db.Model):
    __tablename__ = 'oprs'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),primary_key=True)
    diff=db.Column(db.Integer,nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.material_id'))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    mt1 = Materials(name='wood',count='10000')
    mt2 = Materials(name='stone',count='20000')
    db.session.add_all([mt1,mt2])
    db.session.commit()
    us1 = Users(name='wang')
    us2 = Users(name='zhang')
    us3 = Users(name='chen')
    us4 = Users(name='zhou')
    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()
    op1 = Oprs(user_id='1',material_id='1',diff=10)
    op2 = Oprs(user_id='4',material_id='2',diff=-12)
    db.session.add_all([op1,op2])
    db.session.commit()
    print(db)
    app.run(debug=True)