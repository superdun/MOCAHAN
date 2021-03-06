# coding=utf-8
from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import flask_login
import flask_restless
import datetime
from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success
from flask_mail import Mail

db = SQLAlchemy()

admin = Admin()
login_manager = flask_login.LoginManager()
manager = flask_restless.APIManager(flask_sqlalchemy_db=db)
mail = Mail()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('localConfig.py')
    mail.init_app(app)
    db.init_app(app)
    db.app = app
    ckeditor = CKEditor(app)
    login_manager.init_app(app)

    from models.dbORM import User as Us

    @app.route('/robots.txt')
    @app.route('/sitemap.xml')
    @app.route('/sitemap.html')
    @app.route('/baidu_verify_dmic8XkyMB.html')
    @app.route('/BingSiteAuth.xml')
    def static_from_root():
        return send_from_directory(app.static_folder+"/file", request.path[1:])

    def getusers():
        users = {}
        raw_users = Us.query.all()

        for user in raw_users:
            users[user.name] = {'password': user.password, 'username': user.name,
                                'id': user.id}
        return users

    class User(flask_login.UserMixin):
        pass

    @login_manager.unauthorized_handler
    def unauthorized_handler():

        return render_template("login.html")

    @login_manager.user_loader
    def user_loader(username):
        users = getusers()
        if username not in users:
            return

        user = User()
        user.name = username
        user.id = users[username]['id']
        return user

    @login_manager.request_loader
    def request_loader(request):
        users = getusers()

        username = request.form.get('username')
        password = request.form.get('password')
        if password == "":
            return
        if username not in users:
            return

        user = User()
        user.name = username
        user.id = users[username]['id']
        db.session.commit()
        # DO NOT ever store passwords in plaintext and always compare password
        # hashes using constant-time comparison!

        user.is_authenticated = request.form[
            'password'] == users[username]['password']

        return user

    # 注册蓝本
    from views import Login, Api, Web
    app.register_blueprint(Api.api, url_prefix='/api')
    app.register_blueprint(Login.login_bp, url_prefix='')
    app.register_blueprint(Web.web, url_prefix='')
    manager.init_app(app)

    # 附加路由和自定义的错误页面
    with app.app_context():
        from modules.Admin import dashboard

        dashboard()

    return app
