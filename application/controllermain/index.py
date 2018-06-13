from flask import render_template,app
from application import controllermain


@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')