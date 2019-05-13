# -*- coding:utf-8 -*-
import os
import sys
from flask import Blueprint, request, current_app, url_for, jsonify
from ..models.dbORM import *
from ..modules.Wechat import *
from datetime import datetime
from ..helpers.session3rd import *
from ..modules.Cache import *
from app import db,manager
import json
import flask_restless
api = Blueprint('api', __name__)

def preprocessor(search_params=None, **kw):
    if search_params is None:
        return
    filt = dict(name='status', op='eq', val="published")
    # Check if there are any filters there already.
    if 'filters' not in search_params:
        search_params['filters'] = []
    # *Append* your filter to the list of filters.
    search_params['filters'].append(filt)

manager.create_api(Calender, preprocessors=dict(GET_MANY=[preprocessor]),url_prefix='/api')

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


@api.route('/calenders', methods=['GET'])
def CalendersAPI():
    calenders = Calender.query.filter_by(status="published").all()
    return jsonify(result=calenders)

