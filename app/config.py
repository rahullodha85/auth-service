class Config(object):
    """
    Default configurations
    """
    SECRET_KEY = 'my_secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = '0.0.0.0'
    PORT = 8000


class DevConfig(Config):
    """
    Local dev config
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test123@localhost:3306/medicalclinic'

class ProdConfig(Config):
    """
    production config
    """


config_vals = {
    'dev': DevConfig,
    'prod': ProdConfig
}