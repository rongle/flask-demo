#! /srv/venv/yaoyingli/bin/python
# -*- coding: utf-8 -*-

import os

from api import create_app, db
from flask_script import Manager, Shell, Server

api = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(api)

def make_shell_context():
    return dict(app=api, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host='127.0.0.1', port=6001))

if __name__ == '__main__':
    manager.run()

