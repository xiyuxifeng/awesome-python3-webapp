#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /handlers.py
# Project: www
# Created Date: Wednesday, May 16th 2018, 9:46:02 pm
# Author: Wang Hui
# -----
# Last Modified:
# Modified By:
# -----
# Copyright (c) 2018 WH
# ------------------------------------
# Life is short, you need Python
###

'''
url handlers
'''

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post
from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }