# -*- coding: utf-8 -*-
from flask import request
import os
import os.path as op
import time
from flask_admin import Admin
import flask_login
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.view import func
from jinja2 import Markup
from flask import current_app
from ..models.dbORM import *
from ..helpers import thumb
from flask_qiniustorage import Qiniu
from wtforms import SelectField, PasswordField
from flask_admin import BaseView, expose
import hashlib
from app import db
from flask_ckeditor import CKEditor, CKEditorField
from ..helpers.thumb import routate


def getQiniuDomain():
    return current_app.config.get('QINIU_BUCKET_DOMAIN', '')


def getUploadUrl():
    return current_app.config.get('UPLOAD_URL')


def date_format(value):
    return time.strftime(u'%Y/%m/%d %H:%M:%S', time.localtime(float(value)))


def img_url_format(value):
    return Markup("<img src='%s'>" % (url_for('static', filename=value)))


def dashboard():
    admin = Admin(current_app, name=u'锢维后台管理')
    #admin.add_view(UserView(User, db.session, name=u"管理员管理"))
    #admin.add_view(TagView(Tag, db.session, name=u"标签"))
    admin.add_view(PostView(Post, db.session, name=u"文章"))
    admin.add_view(FirststageView(Firststage, db.session, name=u"一级菜单"))
    admin.add_view(CarouselView(Carousel, db.session, name=u"轮播图"))
    admin.add_view(FooterView(Footer, db.session, name=u"页脚"))
    admin.add_view(FeedbackView(Feedback, db.session, name=u"联系我们"))
    admin.add_view(CalenderView(Calender, db.session, name=u"实验日历"))
    admin.add_view(TranslationView(Translation, db.session, name=u"多语言"))
    admin.add_view(MaterialView(Material, db.session, name=u"焊接材料"))


class UploadWidget(form.ImageUploadInput):
    def get_url(self, field):
        if field.thumbnail_size:
            filename = field.thumbnail_fn(field.data)
        else:
            filename = field.data

        if field.url_relative_path:
            # filename = "http://" + field.url_relative_path + filename
            filename = field.url_relative_path + filename
        return filename


class ImageUpload(form.ImageUploadField):
    widget = UploadWidget()

    def _save_file(self, data, filename):
        path = self._get_path(filename)
        if not op.exists(op.dirname(path)):
            os.makedirs(os.path.dirname(path), self.permission | 0o111)
        newF, exif = routate(data)
        newF.seek(0)
        newF.save(path)
        return filename
        # qiniu_store = Qiniu(current_app)
        # with open(path, 'rb') as fp:
        #     ret, info = qiniu_store.save(fp, filename)
        #     if 200 != info.status_code:
        #         raise Exception("upload to qiniu failed", ret)
        #     # shutil.rmtree(os.path.dirname(path))
        #     return filename


class AdminModel(ModelView):
    column_default_sort = ('id', True)

    def is_accessible(self):
        if flask_login.current_user.is_authenticated:
            return True
        else:
            return False


# super admin models


class UserView(AdminModel):

    def on_model_change(self, form, model, is_created):
        password = model.password
        md5 = hashlib.md5()
        md5.update(password)
        model.password = md5.hexdigest()


class TagView(AdminModel):
    pass


class CustomerView(AdminModel):
    form_extra_fields = {
        'img': ImageUpload(u'头像', base_path=getUploadUrl(), relative_path=thumb.relativePath(),
                           url_relative_path="/static/"),

    }


class AttitudeView(AdminModel):
    pass


class PostView(AdminModel):
    column_exclude_list = (
        'content', 'img', 'Secondstage', 'Thirdstage', 'cover')
    form_excluded_columns = ('Secondstage', 'Thirdstage')
    form_columns = ('created_at', 'title', 'description', 'subtitle',
                    'Firststage', 'status', 'cover', 'content')
    column_labels = dict(created_at=u'创建时间', title=u'标题', description=u'描述', content=u'内容', subtitle=u'副标题',
                         Firststage=u'一级分类', status=u'状态', cover=u'封面', img=u"图片")
    form_overrides = dict(content=CKEditorField)
    create_template = 'edit.html'
    edit_template = 'edit.html'
    @property
    def form_extra_fields(self):
        return {
            'img': ImageUpload(u'图片', base_path=getUploadUrl(), relative_path=thumb.relativePath(),
                               url_relative_path="/static/"),
            'cover': ImageUpload(u'封面', base_path=getUploadUrl(), relative_path=thumb.relativePath(),
                                 url_relative_path="/static/"),
            'status': SelectField(u'状态', choices=(("deleted", u"已删除"), ("published", u"发布"),))
        }


class FirststageView(AdminModel):
    column_exclude_list = ('title', 'subtitle', 'subid',
                           'img', 'content', 'banner')
    form_excluded_columns = ('Title', 'Subtitle', 'subid', 'img', 'content')
    column_labels = dict(created_at=u'创建时间', title=u'标题', description=u'描述', name=u'名称', subtitle=u'副标题',
                         link=u'链接', status=u'状态', humanname=u"中文名称", Posts=u"相关文章")

    @property
    def form_extra_fields(self):
        return {
            'banner': ImageUpload(u'图片', base_path=getUploadUrl(), relative_path=thumb.relativePath(),
                                  url_relative_path="/static/"),
            'status': SelectField(u'状态', choices=(("deleted", u"已删除"), ("published", u"发布"),))
        }


class CarouselView(AdminModel):
    column_exclude_list = ('media', 'img')
    form_excluded_columns = ('media',)

    column_labels = dict(created_at=u'创建时间', title=u'标题', description=u'描述', name=u'名称', subtitle=u'副标题',
                         link=u'链接', status=u'状态', humanname=u"中文名称", Posts=u"相关文章", linktitle=u'链接标题', content=u'内容')

    @property
    def form_extra_fields(self):
        return {
            'img': ImageUpload(u'图片', base_path=getUploadUrl(), relative_path=thumb.relativePath(),
                               url_relative_path="/static/"),
            'status': SelectField(u'状态', choices=(("deleted", u"已删除"), ("published", u"发布"),))
        }


class FooterView(AdminModel):
    # column_exclude_list = ('title', 'subtitle', 'subid', 'img', 'content')
    # form_excluded_columns = ('Title', 'Subtitle', 'Subid', 'Img', 'Content')
    column_editable_list = ('content',)
    column_labels = dict(content=u'内容')

    @property
    def form_extra_fields(self):
        return {
            'img': ImageUpload(u'图片', base_path=getUploadUrl(), relative_path=thumb.relativePath(),
                               url_relative_path="/static/"),
            'status': SelectField(u'状态', choices=(("deleted", u"已删除"), ("published", u"发布"),))
        }


class FeedbackView(AdminModel):
    # column_exclude_list = ('title', 'subtitle', 'subid', 'img', 'content')
    # form_excluded_columns = ('Title', 'Subtitle', 'Subid', 'Img', 'Content')
    column_labels = dict(created_at=u'创建时间', name=u'名称', company_name=u"公司名", position=u"位置",
                         address=u"地址", phone=u"电话", target=u"意向", contact=u"联系方式", comment=u"其他")
    pass


class CalenderView(AdminModel):
    column_exclude_list = ('startstr', 'endstr', "color")
    form_excluded_columns = ('startstr', 'endstr', "color")
    column_labels = dict(content=u'内容', title=u'标题',
                         start=u'起始时间', end=u'结束时间', status=u'状态')

    @property
    def form_extra_fields(self):
        return {
            'status': SelectField(u'状态', choices=(("deleted", u"已删除"), ("published", u"发布"),))
        }


class TranslationView(AdminModel):
    column_editable_list = ('name', 'cn', 'en')
    column_labels = dict(name=u'内容', cn=u'中文',
                         en=u'英文')
    # column_exclude_list = ('title', 'subtitle', 'subid', 'img', 'content')
    # form_excluded_columns = ('Title', 'Subtitle', 'Subid', 'Img', 'Content')


class MaterialView(AdminModel):
    column_exclude_list = ('materials',)
    form_excluded_columns = ('materials',)
    column_labels = dict(name=u'材料名称', material=u'可焊接材料')
