# -*- coding:utf-8 -*-
import os
import os.path as op
import string
import random
from werkzeug import secure_filename
from flask_qiniustorage import Qiniu
import shutil
from PIL import Image
import piexif

def routate(imgData):
    img = Image.open(imgData)
    exif_bytes=""
    if "exif" in img.info:
        exif_dict = piexif.load(img.info["exif"])

        if piexif.ImageIFD.Orientation in exif_dict["0th"]:
            orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
            exif_bytes = piexif.dump(exif_dict)

            if orientation == 2:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 3:
                img = img.rotate(180)
            elif orientation == 4:
                img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 5:
                img = img.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 6:
                img = img.rotate(-90, expand=True)
            elif orientation == 7:
                img = img.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 8:
                img = img.rotate(90, expand=True)

    return [img,exif_bytes]

def relativePath():
    return "upload/"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) + '/'


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_file(file, basePath, domain, storeModel):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        pic_dir = basePath + '/' + relativePath()
        path = pic_dir + filename
        if not op.exists(op.dirname(path)):
            os.makedirs(os.path.dirname(path))

        file.seek(0)
        file.save(path)
        qiniu_file_name = relativePath() + filename
        with open(path, 'rb') as fp:
            ret, info = storeModel.save(fp, qiniu_file_name)
            if 200 != info.status_code:
                raise Exception("upload to qiniu failed", info)

        shutil.rmtree(pic_dir)
        # return filename
        localUrl = 'http://' + domain + '/' + qiniu_file_name
        title = filename.rsplit('.', 1)[0]
        return {"title": title, "isImage": 1, "fileName": filename, "localUrl": localUrl, "result": 1}


def upload_file_by_pillow(file, filename, basePath, domain, storeModel):
    if file:
        filename = secure_filename(filename)
        pic_dir = basePath + '/' + relativePath()
        path = pic_dir + filename
        if not op.exists(op.dirname(path)):
            os.makedirs(os.path.dirname(path))

        file.save(path, 'JPEG')
        qiniu_file_name = relativePath() + filename
        with open(path, 'rb') as fp:
            ret, info = storeModel.save(fp, qiniu_file_name)
            if 200 != info.status_code:
                raise Exception("upload to qiniu failed", info)

        shutil.rmtree(pic_dir)
        # return filename
        localUrl = 'http://' + domain + '/' + qiniu_file_name
        title = filename.rsplit('.', 1)[0]
        return {"title": title, "isImage": 1, "fileName": filename, "localUrl": localUrl, "result": 1}
