from flask import render_template, redirect, url_for
from .form import Register
from . import auth
from ..models import User
from .. import db

@auth.route('/register')
def register():
    form = Register()
    if form.validate_on_submit:
        user = User(username= form.username.data,
                    email = form.email.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    render_template('register.html', form = form)