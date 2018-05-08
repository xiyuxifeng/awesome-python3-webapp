#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /ormTest.py
# Project: unittest
# Created Date: Wednesday, May 9th 2018, 12:02:43 am
# Author: Wang Hui
# -----
# Last Modified:
# Modified By:
# -----
# Copyright (c) 2018 WH
# ------------------------------------
# Life is short, you need Python
###

import unittest
import aiomysql
import asyncio
from orm import *


class TestUser(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id', primary_key=True)
    name = StringField('name')


class TestORM(unittest.TestCase):

    database = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'db': 'test'
    }

    async def main(loop):
        await create_pool(loop, **database)
        user = TestUser()
        user.id = 3
        user.name = 'test'
        await user.save()
        return user.name

    loop = asyncio.get_event_loop()

    async def test_save(self):
        task = asyncio.ensure_future(main(loop))
        res = loop.run_until_complete(task)
        self.assertEqual(res, 'test')


if __name__ == '__main__':
    unittest.main()








print(res)