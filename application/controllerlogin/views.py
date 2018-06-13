from flask import render_template, session, redirect, url_for,flash,request,app
from flask_login import login_user, logout_user, login_required
from ..modules.UserModel import Users
from .. import controllerlogin
from .forms import UserLoginForm


@app.route('/user/<username>')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        user = Users.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                return redirect(url_for('controllermain.index'))
        flash('Invalid username or password.')
    return render_template('templates/login.html', username=form.username.data,form=form)

@controllerlogin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))