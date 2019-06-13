# -*- coding:utf-8 -*-
from datetime import datetime
from app import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
    humanname = db.Column(db.String(200))

    def __repr__(self):
        if self.humanname:
            return str(self.id)+"--"+self.humanname.encode('utf8').decode('utf8')
        else:
            return str(self.id)


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
        return str(self.id)


class Thirdstage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    subtitle = db.Column(db.String(200))
    name = db.Column(db.String(200))
    subid = db.Column(db.Integer)
    img = db.Column(db.String(200))
    content = db.Column(db.Text)
    status = db.Column(db.String(200))
    posts = db.relationship('Post', backref='Thirdstage', lazy='dynamic')

    def __repr__(self):
        return str(self.id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(80))
    description = db.Column(db.String(2000))
    cover = db.Column(db.String(200))
    img = db.Column(db.String(200))
    content = db.Column(db.String(60000))
    tagoneid = db.Column(db.Integer, db.ForeignKey('firststage.id'))
    tagtwoid = db.Column(db.Integer, db.ForeignKey('secondstage.id'))
    tagthreeid = db.Column(db.Integer, db.ForeignKey('thirdstage.id'))
    status = db.Column(db.String(200), default="published")
    link = db.Column(db.String(200))
    subtitle = db.Column(db.String(200))

    def __repr__(self):
        if(self.title):
            return self.title
        return self.id


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


class Calender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(80))
    color = db.Column(db.String(80))
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    startstr = db.Column(db.String(80))
    endstr = db.Column(db.String(80))
    status = db.Column(db.String(200), default="published")

    def __repr__(self):
        return self.title


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    name = db.Column(db.String(80))
    company_name = db.Column(db.String(80))
    position = db.Column(db.String(80))
    address = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    email = db.Column(db.String(80))
    target = db.Column(db.String(80))
    contact = db.Column(db.String(80))
    comment = db.Column(db.String(800))

    def __repr__(self):
        return self.id

class Pair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paironeid = db.Column(db.Integer, db.ForeignKey('materialone.id'))
    pairtwoid = db.Column(db.Integer, db.ForeignKey('materialone.id'))

    def __repr__(self):
        return self.paironeid

Pairtable = db.Table(
    'pair', Base.metadata,
    db.Column('paironeid', db.Integer, db.ForeignKey('material.id')),
    db.Column('pairtwoid', db.Integer, db.ForeignKey('material.id'))
    )

class Material(Base):
    __tablename__ = "material"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    materials = db.relationship(
        'Material', secondary=Pairtable,
        primaryjoin=Pairtable.c.paironeid == id,
        secondaryjoin=Pairtable.c.pairtwoid == id,
        backref="material")

    def __repr__(self):
        return self.name



