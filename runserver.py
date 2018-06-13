from application.modules.MaterialModel import *
from application.modules.OprModel import *

from application.modules.UserModel import *

if __name__ == '__main__':
    # if db is not None:
    #     db.drop_all()
    # db.create_all()
    # mt1 = Materials(name='wood',count='10000')
    # mt2 = Materials(name='stone',count='20000')
    # db.session.add_all([mt1,mt2])
    # db.session.commit()
    # us1 = Users(name='wang',password='1234')
    # us2 = Users(name='zhang',password='1234')
    # us3 = Users(name='chen',password='1234')
    # us4 = Users(name='zhou',password='1234')
    # db.session.add_all([us1,us2,us3,us4])
    # db.session.commit()
    # op1 = Oprs(user_id='1',material_id='1',diff=10)
    # op2 = Oprs(user_id='4',material_id='2',diff=-12)
    # db.session.add_all([op1,op2])
    # db.session.commit()
    # print(db)
    app.run(debug=True)

