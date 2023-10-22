"""This module contaims my personalized configuration"""
from os import getenv, path


basedir = path.abspath(path.dirname(__file__))


class Config(object):
    SECRET_KEY = getenv('SECRET_KEY', 'you-will-never-guess')

    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL', 'sqlite:///' + path.join(basedir, 'app.db')) 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = getenv('MAIL_SERVER')
    MAIL_PORT = int(getenv('MAIL_PORT', 25))
    MAIL_USE_TLS = getenv('MAIL_USE_TLS') is not None
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')
    ADMINS = ['michaeldecent2@mail.com']
