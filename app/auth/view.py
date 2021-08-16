import re
from flask import render_template, redirect, url_for
from .form import Register,LoginForm
from . import auth
from ..models import User
from .. import db
from flask_login import login_required,login_user,logout_user, current_user

@auth.route('/register', methods = ['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit:
        user = User(username= form.username.data,email = form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form = form)


@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html',form = form)
