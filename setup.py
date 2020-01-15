#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : setup.py
# @Author: Fuxitong
# @Date  : 2020/1/15
# @Desc  :

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)