##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
