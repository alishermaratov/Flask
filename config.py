class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI= 'postgres+psycopg2://postgres:postgres@localhost/test1'
