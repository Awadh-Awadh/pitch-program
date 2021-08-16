from flask import render_template
from . import main

@main.errorhandler(404)
def four0h(e):
    return render_template('404.html'),404

@main.errorhandler(500)
def fiveoh(e):
    return render_template('500.html'), 500