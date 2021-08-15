from . import main
from flask import render_template

@main.route('/')
def inder():
  return render_template('index.html')
