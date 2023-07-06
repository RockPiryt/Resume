from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy


# ----------Create instances db and migrate
db = SQLAlchemy()
# migrate = Migrate()
# ------------------------Create app


def create_app(config_name):
    '''Create app with passed configuration'''

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # db.init_app(app)
    # migrate.init_app(app, db)

    # ------------------------Register Blueprints
    from myresume.single_page.views import single_page_blueprint
    app.register_blueprint(single_page_blueprint, url_prefix='/')

    return app
