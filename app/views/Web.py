# -*- coding:utf-8 -*-
import hashlib
from flask import current_app, render_template, request, redirect, url_for, Blueprint, abort
import flask_login
from ..models.dbORM import Carousel, Translation, Tag, Post, Footer, Firststage, Material
from app import db, login_manager
from sqlalchemy import or_
web = Blueprint('web', __name__)


def getTranslations(lang):
    translation = Translation.query.all()
    translations = {}
    for i in translation:
        if i.name:
            if lang == "en":
                translations[i.name] = i.en
            else:
                translations[i.name] = i.cn
    return translations


@web.route('/<lang>')
def index(lang):
    carousel = Carousel.query.filter_by(status="published").all()
    translations = getTranslations(lang)
    materials = db.session.query(Material).all()
    stages = Firststage.query.filter_by(status="published").all()
    posts = Post.query.filter_by(
        status="published").filter_by(tagoneid=1).all()
    footer = Footer.query.first()
    active = "home"
    return render_template("index.html", carousel=carousel, translation=translations, posts=posts, footer=footer, stages=stages, isHome=True, materials=materials)


@web.route('/<lang>/<route>')
def second(lang, route):
    stages = Firststage.query.filter_by(status="published").all()
    firststage = Firststage.query.filter_by(
        status="published").filter_by(link=route).first()
    posts = firststage.posts.filter_by(status="published").all()
    footer = Footer.query.first()
    translations = getTranslations(lang)
    return render_template(firststage.link+".html",  translation=translations, footer=footer, stages=stages, firststage=firststage, posts=posts, route=route, isHome=False)


@web.route('/<lang>/<route>/posts/<id>')
def post(lang, route, id):
    stages = Firststage.query.filter_by(status="published").all()
    firststage = Firststage.query.filter_by(
        status="published").filter_by(link=route).first()
    footer = Footer.query.first()
    translations = getTranslations(lang)
    post = Post.query.filter_by(
        status="published").filter_by(id=id).first()
    if not post:
        return abort(404)
    return render_template("post.html",  translation=translations, footer=footer, stages=stages, firststage=firststage, post=post, route=route, isHome=False)


@web.route('/<lang>/search')
def Search(lang):
    stages = Firststage.query.filter_by(status="published").all()
    # TODO public banner
    firststage = Firststage.query.filter_by(
        status="published").filter_by(link="about").first()
    footer = Footer.query.first()
    translations = getTranslations(lang)
    q = request.args.get('q')
    if not q:
        posts = Post.query.filter_by(
            status="published").all()
    else:
        posts = Post.query.filter_by(
            status="published").filter(or_(Post.content.like('%'+q+'%'), Post.title.like('%'+q+'%'))).all()
    if not post:
        return abort(404)
    return render_template("searchResults.html",  translation=translations, footer=footer, stages=stages, firststage=firststage, posts=posts,  isHome=False)


@web.route('/<lang>/posts/<id>')
def postDetail(lang, id):
    stages = Firststage.query.filter_by(status="published").all()
    # TODO public banner
    firststage = Firststage.query.filter_by(
        status="published").filter_by(link="about").first()
    footer = Footer.query.first()
    translations = getTranslations(lang)
    post = Post.query.filter_by(
        status="published").filter_by(id=id).first()
    if not post:
        return abort(404)
    return render_template("post.html",  translation=translations, footer=footer, stages=stages, firststage=firststage, post=post,  isHome=False)
