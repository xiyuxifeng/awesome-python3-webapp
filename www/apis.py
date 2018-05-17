#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /apis.py
# Project: www
# Created Date: Wednesday, May 16th 2018, 9:32:44 pm
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
JSON API definition
'''

import functools
import inspect
import json
import logging


class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional)
    '''
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    '''
    Indicate the input value has error or invaild. the data specifies the error field of input form.
    '''
    def __init(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. the data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    '''
    Indicate the api has no permission
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permisson:forbidden', 'permisson', message)
