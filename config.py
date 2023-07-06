import os
from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path

# ----------------Load .env file
# base_dir = Path(__file__).resolve().parent
# env_file = base_dir / '.env'
# load_dotenv(env_file)


# ---------------------Create Config class
class Config:
    # #-------------------------Get secrets
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    SECRET_KEY= os.getenv("secret_key")
    # SQLALCHEMY_DATABASE_URI = ''  # DevelopmentConfig or TestingConfig add URI to dabase
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PER_PAGE = 5


# ------------------------Configuration for Developing - local server (MySQL database)
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('sqlalchemy_database_URI')


# -------------------------Configuration for testing (SQLite database)
class TestingConfig(Config):
    # DB_FILE_PATH = base_dir / 'tests' / 'test.db'
    # SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE_PATH}'
    DEBUG = True
    TESTING = True


# ---------------------Configuration for production (MySQL database - AWS RDS)
class ProductionConfig(Config):
    DB_HOST = os.environ.get('DB_HOST')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    # SQLALCHEMY_DATABASE_URI = F'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4'


# ----------------------Config dict
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
