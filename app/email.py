from . import mail
from flask_mail import Message
from flask import render_template

def mail_message(subject, template, to, **kwags):
  sender = 'awadh.awadh@student.moringaschool.com'
  email = Message(subject, sender=sender, recipients=[to])
  email.body = render_template(template + ''.txt, **kwags)
  email.html = render_template(template + ''.html, **kwags)

  mail.send(email)