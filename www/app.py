#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /app.py
# Project: www
# Created Date: Monday, December 4th 2017, 11:04:27 pm
# Author: Wang Hui
# -----
# Last Modified: Sun May 06 2018
# Modified By: Wang Hui
# -----
# Copyright (c) 2017 WH
# ------------------------------------
# Life is short, you need Python
###

import asyncio
import logging
from aiohttp import web


logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000....')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
