class Config():
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}