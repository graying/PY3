class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "\xcb+3{\xe8\\;\x84"
    DATABASE = "sample_sqlite3.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///sample_SQLAlchemy.db"


class ProductionConfig(BaseConfig):
    DEBUG = False
