#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /orm.py
# Project: www
# Created Date: Tuesday, December 5th 2017, 10:21:11 pm
# Author: Wang Hui
# -----
# Last Modified: Tue Dec 26 2017
# Modified By: Wang Hui
# -----
# Copyright (c) 2017 WH
# ------------------------------------
# Life is short, you need Python
###

import asyncio
import aiomysql
import logging

'==============分装SQL方法============='

'创建连接池'


def log(sql, args=()):
    logging.info('SQL: %s' % sql)


@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop)


'Select'


@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs


'Insert, Update, Delete'


@asyncio.coroutine
def execute(sql, args, autocommit=True):
    log(sql)
    with (yield from __pool) as conn:
        if not autocommit:
            yield from conn.begin()
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()

            if not autocommit:
                yield from conn.commit() 
        except BaseException as e:
            if not autocommit:
                yield from conn.rollback()
            raise
        return affected


def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)


'======== ORM ==========='


class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type,
                                self.name)


class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BolleanField(Field):
    def __init(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)
    

class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)
    

class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)
    

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键
                    if primaryKey:
                        raise ValueError('Duplicate primary key for field: %s' % k)
                        
                    primaryKey = k
                else:
                    fields.append(k)
                
        if not primaryKey:
            raise ValueError('Primary key not found')
        
        for k in mappings.keys():
            attrs.pop(k)
        
        