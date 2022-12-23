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
