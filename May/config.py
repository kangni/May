# -*- coding: utf-8 -*-
#import os
#basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'ef6ed3c476c45eb39931abb50c2b40b4%'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    #SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data-dev.sqlite'

