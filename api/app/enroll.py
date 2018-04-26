# encoding: utf-8

from flask import request
from . import apply
from api.models import AiweiCampaignEnroll
from datetime import  datetime
import redis
import os
import random
from common.func import get_params
from sqlalchemy.sql import func
from common.func import error, ok, json_has_keys
from .. import limiter, db
from .. import config, basedir

redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=redis_pool)

@apply.route('/apply', methods=['POST'])
def enroll():

    j = request.get_json(force=True)
    if not json_has_keys(j, ['phone', 'name', 'age', 'captcha']):
        return error()
    if len(j.get('phone')) != 11:
        return error("手机号码有误。", 2)
    if AiweiCampaignEnroll.query.filter_by(phone = j.get('phone')).first():
        return error("该手机号码已申请。", 3)
    if j.get('captcha') != r.get('phone'):
        return error("验证码有误！", 4)

    m = AiweiCampaignEnroll(
        phone = j.get('phone'),
        name = j.get('name'),
        age = j.get('age'),
        created_at = datetime.now()
    )
    db.session.add(m)
    db.session.commit()
    return ok()


@apply.route('/upload', methods=['POST', 'GET'])
@limiter.limit('3 per minute')
def upload_img():

    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            t = datetime.now()
            #filepath = os.path.join(config['default'].UPLOAD_FOLDER, t.strftime('%Y%m%d'))
            filepath = os.path.join(basedir + '/upload', t.strftime('%Y%m%d'))
            print(basedir)
            if not os.path.isdir(filepath):
                 os.mkdir(filepath)
            timestamp = t.strftime("%H%M%S%f.")
            file_name = os.path.join(filepath, timestamp)
            file.save(os.path.join(file_name))

            url = os.path.join(config['default'].IMAGE_PREFIX, t.strftime('%Y%m%d'), timestamp)
            return ok({"url": url})
    return error("invalid request")



# @apply.route('/captcha', methods=['GET'])
# @limiter.limit("3 per minute")
# def captcha():
#     """ 获取验证码
#
#     :<json string account: 帐号
#     """
#     j = request.args.get('phone')
#     if not j:
#         return error()
#     redis_str = 'phone'
#     if 300 - r.ttl(redis_str) < 60:
#         return error("验证码已发送，请稍后再试。", 1)
#     rnd_int = random.randrange(123457,999999)
#     #rnd_int = 123456
#     print(rnd_int)
#     r.setex(redis_str, 300, rnd_int)
#     return ok()