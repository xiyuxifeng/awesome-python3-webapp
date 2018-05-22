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

    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'

    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, create_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, create_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, create_at=time.time()-7200)
    ]

    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


@get('/api/users')
async def api_get_users():
    users = await User.findAll(orderBy='create_at desc')
    for u in users:
        u["passwd"] = '*******'

    return dict(users=users)
