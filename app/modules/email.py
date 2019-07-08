# -*- coding: utf-8 -*-
from app import mail
from flask import current_app
import thread
from flask_mail import Message


def SendSync(msg):
    recipient = current_app.config.get("MAIL_DEFAULT_RECIP")
    subject = current_app.config.get("MAIL_DEFAULT_SUBJECT")
    msgObj = Message(subject, recipients=[recipient, ])
    msgObj.body = msg
    mail.send(msgObj)
