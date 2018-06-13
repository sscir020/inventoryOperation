from flask import Flask,app, render_template, session, redirect, url_for
from ..controllerlogin.forms import UserLoginForm
from .. import controllermaterial
from ..modules.MaterialModel import Materials

@app.route('/materials_show', methods=['GET', ''])
def index():
    # form = UserLoginForm()
    # if form.validate_on_submit():
    #     session['name'] = form.name.data
    #     return redirect(url_for('index'))
    # return render_template('index.html', form=form, name=session.get('name'))
    materials=Materials.query()
    return render_template('inventory.html',materials)

@app.route('/materials_update/<material_id>/<username>', methods=['', 'POST'])
def update():
    materials=Materials.query()
    return render_template('inventory.html',materials)