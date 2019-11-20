class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
