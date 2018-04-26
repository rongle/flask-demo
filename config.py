import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    @staticmethod
    def init_app(app):
        pass



class Default(Config):
    PAGE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'aiweiKieSie9ohph'
    SQLALCHEMY_ECHO=True
    UPLOAD_FOLDER = '/upload/'
    IMAGE_PREFIX = "http://afaf.sfs.com/"
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'postgresql://postgres@localhost/aiwei_campaign_enroll'


    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)


config = {
    'development': Default,
    'default': Default,
}



