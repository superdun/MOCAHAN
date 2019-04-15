# -*- coding:utf-8 -*-
from datetime import datetime
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(80))
    img = db.Column(db.String(200))
    content = db.Column(db.String(60000))
    comment = db.Column(db.String(5000))
    status = db.Column(db.String(200), default="publish")

    def __repr__(self):
        return self.title


class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    cn = db.Column(db.String(60000))
    en = db.Column(db.String(60000))

    def __repr__(self):
        return self.name


class Carousel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(6000))
    media = db.Column(db.String(6000))
    link = db.Column(db.String(6000))
    linktitle = db.Column(db.String(6000))
    img = db.Column(db.String(6000))
    status = db.Column(db.String(200), default="publish")

    def __repr__(self):
        return self.title


class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(60000))
    media = db.Column(db.String(60000))

    def __repr__(self):
        return self.title


class Footer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(60000))

    def __repr__(self):
        return self.id


class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(80))
    img = db.Column(db.String(200))
    content = db.Column(db.String(60000))
    comment = db.Column(db.String(5000))
    status = db.Column(db.String(200), default="published")

    def __repr__(self):
        return self.title


class Firststage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    subtitle = db.Column(db.String(200))
    name = db.Column(db.String(200))
    subid = db.Column(db.Integer)
    img = db.Column(db.String(200))
    content = db.Column(db.Text)
    link = db.Column(db.String(200))
    status = db.Column(db.String(200))
    banner = db.Column(db.String(200))
    posts = db.relationship('Post', backref='Firststage', lazy='dynamic')

    def __repr__(self):
        return self.title


class Secondstage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    subtitle = db.Column(db.String(200))
    name = db.Column(db.String(200))
    subid = db.Column(db.Integer)
    img = db.Column(db.String(200))
    content = db.Column(db.Text)
    link = db.Column(db.String(200))
    status = db.Column(db.String(200))
    posts = db.relationship('Post', backref='Secondstage', lazy='dynamic')

    def __repr__(self):
        return self.title


class Thirdstage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    subtitle = db.Column(db.String(200))
    name = db.Column(db.String(200))
    subid = db.Column(db.Integer)
    img = db.Column(db.String(200))
    content = db.Column(db.Text)
    link = db.Column(db.String(200))
    status = db.Column(db.String(200))
    posts = db.relationship('Post', backref='Thirdstage', lazy='dynamic')

    def __repr__(self):
        return self.title


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(80))
    img = db.Column(db.String(200))
    content = db.Column(db.String(60000))
    tagoneid = db.Column(db.Integer, db.ForeignKey('firststage.id'))
    tagtwoid = db.Column(db.Integer, db.ForeignKey('secondstage.id'))
    tagthreeid = db.Column(db.Integer, db.ForeignKey('thirdstage.id'))
    status = db.Column(db.String(200), default="published")
    link = db.Column(db.String(200))
    subtitle = db.Column(db.String(200))

    def __repr__(self):
        return self.title


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    stage = db.Column(db.Integer)

    def __repr__(self):
        return self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __repr__(self):
        return self.name


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(8000))
    created_at = db.Column(db.DateTime, default=datetime.now())
    openid = db.Column(db.String(80), db.ForeignKey('customer.openid'))

    def __repr__(self):
        return self.id
