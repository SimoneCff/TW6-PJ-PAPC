import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Ah-Non-Lo-So-Io'