#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Fuxitong
# @Date  : 2020/1/15
# @Desc  :

from flask import Flask
from flask import Blueprint


def register_blueprint(app):
    pass

def create_app():
    __app = Flask(__name__)
    return __app