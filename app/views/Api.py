# -*- coding:utf-8 -*-
import os
import sys
from flask import Blueprint, request, current_app, url_for, jsonify
from ..models.dbORM import *
from ..modules.Wechat import *
from datetime import datetime
from ..helpers.session3rd import *
from ..modules.Cache import *
from app import db
import json
api = Blueprint('api', __name__)


@api.route('/feedback', methods=['POST'])
def post():
    name = request.form['name']
    company_name = request.form['company_name']
    position = request.form['position']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    target = request.form['target']
    contact = request.form['contact']
    comment = request.form['comment']
    if not(name and (phone or email)):
        return jsonify({"status": "failed"})
    fb = Feedback(name=name, company_name=company_name, position=position,
                  address=address, phone=phone, email=email, target=target,
                  contact=contact, comment=comment)
    db.session.add(fb)
    db.session.commit()
    return jsonify({"status": "ok"})
