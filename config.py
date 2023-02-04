import os


class Config:
    SECRET_KEY = 'ade856f07576deb1f86bb2b12fb627d3619986f98116cc835205bd2db7a9'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = 'ru'

    # CKEditor config
    CKEDITOR_SERVE_LOCAL = False
    CKEDITOR_HEIGHT = 400
    CKEDITOR_FILE_UPLOADER = '/upload'
    UPLOADED_PATH = os.path.join('uploads')



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:MySQL.root.85@localhost:3306/salus'
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:MySQL.root.85@localhost:3306/salus'
    DEBUG = True
config = {
    "default":DevConfig,
    "dev": DevConfig,
    "prod": ProdConfig
}
