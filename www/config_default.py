#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /config_default.py
# Project: www
# Created Date: Thursday, May 17th 2018, 10:04:35 pm
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
Default Configurations
'''

configs = {
    'debug': True,
    'db': {
        'host': 'localhost',
        'port': 3306,
        'user': 'python',
        'password': 'python',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
