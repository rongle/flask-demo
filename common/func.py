# -*- coding: utf-8 -*-
'''
    func
    ~~~~~~

    common routine

    :copyright: (c) 2016 jhhy
    :author: weiee .
    :date: 2016/04/18
'''

import datetime, collections,os
import json
from flask import abort, json, jsonify, make_response, request, current_app, \
    url_for, redirect, render_template


def error(ret=1, msg='bad request'):
    return jsonify({
        "status": ret,
        "message": msg
    })


def ok(data=None):
    return jsonify({
        "status": 0,
        "data"  : data
    })


def json_has_keys(json, keys):
    for k in keys:
        if not json.has_key(k):
            return None
    return True


def get_params():
    if request.method == "POST":
        return request.get_json(force=True, silent=True) or {}
    elif request.method == "GET":
        return request.args.to_dict()


class UTC8(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=8)
    def dst(self, dt):
            return datetime.timedelta(0)
    def tzname(self, dt):
        return '+08:00'


